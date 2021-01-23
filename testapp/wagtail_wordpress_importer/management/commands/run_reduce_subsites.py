from django.core.management import BaseCommand
from wagtail_wordpress_importer.utils import spinner
from wagtail_wordpress_importer.models import ImportCategory, MasterImportCategory


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # reset usage count to start with
        self.stdout.write('Reducing sub sites. This may take a while...')
        self.stdout.write(next(spinner), ending='\b')
        
        self.reduce_categories()


    def reduce_categories(self):
        # add all root categories
        root_categories = ImportCategory.objects.filter(sub_site='root')
        for category in root_categories:
            MasterImportCategory.objects.create(
                category = category,
                name = category.name
            )

        # now add other categories not in root if they don't exist
        sub_sites = []
        root_categories = ImportCategory.objects.all().exclude(sub_site='root')
        for category in root_categories:
            if category.sub_site not in sub_sites:
                sub_sites.append(category.sub_site)

        for sub_site in sub_sites:
            sub_site_categories = ImportCategory.objects.filter(sub_site=sub_site)

            for category in sub_site_categories:
                try:
                    obj = MasterImportCategory.objects.get(name=category.name)
                except MasterImportCategory.DoesNotExist:
                    MasterImportCategory.objects.create(
                        category=category,
                        name=category.name
                    )
