from django.views.generic import ListView, DetailView
from .models import Question


class QuestionDetail(DetailView):

    template_name = 'questions/question_detail.html'
    model = Question


class QuestionList(ListView):

    template_name = 'questions/question_list.html'
    model = Question
