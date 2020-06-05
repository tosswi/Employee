from django import template

register = template.Library()

@register.sample_tag
def url_replace(request,field,value):
  url_dict = request.GET.copy()
  url_dict[field]= value
  return url_dict.urlencode()


