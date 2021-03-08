from os import path
from typing import Any

import ckeditor_uploader.fields
from django.conf import settings
from django.db import models


class Content(models.Model):
    about = ckeditor_uploader.fields.RichTextUploadingField('¿Quiénes somos?')
    recording = ckeditor_uploader.fields.RichTextUploadingField('Estudio Online')
    contact = ckeditor_uploader.fields.RichTextUploadingField('Contacto')

    class Meta:
        verbose_name = 'Contenido'
        verbose_name_plural = 'Contenidos'

    @property
    def json(self) -> dict[str, Any]:
        return {
            'about': self.about,
            'recording': self.recording,
            'contact': self.contact,
            'members': [member.json for member in self.members.all()],
            'services': [service.json for service in self.services.all()],
            'projects': [project.json for project in self.projects.all()]
        }


class Member(models.Model):
    content = models.ForeignKey(
        Content,
        verbose_name='Contenido',
        related_name='members',
        on_delete=models.CASCADE
    )
    name = models.CharField('Nombre', max_length=255, unique=True, default='')
    desc = ckeditor_uploader.fields.RichTextUploadingField('Descripción')
    img = models.ImageField('Imágen', upload_to='members/', blank=True, null=True)

    class Meta:
        verbose_name = 'Miembro'
        verbose_name_plural = 'Miembros'

    @property
    def json(self) -> dict[str, str]:
        return {
            'name': self.name,
            'desc': self.desc,
            'img': path.join(settings.MEDIA_URL, self.img.url) if self.img else ''
        }


class Service(models.Model):
    content = models.ForeignKey(
        Content,
        verbose_name='Contenido',
        related_name='services',
        on_delete=models.CASCADE
    )
    name = models.CharField('Nombre', max_length=255, unique=True, default='')
    desc = ckeditor_uploader.fields.RichTextUploadingField('Descripción')
    icon = models.ImageField('Icono', upload_to='icons/', blank=True, null=True)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    @property
    def json(self) -> dict[str, str]:
        return {
            'name': self.name,
            'desc': self.desc,
            'icon': path.join(settings.MEDIA_URL, self.icon.url) if self.icon else ''
        }


class Project(models.Model):
    content = models.ForeignKey(
        Content,
        verbose_name='Contenido',
        related_name='projects',
        on_delete=models.CASCADE
    )
    name = models.CharField('Nombre', max_length=255, unique=True, default='')
    slides = models.TextField('Links de youtube', help_text='Un link por línea')

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

    @property
    def json(self) -> dict[str, Any]:
        return {
            'name': self.name,
            'slides': [url.strip() for url in self.slides.split('\n') if url]
        }
