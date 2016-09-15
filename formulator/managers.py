from django.db import models


class FormQuerySet(models.QuerySet):

    def default(self):
        return self.prefetch_related(
            'fields',
            'fieldsets',
            'fieldsets__fields',
            'fields__options',)

