# -*- coding: utf-8 -*-


from coffin.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.cache import cache_page


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


class JeanWeavesAboutView(JeanWeavesPageView):
    template_name = 'jeanweaves_public/about.html'
    page_title = _('About')


class JeanWeavesContactView(JeanWeavesPageView):
    template_name = 'jeanweaves_public/contact.html'
    page_title = _('Contact me')


class JeanWeavesExhibitsView(JeanWeavesPageView):
    template_name = 'jeanweaves_public/exhibits.html'
    page_title = _('Exhibits')


# class JeanWeavesToolsView(JeanWeavesPageView):
#     template_name = 'jeanweaves_public/tools.html'
#     page_title = _('Tools')


THIRTY_DAYS = 60 * 60 * 24 * 30
about = cache_page(THIRTY_DAYS)(JeanWeavesAboutView.as_view())
contact = cache_page(THIRTY_DAYS)(JeanWeavesContactView.as_view())
exhibits = cache_page(THIRTY_DAYS)(JeanWeavesExhibitsView.as_view())
