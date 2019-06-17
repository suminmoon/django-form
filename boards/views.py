from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_GET, require_http_methods
from .models import Board
from .forms import BoardForm


# Board 의 리스트
@require_GET
def index(request):
    boards = Board.objects.order_by('-pk')
    context = {'boards': boards}
    return render(request, 'boards/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            board = Board.objects.create(title=title, content=content)
            return redirect('boards:detail', board.pk)
    else:
        form = BoardForm()
    context = {'form': form}
    return render(request, 'boards/create.html', context)


# boards/3/
@require_GET
def detail(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    context = {'board': board}
    return render(request, 'boards/detail.html', context)


# POST boards/3/delete/
@require_POST
def delete(request, board_pk):
    # 특정 보드를 불러와서 삭제한다.
    board = get_object_or_404(Board, pk=board_pk)
    board.delete()
    return redirect('boards:index')
