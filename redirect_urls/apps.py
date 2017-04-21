from django.apps import AppConfig, apps
from django.utils.module_loading import import_string

from redirect_urls.utils import register


class RedirectsConfig(AppConfig):
    name = 'redirect_urls'
    label = 'Redirect URLs'

    def ready(self):
        for app in apps.get_app_configs():
            try:
                patterns = import_string(app.name + '.redirects.redirectpatterns')
            except ImportError:
                continue

            register(patterns)
