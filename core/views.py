from django.views.generic import FormView
from .forms import UrlInputForm
from django.shortcuts import resolve_url
from django.http import JsonResponse


class IndexView(FormView):
    template_name = 'core/index.html'
    form_class = UrlInputForm

    def form_valid(self, form):
        return JsonResponse({'urls': str(form.cleaned_data['urls'])})
