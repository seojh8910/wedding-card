from django.contrib.auth.hashers import make_password
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from card.models import Card
from guest_book.forms import GuestBookCreationForm


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
    return

