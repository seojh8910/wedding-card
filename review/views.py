from datetime import timedelta

from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.utils import timezone

from review.forms import ReviewCreationForm
from review.models import Review


def review_list(request):

    two_days_ago = timezone.now() - timedelta(days=1)
    review_count = Review.objects.all().count()
    review_object_list = Review.objects.all().order_by('-created_at')
    page = request.GET.get('page')
    paginator = Paginator(review_object_list, 10)
    try:
        page_obj_list = paginator.page(page)
    except Exception as e:
        page = 1
        page_obj_list = paginator.page(page)

    context = {
        'review_object_list': page_obj_list,
        'review_count': review_count,
        'paginator': paginator,
        'two_days_ago': two_days_ago
    }

    return render(request, 'review/list.html', context=context)


def review_create(request):
    if request.method == 'POST':
        form = ReviewCreationForm(request.POST, request.FILES)
        if form.is_valid():
            temp_review = form.save(commit=False)
            temp_review.writer = request.user
            temp_review.save()
            messages.success(request, '리뷰 생성 완료!')
            return redirect('review:review_list')
        else:
            messages.error(request, '이미지 및 리뷰를 작성하세요.')
            return redirect('review:review_create')
    form = ReviewCreationForm
    return render(request, 'review/create.html', context={'form': form})


def review_delete(request, pk):
    target_review = Review.objects.filter(pk=pk).first()
    if not target_review:
        messages.error(request, '존재하지않는 고객 리뷰입니다.')
        return redirect('review:review_list')

    if request.user == target_review.writer or request.user.is_staff:
        target_review.delete()
        messages.success(request, '리뷰가 삭제되었습니다.')
    else:
        messages.error(request, '리뷰 삭제 권한이 없습니다.')

    return redirect('review:review_list')
