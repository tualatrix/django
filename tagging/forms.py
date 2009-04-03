import time
import datetime

from django import forms
from django.forms.util import ErrorDict
from django.conf import settings
from django.http import Http404
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_unicode
from django.utils.hashcompat import sha_constructor
from django.utils.text import get_text_list
from django.utils.translation import ungettext, ugettext_lazy as _
from models import Tag
from utils import parse_tag_input

FORCE_LOWERCASE_TAGS = getattr(settings, 'FORCE_LOWERCASE_TAGS', False)
MAX_TAG_LENGTH = getattr(settings, 'MAX_TAG_LENGTH', 50)

class AdminTagForm(forms.ModelForm):
    class Meta:
        model = Tag

    def clean_name(self):
        value = self.cleaned_data['name']
        tag_names = parse_tag_input(value)
        if len(tag_names) > 1:
            raise forms.ValidationError(_('Multiple tags were given.'))
        elif len(tag_names[0]) > MAX_TAG_LENGTH:
            raise forms.ValidationError(
                _('A tag may be no more than %s characters long.') %
                    MAX_TAG_LENGTH)
        return value

class TagField(forms.CharField):
    """
    A ``CharField`` which validates that its input is a valid list of
    tag names.
    """
    def clean(self, value):
        value = super(TagField, self).clean(value)
        if value == u'':
            return value
        for tag_name in parse_tag_input(value):
            if len(tag_name) > MAX_TAG_LENGTH:
                raise forms.ValidationError(
                    _('Each tag may be no more than %s characters long.') %
                        MAX_TAG_LENGTH)
        return value
