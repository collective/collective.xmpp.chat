from Products.Five import BrowserView
from collective.xmpp.core.browser import userinfo
from plone.app.controlpanel.usergroups import UsersOverviewControlPanel
import json


class XMPPUserDetails(userinfo.XMPPUserDetails):

    def isSelf(self):
        return self.user_id == self.pm.getAuthenticatedMember().getId()


class SearchUsers(BrowserView):

    def __call__(self):
        searchtext = self.request.form.get('q')
        # search terms of less then 3 chars return empty list
        if len(searchtext) < 2:
            return []
        panel = UsersOverviewControlPanel(self.context, self.request)
        return json.dumps(panel.doSearch(searchtext))
