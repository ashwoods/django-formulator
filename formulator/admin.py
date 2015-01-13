from django.contrib import admin
from .models import Form, FieldSet, Field
from django.core import urlresolvers
from hvad.admin import TranslatableAdmin


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


class FieldSetAdmin(TranslatableAdmin):
    inlines = [FieldInline]


class FormAdmin(admin.ModelAdmin):
    inlines = [FieldSetInline]


class FieldAdmin(TranslatableAdmin):
    pass


admin.site.register(Form, FormAdmin)
admin.site.register(FieldSet, FieldSetAdmin)
admin.site.register(Field, FieldAdmin)
