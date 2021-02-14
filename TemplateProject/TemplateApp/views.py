from django.shortcuts import render

def index(request):
    val = 'Good Bye'
    return render(request, 'index.html', context={'value': val})
