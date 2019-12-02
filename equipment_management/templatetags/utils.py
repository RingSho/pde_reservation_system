from django import template
 
 
register = template.Library()
 
@register.filter(name="test")
def multipliy(dic, target_id):
    return dic[target_id]