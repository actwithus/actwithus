from django.conf import settings


def media_url(context):
    return dict(MEDIA_URL=settings.MEDIA_URL)


def site_title(context):
    return dict(SITE_TITLE=settings.SITE_TITLE)
