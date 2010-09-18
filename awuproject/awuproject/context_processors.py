from django.conf import settings


def site_title(context):
    return dict(SITE_TITLE=settings.SITE_TITLE)
