# リスト4-8:修正。(1-B)アプリの言語、時間とアップロードファイル保存先に関する環境設定
# import
import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-#@gvrw@&el(%ejf=v_xn^p(=jpow2#6dhoa7g0nje1bxd^g_dm"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3.2.3 Djangoアプリの登録、図3-9:アプリの登録
    "datashare",
    # リスト4-25:追加。4.6.1 ユーザ認証のテスト実装、(1)手順1:アプリケーションaccountの登録
    "account.apps.AccountConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project_gis2.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # リスト4-26:修正。
        #"DIRS": [],4.6.1 ユーザ認証のテスト実装、(2)手順2:
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project_gis2.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
# リスト4-2:projcct_gis/settings.py。4.3.2 ユーザモデルのデータベース移行、(1)手順1:PostgreSQLの使用設定
DATABASES = {
    "default": {
        "ENGINE":"django.db.backends.postgresql",
        "NAME":"project_gis_db",
        "USER":"taka648",
        "PASSWORD":"Akie2Suzuki", 
        "PORT":"5432", 
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

# リスト4-8:修正。(1-B)アプリの言語、時間とアップロードファイル保存先に関する環境設定
# LANGUAGE_CODE = "en-us"
# TIME_ZONE = "UTC"
LANGUAGE_COOE = "ja"
TIME_ZONE = "Asia/Tokyo"

USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# リスト4-8:修正。(1-B)アプリの言語、時間とアップロードファイル保存先に関する環境設定
#STATIC_URL = "static/"
STATIC_URL = "/static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# リスト4-8:修正。(1-B)アプリの言語、時間とアップロードファイル保存先に関する環境設定
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# リスト4-27:追加。4.6.1 ユーザ認証のテスト実装、(2)手順2:
#LOGIN_URL = "account:login"
#LOGIN_REDIRECT_URL = "account:top"
# リスト4-42:変更。4.6.2 アプリケーションdatashareにおけるユーザ認証機能の実装、(5)手順5:
LOGIN_URL = 'datashare:login'
LOGIN_REDIRECT_URL = 'datashare:mypage_db' #リスト4-42:変更
