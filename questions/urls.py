from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.QuestionList.as_view(), name='question_list'),
    url(r'(?P<pk>\d+)/$', views.QuestionDetail.as_view(), name='question_detail'),
]
