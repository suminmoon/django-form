from django.shortcuts import render
from .models import Board


# Board 의 리스트
def index(request):
    boards = Board.objects.order_by('-pk')
    context = {'boards': boards}
    return render(request, 'boards/index.html', context)
