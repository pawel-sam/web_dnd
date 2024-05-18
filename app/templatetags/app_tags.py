from django import template
from .test import Map

register = template.Library()


@register.simple_tag()
def create_map():
    map = Map()
    map.fill_water()
    map.create_land()
    map.get_json() # файл .json создается в самой верней директории приложения
    # print(map.print_map('only_letter'))
    # Полный вывод: 'full_info'
    # Вывод–рисунок: 'only_letter'
    # return map
    return "Map created!"

