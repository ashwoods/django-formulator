# -*- coding: utf-8 -*-
import factory
from .models import Form


class FormFactory(factory.DjangoModelFactory):

    name = factory.Faker('word')

    class Meta:
        model = Form


class FieldFactory(factory.DjangoModelFactory):
    name = factory.Faker('word')
    form = factory.SubFactory(FormFactory)

    class Meta:
        model = 'formulator.Field'


class FieldSetFactory(factory.DjangoModelFactory):
    form = factory.SubFactory(FormFactory)


class FieldAttribute(factory.DjangoModelFactory):
    field = factory.SubFactory(FieldFactory)

    class Meta:
        model = 'formulator.FieldAttribute'


class WidgetAttribute(factory.DjangoModelFactory):
    field = factory.SubFactory(FieldFactory)

    class Meta:
        model = 'formulator.WidgetAttribute'


class ChoiceFactory(factory.DjangoModelFactory):
    field = factory.SubFactory(FieldFactory)

    class Meta:
        model = 'formulator.Choice'
