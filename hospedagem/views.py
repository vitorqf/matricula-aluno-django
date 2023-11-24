from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Hospedagem
from .forms import HospedagemFilterForm, HospedagemForm
from django.urls import reverse_lazy

# Create your views here.
class HospedagemListView(ListView):
    model = Hospedagem
    template_name = 'hospedagem/hospedagens.html'
    context_object_name = 'hospedagens'
    paginate_by = 3
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = HospedagemFilterForm(self.request.GET) 
        return context
    
class HospedagemCreateView(CreateView):
    model = Hospedagem
    template_name = 'hospedagem/form.html'
    form_class = HospedagemForm
    success_url = reverse_lazy('hospedagem_listar')
    
class HospedagemDetailView(DetailView):
    model = Hospedagem
    template_name = 'hospedagem/hospedagem_detalhar.html'
    context_object_name = 'hospedagem'
    
class HospedagemUpdateView(UpdateView):
    model = Hospedagem
    template_name = 'hospedagem/form.html'
    form_class = HospedagemForm
    success_url = reverse_lazy('hospedagem_listar')
    
class HospedagemDeleteView(DeleteView):
    model = Hospedagem
    success_url = reverse_lazy('hospedagem_listar')
    
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
