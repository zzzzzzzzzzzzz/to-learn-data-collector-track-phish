# coding=utf-8
import subprocess
from django.contrib import messages
from django.views.generic import FormView
from .forms import UrlInputForm
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
        with open(filename, 'a') as f:
            f.write(urls)

        subprocess.Popen(['scrapy crawl phish -a filename=%s' % filename], shell=True)

        urls_arr = urls.split('\n')
        filename_external = 'urls_log_external_%d.txt' % timestamp
        with open(filename_external, 'a') as f:
            for line in urls_arr:
                f.write(str(line))

        subprocess.Popen(['scrapy crawl external -a filename=%s' % filename_external], shell=True)
        messages.success(self.request, self.success_message)
        return super(IndexView, self).form_valid(form)  # It's just the httpresponseredirect object
