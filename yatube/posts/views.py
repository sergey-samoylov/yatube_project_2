from django.shortcuts import render

from django.http import HttpResponse


# Главная страница
def index(request):
    template = 'posts/index.html'
    main_heading = 'Это главная страница проекта Yatube'
    context = {
        "main_heading": main_heading,
    }
    return render(request, template, context)


def group_posts(request):
    template = 'posts/group_posts.html'
    main_heading = 'Здесь будет информация о группах проекта Yatube'
    context = {
        "main_heading": main_heading,
    }
    # return HttpResponse(f'Cтраница группы {slug}')
    return render(request, template, context)
