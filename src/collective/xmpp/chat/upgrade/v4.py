from Products.CMFCore.utils import getToolByName
def updateJSRegistry(context):
    context.runImportStepFromProfile('profile-collective.xmpp.chat:default',
                                     'jsregistry')
    getToolByName(context, 'portal_css').cookResources()