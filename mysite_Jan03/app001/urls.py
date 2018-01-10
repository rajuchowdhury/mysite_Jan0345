from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic import RedirectView


urlpatterns = [
path('admin/', admin.site.urls),
path('app001/', include('app001.urls')),
path('/', RedirectView.as_view(url='/app001/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [

]