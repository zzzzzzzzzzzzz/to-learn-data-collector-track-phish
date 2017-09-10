from django.conf.urls import url, include
from django.contrib import admin


from core.views import IndexView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^core/', include('core.urls', namespace='core')),
    url(r'^$', IndexView.as_view(), name='index'),
]
