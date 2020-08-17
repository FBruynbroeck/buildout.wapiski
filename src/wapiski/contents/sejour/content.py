# encoding: utf-8
from plone import schema
from plone.app.contenttypes.content import Event
from plone.app.contenttypes.interfaces import IEvent
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage
from zope.interface import implements


class ISejour(IEvent):

    title = schema.TextLine(
        title=u"Titre",
        required=False,
    )

    description = schema.TextLine(
        title=u"Résumé du séjour",
        required=False,
    )

    text = RichText(
        title=u"Description du séjour",
        required=False,
    )

    image = NamedBlobImage(
        title=u"Photo du séjour",
        required=False,
    )

    price = schema.TextLine(
        title=u"Prix du séjour",
        required=False,
    )


class Sejour(Event):
    implements(ISejour)
