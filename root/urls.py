from django.contrib import admin
from django.urls import path, include
from root.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('blog/', include('blog.urls')),  # add blog path
    path('event/', include('event.urls')),  # add event path
]
