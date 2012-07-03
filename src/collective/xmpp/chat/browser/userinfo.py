import json
from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName
from jarn.xmpp.core.browser import userinfo

class XMPPUserDetails(userinfo.XMPPUserDetails):

    def isSelf(self):
        return self.user_id == self.pm.getAuthenticatedMember().getId()

class SearchUsers(BrowserView):

    def __call__(self):
        searchtext = self.request.form.get('q')
        # search terms of less then 3 chars return empty list
        if len(searchtext) < 3:
            return []

        # search for usernames
        acl_users = getToolByName(self.context, 'acl_users')
        user_ids = [user['id'] for user in acl_users.searchUsers(name=searchtext)]
        return json.dumps(self._getUserDefs(user_ids))

    def _getUserDefs(self, uids):
        aclu = getToolByName(self.context, 'acl_users')
        users = [aclu.getUserById(user_id) for user_id in uids]
        ret = []
        for user in users:
            if user is None:
                continue
            user_id = user.getId()
            user_fn = None
            for psheet in user.getOrderedPropertySheets():
                if psheet.hasProperty('fullname'):
                    user_fn = psheet.getProperty('fullname')
                    if user_fn:
                        # do not search other sheets
                        break
            user_fn = user_fn or user_id
            entry = {
                'id': user_id,
                'fullname': user_fn,
            }
            ret.append(entry)
        ret.sort(cmp=lambda x, y: \
            x['fullname'].lower() > y['fullname'].lower() and 1 or -1)
        return ret
