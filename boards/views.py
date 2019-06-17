from django.shortcuts import render, redirect
from .models import Board


# Board 의 리스트
def index(request):
    boards = Board.objects.order_by('-pk')
    context = {'boards': boards}
    return render(request, 'boards/index.html', context)


def create(request):
    if request.method == 'GET':
        return render(request, 'boards/create.html')
    else:
        # Board 정보를 받아서 데이터베이스에 저장하는 로직
        title = request.POST.get('title')
        content = request.POST.get('content')
        board = Board(title=title, content=content)
        board.save()
        return redirect('boards:index')
