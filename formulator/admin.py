from django.contrib import admin
from .models import Form, Field


class FieldInline(admin.TabularInline):
    model = Field
    sortable_field_name = "position"
    extra = 0
    fields = ('name', 'field', 'widget', 'maxlength', 'required', 'position',)


class FormAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'form_name', 'form_action', 'form_method', 'form_id', 'form_class']
    inlines = [FieldInline]


admin.site.register(Form, FormAdmin)
