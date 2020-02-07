from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from familias.models import Niñe
from .models import Aporte

# Create your views here.

class AporteCreateViewCreate(LoginRequiredMixin, CreateView):
    model = Aporte
    fields = ['monto', 'concepto', 'comentario']

    def form_valid(self, form):
        niñe = get_object_or_404(Niñe, pk=self.kwargs.get('niñe_id'))
        form.instance.niñe = niñe
        form.instance.cobrado_por = self.request.user
        form.instance.status = 'cobrado'
        return super().form_valid(form)



