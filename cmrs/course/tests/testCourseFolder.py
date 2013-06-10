from Acquisition import aq_inner
import unittest2 as unittest
from zope.component import getMultiAdapter

from plone.app.customerize import registration
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.browserlayer.utils import registered_layers

from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView as View

from cmrs.course.interfaces.coursefolder import ICourseFolder

from base import CMRS_COURSE_INTEGRATION_TESTING

class TestContentType(unittest.TestCase):
    """Test course folder content type"""
    layer = CMRS_COURSE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def testAddType(self):
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('CourseFolder', 'cf1')
        cf1 = getattr(self.portal, 'cf1')
        assert 'cf1' in self.portal.objectIds()

class TestView(unittest.TestCase):
    """Test the view for course folder content type"""
    layer = CMRS_COURSE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('CourseFolder', 'cf1')
        self.cf1 = getattr(self.portal, 'cf1')

    def testGetCoursesReturnsNone(self):
        """Should return empty list if no courses
        """
        cf1 = self.cf1
        view = getMultiAdapter((aq_inner(cf1), self.portal.REQUEST), name='course_search')
        view = view.__of__(cf1)
        assert view.getCourses() == []

    def testGetCoursesReturnNone(self):
        """Should return list of one item
        """
        cf1 = self.cf1
        cf1.invokeFactory('Course', 'c1')
        view = getMultiAdapter((aq_inner(cf1), self.portal.REQUEST), name='course_search')
        view = view.__of__(cf1)
        courses = view.getCourses()
        assert len(courses) == 1
