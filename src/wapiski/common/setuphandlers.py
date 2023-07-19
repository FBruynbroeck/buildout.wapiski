# encoding: utf-8
from plone import api
from Products.CMFPlone.interfaces import constrains


def run_after(context):
    portal = api.portal.get()
    if not api.content.get('/stages'):
        stages = api.content.create(
            type='Folder',
            title='Stages',
            id='stages',
            container=portal)
        api.group.grant_roles(
            groupname='AuthenticatedUsers',
            roles=['Contributor'],
            obj=stages)
        behavior = constrains.ISelectableConstrainTypes(stages)
        behavior.setConstrainTypesMode(constrains.ENABLED)
        behavior.setLocallyAllowedTypes(['wapiski.Stage', 'EasyForm'])
        behavior.setImmediatelyAddableTypes(['wapiski.Stage', 'EasyForm'])
        api.content.transition(stages, transition='publish')
    if not api.content.get('/sejours'):
        sejours = api.content.create(
            type='Folder',
            title='Séjours',
            id='sejours',
            container=portal)
        api.group.grant_roles(
            groupname='AuthenticatedUsers',
            roles=['Contributor'],
            obj=sejours)
        behavior = constrains.ISelectableConstrainTypes(sejours)
        behavior.setConstrainTypesMode(constrains.ENABLED)
        behavior.setLocallyAllowedTypes(['wapiski.Sejour', 'EasyForm'])
        behavior.setImmediatelyAddableTypes(['wapiski.Sejour', 'EasyForm'])
        api.content.transition(sejours, transition='publish')
