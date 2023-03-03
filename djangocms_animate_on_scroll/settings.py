import json

from django.conf import settings

# Settings possible: https://github.com/michalsnik/aos#1-initialize-aos
DEFAULT_AOS_PARAMS = {
    "easing": "ease",
    "disable": False,
    "offset": 120,
    "duration": 400,
    "delay": 0,
    "once": False,
    "mirror": False,
    "anchor-placement": "top-bottom",
}


def get_aos_init_params():
    return {**DEFAULT_AOS_PARAMS, **getattr(settings, "AOS_INIT_PARAMS", {})}


def get_aos_init_params_js():
    return json.dumps(get_aos_init_params())
