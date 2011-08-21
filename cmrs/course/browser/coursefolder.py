from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

from cmrs.course.config import COURSE_TYPE, SUBJECT_CREDIT

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
        request = self.request
        portal_catalog = getToolByName(self, 'portal_catalog')
        if hasattr(self.request, 'course_type'):
            course_type = getattr(self.request, 'course_type')
        else:
            course_type = self.uniqueValuesForCourseType()
        if hasattr(self.request, 'course_subject'):
            course_subject = getattr(self.request, 'course_subject')
        else:
            course_subject = self.uniqueValuesForCourseSubject()
        if hasattr(self.request, 'course_availability'):
            course_availability = getattr(self.request, 'course_availability')
        else:
            course_availability = self.uniqueValuesForCourseAvailability()
        courses = portal_catalog(portal_type='Course',
                                 review_state='published',
                                 getCourseAvailability=course_availability,
                                 getCourseSubject=course_subject,
                                 getCourseType=course_type,
                                 )
        return courses

    def vocabCourseType(self):
        """Get the vocab for the course type
        """
        return COURSE_TYPE

    def vocabCourseSubject(self):
        """Get the vocab for the course subject
        """
        return SUBJECT_CREDIT

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
