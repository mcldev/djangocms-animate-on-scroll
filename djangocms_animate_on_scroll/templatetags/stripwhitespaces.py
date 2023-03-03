import re

from django import template

register = template.Library()

"""
Simple tag to remove all duplicate whitespaces
{% stripwhitespaces %}
<div
    data-aos-blop="400"  
        data-aos-truc="true"


 >
{% endstripwhitespaces %}

=> <div data-aos-blop="400" data-aos-truc="true" >
"""


@register.tag(name="stripwhitespaces")
def do_stripwhitespaces(parser, token):
    nodelist = parser.parse(("endstripwhitespaces",))
    parser.delete_first_token()
    return StripWhitespacesNode(nodelist)


class StripWhitespacesNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        return re.sub(r"\s+", " ", output)
