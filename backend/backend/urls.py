from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('apps.users.urls')),
    path('api/shop/', include('apps.shop.urls')),
    re_path(r'.*', TemplateView.as_view(template_name="index.html")),
]
