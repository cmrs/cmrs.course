import transaction
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

    security.declarePrivate('_renameAfterCreation')
    def _renameAfterCreation(self, check_auto_id=False):
        plone_tool = getToolByName(self, 'plone_utils', None)
        # Can't rename without a subtransaction commit when using
        # portal_factory!
        transaction.savepoint(optimistic = True)
        new_id = self.getCourseCode()
        new_id = plone_tool.normalizeString(new_id)
        self.setId(new_id)

    security.declarePublic('getCourseSemesters')
    def getCourseSemesters(self):
        return self.aq_inner.aq_parent.getCourseAvailabilityVocab()

    security.declarePublic('Description')
    def Description(self):
        tansform_tool = getToolByName(self, 'portal_transforms')
        text = self.getText()
        if not text:
            return ''
        text = tansform_tool.convert('html_to_text', text).getData()
        if len(text) < 300:
            return text
        return self.text[:150] + '...'

registerType(Course, PROJECTNAME)
