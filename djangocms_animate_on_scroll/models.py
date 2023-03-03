import json

from cms.models import CMSPlugin
from djangocms_attributes_field.fields import AttributesField

from django.db import models
from django.db.models.deletion import SET_NULL
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


class AnimateOnScroll_Anchor(CMSPlugin):
    id_name = models.CharField(
        verbose_name=_("ID name"),
        max_length=255,
    )

    def __str__(self):
        return self.id_name

    def clean(self):
        valid_id_name = slugify(self.id_name)
        self.id_name = valid_id_name


class AnimateOnScroll_Element(CMSPlugin):
    # AOS Standard
    # --------------------------------
    aos_animation = models.CharField(
        verbose_name=_("AOS Animation"),
        max_length=255,
        help_text=_('Script will trigger "animation_name" animation on this element, if you scroll to it.'),
    )

    aos_easing = models.CharField(
        verbose_name=_("Anchor Easing"),
        blank=True,
        max_length=255,
        help_text=_("Choose timing function to ease elements in different ways"),
    )

    # AOS Anchors
    # --------------------------------
    aos_anchor_placement = models.CharField(
        verbose_name=_("Anchor Placement"),
        blank=True,
        max_length=255,
        help_text=_("Anchor placement - which one position of element on the screen should trigger animation"),
    )

    aos_anchor = models.ForeignKey(
        AnimateOnScroll_Anchor,
        verbose_name=_("Animate On Scroll Anchor"),
        related_name="aos_anchor",
        blank=True,
        null=True,
        help_text=_(
            "Anchor element, whose offset will be counted to trigger animation instead of actual elements offset"
        ),
        on_delete=SET_NULL,
    )

    # AOS Advanced
    # --------------------------------
    aos_offset = models.IntegerField(
        verbose_name=_("Offset"),
        null=True,
        blank=True,
        help_text=_("Change offset to trigger animations sooner or later (px)"),
    )
    aos_duration = models.IntegerField(
        verbose_name=_("Duration"),
        null=True,
        blank=True,
        help_text=_("Duration of animation (ms)"),
    )
    aos_delay = models.IntegerField(
        verbose_name=_("Delay"),
        null=True,
        blank=True,
        help_text=_("Delay animation (ms)"),
    )
    aos_once = models.BooleanField(
        verbose_name=_("Once"),
        null=True,
        help_text=_("Choose wheter animation should fire once, or every time you scroll up/down to element"),
    )
    aos_mirror = models.BooleanField(
        verbose_name=_("Mirror"),
        null=True,
        help_text=_("Choose whether elements should animate out while scrolling past them"),
    )

    # Default id/classes/attributes
    # --------------------------------
    id_name = models.CharField(
        verbose_name=_("ID name"),
        blank=True,
        max_length=255,
    )
    additional_classes = models.CharField(
        verbose_name=_("Additional classes"),
        blank=True,
        max_length=255,
        help_text=_(
            "Additional comma separated list of classes " 'to be added to the element e.g. "row, column-12, clearfix".'
        ),
    )
    attributes = AttributesField(
        verbose_name=_("Attributes"),
        blank=True,
        excluded_keys=["class", "id", "style"],
    )

    def get_additional_classes(self):
        return " ".join(item.strip() for item in self.additional_classes.split(",") if item.strip())

    def __str__(self):
        return ("%s - " % self.aos_animation) + self.aos_anchor_placement + self.id_name or str(self.pk)
