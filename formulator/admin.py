from django.contrib import admin
from .models import Form, Field, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0
    fields = ('key', 'value')
    fk_name = 'field'

class FieldAdmin(admin.ModelAdmin):
    model = Field
    extra = 0
    fields = ('name', 'label', 'help_text', 'field_type', 'widget', 'max_length', 'placeholder', 'required', 'position')
    list_display = ['name', 'label', 'form']
    fk_name = 'form'
    inlines = [ChoiceInline]

class FormAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'form_name', 'form_action', 'form_method', 'form_id', 'form_class']


admin.site.register(Form, FormAdmin)
admin.site.register(Field, FieldAdmin)
