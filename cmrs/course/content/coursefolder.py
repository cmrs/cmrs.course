from AccessControl import ClassSecurityInfo
from zope.interface import implements

from plone.app.folder.folder import ATFolder

from Products.Archetypes.atapi import DisplayList
from Products.Archetypes.atapi import registerType
from Products.CMFCore.utils import getToolByName

from cmrs.course.config import PROJECTNAME
from cmrs.course.interfaces.coursefolder import ICourseFolder

from schemata import CourseFolderSchema

class CourseFolder(ATFolder):
    """Folder to contain course objects"""

    security = ClassSecurityInfo()

    implements(ICourseFolder)

    meta_type = 'CourseFolder'
    _at_rename_after_creation = True

    schema = CourseFolderSchema

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

    security.declarePublic('getCourseAvailabilityVocab')
    def getCourseAvailabilityVocab(self):
        vocab = DisplayList()
        for item in self.getCourseSemesters():
            vocab.add(item, item)
        return vocab

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

registerType(CourseFolder, PROJECTNAME)
