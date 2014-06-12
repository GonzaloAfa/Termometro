#encoding:utf-8
"""
Django settings for termometro project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url

BASE_DIR        = os.path.dirname(os.path.abspath(__file__))
SITE_ROOT       = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n%k_1#-q7o97j&4$2e*3+*3u=obs62e!v4776igmv7ycb+p(mg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []
SITE_ID = 1

# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrapform',
    'registrarse',
    'preguntar',
    'comentario',
    'social.apps.django_app.default',
    'django.contrib.sites',
    'login',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'termometro.urls'

WSGI_APPLICATION = 'termometro.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE'    : 'django.db.backends.sqlite3',
        'NAME'      : 'database-SQLi.db',
        'USER'      : '',
        'PASSWORD'  : '',
        'HOST'      : '',
        'PORT'      : '',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE'    : 'django.db.backends.postgresql_psycopg2',
#         'NAME'      : 'd7mtcl7epem3m',
#         'USER'      : 'cgoajpyealkokc',
#         'PASSWORD'  : 'TaIxmHmNzhlzPIbO5DfS7lH0WK',
#         'HOST'      : 'ec2-54-83-14-68.compute-1.amazonaws.com',
#         'PORT'      : '5432',
#     }
# }
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
# 'django.template.loaders.eggs.Loader',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
 )

STATICFILES_DIRS = (
    os.path.join(SITE_ROOT,'static_root','static'),
)


TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT,'templates'),
)


# Parse database configuration from $DATABASE_URL
#DATABASES['default'] =  dj_database_url.config(default=os.environ['DATABASE_URL'])

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']


MEDIA_ROOT = os.path.normpath(os.path.join(SITE_ROOT,'media'))
MEDIA_URL = '/media/'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, 'static'),
)

#Authentications things with django-social-auth



AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'django.contrib.auth.context_processors.auth',

)
SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'
URL_PATH = 'http://megafono.herokuapp.com'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/logged-in/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/login-error/'
SOCIAL_AUTH_LOGIN_URL = '/login-url/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/new-user-redirect-url'
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/new-association-redirect-url/'
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/account-disconnected-redirect-url/'
SOCIAL_AUTH_INACTIVE_USER_URL = '/inactive-user/'


#In case of need a custom user model
AUTH_USER_MODEL = 'login.CustomUser'

#Media providers special configuration
#Facebook
SOCIAL_AUTH_FACEBOOK_KEY = '644854592229779' 
SOCIAL_AUTH_FACEBOOK_SECRET = 'b480d65d080a2fc92fc405c3ca481da6'
SOCIAL_AUTH_FACEBOOK_APP_NAMESPACE = 'megafonoci'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    #'social.pipeline.mail.mail_validation',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)