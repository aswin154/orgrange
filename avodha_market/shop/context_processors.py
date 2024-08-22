# context processor for setting default name for web app

# from django.conf import settings


def default_values(request):
    return {
        "app_name": "Avodha Shopping",
        "tagline": "Your go-to platform for buying stuff.",
        "footer_about": "Learn more about our mission, vision, and values.",
        "instagram_url": "#",
        "facebook_url": "#",
        "twitter_url": "#",
        "youtube_url": "#",
    }
