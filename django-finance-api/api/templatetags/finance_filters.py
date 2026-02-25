from django import template
from decimal import Decimal

register = template.Library()

@register.filter
def currency(value):
    try:
        return f"${float(value):,.2f}"
    except (ValueError, TypeError):
        return "$0.00"

@register.filter
def percentage(value, total):
    try:
        if float(total) == 0:
            return "0%"
        percent = (float(value) / float(total)) * 100
        return f"{percent:.1f}%"
    except (ValueError, TypeError, ZeroDivisionError):
        return "0%"

@register.filter
def abs_value(value):
    try:
        return abs(float(value))
    except (ValueError, TypeError):
        return 0

@register.filter
def positive_negative_class(value):
    try:
        return 'positive' if float(value) >= 0 else 'negative'
    except (ValueError, TypeError):
        return ''
