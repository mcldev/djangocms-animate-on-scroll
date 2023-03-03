Django Animate on Scroll
========================

An extension for Django CMS that adds the aos library to animate elements on your page as you scroll.

Installation
------------

1. Install with pip ``pip install djangocms-animate-on-scroll``

2. Add ``djangocms_animate_on_scroll`` to INSTALLED_APPS

3. Run migrations ``python manage.py migrate``


Usage
-----

After installation simply add the plugins to the page.

Depending your configuration, you will probably need to specify the plugins in your `CMS_PLACEHOLDER_CONF` setting:

.. code:: python

    CMS_PLACEHOLDER_CONF = {
        'content': {
            #...
            'plugins': [
                #..., 
                'AnimateOnScroll_Anchor_Plugin', 
                'AnimateOnScroll_Element_Plugin'
            ],
            #...
        },
    }

Configuration
-------------

You can define the initial and default settings of AOS with the `AOS_INIT_PARAMS` setting:

.. code:: python

    # settings.py

    AOS_INIT_PARAMS = {
        "easing": "ease",
        "disable": False,
        "offset": 120,
        "duration": 400,
        "delay": 0,
        "once": False,
        "mirror": False,
        "anchor-placement": "top-bottom",
    }


All settings from https://github.com/michalsnik/aos#1-initialize-aos can be specified.
