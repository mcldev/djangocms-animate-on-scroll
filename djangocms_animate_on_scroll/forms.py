from django import forms
from django.forms.models import ModelForm

from .consts import AOS_ANCHOR_PLACEMENT, AOS_ANIMATIONS, AOS_EASING
from .settings import get_aos_init_params


class AnimateOnScroll_Element_Form(ModelForm):
    aos_animation = forms.ChoiceField(choices=AOS_ANIMATIONS)

    aos_easing = forms.ChoiceField(choices=AOS_EASING, required=False)

    aos_anchor_placement = forms.ChoiceField(choices=AOS_ANCHOR_PLACEMENT, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        aoe_init_params = get_aos_init_params()
        self.fields["aos_offset"].widget.attrs["placeholder"] = aoe_init_params["offset"]
        self.fields["aos_duration"].widget.attrs["placeholder"] = aoe_init_params["duration"]
        self.fields["aos_delay"].widget.attrs["placeholder"] = aoe_init_params["delay"]
