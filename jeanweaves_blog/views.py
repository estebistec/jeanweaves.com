# -*- coding: utf-8 -*-


from django.views.decorators.cache import cache_page

from .blog import blog
from jeanweaves_public.views import JeanWeavesPageView


class BlogPostsView(JeanWeavesPageView):

    template_name = 'jeanweaves_blog/posts.html'

    def get_context_data(self, **kwargs):
        context = super(BlogPostsView, self).get_context_data(**kwargs)
        context['posts'] = blog.get_posts()
        return context


posts = BlogPostsView.as_view()

THIRTY_MINUTES = 60 * 30
posts = cache_page(THIRTY_MINUTES)(posts)
