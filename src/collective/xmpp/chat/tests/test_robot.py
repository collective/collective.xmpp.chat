from collective.xmpp.chat.testing import XMPPCHAT_FUNCTIONAL_TESTING
from plone.testing import layered
import robotsuite
import unittest


def test_suite():
    suite = unittest.TestSuite()
    # TODO
    return suite
    suite.addTests([
        layered(robotsuite.RobotTestSuite("robot_hello.txt"),
                layer=XMPPCHAT_FUNCTIONAL_TESTING)
    ])
    return suite
