from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import BingoSerializer
from .models import Bingo


# Create your views here.
@api_view(['GET'])
def get_current_bingo(request):
    bingo = get_object_or_404(Bingo, current=True)
    print(bingo)
    serializer = BingoSerializer(bingo)
    return Response(serializer.data)

