from django import template

from datetime import date, timedelta

register = template.Library()

@register.simple_tag(name="todays_date")
def get_current_date():
    now = date.today().isoformat() 
    return now

@register.simple_tag(name="max_date")
def get_current_date():
    max = (date.today()+timedelta(days=30)).isoformat()  
    return max

@register.simple_tag(name="tommorow")
def get_current_date():
    max = (date.today()+timedelta(days=1)).isoformat()  
    return max



@register.filter
def percentage(value1, value2=100):
    try:
        value1 = int(value1)
        value2 = int(value2)
        if value2 == 0:
            return 0  
        return (value1 / value2) * 100
    except (ValueError, TypeError):
        return 0  
