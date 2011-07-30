from AccessControl import ClassSecurityInfo
from zope.interface import implements

from plone.app.folder.folder import ATFolder

from Products.Archetypes.atapi import registerType

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

registerType(CourseFolder, PROJECTNAME)
