import logging
from Products.CMFCore.utils import getToolByName

def add_catalog_indexes(context, logger=None):
    """Method to add our wanted indexes to the portal_catalog.
    """
    catalog = getToolByName(context, 'portal_catalog')
    indexes = catalog.indexes()
    wanted = (('getCourseType', 'FieldIndex'),
              ('getCourseSubject', 'FieldIndex'),
              ('getCourseAvailability', 'FieldIndex'),
              )
    indexables = []
    for name, meta_type in wanted:
        if name not in indexes:
            catalog.addIndex(name, meta_type)
            indexables.append(name)
            logger.info("Added %s for field %s.", meta_type, name)
    if len(indexables) > 0:
        logger.info("Indexing new indexes %s.", ', '.join(indexables))
        catalog.manage_reindexIndex(ids=indexables)    
    
def setupVarious(context):

    if context.readDataFile('cmrs.course_various.txt') is None:
        return
    logger = context.getLogger('cmrs.course')
    site = context.getSite()
    add_catalog_indexes(site, logger)
