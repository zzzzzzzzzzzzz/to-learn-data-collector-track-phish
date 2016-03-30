from django.conf.urls import url
import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', views.QuestionList.as_view(), name='question_list'),
    url(r'^create/$', login_required(views.QuestionCreate.as_view()), name='question_create'),
    url(r'^(?P<pk>\d+)/$', views.QuestionDetail.as_view(), name='question_detail'),
    url(r'^categories/(?P<pk>\d+)/$', views.CategoryDetail.as_view(), name='category_detail'),
    url(r'^(?P<pk>\d+)/update/$', views.QuestionUpdate.as_view(), name='question_update'),
]
