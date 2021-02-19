from django.shortcuts import render

def index(request):
    val = 'Good Bye'
    return render(request, 'index.html', context={'value': val})

def home(request):
    my_name = 'Taro Tamada'
    favorite_fruits = ['apple', 'grape', 'lemon']
    my_info = {
        'name' : 'Taro',
        'age' : 18
    }

    return render(request, 'home.html', context={
        'my_name': my_name,
        'favorite_fruits': favorite_fruits,
        'my_info': my_info
    })