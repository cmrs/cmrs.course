from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

class CourseFolderView(BrowserView):  

    template = ViewPageTemplateFile('templates/course_list.pt')

    def __call__(self):
        return self.template() 

    def getCourses(self):
        """Return the courses as objects
        """
        courses = self.context.getFolderContents(contentFilter={'portal_type':'Course',
                                                                  'sort_on':'sortable_title'},
                                                   full_objects=True)
        return courses

    def searchCourses(self):
        """Return the courses as objects
        """
        courses = self.context.getFolderContents(contentFilter={'portal_type':'Course',
                                                                  'sort_on':'sortable_title'},
                                                   full_objects=True)
        return courses

    def uniqueValuesForCourseType(self):
        """Get the list of values for the course type facet
        """
        portal_catalog = getToolByName(self, 'portal_catalog')
        course_types = portal_catalog.uniqueValuesFor("getCourseType")
        return course_types

    def uniqueValuesForCourseSubject(self):
        """Get the list of values for the course subject facet
        """
        portal_catalog = getToolByName(self, 'portal_catalog')
        course_subjects = portal_catalog.uniqueValuesFor("getCourseSubject")
        return course_subjects

    def uniqueValuesForCourseAvailability(self):
        """Get the list of values for the course availability facet
        """
        portal_catalog = getToolByName(self, 'portal_catalog')
        course_availability = portal_catalog.uniqueValuesFor("getCourseAvailability")
        return course_availability
