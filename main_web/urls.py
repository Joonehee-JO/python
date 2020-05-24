from django.contrib import admin
from django.urls import path, include
from main import views
from login import urls
from category import urls as category_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
    path('login/', include(urls)),
    path('category/', include(category_urls)),
]
