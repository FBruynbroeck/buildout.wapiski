# encoding: utf-8
from plone.app.contenttypes.browser.collection import CollectionView
from plone.app.event.base import spell_date
from plone.dexterity.browser.view import DefaultView
from zope.component import getMultiAdapter
from zope.contentprovider.interfaces import IContentProvider


class SejourView(DefaultView):

    def formatted_date(self, item):
        provider = getMultiAdapter(
            (self.context, self.request, self),
            IContentProvider, name='formatted_date'
        )
        return provider(item)


class SejourCollection(CollectionView):

    def date_speller(self, date):
        return spell_date(date, self.context)
