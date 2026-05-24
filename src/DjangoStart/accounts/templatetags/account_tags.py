from django import template
from django.utils import timezone

register = template.Library()

@register.simple_tag
def days_on_site(date_joined):
    today = timezone.now().date()
    days = (today - date_joined.date()).days
    if days % 10 == 1 and days % 100 != 11:
        return f"{days} день"
    elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
        return f"{days} дня"
    else:
        return f"{days} днів"