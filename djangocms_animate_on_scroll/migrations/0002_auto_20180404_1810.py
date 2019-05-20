# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_aos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animateonscroll_element',
            name='aos_anchor',
            field=models.ForeignKey(related_name='aos_anchor', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='djangocms_animate_on_scroll.AnimateOnScroll_Anchor', help_text='Anchor element, whose offset will be counted to trigger animation instead of actual elements offset', null=True, verbose_name='Animate On Scroll Anchor'),
        ),
    ]
