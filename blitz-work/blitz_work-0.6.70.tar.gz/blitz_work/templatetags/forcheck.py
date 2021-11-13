from django.template.defaultfilters import register


@register.filter
def checkfor (list):
    exist = 'checked'
    for name,_ in list:
        if name == 'checked':
            return ''
    return exist

