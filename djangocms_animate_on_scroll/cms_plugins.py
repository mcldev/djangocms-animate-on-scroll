import json

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django.utils.translation import gettext_lazy as _

from .forms import AnimateOnScroll_Element_Form
from .models import AnimateOnScroll_Anchor, AnimateOnScroll_Element
from .settings import get_aos_init_params_js


class AnimateOnScroll_Anchor_Plugin(CMSPluginBase):
    model = AnimateOnScroll_Anchor
    name = _("AnimateOnScroll - Anchor")
    module = _("Animate On Scroll")
    render_template = "djangocms_animate_on_scroll/aos_anchor.html"

    fieldsets = ((None, {"fields": ("id_name",)}),)


plugin_pool.register_plugin(AnimateOnScroll_Anchor_Plugin)


class AnimateOnScroll_Element_Plugin(CMSPluginBase):
    model = AnimateOnScroll_Element
    name = _("AnimateOnScroll - Element")
    module = _("Animate On Scroll")
    render_template = "djangocms_animate_on_scroll/aos_element.html"
    allow_children = True
    form = AnimateOnScroll_Element_Form

    fieldsets = (
        (
            None,
            {"fields": (("aos_animation", "aos_easing"),)},
        ),
        (
            _("AOS Anchor settings"),
            {
                "classes": ("collapse",),
                "fields": (("aos_anchor_placement", "aos_anchor"),),
            },
        ),
        (
            _("AOS Advanced settings"),
            {
                "classes": ("collapse",),
                "fields": (
                    ("aos_offset", "aos_duration", "aos_delay"),
                    ("aos_once", "aos_mirror"),
                ),
            },
        ),
        (
            _("Advanced Element settings"),
            {
                "classes": ("collapse",),
                "fields": (
                    "id_name",
                    "additional_classes",
                    "attributes",
                ),
            },
        ),
    )

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        context["aos_init_params"] = get_aos_init_params_js()
        return context


plugin_pool.register_plugin(AnimateOnScroll_Element_Plugin)
