from django.contrib import admin
from django.urls import path, include

from apps.accounts import urls as urls_account, views as views_account


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include(urls_account)),
    path('',  views_account.dashboard, name='dashboard')
]
