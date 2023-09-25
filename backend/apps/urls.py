from django.urls import path, include

urlpatterns = [
    path('images/', include('apps.picsart.urls')),
    path('auth/', include('apps.users.urls'))
]
