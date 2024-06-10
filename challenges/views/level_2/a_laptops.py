"""
В этом задании вам предстоит работать с моделью ноутбука. У него есть бренд (один из нескольких вариантов),
год выпуска, количество оперативной памяти, объём жесткого диска, цена, количество этих ноутбуков на складе
и дата добавления.

Ваша задача:
- создать соответствующую модель (в models.py)
- создать и применить миграцию по созданию модели (миграцию нужно добавить в пул-реквест)
- заполнить вашу локальную базу несколькими ноутбуками для облегчения тестирования
  (я бы советовал использовать для этого shell)
- реализовать у модели метод to_json, который будет преобразовывать объект ноутбука в json-сериализуемый словарь
- по очереди реализовать каждую из вьюх в этом файле, проверяя правильность их работу в браузере
"""
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404

from challenges.models import Laptop, Brand
from django.core import serializers


def laptop_details_view(request: HttpRequest, laptop_id: int) -> HttpResponse:
    """
    В этой вьюхе вам нужно вернуть json-описание ноутбука по его id.
    Если такого id нет, вернуть 404.
    """
    qs = get_object_or_404(Laptop, id=laptop_id)
    laptop = serializers.serialize('json', [qs])
    return HttpResponse(laptop)


def laptop_in_stock_list_view(request: HttpRequest) -> HttpResponse:
    """
    В этой вьюхе вам нужно вернуть json-описание всех ноутбуков, которых на складе больше нуля.
    Отсортируйте ноутбуки по дате добавления, сначала самый новый.
    """
    qs = Laptop.objects.filter(stock_quantity__gt=0).order_by('-date_added')
    laptops = serializers.serialize('json', qs)
    return HttpResponse(laptops, content_type='application/json')


def laptop_filter_view(request: HttpRequest) -> HttpResponse:
    """
    В этой вьюхе вам нужно вернуть список ноутбуков с указанным брендом и указанной минимальной ценой.
    Бренд и цену возьмите из get-параметров с названиями brand и min_price.
    Если бренд не входит в список доступных у вас на сайте или если цена отрицательная, верните 403.
    Отсортируйте ноутбуки по цене, сначала самый дешевый.
    """
    if request.method == 'GET':
        brand = request.GET.get('brand', None)
        min_price = int(request.GET.get('min_price', -1))
        if brand not in Brand.values:
            raise PermissionDenied
        if min_price < 0:
            raise PermissionDenied

        qs = Laptop.objects.filter(brand=brand, price__gte=min_price).order_by('price')
        laptops = serializers.serialize('json', qs)
        return HttpResponse(laptops, content_type='application/json')
    return HttpResponseNotAllowed(['GET'])


def last_laptop_details_view(request: HttpRequest) -> HttpResponse:
    """
    В этой вьюхе вам нужно вернуть json-описание последнего созданного ноутбука.
    Если ноутбуков нет вообще, вернуть 404.
    """
    qs = Laptop.objects.last()
    laptop = serializers.serialize('json', [qs])
    return HttpResponse(laptop, content_type='application/json')
