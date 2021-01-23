from wagtail.core.models import Page


class BlogPage(Page):
    parent_page_types = ('blog.BlogIndexPage', )


class BlogIndexPage(Page):
    pass
