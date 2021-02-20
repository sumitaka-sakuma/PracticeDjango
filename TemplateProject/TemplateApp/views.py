from django.shortcuts import render

def index(request):
    val = 'Good Bye'
    return render(request, 'index.html', context={'value': val})

def home(request, first_name, last_name):
    my_name = f'{first_name}{last_name}'
    favorite_fruits = ['apple', 'grape', 'lemon']
    my_info = {
        'name' : 'Taro',
        'age' : 18
    }
    status = 20

    return render(request, 'home.html', context={
        'my_name': my_name,
        'favorite_fruits': favorite_fruits,
        'my_info': my_info,
        'status': status
    })

def sample1(request):
    return render(request, 'sample1.html')

def sample2(request):
    return render(request, 'sample2.html')

def sample(request):
    name = 'ichiro Yamada'
    height = 178.2
    weight = 72
    bmi = weight / (height / 100)**2
    page_url = 'ホームページ： https://www.google.com'
    favorite_fruits = [
        'Apple', 'Grape', 'Lemon'
    ]
    msg = """hello
    my name is
    ichoro
    """
    msg2 = '1234567890'
    return render(request, 'sample.html', context={
        'name': name,
        'bmi': bmi,
        'page_url': page_url,
        'fruits': favorite_fruits,
        'msg': msg,
        'msg2': msg2
    })

