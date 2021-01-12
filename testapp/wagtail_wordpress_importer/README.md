# Commands
A range of commands are available to get the data into the Django database

# Production Workflow

## Apps

IMPORT All apps: `python manage.py` and append
```
run_import
```

Import individual apps: `python manage.py` and append

```
import_atlas_case_studies
import_blogs
import_categories
import_custom_fields
import_documents
import_media
import_pages
import_posts
import_publication_types
import_regions
import_settings
```
`run_import` runs each of the above in one go

After these scripts are all run all the apps under Wordpress Importer in Django will have content

---

Delete All apps: `python manage.py` and append

```
run_delete
```

Delete individual apps: `python manage.py` and append

```
delete_atlas_case_studies
delete_blogs
delete_categories
delete_custom_fields
delete_documents
delete_media
delete_pages
delete_posts
delete_publication_types
delete_regions
delete_settings
```
`run_import` runs each of the above in one go

After these scripts are all run all the apps under Wordpress Importer in Django will have content

---

## Media Files
Media files are not collected after the import scripts above are run.

Collect media files: `manage.py` +
```
run_fetch_media
```
This takes some time to complete

---

# Development Workflow
Extra scripts are available for development whixh don't need to be run in production.

### Registering cutom fields
This calculates how many times a custom field is used across all the imported apps. It's helpful to see which custom fields can be ingnored and don't need processing when the contyent is imported into Wagtail. See USAGE COUNT in the Custom Fields app

Register custom fields: `python manage.py` +
```
run_register_custom_fields
```
Takes some time to complete