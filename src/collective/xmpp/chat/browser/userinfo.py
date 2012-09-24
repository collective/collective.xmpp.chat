import json
from plone.app.controlpanel.usergroups import UsersOverviewControlPanel
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from collective.xmpp.core.browser import userinfo

class XMPPUserDetails(userinfo.XMPPUserDetails):

    def isSelf(self):
        return self.user_id == self.pm.getAuthenticatedMember().getId()

class SearchUsers(BrowserView):

    def __call__(self):
        searchtext = self.request.form.get('q')
        # search terms of less then 3 chars return empty list
        if len(searchtext) < 2:
            return []
        acl_users = getToolByName(self.context, 'acl_users')
        panel = UsersOverviewControlPanel(self.context, self.request)
        return  json.dumps(panel.doSearch(searchtext))
