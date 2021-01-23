from .base_command import BaseProcessCommand
from blog.models import BlogIndexPage, BlogPage

class Command(BaseProcessCommand):
    
    def handle(self, *args, **options):
        self.output_start('Deleting blogs...')

        blogs = BlogPage.objects.all()
        for blog in blogs:
            self.output_spinner()
            blog.delete()
        blog_indexes = BlogIndexPage.objects.all()
        for blog_index in blog_indexes:
            self.output_spinner()
            blog_index.delete()

        self.output_message_end('Finished')