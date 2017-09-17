# coding=utf-8
import subprocess
from django.contrib import messages
from django.views.generic import FormView
from .forms import UrlInputForm
import io
import os.path
import time


class IndexView(FormView):
    template_name = 'core/index.html'
    success_url = '/'
    success_message = u'URL-ы успешно добавлены и отправлены на анализ, спасибо большое, продолжайте в том же духе, ' \
                      u'пожалуйста =) '
    form_class = UrlInputForm

    def form_valid(self, form):
        timestamp = int(time.time())
        urls = form.cleaned_data['urls']
        filename = 'urls_log_%d.txt' % timestamp
        with io.open(filename, 'a', encoding='utf-8') as file:
            file.write(urls)

        subprocess.Popen(['scrapy crawl phish -a filename=%s' % filename], shell=True)
        messages.success(self.request, self.success_message)
        return super(IndexView, self).form_valid(form) # It's just the httpresponseredirect object
