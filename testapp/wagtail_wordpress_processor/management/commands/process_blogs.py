from blog.models import BlogIndexPage, BlogPage
from django.apps import apps
from wagtail.core.models import Page
from wagtail_wordpress_importer.models import ImportPage

from ... import conf
from .base_command import BaseProcessCommand


class Command(BaseProcessCommand):

    BlogPage = apps.get_model(
        conf.BLOG_APP, conf.BLOG_PAGE_MODEL
    )
    BlogIndexPage = apps.get_model(
        conf.BLOG_APP, conf.BLOG_INDEX_PAGE_MODEL
    )

    home_page = Page.objects.filter(title='Home')[0]

    def handle(self, *args, **options):
        self.output_start('Processing blogs. This can take while')

        # the landing page
        import_blog_panding_page = ImportPage.objects.filter(
            template='page-blog-landing.php')

        for blog_landing_page in import_blog_panding_page:
            subsite = blog_landing_page.sub_site
            blog_index = BlogIndexPage(
                title=blog_landing_page.title
            )
            self.home_page.add_child(instance=blog_index)
            rev = blog_index.save_revision()
            rev.publish()

            import_blog_page = ImportPage.objects.filter(
                sub_site = subsite
            )

            for blog_page in import_blog_page:
                blog = BlogPage(
                    title=blog_page.title
                )
                blog_index.add_child(instance=blog)
                rev = blog.save_revision()
                rev.publish()
                self.output_spinner()

        self.output_message_end('Finished')
