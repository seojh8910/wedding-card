from django.shortcuts import render

# Create your views here.
def hello_world(request):
    return render(request, 'account/hello_world.html')