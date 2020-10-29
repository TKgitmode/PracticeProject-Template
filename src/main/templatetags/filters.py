from django import template

register = template.Library()


@register.filter(name='greeting')
def greeting(value):
    if len(value) >= 8:
        largo="Ur name is too long .. "
    return f"<h1 style='background:green;color:white'>Bienvenido, {value}</h1>"+largo
    