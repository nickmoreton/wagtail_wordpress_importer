from django.apps import AppConfig


class WagtailWordpressImporterConfig(AppConfig):
    name = 'wagtail_wordpress_importer'
    verbose_name = 'Wordpress Importer'

    def ready(self):
        import wagtail_wordpress_importer.signals