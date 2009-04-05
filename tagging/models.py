from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _
from managers import TagManager, TaggedItemManager

class Tag(models.Model):
    '''Tag entity'''
    name = models.CharField('Name', unique = True, max_length = 64)
    slug = models.CharField('Slug', max_length = 255, unique = True,\
            blank = True, help_text = 'Use as url')
    objects = TagManager()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return u'/tag/%s/' % self.slug

class TaggedItem(models.Model):
    """
    Holds the relationship between a tag and the item being tagged.
    """
    tag = models.ForeignKey(Tag, verbose_name=_('tag'), related_name='items')
    content_type = models.ForeignKey(ContentType, verbose_name=_('content type'))
    object_id = models.PositiveIntegerField(_('object id'), db_index=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    objects = TaggedItemManager()

    def __unicode__(self):
        return u'%s [%s]' % (self.content_object, self.tag)
