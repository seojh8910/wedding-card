from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages

from card.models import Card
from guest_book.forms import GuestBookCreationForm
from guest_book.models import GuestBook


# Create your views here.
def guestbook_create(request):
    if request.method == 'POST':
        card_pk = request.POST['card_pk']
        form = GuestBookCreationForm(request.POST)
        if form.is_valid():
            guestbook = form.save(commit=False)
            guestbook.card = Card.objects.filter(pk=card_pk).first()
            guestbook.writer = request.POST['writer']
            guestbook.password = make_password(request.POST['password'])
            guestbook.save()
            return redirect(f'/cards/detail/{card_pk}')
        else:
            for field in form:
                print('오류 발생: ', field.name, field.errors)
            return redirect(f'/cards/detail/{card_pk}')


def guestbook_delete(request, pk):
    guestbook = get_object_or_404(GuestBook, pk=pk)

    if request.method == 'POST':
        # 사용자가 입력한 비밀번호
        entered_password = request.POST.get('password')
        
        # 방명록에 저장된 비밀번호와 사용자가 입력한 비밀번호 비교
        password_match = check_password(entered_password, guestbook.password)

        if password_match:
            guestbook.delete()
            return JsonResponse({"status": "success"})
        else:
            return JsonResponse({"status": "fail"})
