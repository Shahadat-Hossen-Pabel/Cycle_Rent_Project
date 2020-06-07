from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from home.views import home_view
from about.views import about_view
from contact.views import contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('go_for_rent/', include('rent.urls', namespace='rent')),
    path('', home_view, name="home"),
    path('about/', about_view, name="about"),
    path('contact/', contact_view, name="contact"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
