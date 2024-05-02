from django.contrib import messages
from django.shortcuts import render, redirect

from review.forms import ReviewCreationForm
from review.models import Review


def review_list(request):
    review_object_list = Review.objects.all().order_by('-created_at')
    return render(request, 'review/list.html', context={'review_object_list': review_object_list})


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
            messages.error(request, '리뷰 생성 실패')
            return redirect('review:review_create')
    form = ReviewCreationForm
    return render(request, 'review/create.html', context={'form': form})
