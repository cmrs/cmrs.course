from AccessControl import ClassSecurityInfo
from zope.interface import implements

from Products.Archetypes.atapi import registerType
from Products.ATContentTypes.content.base import ATCTContent
from Products.CMFCore import permissions
from Products.CMFCore.utils import getToolByName

from cmrs.course.config import PROJECTNAME
from cmrs.course.interfaces.course import ICourse

from schemata import CourseSchema

class Course(ATCTContent):
    """A Course"""

    security = ClassSecurityInfo()

    implements(ICourse)

    meta_type = 'Course'
    _at_rename_after_creation = True

    schema = CourseSchema

    security.declarePublic('canSetConstrainTypes')
    def canSetConstrainTypes(self):
        return False

    security.declarePublic('getCourseSemesters')
    def getCourseSemesters(self):
        return self.aq_inner.aq_parent.getCourseAvailabilityVocab()

registerType(Course, PROJECTNAME)
