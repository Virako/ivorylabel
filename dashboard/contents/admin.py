from django.contrib import admin

from contents.models import (
    Content,
    Member,
    Project,
    Service,
)


class ServiceInline(admin.TabularInline):
    model = Service
    fk_name = 'content'
    classes = ('collapse',)


class MemberInline(admin.TabularInline):
    model = Member
    fk_name = 'content'
    classes = ('collapse',)


class ProjectInline(admin.TabularInline):
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
