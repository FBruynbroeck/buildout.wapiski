# -*- coding: utf-8 -*-
from collective.folderishtypes.browser.viewlets import ListingViewlet


class ListingViewletSejour(ListingViewlet):

    def available(self):
        return False
