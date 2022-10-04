from django import template

register = template.Library()


@register.filter(name='calculate_subtotal')
def calculate_subtotal(quantity, price):
    return quantity * price
