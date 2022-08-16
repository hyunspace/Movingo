from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Count

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movies.models import Movie
from community.models import Thread, Comment
from community.serializers import MainThreadSerializer, CommentSerializer, ThreadSerializer, ThreadCreateSerializer


@api_view(['GET', 'POST'])
def threads_or_create(request):
    def thread_list():
        threads = Thread.objects.annotate(comment_count=Count('comments', distinct=True)).order_by('-pk')
        serializer = MainThreadSerializer(threads, many=True)
        return Response(serializer.data)

    def create_thread():
        serializer = ThreadCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)

    if request.method == 'GET':    # 스레드 전체(커뮤니티 메인)
        return thread_list()
    elif request.method == 'POST': # 스레드 1개 생성
        return create_thread()


@api_view(['POST'])
def create_thread(request, movie_pk):    
    movie = get_object_or_404(Movie, pk=movie_pk)
    preprocessed_data = request.data
    preprocessed_data['movie'] = movie.pk

    serializer = ThreadCreateSerializer(data=preprocessed_data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    print(serializer.errors)




@api_view(['GET', 'DELETE'])
def thread_read_delete(request, thread_pk):
    thread = get_object_or_404(Thread, pk=thread_pk)
    
    def thread_detail():
        serializer = ThreadSerializer(thread)
        return Response(serializer.data)

    def delete_thread():
        thread.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':     # 스레드 디테일 (READ)
        return thread_detail()
    elif request.method == 'DELETE': # 스레드 삭제 (관리자만)
        if request.user.is_superuser():
            return delete_thread()


@api_view(['POST'])
def create_comment(request, thread_pk):
    user = request.user
    thread = get_object_or_404(Thread, pk=thread_pk)
    
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(thread=thread, user=user)

        # 추가된 댓글을 바로 반영해서 보여줄 수 있도록
        serializer = ThreadSerializer(thread)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def comment_ud(request, thread_pk, comment_pk):
    thread = get_object_or_404(Thread, pk=thread_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    def update_comment():
        if comment.user.pk == request.user.pk:
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(thread=thread, user=request.user)

    def delete_comment():
        comment.delete()
        serializer = ThreadSerializer(thread)
        return Response(serializer.data)

    if request.method == 'PUT':
        return update_comment()
    elif request.method == 'DELETE':
        return delete_comment()


@api_view(['GET'])
def thread_exists(request, movie_pk):
    threads = get_list_or_404(Thread)
    movie_title = Movie.objects.filter(pk=movie_pk).values('title')[0]
    movie_title = movie_title['title']
    
    for thread in threads:
        if thread.movie.title == movie_title:
            return Response({'threadPk': thread.pk})
    return Response({'threadPk': -1})