from django.contrib import admin
from .models import Form, FieldSet, Field

class FieldInline(admin.StackedInline):
    model = Field
    extra = 1

class FieldSetAdmin(admin.ModelAdmin):
    inlines = [FieldInline]

admin.site.register(Form)
admin.site.register(FieldSet, FieldSetAdmin)
