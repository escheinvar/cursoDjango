from django.db import models
from aplicaciones.departamento.models import Departamento
#from ckeditor.fields import RichTextField

######################################## TABLA DE HABILIDADES
class Habilidades (models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'habilidad una'
        verbose_name_plural ='Habilidades todas'

    def __str__(self):
        return str(self.id)+'-'+self.habilidad

######################################## TABLA DE EMPLEADOS
class Empleado(models.Model):
    JOB_CHOICES =(
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Programador'),
        ('4', 'Ingeniero'),
        ('5', 'Abogado'),
        ('6', 'Licenciado'),
    )
    BORRAR =(
        ('0', 'Activo'),
        ('1', 'Borrado'),
    )
    first_name = models.CharField('Nombre(s)', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField('Nombre completo', max_length=122, blank=True)
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='archivos', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    #hoja_vida = RichTextField()
    activo = models.CharField('Activo', max_length=1, choices=BORRAR, default='0')

    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural ='Mis Empleados todos'
        ordering = ['first_name','last_name']
        unique_together = ('first_name', 'departamento')

    def __str__(self):
        return str(self.id)+'-'+self.first_name+'-'+self.last_name 