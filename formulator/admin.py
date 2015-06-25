from django.contrib import admin
from .models import Form, FieldSet, Field
from django.core import urlresolvers


class FieldSetInline(admin.TabularInline):
    model = FieldSet
    sortable_field_name = "position"
    extra = 0
    fields = ('name', 'position')
    #readonly_fields = ('get_change_url',)

    def get_change_url(self, object):
        url = urlresolvers.reverse('admin:formulator_fieldset_change', args=(object.id,))
        return """
        <a href="%s" class="grp-icon grp-viewsite-link" title="View on Site" target="_blank">Link</a>
        """ % url

    get_change_url.short_description = "Details"
    get_change_url.allow_tags = True


class FieldInline(admin.TabularInline):
    model = Field
    sortable_field_name = "position"
    extra = 0
    fields = ('name', 'field', 'widget', 'required', 'position', 'get_change_url')
    readonly_fields = ('get_change_url',)

    def get_change_url(self, object):
        url = urlresolvers.reverse('admin:formulator_field_change', args=(object.id,))
        return """
        <a href="%s" class="grp-icon grp-viewsite-link" title="View on Site" target="_blank">Link</a>
        """ % url

    get_change_url.short_description = "Details"
    get_change_url.allow_tags = True


class FormAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'form_name', 'form_action', 'form_method', 'form_id', 'form_class']
    inlines = [FieldSetInline]


class FieldSetAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'form', 'slug', 'position']
    inlines = [FieldInline]


class FieldAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'get_form_field', 'get_fieldset_field','field_id', 'position', 'maxlength', 'required', 'field', 'widget']

    def get_fieldset_field(self, obj):
        return obj.fieldset.name

    def get_form_field(self, obj):
        return obj.fieldset.form.name

    get_fieldset_field.short_description = 'Fieldset'
    get_form_field.short_description = 'Form'

admin.site.register(Form, FormAdmin)
admin.site.register(FieldSet, FieldSetAdmin)
admin.site.register(Field, FieldAdmin)
