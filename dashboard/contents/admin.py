from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea

from contents.models import (
    Content,
    Member,
    Project,
    Service,
)


class ServiceInline(admin.TabularInline):
    formfield_overrides = {
        models.CharField: {
            'widget': TextInput(attrs={'size': 20})
        }
    }
    model = Service
    fk_name = 'content'
    classes = ('collapse',)


class MemberInline(admin.TabularInline):
    formfield_overrides = {
        models.CharField: {
            'widget': TextInput(attrs={'size': 20})
        }
    }
    model = Member
    fk_name = 'content'
    classes = ('collapse',)


class ProjectInline(admin.TabularInline):
    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(attrs={'rows': 8, 'cols': 40})
        },
        models.CharField: {
            'widget': TextInput(attrs={'size': 20})
        }
    }
    model = Project
    fk_name = 'content'
    classes = ('collapse',)


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id',)
    inlines = (
        MemberInline,
        ProjectInline,
        ServiceInline
    )
