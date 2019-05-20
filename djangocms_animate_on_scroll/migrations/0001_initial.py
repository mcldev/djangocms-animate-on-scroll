# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_attributes_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimateOnScroll_Anchor',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='djangocms_aos_animateonscroll_anchor', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('id_name', models.CharField(max_length=255, verbose_name='ID name')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='AnimateOnScroll_Element',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='djangocms_aos_animateonscroll_element', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('aos_animation', models.CharField(help_text='Script will trigger "animation_name" animation on this element, if you scroll to it.', max_length=255, verbose_name='AOS Animation')),
                ('aos_easing', models.CharField(help_text='Choose timing function to ease elements in different ways', max_length=255, verbose_name='Anchor Easing', blank=True)),
                ('aos_anchor_placement', models.CharField(help_text='Anchor placement - which one position of element on the screen should trigger animation', max_length=255, verbose_name='Anchor Placement', blank=True)),
                ('aos_offset', models.IntegerField(default=120, help_text='Change offset to trigger animations sooner or later (px)', verbose_name='Offset')),
                ('aos_duration', models.IntegerField(default=400, help_text='*Duration of animation (ms)', verbose_name='Duration')),
                ('aos_delay', models.IntegerField(default=0, help_text='Delay animation (ms)', verbose_name='Delay')),
                ('aos_once', models.BooleanField(default=False, help_text='Choose wheter animation should fire once, or every time you scroll up/down to element', verbose_name='Once')),
                ('id_name', models.CharField(max_length=255, verbose_name='ID name', blank=True)),
                ('additional_classes', models.CharField(help_text='Additional comma separated list of classes to be added to the element e.g. "row, column-12, clearfix".', max_length=255, verbose_name='Additional classes', blank=True)),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True)),
                ('aos_anchor', models.ForeignKey(related_name='aos_anchor', blank=True, to='djangocms_animate_on_scroll.AnimateOnScroll_Anchor', help_text='Anchor element, whose offset will be counted to trigger animation instead of actual elements offset', null=True, verbose_name='Animate On Scroll Anchor')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
