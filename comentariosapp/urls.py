from django.urls import path
from . import views
from .views import ComentarioList, TodosComentarios, Confirmacion, ComentarioDetalle, Edit, Delete

urlpatterns = [
    path('',ComentarioList.as_view(), name='comentario_list'),
    path('confirmacion', Confirmacion.as_view(), name='confirmacion'),
    path('todos_comentarios', TodosComentarios.as_view(), name='todos_comentarios'),
    path('comentario/<int:pk>/', ComentarioDetalle.as_view(), name='comentario_details'),
    path('comentario/<int:pk>/edit/', Edit.as_view(), name='comentario_edit'),
    path('comentario/<int:pk>/delete/', Delete.as_view(), name='comentario_delete'),
]