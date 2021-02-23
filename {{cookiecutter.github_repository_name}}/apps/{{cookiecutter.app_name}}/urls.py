"""Social app url configuration."""
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
# from rest_framework_simplejwt.views import TokenRefreshView

from . import views
from . import viewsets

router = routers.DefaultRouter()

urlpatterns = [
    path('', include((router.urls, '{{ cookiecutter.app_name }}'), '{{ cookiecutter.app_name }}'), name='{{ cookiecutter.app_name }}-root'),
    # path('api/token/', views.TokenObtainPairWithIDView.as_view(),
    #      name='token_obtain_pair'),
    # path('api/refresh/', TokenRefreshView.as_view(),
    #      name='token_refresh'),
    # path('activate/<uidb64>/<token>', views.ActivateAccountView.as_view(),
    #      name='activate'),
    # path('password-reset', views.PasswordResetView.as_view(),
    #      name='password-reset'),
    # path('password-change/<uidb64>/<token>',
    #      views.PasswordChangeView.as_view(), name='password-change'),
    # path('health-check', views.HealthCheckView.as_view(), name='health-check'),
    # path('oauth/', views.SocialLoginView.as_view(), name='oauth'),
    # path('upload-media/', views.UploadMediaView.as_view(), name='upload-media')
]
