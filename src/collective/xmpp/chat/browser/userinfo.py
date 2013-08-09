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
        users = panel.doSearch(searchtext)
        # complete name and surname can contain badly encoded values
        # when returned from plone.pas search therefore we try to convert
        # them to unicode with the latin characters encoding
        fields = ['cn', 'sn']
        for user_dict in users:
            for field in fields:
                try:
                    field_value = user_dict.get(field)
                    if field_value:
                        user_dict[field] = unicode(field_value, "ISO-8859-1")
                except UnicodeDecodeError:
                    users.remove(user_dict)
                    log.warn("Can't decode %s", user_dict[field])

        return json.dumps(users)
