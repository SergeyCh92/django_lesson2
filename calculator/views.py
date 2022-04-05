from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def home(request):
    return HttpResponse('Стартовая страница.')


def make_dish(request):
    dish = request.path[1:-1]
    servings = int(request.GET.get('servings', 1))
    data = DATA[dish].copy()
    for i in data:
        data[i] = data[i] * servings
    context = {
        'recipe': data,
    }
    return render(request, 'index.html', context)
