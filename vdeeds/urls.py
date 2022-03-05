from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('vdeed_app.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('index/', include('vdeed_app.urls')),
    path('view_offerings/', include('vdeed_app.urls')),
    path('view_merits/', include('vdeed_app.urls')),
    path('view_merits_detail/', include('vdeed_app.urls')),
    path('view_home/', include('vdeed_app.urls')),
    path('view_add_counter/', include('vdeed_app.urls')),
]
