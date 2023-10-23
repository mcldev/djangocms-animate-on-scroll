from django import forms
from django.forms.models import ModelForm
from django.utils.translation import gettext_lazy as _

from .consts import AOS_ANCHOR_PLACEMENT, AOS_ANIMATIONS, AOS_EASING
from .settings import get_aos_init_params


def choices_with_default_value(choices, default_value):
    if isinstance(default_value, bool):
        default_value = _("Yes") if default_value else _("No")
    first_choice_str = f'{_("Default")} ({default_value})'
    first_choice = (choices[0][0], first_choice_str)
    return (first_choice, *choices[1:])


class AnimateOnScroll_Element_Form(ModelForm):
    aos_animation = forms.ChoiceField(choices=AOS_ANIMATIONS)

    aos_easing = forms.ChoiceField(choices=AOS_EASING, required=False)

    aos_anchor_placement = forms.ChoiceField(choices=AOS_ANCHOR_PLACEMENT, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        aoe_init_params = get_aos_init_params()

        self.fields["aos_easing"].widget.choices = choices_with_default_value(
            self.fields["aos_easing"].widget.choices, aoe_init_params["easing"]
        )

        self.fields["aos_anchor_placement"].widget.choices = choices_with_default_value(
            self.fields["aos_anchor_placement"].widget.choices, aoe_init_params["anchor-placement"]
        )

        self.fields["aos_offset"].widget.attrs["placeholder"] = aoe_init_params["offset"]
        self.fields["aos_duration"].widget.attrs["placeholder"] = aoe_init_params["duration"]
        self.fields["aos_delay"].widget.attrs["placeholder"] = aoe_init_params["delay"]

        self.fields["aos_once"].widget.choices = choices_with_default_value(
            self.fields["aos_once"].widget.choices, aoe_init_params["once"]
        )

        self.fields["aos_mirror"].widget.choices = choices_with_default_value(
            self.fields["aos_mirror"].widget.choices, aoe_init_params["mirror"]
        )
