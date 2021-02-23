"""Third party application configurations."""
from datetime import timedelta

from .environment import env

# DRF
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ],

    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],

    'DEFAULT_VERSIONING_CLASS':
        'rest_framework.versioning.NamespaceVersioning',


    "DEFAULT_VERSION": "v1"
}

#  CORS headers
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'cache-control',
)

# # Simple JWT
# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=60)
# }


# DRF yasg
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        }
    },
    'LOGIN_URL': '/accounts/login',
    'LOGOUT_URL': '/accounts/logout',
    'USE_SESSION_AUTH': True
}

# if env.str('FILE_STORAGE', 'Local') == 'Google':
#     DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
#
# # GCS
# GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
#     env.str('SERVICE_ACCOUNT_NAME', default='petnation-a88f82b652cd.json')
# )
# GS_BUCKET_NAME = env.str('GS_BUCKET_NAME', 'dev-live-media')
# GS_STAGING_BUCKET_NAME = 'dev-staging-media'
# BASE_MEDIA_PATH = 'media'
#
# # Social auth
#
# SOCIAL_AUTH_POSTGRES_JSONFIELD = True
# SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
#
# # Facebook configuration
# SOCIAL_AUTH_FACEBOOK_KEY = env.int('FACEBOOK_KEY')
# SOCIAL_AUTH_FACEBOOK_SECRET = env.str('FACEBOOK_SECRET')
# SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
# SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'fields': 'id, name, email'}
#
# FACEBOOK_EXTENDED_PERMISSIONS = ['email']
# SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']
# SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
#
# # Google configuration
# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = env.str('GOOGLE_OAUTH2_KEY')
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = env.str('GOOGLE_OAUTH2_SECRET')
# SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
#     'https://www.googleapis.com/auth/userinfo.email',
#     'https://www.googleapis.com/auth/userinfo.profile',
# ]
#
# SOCIAL_AUTH_PIPELINE = (
#     'social_core.pipeline.social_auth.social_details',
#     'social_core.pipeline.social_auth.social_uid',
#     'social_core.pipeline.social_auth.auth_allowed',
#     'social_core.pipeline.social_auth.social_user',
#     'social_core.pipeline.user.get_username',
#     'social_core.pipeline.social_auth.associate_by_email',
#     'social_core.pipeline.social_auth.associate_user',
#     'social_core.pipeline.social_auth.load_extra_data',
#     'social_core.pipeline.user.user_details',
# )
#
# # Sendgrid
#
# EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
# SENDGRID_API_KEY = env.str("SENDGRID_API_KEY")
# SENDGRID_SANDBOX_MODE_IN_DEBUG = env.bool('SANDBOX_MODE')
#
# # TODO: change default sender when switching to prod sendgrid account.
# DEFAULT_FROM_EMAIL = env.str('SENDGRID_SENDER', "keaton@dotmodus.com")
