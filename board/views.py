from django.contrib import messages
from django.shortcuts import render, redirect

from board.forms import BoardCreationForm
from board.models import Board


def board_list(request):
    board_object_list = Board.objects.all().order_by('-created_at')
    return render(request, 'board/list.html', context={'board_object_list': board_object_list})


def board_create(request):
    if request.method == 'POST':
        form = BoardCreationForm(request.POST)
        if form.is_valid():
            temp_board = form.save(commit=False)
            temp_board.writer = request.user
            temp_board.save()
            return redirect('board:board_list')
        else:
            messages.error(request, "오류가 발생했습니다.")
            return render(request, 'board/create.html', context={'form': form})
    form = BoardCreationForm
    return render(request, 'board/create.html', context={'form': form})


def board_detail(request, pk):
    board = Board.objects.filter(pk=pk).first()
    if not board:
        return 'does not exists'
    return render(request, 'board/detail.html', context={'board': board})


def board_delete(request, pk):
    board = Board.objects.filter(pk=pk).first()
    login_user = request.user
    if not board:
        return 'does not exists'
    elif board.writer != login_user and not login_user.is_staff:
        return '권한없음'
    board.delete()
    return redirect('board:board_list')
