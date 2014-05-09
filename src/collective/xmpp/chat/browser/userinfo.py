from Products.Five import BrowserView
from collective.xmpp.core.browser import userinfo
from plone.app.controlpanel.usergroups import UsersOverviewControlPanel
import json
import logging
log = logging.getLogger(__name__)


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
        return json.dumps([{
            'fullname': u['fullname'],
            'id': u['id']
            } for u in panel.doSearch(searchtext)])
