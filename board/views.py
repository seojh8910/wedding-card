from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from board.forms import BoardCreationForm, CommentCreationForm
from board.models import Board, Comment


def board_list(request):
    all_board_list = Board.objects.all().order_by('-is_notice', '-created_at')
    page = request.GET.get('page')
    paginator = Paginator(all_board_list, 15)
    try:
        board_object_list = paginator.page(page)
    except Exception as e:
        page = 1
        board_object_list = paginator.page(page)

    context = {
        'board_object_list': board_object_list,
        'paginator': paginator,
    }
    return render(request, 'board/list.html', context=context)


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
    form = BoardCreationForm(user=request.user)
    return render(request, 'board/create.html', context={'form': form})


def board_detail(request, pk):
    board = Board.objects.filter(pk=pk).first()

    if not board:
        return 'does not exists'

    if request.user == board.writer or request.user.is_staff or not board.is_secret:
        comment_list = board.comment.all().order_by('-created_at')
        form = CommentCreationForm
        return render(request, 'board/detail.html', context={'board': board, 'comment_list': comment_list, 'form': form})

    else:
        return redirect('board:board_list')


def board_delete(request, pk):
    board = Board.objects.filter(pk=pk).first()
    login_user = request.user
    if not board:
        return 'does not exists'
    elif board.writer != login_user and not login_user.is_staff:
        return '권한없음'
    board.delete()
    return redirect('board:board_list')


def board_update(request, pk):
    board = Board.objects.filter(pk=pk).first()
    if not board:
        return 'does not exists'

    if request.method == 'POST':
        form = BoardCreationForm(request.POST, instance=board)
        if form.is_valid():
            form.save()
            return redirect(f'/boards/detail/{pk}')
    form = BoardCreationForm(instance=board)
    return render(request, 'board/update.html', context={'form': form, 'board': board})


def comment_create(request):
    if request.method == 'POST':
        board_pk = request.POST['board_pk']
        form = CommentCreationForm(request.POST)
        if form.is_valid():
            temp_commit = form.save(commit=False)
            temp_commit.board = Board.objects.get(pk=board_pk)
            temp_commit.writer = request.user
            temp_commit.save()
            return redirect(f'/boards/detail/{board_pk}')


def comment_delete(request, pk):
    comment = Comment.objects.filter(pk=pk).first()
    if not comment:
        return 'does not exist comment'
    board_pk = comment.board.pk
    if request.user == comment.writer or request.user.is_staff:
        comment.delete()
        messages.success(request, '삭제 완료!')
    else:
        messages.error(request, '권한이 없습니다.')
    return redirect(f'/boards/detail/{board_pk}')
