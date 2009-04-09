from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _

class Rating(models.Model):
    content_type    = models.ForeignKey(ContentType)
    object_pk       = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey(ct_field='content_type', fk_field='object_pk')
    user            = models.ForeignKey(User)
    value           = models.PositiveIntegerField()

class RatingMeta(models.Model):
    rating          = models.ForeignKey(Rating)
    key             = models.CharField(max_length=128)
    value           = models.CharField(max_length=128)
