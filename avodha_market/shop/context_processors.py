# context processor for setting default name for web app

# from django.conf import settings


def default_values(request):
    return {
        "app_name": "Avodha Shopping",
        "tagline": "Your go-to platform for online shopping",
        "footer_about": "Learn more about our mission, vision and values.",
        "social_1": "Facebook",
        "social_1_url": "#",
        "social_2": "Youtube",
        "social_2_url": "#",
    }
