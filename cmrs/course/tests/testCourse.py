import unittest2 as unittest

from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.browserlayer.utils import registered_layers

from Products.CMFCore.utils import getToolByName

from base import CMRS_COURSE_INTEGRATION_TESTING

class TestContentType(unittest.TestCase):
    """Tes course content type"""
    layer = CMRS_COURSE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def testAddType(self):
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('CourseFolder', 'cf1')
        cf1 = getattr(self.portal, 'cf1')
        cf1.invokeFactory('Course', 'c1')
        assert 'c1' in cf1.objectIds()

class TestSchema(unittest.TestCase):
    """Test course content type"""
    layer = CMRS_COURSE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('CourseFolder', 'cf1')
        self.cf1 = getattr(self.portal, 'cf1')
