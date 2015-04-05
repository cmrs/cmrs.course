import string
import transaction
from AccessControl import ClassSecurityInfo
from lxml import etree
from OFS.CopySupport import CopyError
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
        base_id = self.getCourseCode()
        base_id = plone_tool.normalizeString(base_id)
        try:
            self.setId(base_id)
        except CopyError:
            for letter in string.ascii_lowercase:
                new_id = base_id + '-' + letter
                try:
                    self.setId(new_id)
                    break
                except CopyError:
                    pass

    security.declarePrivate('at_post_create_script')
    def at_post_edit_script(self):
        self._renameAfterCreation()

    security.declarePublic('getCourseSemesters')
    def getCourseSemesters(self):
        return self.aq_inner.aq_parent.getCourseAvailabilityVocab()

    security.declarePublic('Title')
    def Title(self):
        if self.getCourseCode():
            title = self.getCourseCode() + ' '
        else:
            return self.Schema()['title'].get(self)
        return title + self.Schema()['title'].get(self)


    security.declarePublic('editTitle')
    def editTitle(self):
        return self.Schema()['title'].get(self)

    security.declarePublic('Description')
    def Description(self):
        desc = self.schema['description'].get(self)
        if desc:
            return desc
        tansform_tool = getToolByName(self, 'portal_transforms')
        text = self.getText()
        if not text:
            return ''
        # wrap the text in a single root element
        # otherwise lxml throws an error
        text = '<course>' + text + '</course>'
        course_xml = etree.fromstring(text)
        return course_xml[0].text

registerType(Course, PROJECTNAME)
