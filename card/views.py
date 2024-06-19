from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from card.forms import CardCreationForm, TransportFormSet, AccountFormSet
from card.models import Card, Gallery
from guest_book.forms import GuestBookCreationForm


@login_required
def list_card(request):
    user = request.user
    today = timezone.now()
    one_month_ago = today - timedelta(days=30)

    # 예식일 30일 지난 카드 삭제
    expired_cards = Card.objects.filter(user=user,
                                        wedding_date__isnull=False,
                                        wedding_date__lt=one_month_ago)
    expired_cards.delete()

    card_list = Card.objects.filter(user=user).order_by('-created_at')
    context = {'cards': card_list}
    return render(request, 'card/list_card.html', context)


def remove_wedding_after_one_month_card(card_list):
    today = timezone.now()
    for card in card_list:
        if card.wedding_date and card.wedding_date + timedelta(days=30) < today:
            card.delete()


def create_card(request):
    if request.method == 'POST':
        form = CardCreationForm(request.POST, request.FILES)
        transport_formset = TransportFormSet(request.POST, instance=Card())
        account_formset = AccountFormSet(request.POST, instance=Card())

        if form.is_valid() and transport_formset.is_valid() and account_formset.is_valid():
            card = form.save(commit=False)
            card.user = request.user
            card.wedding_hall_address = form.cleaned_data['wedding_hall_address']
            card.save()

            transport_formset.instance = card
            transport_formset.save()

            account_formset.instance = card
            account_formset.save()

            images = request.FILES.getlist('images')
            for image in images:
                Gallery.objects.create(card=card, gallery_img=image)

            return JsonResponse({'status': 200, 'redirect_url': reverse('card:list')})
        else:
            for field in form:
                print('오류 발생: ', field.name, field.errors)
            return redirect('card:create')

    form = CardCreationForm()
    transport_formset = TransportFormSet(instance=Card())
    account_formset = AccountFormSet(instance=Card())

    return render(request, 'card/create_card.html', {
        "form": form,
        'transport_formset': transport_formset,
        'account_formset': account_formset,
    })


def detail_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    form = GuestBookCreationForm()
    return render(request, 'card/detail_card.html', {"form": form, "card": card})


def update_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == "POST":
        form = CardCreationForm(request.POST, request.FILES, instance=card)
        if form.is_valid():
            card = form.save(commit=False)
            card.save()
            return redirect('/cards/detail/' + str(pk))
        else:
            return redirect('/cards/list/')
    else:
        form = CardCreationForm(instance=card)
        context = {'form': form, 'card': card}
        return render(request, 'card/update_card.html', context)


def delete_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    card.delete()
    return redirect('/cards/list/')
