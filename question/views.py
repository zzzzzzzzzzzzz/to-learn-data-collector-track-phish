from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Question, Category
from django.db.models import Q
from answers.models import Answer
from .forms import QuestionListForm
from django.shortcuts import resolve_url, get_object_or_404


class CategoryDetail(DetailView):

    model = Category
    template_name = 'questions/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        context['questions'] = self.object.questions.filter(is_published=True)
        return context


class QuestionCreate(CreateView):

    model = Question
    template_name = 'questions/question_create.html'
    fields = ('category', 'title', 'text', 'is_published')
    context_object_name = 'question'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(QuestionCreate, self).form_valid(form)

    def get_success_url(self):
        return resolve_url('questions:question_detail', pk=self.object.pk)


class QuestionUpdate(UpdateView):

    template_name = 'questions/question_update.html'
    model = Question
    fields = ('category', 'title', 'text', 'is_published')
    context_object_name = 'question'

    def get_queryset(self):
        return super(QuestionUpdate, self).get_queryset().filter(author=self.request.user)

    def get_success_url(self):
        return resolve_url('questions:question_detail', pk=self.object.pk)


class QuestionDetail(CreateView):

    template_name = 'questions/question_detail.html'
    model = Answer
    fields = ('text', )
    context_object_name = 'answer'

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.question = get_object_or_404(Question.objects.all(), pk=pk)
        return super(QuestionDetail, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.question = self.question
        form.instance.author = self.request.user
        return super(QuestionDetail, self).form_valid(form)

    def get_success_url(self):
        return resolve_url("questions:question_detail", pk=self.question.pk)

    def get_context_data(self, **kwargs):
        context = super(QuestionDetail, self).get_context_data(**kwargs)
        context['question'] = self.question
        return context


class QuestionList(ListView):

    template_name = 'questions/question_list.html'
    model = Question
    context_object_name = 'questions'

    def dispatch(self, request, *args, **kwargs):
        self.form = QuestionListForm(request.GET)
        self.form.is_valid()
        self.search = self.form.cleaned_data.get('search')
        self.sort_field = self.form.cleaned_data.get('sort_field')
        return super(QuestionList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(QuestionList, self).get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def get_queryset(self):
        queryset = super(QuestionList, self).get_queryset()
        if self.request.user.is_authenticated():
            queryset = queryset.filter(Q(author=self.request.user) | Q(is_published=True))
        else:
            queryset = queryset.filter(is_published=True)
        if self.search:
            queryset = queryset.filter(Q(title__icontains=self.search) | Q(text__icontains=self.search))
        if self.sort_field:
            queryset = queryset.order_by(self.sort_field)
        return queryset
