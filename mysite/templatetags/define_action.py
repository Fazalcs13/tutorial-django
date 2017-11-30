from django import template
register = template.Library()

@register.assignment_tag
def define(val=None):
  return val

@register.filter
def to_underscore(value):
    val = value.replace(" ","_")
    val = val.replace("&","")
    val = val.replace("__", "_")
    return val

@register.filter
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)