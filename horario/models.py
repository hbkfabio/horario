from django.db import models
from parametros.models import (Periodo,
                             Profesor,
                             Modulo,
                             Bloque,
                             Carrera,
                             Plan,
                              )
# Create your models here.

class PeriodoProfesorModulo(models.Model):
    carrera = models.ForeignKey(Carrera, default=None)
    plan = models.ForeignKey(Plan, default=None)
    periodo = models.ForeignKey(Periodo, default=None)
    modulo = models.ForeignKey(Modulo, default=None)
    profesor = models.ForeignKey(Profesor, default=None)

    def __str__(self):
        return ('%s %s %s')%(self.periodo, self.profesor, self.modulo)


class Horario(models.Model):
    periodoprofesormodulo = models.ForeignKey(PeriodoProfesorModulo)
    bloque1 = models.CharField(max_length=1)
    bloque2 = models.CharField(max_length=1)
    bloque3 = models.CharField(max_length=1)
    bloque4 = models.CharField(max_length=1)
    bloque5 = models.CharField(max_length=1)
    bloque6 = models.CharField(max_length=1)
    bloque7 = models.CharField(max_length=1)
    bloque8 = models.CharField(max_length=1)
    bloque9 = models.CharField(max_length=1)
    bloque10 = models.CharField(max_length=1)
    dia_semana = models.CharField(max_length=20, default="")



class ReservaBloqueProtegido(models.Model):
    bloque = models.ForeignKey(Bloque, default=None)
    reservado = models.BooleanField(default=False)

    class Meta:
        ordering = ["bloque"]
