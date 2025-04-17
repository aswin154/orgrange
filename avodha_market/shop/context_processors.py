# context processor for setting default name for web app

# from django.conf import settings


def default_values(request):
    return {
        "app_name": "OrgranGe",
        "tagline": "Home for all your shopping",
        "footer_about": "This is only a test website. Not an actual e-commerce platform.",
        "social_1": "Instagram",
        "social_1_url": "#",
        "social_2": "Youtube",
        "social_2_url": "#",
    }
