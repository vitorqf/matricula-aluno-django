"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aluno.views import IndexView, AlunoEditar, AlunoCriar, AlunoRemover, AlunoListar
from hospedagem.views import HospedagemListView, HospedagemCreateView, HospedagemUpdateView, HospedagemDeleteView, HospedagemDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexView.as_view(), name='index'),
    path('aluno/editar/<int:id>/',AlunoEditar.as_view(), name='aluno_editar'),
    path('aluno/criar/',AlunoCriar.as_view(), name='aluno_criar'),
    path('aluno/remover/<int:id>/',AlunoRemover.as_view(), name='aluno_remover'),
    path('aluno/listar/',AlunoListar.as_view(), name='aluno_listar'),
    
    path('hospedagem/listar/',HospedagemListView.as_view(), name='hospedagem_listar'),
    path('hospedagem/criar/',HospedagemCreateView.as_view(), name='hospedagem_criar'),
    path('hospedagem/editar/<int:pk>/',HospedagemUpdateView.as_view(), name='hospedagem_editar'),
    path('hospedagem/remover/<int:pk>/',HospedagemDeleteView.as_view(), name='hospedagem_remover'),
    path('hospedagem/detalhes/<int:pk>/',HospedagemDetailView.as_view(), name='hospedagem_detalhar'),

]



