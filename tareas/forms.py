from django import forms
from django.forms import ModelForm
from .models import Tarea


class TareaForm(forms.ModelForm):

    class Meta:
        model = Tarea
        fields = "__all__"
        labels = {
            "titulo": "Título",
            "descripcion": "Descripción",
            "prioridad": "Prioridad",
            "completada": "Completada",
        }
        widgets = {
            "titulo": forms.TextInput(
                attrs={
                    "class": (
                        "w-full px-4 py-2.5 rounded-xl border border-slate-300"
                        "focus:border-brand-primary focus:ring-2"
                        "focus:ring-blue-500/20 outline-none transition-all"
                        "text-text-main placeholder:text-slate-400 bg-slate-50/50"
                        "focus:bg-white"
                    ),
                    "placeholder": "Título de la actividad",
                }
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "class": (
                        "w-full px-4 py-2.5 rounded-xl border border-slate-300"
                        " focus:border-brand-primary focus:ring-2"
                        " focus:ring-blue-500/20 outline-none transition-all"
                        " text-text-main placeholder:text-slate-400 bg-slate-50/50"
                        " focus:bg-white resize-y min-h-[120px]"
                    ),
                    "placeholder": "Escribe los detalles de la actividad",
                    "rows": 4,
                }
            ),
            "prioridad": forms.Select(
                attrs={
                    "class": (
                        "w-full px-4 py-2.5 rounded-xl border border-slate-300"
                        " focus:border-brand-primary focus:ring-2"
                        " focus:ring-blue-500/20 outline-none transition-all"
                        " text-text-main bg-slate-50/50 focus:bg-white"
                        " cursor-pointer"
                    )
                }
            ),
            "completada": forms.CheckboxInput(
                attrs={
                    "class": (
                        "w-5 h-5 rounded border-slate-300 text-brand-primary"
                        " focus:ring-brand-primary/20 cursor-pointer"
                    )
                }
            ),
        }


# class TareaForm(forms.ModelForm):
#     class Meta:
#         model = Tarea
#         fields = "__all__"
#         labels = {
#             "titulo": "Título",
#             "descripcion": "Descripción",
#             "prioridad": "Prioridad",
#         }
#         widgets = {
#             "titulo": forms.TextInput(
#                 attrs={
#                     "class": "border border-gris  pl-1",
#                     "placeholder": "Actividad",
#                 }
#             ),
#             "descripcion": forms.Textarea(
#                 attrs={
#                     "class": "border border-gris  pl-1",
#                     "placeholder": "Descripción",
#                 }
#             ),
#             "prioridad": forms.Select(attrs={"class": "border border-gris "}),
#             "completada": forms.CheckboxInput(),
#         }
