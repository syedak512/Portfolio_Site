
from django.contrib import admin
from django.urls import path, include
#from quote_generator import views
from portfolio import views
# from exc...
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', views.home, name='home'),
   
    #path('about/', views.about, name='about'),
    #path('exchange_rate/', views.index, name='index'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
