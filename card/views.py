from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from card.forms import CardCreationForm
from card.models import Card


def list_card(request):
    card_list = Card.objects.order_by('-created_at')
    context = {'cards': card_list}
    return render(request, 'card/list_card.html', context)


# Create your views here.
def create_card(request):
    if request.method == 'POST':
        form = CardCreationForm(request.POST, request.FILES)
        if form.is_valid():
            card = form.save(commit=False)
            card.user = request.user
            card.save()
            return redirect('card:list')
        else:
            for field in form:
                print('오류 발생: ', field.name, field.errors)
            return redirect('card:create')
    form = CardCreationForm()
    return render(request, 'card/create_card.html', {"form": form})


def detail_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    return render(request, 'card/detail_card.html', {"card": card})


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
