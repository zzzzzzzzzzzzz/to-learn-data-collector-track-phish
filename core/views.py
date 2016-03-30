from django.views.generic import TemplateView
from django.db.models import Q
from question.models import Question, Category
from answers.models import Answer


class IndexView(TemplateView):

    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['last_questions'] = Question.objects.filter(is_published=True)[:5]
        context['last_answers'] = Answer.objects.filter(question__is_published=True)[:5]
        context['categories'] = Category.objects.all()
        return context
