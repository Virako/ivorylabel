import ckeditor_uploader.fields
from django.db import models


class Content(models.Model):
    about = ckeditor_uploader.fields.RichTextUploadingField('¿Quiénes somos?')
    recording = ckeditor_uploader.fields.RichTextUploadingField('Estudio Online')
    contact = ckeditor_uploader.fields.RichTextUploadingField('Contacto')

    class Meta:
        verbose_name = 'Contenido'
        verbose_name_plural = 'Contenidos'


class Member(models.Model):
    content = models.ForeignKey(Content, verbose_name='Contenido', on_delete=models.CASCADE)
    name = models.CharField('Nombre', max_length=255, unique=True, default='')
    desc = ckeditor_uploader.fields.RichTextUploadingField('Descripción')
    img = models.ImageField('Imágen', upload_to='members/', blank=True, null=True)

    class Meta:
        verbose_name = 'Miembro'
        verbose_name_plural = 'Miembros'


class Service(models.Model):
    content = models.ForeignKey(Content, verbose_name='Contenido', on_delete=models.CASCADE)
    name = models.CharField('Nombre', max_length=255, unique=True, default='')
    desc = ckeditor_uploader.fields.RichTextUploadingField('Descripción')
    icon = models.ImageField('Icono', upload_to='icons/', blank=True, null=True)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'


class Project(models.Model):
    content = models.ForeignKey(Content, verbose_name='Contenido', on_delete=models.CASCADE)
    name = models.CharField('Nombre', max_length=255, unique=True, default='')
    slides = models.TextField('Links de youtube', help_text='Un link por línea')

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
