from django.shortcuts import render


def review_list(request):

    return render(request, 'review/list.html')
