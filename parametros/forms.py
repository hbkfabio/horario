from django import forms
from django.db.models import Q
from .sectioned_form import SectionedForm
from .models import (
    Carrera,
    Departamento,
    Plan,
    Modulo,
    Anio,
    Periodo,
    Bloque,
    Profesor,
    Semestre,
    Actividad,
)


import inspect


def retrieve_name(var):
        """
        Gets the name of var. Does it from the out most frame inner-wards.
        :param var: variable to get name from.
        :return: string
        """
        for fi in reversed(inspect.stack()):
            names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
            if len(names) > 0:
                return names[0]

def valida_campo(modelo, campo, valor):
    varname_campo = retrieve_name(campo)
    n = self.cleaned_data.get(varname_campo)
    query = modelo.objects.all().filter(campo = n)
    if query.exists():
        raise forms.ValidationError("%s ya se ha ingresado"%n)
        return False
    else:
        return n


class MaestroForm(forms.ModelForm):

    class Meta:
        model = None
        fields = ["nombre", "descripcion"]


class DepartamentoForm(MaestroForm):

     MaestroForm.Meta.model = Departamento


class CarreraForm(MaestroForm):

    MaestroForm.Meta.model = Carrera


class PlanForm(forms.ModelForm):

    class Meta:
        model = Plan
        fields = ["nombre", "carrera"]


class ModuloForm(forms.ModelForm):

    class Meta:
        model = Modulo

        fields = ["nombre",
                    "semestre",
                    "plan",
                    "horas_clase",
                    "horas_seminario",
                    "horas_laboratorio",
                    "horas_taller",
                    "horas_ayudantia",
                 ]


class AnioForm(forms.ModelForm):

    class Meta:
        model = Anio
        fields = ["nombre"]


class PeriodoForm(forms.ModelForm):

    class Meta:
        model = Periodo
        fields = ["nombre", "anio"]


class BloqueForm(forms.ModelForm):

    class Meta:
        model = Bloque
        fields = ["nombre"]


class ProfesorForm(forms.ModelForm):

    class Meta:
        model = Profesor
        fields = ["nombre", "rut", "correo", "departamento"]



class SemestreForm(forms.ModelForm):

    class Meta:
        model = Semestre
        fields = ["nombre"]



class ActividadForm(forms.ModelForm):

    class Meta:
        model = Actividad
        fields = ["nombre",
                "identificador",]

    def clean_nombre(self):
        n = self.cleaned_data.get("nombre")
        # n = cleaned_data("nombre")
        pk = self.instance.pk
        print (pk)
        query = Actividad.objects.all().filter(nombre = n)
        query = query.filter(~Q(id=pk))
        if query.exists():
            raise forms.ValidationError("%s ya se ha ingresado"%n)
        return n
