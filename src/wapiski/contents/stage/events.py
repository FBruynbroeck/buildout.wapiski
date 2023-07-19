# encoding: utf-8
import datetime
import plone.api


def copyEasyForm(self, context):
    if plone.api.content.get('/stages/inscription'):
        inscription = plone.api.content.copy(source=plone.api.content.get('/stages/inscription'), target=self)
        inscription.close_date = self.start.replace(hour=0, minute=0, second=0, microsecond=0) - datetime.timedelta(days=7)


def editEasyForm(self, context):
    if self.get('inscription'):
        self.get('inscription').close_date = self.start.replace(hour=0, minute=0, second=0, microsecond=0) - datetime.timedelta(days=7)
