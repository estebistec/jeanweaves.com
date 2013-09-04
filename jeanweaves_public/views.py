# -*- coding: utf-8 -*-


from django.utils.translation import ugettext_lazy as _
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView


class JeanWeavesPageView(TemplateView):

    page_title = None
    page_class = None
    page_layout = 'jeanweaves_public/_layout.html'

    def get_page_context(self):
        return {
            'layout': self.page_layout,
            'title': self.page_title,
            'page_class': self.page_class
        }

    def get_context_data(self, **kwargs):
        context = super(JeanWeavesPageView, self).get_context_data(**kwargs)
        context['page'] = self.get_page_context()
        return context


about = JeanWeavesPageView.as_view(
    template_name='jeanweaves_public/about.html',
    page_title=_('About')
)

contact = JeanWeavesPageView.as_view(
    template_name='jeanweaves_public/contact.html',
    page_title=_('Contact me')
)

exhibits = JeanWeavesPageView.as_view(
    template_name='jeanweaves_public/exhibits.html',
    page_title=_('Exhibits')
)

# tools = JeanWeavesPageView.as_view(
#     template_name='jeanweaves_public/tools.html',
#     page_title=_('Tools')
# ).as_view()

THIRTY_DAYS = 60 * 60 * 24 * 30
about = cache_page(THIRTY_DAYS)(about)
contact = cache_page(THIRTY_DAYS)(contact)
exhibits = cache_page(THIRTY_DAYS)(exhibits)
