from django import template
register = template.Library()

@register.simple_tag
def setvar(val=None):
  return val
  
def phonenumber(value):
    value = str(value)
    phone = '-'.join((value[:3],value[3:6],value[6:]))
    return phone

register.filter('phonenumber', phonenumber)