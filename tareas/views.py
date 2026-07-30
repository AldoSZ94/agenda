from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarea
from .forms import TareaForm


def lista_tareas(request):
    tareas = Tarea.objects.all().order_by("id")
    paginator = Paginator(tareas, 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request, "tareas/lista_tareas.html", {"tareas": tareas, "page_obj": page_obj}
    )


def editar_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, pk=tarea_id)
    form = TareaForm(request.POST or None, instance=tarea)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("lista_tareas")
    return render(
        request, "tareas/formulario.html", {"form": form, "titulo": "Editar tarea"}
    )


def eliminar_tarea(request, tarea_id):
    tarea = Tarea.objects.get(pk=tarea_id)
    if request.method == "POST":
        tarea.delete()
        return redirect("lista_tareas")
    return render(request, "tareas/eliminar_tarea.html", {"tarea": tarea})


def nueva_tarea(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_tareas")
    else:
        form = TareaForm()

    return render(request, "tareas/formulario.html", {"form": form})
