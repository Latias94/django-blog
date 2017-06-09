import markdown
from django.contrib.syndication.views import Feed
from markdown.extensions.toc import TocExtension
from .models import Post


class AllPostsRssFeed(Feed):
    title = "博客"
    link = "/"
    description = "Django 博客示例"

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)

    def item_description(self, item):
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        item.body = md.convert(item.body)
        return item.body
