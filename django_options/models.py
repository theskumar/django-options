# -*- coding: utf-8 -*-s
from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.sites.models import Site
from picklefield import PickledObjectField
from .managers import OptionManager


class Option(models.Model):

    site = models.ForeignKey(Site, related_name='options',
                             verbose_name=_('Site'))

    key = models.CharField(max_length=255,
                           verbose_name=_('Key'))
    value = PickledObjectField(null=True, default=True,
                               verbose_name=_('Value'))
    autoload = models.BooleanField(default=False,
                                   verbose_name=_('Autoload'))

    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name=_('Update at'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('Create at'))
    expires_at = models.DateTimeField(blank=True, null=True,
                                      verbose_name=_('Expires at'))

    # override default manager
    objects = OptionManager()
    all = models.Manager()
    on_site = objects

    def __unicode__(self):
        return u"%s:%s" % (self.site.name[:10], self.key[:10])

    class Meta:
        unique_together = ('site', 'key',)
        verbose_name = _('Option')
        verbose_name_plural = _('Options')
