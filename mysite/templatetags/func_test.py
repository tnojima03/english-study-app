import os
from django import template
register = template.Library()

 
@register.filter(name="test_func")
def test_func(some_text):
    is_file = os.path.isfile("test.txt")
    if is_file:
        with open("static/testaaa.txt", 'a') as f:
            f.write("static/testaaaa.txt")
    else:
        with open("test.txt", 'a') as f:
            f.write("test1")

    return some_text + some_text

