from django.views.generic import FormView
from .forms import UrlInputForm
from django.shortcuts import resolve_url
from django.http import JsonResponse
import os.path


class IndexView(FormView):
    template_name = 'core/index.html'
    form_class = UrlInputForm

    def form_valid(self, form):
        urls = str(form.cleaned_data['urls'])
        urls_log_file = open(os.path.dirname(__file__) + '/../urls_log.txt', 'a')
        urls_log_file.write(urls)
        urls_log_file.write(",\n")
        urls_log_file.close()
        return JsonResponse({'urls': urls})
