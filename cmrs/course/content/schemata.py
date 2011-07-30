from plone.app.folder.folder import ATFolderSchema

from Products.Archetypes.atapi import Schema

from Products.ATContentTypes.content.schemata import ATContentTypeSchema
from Products.ATContentTypes.content.schemata import finalizeATCTSchema

CourseFolderSchema = ATFolderSchema.copy() + Schema((

))

CourseSchema = ATContentTypeSchema.copy() + Schema((

))

finalizeATCTSchema(CourseSchema)
