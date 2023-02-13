from django.contrib import admin
from django.urls import path, include
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('fleet/', include('fleet.urls')),
    path('panel/', include('panel.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]
