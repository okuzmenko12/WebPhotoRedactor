from django.urls import path, include

from drf_spectacular.views import (SpectacularAPIView,
                                   SpectacularRedocView,
                                   SpectacularSwaggerView)

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('images/', include('apps.picsart.urls')),
    path('auth/', include('apps.users.urls')),
    path('payments/', include('apps.payments.urls')),
    path('main/', include('apps.main.urls'))
]
