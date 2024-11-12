from django.db import models

class ClassNameModel(models.Model):
    classname_code = models.CharField(verbose_name="N° Clase superior", primary_key=True, max_length=18)

    def __str__(self) -> str:
        return self.classname_code
    
class ChildNameModel(models.Model):
    childname_code = models.CharField(verbose_name="N° Clase inferior", primary_key=True, max_length=18)

    def __str__(self) -> str:
        return self.childname_code

# Create your models here.
class MerchStructure(models.Model):
    custom_primary_key = models.SlugField(primary_key=True, blank=True)
    classname = models.ForeignKey(ClassNameModel, on_delete=models.CASCADE)
    childname = models.ForeignKey(ChildNameModel, on_delete=models.CASCADE)
    description = models.CharField(verbose_name="Descripción", max_length=40)
    hier_level = models.IntegerField(verbose_name="Nivel en jerarquía")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

    @property
    def make_key(self):
        new_key = str(self.classname.classname_code + self.childname.childname_code)
        return new_key

    def save(self, *args, **kwargs):
        self.custom_primary_key = self.make_key
        super(MerchStructure, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Estructura de Mercadería"
        verbose_name_plural = "Estructura de Mercaderías"