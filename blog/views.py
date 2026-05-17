from django.shortcuts import render, redirect
from .models import Game, Category


def home(request):

    return render(request, 'blog/home.html')


def catalogo(request):

    category = request.GET.get('category')

    categories = Category.objects.all()

    if category:

        games = Game.objects.filter(
            category__name=category
        )

    else:

        games = Game.objects.all()

    return render(request, 'blog/publicaciones.html', {
        'games': games,
        'categories': categories
    })


def crear_game(request):

    if request.method == 'POST':

        category_name = request.POST['category']

        category, created = Category.objects.get_or_create(
            name=category_name
        )

        Game.objects.create(

            title=request.POST['title'],

            description=request.POST['description'],

            image=request.FILES['image'],

            release_date=request.POST['release_date'],

            platform=request.POST['platform'],

            category=category
        )

        return redirect('/catalogo/')

    return render(request, 'blog/crear.html')