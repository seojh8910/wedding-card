from django.contrib import messages
from django.shortcuts import render, redirect

from board.forms import BoardCreationForm


def board_list(request):

    return render(request, 'board/list.html')


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
