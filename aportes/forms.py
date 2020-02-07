from django import forms
from .models import Aporte


class AporteModelForm(forms.ModelForm):
	class Meta:
		model = Aporte
		fields = ['monto', 'concepto', 'comentario']

