from pathlib import Path
import os
import pymysql
import openpyxl
pymysql.install_as_MySQLdb()
from django.contrib import messages
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')
MEDIA_DIR = os.path.join(BASE_DIR,'media')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd*8x97+1&+ea&x9=*1ay*b6v&lr14u7l*g6*+#b@oummi^&&z^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Exam.student',

    'Exam.course',
    'Exam.resultprocessing',
    'Exam.studentPreferences',
    'Exam.questions',
    'Exam.faculty',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'examProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'examProject.wsgi.application'


# Database
#https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Marine_Exam_Portal',
        'USER': 'postgres',
        'PASSWORD': 'Afreen@387',
        'HOST': 'localhost',  # Replace with your PostgreSQL server's address if necessary
        'PORT': '5432',          # Leave empty to use the default PostgreSQL port (usually 5432)
    }
}
'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_mysql_db',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',  # or your MySQL server host
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'STRICT_TRANS_TABLES',
        },
    }
}'''






# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS':{'min_length':9}
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE =  'Asia/Calcutta'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'examProject/static')
]
STATIC_ROOT = os.path.join(BASE_DIR,'static')

MESSAGE_TAGS = {
    messages.ERROR : 'danger',
}

MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'

# Media settings
#MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
#EMAIL_HOST = os.environ.get('EMAIL_HOST')
#EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
#EMAIL_USE_TLS = True
#DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
#EMAIL_PORT = 587
#EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')


# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'jishanmd387@gmail.com'
EMAIL_HOST_PASSWORD = 'uhzl qlch gfzc lzwx'  # Use app-specific password if 2FA is enabled
DEFAULT_FROM_EMAIL = 'jishanmd387@gmail.com'
