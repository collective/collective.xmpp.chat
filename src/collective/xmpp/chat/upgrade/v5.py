from Products.CMFCore.utils import getToolByName


def updateRegistries(context):
    pj = getToolByName(context, 'portal_javascripts')
    pcss = getToolByName(context, 'portal_css')
    path = '++resource++collective.xmpp.chat.resources/'
    for id in [
        "Libraries/strophe.roster.js",
        "Libraries/strophe.muc.js",
        "Libraries/strophe.vcard.js",
        "Libraries/strophe.disco.js",
        "Libraries/underscore.js",
        "Libraries/backbone.js",
        "Libraries/backbone.localStorage.js",
        "Libraries/sjcl.js",
        "Libraries/jquery.tinysort.js",
        "Libraries/jed.js",
        "locale/af/LC_MESSAGES/af.js",
        "locale/de/LC_MESSAGES/de.js",
        "locale/it/LC_MESSAGES/it.js",
        "locale/es/LC_MESSAGES/es.js",
        "locale/en/LC_MESSAGES/en.js",
        "converse.js"
    ]:
        pj.manage_removeScript(path+id)
    context.runImportStepFromProfile('profile-collective.xmpp.chat:default',
                                     'jsregistry')

    pcss.manage_removeStylesheet(
        "++resource++collective.xmpp.chat.resources/converse.css")
    context.runImportStepFromProfile('profile-collective.xmpp.chat:default',
                                     'cssregistry')
