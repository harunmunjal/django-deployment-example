from django import template

register = template.Library()

@register.filter(name = 'cut')
def cut(value, arg):
    """
    this cuts out all values of "args" from strings!
    """
    return value.replace(arg, '')

# register.filter('cut', cut)
