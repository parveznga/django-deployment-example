from django import template

register = template.Library()

# Use decorators or use line no. 14 syntax
@register.filter(name='cut_str')
def cut_str(value, arg):
    """
    This cuts out all values of "args" from the string!
    """

    return value.replace(arg,'')

# register.filter('cut',cut)