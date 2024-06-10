"""
В этом задании вам предстоит работать с моделью поста в блоге. У него есть название, текст, имя автора, статус
(опубликован/не опубликован/забанен), дата создания, дата публикации, категория (одна из нескольких вариантов).

Ваша задача:
- создать соответствующую модель (в models.py)
- создать и применить миграцию по созданию модели (миграцию нужно добавить в пул-реквест)
- заполнить вашу локальную базу несколькими постами для облегчения тестирования
- реализовать у модели метод to_json, который будет преобразовывать объект книги в json-сериализуемый словарь
- по очереди реализовать каждую из вьюх в этом файле, проверяя правильность их работу в браузере
"""
from datetime import datetime, timedelta

from django.core import serializers
from django.http import HttpRequest, HttpResponse
from django.db.models import Q

from django.utils import timezone
from challenges.models import BlogPost


def last_posts_list_view(request: HttpRequest) -> HttpResponse:
    """
    В этой вьюхе вам нужно вернуть 3 последних опубликованных поста.
    """
    posts = BlogPost.objects.order_by('-publication_date')[:3]
    posts = serializers.serialize('json', posts)
    return HttpResponse(posts, content_type='application/json')


def posts_search_view(request: HttpRequest) -> HttpResponse:
    """
    В этой вьюхе вам нужно вернуть все посты, которые подходят под поисковый запрос.
    Сам запрос возьмите из get-параметра query.
    Подходящесть поста можете определять по вхождению запроса в название или текст поста, например.
    """
    if request.method == 'GET':
        query = request.GET.get('query', None)
        if query:
            posts = BlogPost.objects.filter(Q(title__contains=query) | Q(text__contains=query))
            posts = serializers.serialize('json', posts)
            return HttpResponse(posts, content_type='application/json')
    return HttpResponse(None, content_type='application/json')


def untagged_posts_list_view(request: HttpRequest) -> HttpResponse:
    """
    В этой вьюхе вам нужно вернуть все посты без категории, отсортируйте их по автору и дате создания.
    """
    posts = BlogPost.objects.filter(category=None).order_by('author', 'creation_date')
    posts = serializers.serialize('json', posts)
    return HttpResponse(posts, content_type='application/json')


def categories_posts_list_view(request: HttpRequest) -> HttpResponse:
    """
    В этой вьюхе вам нужно вернуть все посты, категория которых принадлежит одной из указанных.
    Возьмите get-параметр categories, в нём разделённый запятой список выбранных категорий.
    """
    if request.method == 'GET':
        categories = request.GET.get('categories', None).split(",")
        if categories:
            posts = BlogPost.objects.filter(category__in=categories)
            posts = serializers.serialize('json', posts)
            return HttpResponse(posts, content_type='application/json')
    return HttpResponse(None, content_type='application/json')


def last_days_posts_list_view(request: HttpRequest) -> HttpResponse:
    """
    В этой вьюхе вам нужно вернуть посты, опубликованные за последние last_days дней.
    Значение last_days возьмите из соответствующего get-параметра.
    """
    if request.method == 'GET':
        last_days = int(request.GET.get('last_days', 0))
        print(last_days)
        if last_days:
            publication_date_from = timezone.now()-timedelta(days=last_days)
            posts = BlogPost.objects.filter(publication_date__gte=publication_date_from)
            posts = serializers.serialize('json', posts)
            return HttpResponse(posts, content_type='application/json')
    return HttpResponse(None, content_type='application/json')
