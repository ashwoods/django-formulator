# -*- coding: utf-8 -*-

from django.utils.safestring import mark_safe
from django.template import Context, Template
from django import forms


__all__ = (
   'ShortAnswer', 'Paragraph', 'MultipleChoice', 'Checkboxes', 'DropDown', 'SingleCheckbox',
   'Date', 'DateTime', 'Time', 'Number', 'Slug', 'Email',
)


class ShortAnswer(forms.CharField):
    """Short Answer"""
    pass


class Paragraph(forms.CharField):
    """Paragraph"""
    widget = forms.Textarea


class MultipleChoice(forms.ChoiceField):
    """Multiple Choice"""
    widget = forms.RadioSelect


class Checkboxes(forms.MultipleChoiceField):
    """Checkboxes"""
    pass


class DropDown(forms.ChoiceField):
    """Dropdown"""
    pass


class SingleCheckbox(forms.BooleanField):
    """Single Checkbox"""
    pass


class Date(forms.DateField):
    """Date"""
    pass


class DateTime(forms.DateTimeField):
    """Date & Time"""
    pass


class Time(forms.TimeField):
    """Time"""
    pass


class Number(forms.IntegerField):
    """Number"""
    pass


class Slug(forms.SlugField):
    """Slug"""
    pass


class Email(forms.EmailField):
    """Email"""
    pass
