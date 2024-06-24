from django.shortcuts import render

from review.models import Review


def landing_page(request):
    review_list = Review.objects.all().order_by('-created_at')[:8]
    context = {'review_list': review_list}
    return render(request, 'home/index.html', context)
