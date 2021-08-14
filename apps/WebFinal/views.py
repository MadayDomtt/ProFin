from django.shortcuts import render

# Create your views here.
def may(request):
    return render(request, 'index.html')

