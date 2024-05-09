from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Sca

# CRUD

class ScaListView(ListView):
    model = Sca
    
class ScaCreateView(CreateView):
    model = Sca
    fields = ["nome", "cpf", "matricula", "curso"]
    success_url = reverse_lazy("sca_list")
    
class ScaUpdateView(UpdateView):
    model = Sca
    fields = fields = ["nome", "cpf", "matricula", "curso"]
    success_url = reverse_lazy("sca_list")
    
class ScaDeleteView(DeleteView):
    model = Sca
    success_url = reverse_lazy("sca_list")