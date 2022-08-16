# articles/views.py
from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Count
from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from collects.models import Collection
from collects.serializers import MovieCollectionSerializer
from .models import Movie, Review
from .serializers.movie import MovieListSerializer, MovieSerializer, AutoCompleteSerializer
from .serializers.review import ReviewSerializer

# from .serializers.review import CommentSerializer


@api_view(['GET'])
def movie_list(request):
    keyword = request.GET.get('keyword')

    if keyword:
        movies = Movie.objects.filter(title__contains=keyword).annotate(review_count=Count('reviews', distinct=True), 
        wish_count=Count('wish_users', distinct=True)).order_by('-popularity')
    else:
        movies = Movie.objects.annotate(review_count=Count('reviews', distinct=True), 
        wish_count=Count('wish_users', distinct=True)).order_by('-popularity')

    paginator = Paginator(movies, 20)
    page_number = request.GET.get('page')
    current_page = int(page_number) if page_number else 1

    movie_list = paginator.get_page(current_page)
    serializer = MovieListSerializer(movie_list, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
def create_review(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)

    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=user)

        # 기존 serializer 가 return 되면, 단일 review 만 응답으로 받게됨.
        # 사용자가 리뷰를 입력하는 사이에 업데이트된 전체 review 확인 불가 => 업데이트된 전체 목록 return         
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def movie_review_list(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    reviews = Review.objects.filter(movie=movie).annotate(likes_cnt=Count('like_users', distinct=True)).order_by('-likes_cnt')[:4]
    print(reviews.values())

    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def wish_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.wish_users.filter(pk=user.pk).exists():
        movie.wish_users.remove(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    else:
        movie.wish_users.add(user)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def like_update_delete_review(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    user = request.user

    def like_review():
        if review.like_users.filter(pk=user.pk).exists():
            review.like_users.remove(user)
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        else:
            review.like_users.add(user)
            serializer = MovieSerializer(movie)
            return Response(serializer.data)

    def get_update_review_form():
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def update_review():
        if review.user.pk == user.pk:
            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(movie=movie, user=user)

                serializer = MovieSerializer(movie)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete_review():
         if review.user.pk == user.pk:
            review.delete()
            serializer = MovieSerializer(movie)
            return Response(serializer.data)

    if request.method == 'POST': # 좋아요
        return like_review()
    elif request.method == 'GET': # 수정하기 위한 form 받아오기
        return get_update_review_form()
    elif request.method == 'PUT': # 수정
        return update_review()
    elif request.method == 'DELETE': # 삭제
        return delete_review()


@api_view(['GET'])
def auto_complete(request, keyword):
    movies = Movie.objects.filter(title__contains=keyword).order_by('-vote_average')[:10]
    serializer = AutoCompleteSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_collections(request, movie_pk):
    '''
    Movie에서 역참조하기
    '''
    movie = get_object_or_404(Movie, pk=movie_pk)
    collections = movie.collections.order_by('-created_at')[:3]
    movie_collections = []
    
    for idx in range(len(collections)):
        collection_pk = collections[idx].pk
        collection = get_object_or_404(Collection, pk=collection_pk)
        movie_collections.append(collection)
        # print('-'*30)
        # print(f'지금 추가하려는 것: {collection}')
        # print(Collection.objects.filter(pk=collection_pk).values())
        # print(f'모두 담은 movie_collections: {movie_collections}')
    serializer = MovieCollectionSerializer(movie_collections, many=True)
    return Response(serializer.data)