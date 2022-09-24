from django.shortcuts import render, HttpResponse, redirect, Http404
from .models import *
from django.contrib.auth.decorators import login_required


store = [
    {
        'name': 'pizza Margarita',
        'price': 20
    },
    {
        'name': 'Lazanya',
        'price': 35
    },
    {
        'name': 'Bolonyeze',
        'price': 30
    },
    {
        'name': 'pizza Barbeku',
        'price': 40
    },
]


# Create your views here.
def first_view(request):
    return HttpResponse('<p>My first view</p>')


def restaurant_view(request):
    html = '<table>' \
            '<tr><th>Name</th><th>Price</th></tr>'
    for dish in store:
        html += f'<tr><td>{dish["name"]}</td><td>{dish["price"]}</td></tr>'
    html += '</table>'
    return HttpResponse(html)


def restaurant_views2(request):
    return render(request, 'restaurant.html', context={'amount': 10, 'store': store})


# def all_categories(request):
#     if request.user.is_authenticated:
#         return render(request, 'all_categories.html', context={'categories': Category.objects.all()})
#     else:
#         # raise Http404('you need to be authenticated to see this page')
#         return redirect('/auth/sign_in/')


@login_required
def all_categories(request):
    return render(request, 'all_categories.html', context={'categories': Category.objects.all(),
                                                           'username': request.user.username})


@login_required
def create_category(request):
    data = request.GET
    name = data.get('name')
    description = data.get('description')
    Category.objects.create(name=name, description=description)
    return redirect('/main/all_categories')


@login_required
def delete_category(request, cat_id):
    Category.objects.get(id=cat_id).delete()
    return redirect('/main/all_categories')