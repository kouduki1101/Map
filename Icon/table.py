from django.views.generic import CreateView
from django.urls import reverse
from .models import Table

class TableCreateView(CreateView):
    """テーブル作成"""
    model = Table
    fields = ('name', )
    template_name = 'create.html'

    def get_success_url(self):
        return reverse('table', kwargs={'pk': self.object.id})