from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Sala

@login_required
def home(request):
	return render(request, 'home.html', {'salas': Sala.objects.all()})