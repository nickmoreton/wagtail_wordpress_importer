from django.conf import settings

''' app and models in Wagtail instance '''

BLOG_APP = getattr(
    settings, 'BLOG_APP', 'blog')
    
BLOG_PAGE_MODEL = getattr(
    settings, 'BLOG_PAGE_MODEL', 'BlogPage')
    
BLOG_INDEX_PAGE_MODEL = getattr(
    settings, 'BLOG_INDEX_PAGE_MODEL', 'BlogIndexPage')
