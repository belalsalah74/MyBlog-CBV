from django.conf import settings
from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('articles/', include('articles.urls')),
    path('',include('accounts.urls')),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
