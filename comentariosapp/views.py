from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import render, redirect
from .models import Comentario
from django.views import View
from .forms import ComentarioForm
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

# Create your views here.


class ComentarioList(View):
        
    def get(self, request):
        form=ComentarioForm()
        return render(request, 'comentarios/comentario_list.html', {'form': form})
    
    def post(self, request):
        form=ComentarioForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('confirmacion')
        return render(request, 'comentarios/comentario_list.html', {'form': form})


class Confirmacion(View):

    def get(self, request):
        return render(request, 'comentarios/confirmacion.html')

class Confirmacion(View):

    def get(self, request):
        return render(request, 'comentarios/confirmacion.html')


class TodosComentarios(ListView):

    model = Comentario
    template_name = 'comentarios/todos_comentarios.html'

class ComentarioDetalle(DetailView):

    model = Comentario
    template_name = 'comentarios/comentario_details.html'

class Edit(UpdateView):

    model = Comentario
    fields = ["nombre", "correo", "comentario"]
    template_name = 'comentarios/comentario_edit.html'
    success_url = reverse_lazy("todos_comentarios")

class Delete(DeleteView):

    model = Comentario
    template_name = 'comentarios/comentario_delete.html'
    success_url = reverse_lazy("todos_comentarios")