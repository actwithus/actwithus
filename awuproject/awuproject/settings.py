
import os

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

SITE_TITLE = "ActWithUs"

MANAGERS = ADMINS

DATABASE_ENGINE = 'postgresql_psycopg2'    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'devdb'
DATABASE_USER = 'devuser'             # Not used with sqlite3.
DATABASE_PASSWORD = 'password'         # Not used with sqlite3.
DATABASE_HOST = 'actwithus-dev.local'             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

TIME_ZONE = 'US/Pacific'

LANGUAGE_CODE = 'en-us'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

LOGIN_REDIRECT_URL = '/'

# Don't share this with anybody.
SECRET_KEY = 'ti7zh7jhmb5^tc-!(+(lf82a3=wqqwbhs^0n&h1pal#(d^(8_-'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

ROOT_URLCONF = 'awuproject.urls'


INSTALLED_APPS = (
    #
    # Django
    'django.contrib.auth',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    #
    # Thirdparty
    'taggit',
    #
    # ActWithUs
    'awucontacts',
    'awufundraiser',
    'awuimport',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), "templates"),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'awuproject.context_processors.media_url',
    'awuproject.context_processors.site_title',
)
