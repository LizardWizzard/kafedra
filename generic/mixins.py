from django.views.generic.base import ContextMixin
from main.models import Document

class StepsListMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(StepsListMixin, self).get_context_data(**kwargs)
        context["current_url"] = self.request.path
        context['doc'] = Document.objects.get(name='Билеты')
        return context
