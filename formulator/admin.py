# -*- coding: utf-8 -*-
# from django.contrib import admin
# from django.core.urlresolvers import reverse
# from .models import Form, Field, Choice
#
# #
# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     sortable_field_name = "position"
#     extra = 0
#     fields = ('key', 'value', 'position')
#     fk_name = 'field'
#
#
# class FieldAdmin(admin.ModelAdmin):
#     model = Field
#     extra = 0
#     fields = (('label', 'required'), 'help_text', ('field_type', 'widget'), 'max_length', 'placeholder')
#     list_display = ['form', 'label', 'field_type', 'widget', 'max_length', 'required']
#     fk_name = 'form'
#     inlines = [ChoiceInline]
#
#
#
# class FieldInline(admin.TabularInline):
#     model = Field
#     sortable_field_name = "position"
#     extra = 0
#     fields = ('label', 'help_text', 'field_type', 'max_length', 'required', 'position', 'get_change_url')
#     fk_name = 'form'
#     show_change_link = True
#     readonly_fields = ('get_change_url', )
#
#     def get_change_url(self, object):
#         url = reverse('admin:formulator_field_change', args=(object.id,))
#         return '<a href="%s" class="grp-icon grp-viewsite-link" title="View Options" target="_blank">Options</a>' % url
#
#     get_change_url.short_description = "Options"
#     get_change_url.allow_tags = True
#
#
# class FormAdmin(admin.ModelAdmin):
#     list_display = ['pk', 'name', 'form_name', 'form_action', 'form_method', 'form_id', 'form_class']
#     fields = ('name', ('form_method', 'form_class', 'form_name'))
#     inlines = [FieldInline]
#
#
# admin.site.register(Form, FormAdmin)
# admin.site.register(Field, FieldAdmin)
