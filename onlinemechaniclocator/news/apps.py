from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class NewsConfig(AppConfig):
    name = 'onlinemechaniclocator.news'
    verbose_name = _("News")
