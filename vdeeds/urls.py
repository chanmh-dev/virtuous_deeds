from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('vdeed_app.urls')),
    path('index/', include('vdeed_app.urls')),
    path('admin/', admin.site.urls),
]
