from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_tareas, name="lista_tareas"),
    path("editar_tarea/<int:tarea_id>", views.editar_tarea, name="editar_tarea"),
    path("nueva_tarea/", views.nueva_tarea, name="nueva_tarea"),
    path("eliminar_tarea/<int:tarea_id>/", views.eliminar_tarea, name="eliminar_tarea"),
]
