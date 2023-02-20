import os
from django import template
register = template.Library()

 
@register.filter(name='remove_space')
def remove_space(text):
    return text.replace(' ', '_')

@register.filter(name='addstr')
def addstr(value, arg):
    """ Only concat string argument """
    if isinstance(arg, str):
        return value + arg
    else:
        return value

@register.filter(name='delete_audio')
def delete_audio(text):
    os.remove(f"static/listening/{text}.mp3")
    return ("フレーズを消去する")

# ########   https://gkc.hateblo.jp/entry/2017/08/29/231844  ############
# class SetVarNode(template.Node):

#     def __init__(self, var_name, var_value):
#         self.var_name = var_name
#         self.var_value = var_value

#     def render(self, context):
#         try:
#             value = template.Variable(self.var_value).resolve(context)
#         except template.VariableDoesNotExist:
#             value = ""
#         context[self.var_name] = value

#         return u""

# @register.tag(name='set')
# def set_var(parser, token):
#     """
#     {% set some_var = '123' %}
#     """
#     parts = token.split_contents()
#     if len(parts) < 4:
#         raise template.TemplateSyntaxError("'set' tag must be of the form: {% set <var_name> = <var_value> %}")

#     return SetVarNode(parts[1], parts[3])

# #################