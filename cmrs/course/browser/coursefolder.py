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
