from django.urls import reverse
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404
from .models import Table, Column

class ColumnCreateView(CreateView):
    model = Column
    fields = ('name', )
    template_name = 'create.html'

    def form_valid(self, form):
        # テーブルを置く
        table = get_object_or_404(Table, pk=self.kwargs.get('pk'))
        form.instance.table = table

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('inputs:table', kwargs={'pk': self.kwargs.get('pk')})