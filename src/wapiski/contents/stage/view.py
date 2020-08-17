# encoding: utf-8
from plone.dexterity.browser.view import DefaultView
from zope.component import getMultiAdapter
from zope.contentprovider.interfaces import IContentProvider


class StageView(DefaultView):

    def lf_to_p(self, text):
        if not text:
            return u"<p></p>"
        return u"<p>" + text.replace(u'\n', u'</p><p>') + u"</p>"

    def formatted_date(self, item):
        provider = getMultiAdapter(
            (self.context, self.request, self),
            IContentProvider, name='formatted_date'
        )
        return provider(item)
