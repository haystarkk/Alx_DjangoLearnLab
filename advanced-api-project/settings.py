# Must contain these key configurations
INSTALLED_APPS = [
    ...
    'rest_framework',
    'api',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
