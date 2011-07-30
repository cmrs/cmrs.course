from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class CourseView(BrowserView):  

    template = ViewPageTemplateFile('templates/course_view.pt')

    def __call__(self):
        return self.template() 
