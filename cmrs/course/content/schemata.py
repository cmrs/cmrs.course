from plone.app.folder.folder import ATFolderSchema

from Products.Archetypes.atapi import AnnotationStorage
from Products.Archetypes.atapi import Schema
from Products.Archetypes.atapi import LinesField
from Products.Archetypes.atapi import LinesWidget
from Products.Archetypes.atapi import MultiSelectionWidget
from Products.Archetypes.atapi import RichWidget
from Products.Archetypes.atapi import SelectionWidget
from Products.Archetypes.atapi import StringField
from Products.Archetypes.atapi import StringWidget
from Products.Archetypes.atapi import TextField

from Products.ATContentTypes.content.schemata import ATContentTypeSchema
from Products.ATContentTypes.content.schemata import finalizeATCTSchema

from cmrs.course.config import COURSE_TYPE, SUBJECT_CREDIT

CourseFolderSchema = ATFolderSchema.copy() + Schema((

    LinesField('courseSemesters',
        required = True,
        searchable = False,
        storage = AnnotationStorage(),
        widget = LinesWidget(
            label='Course Semesters',
            description = """Add each course date on a seperate line in the format "season year"
                these will be used wherever the course dates are requried""",
        )
    ),

    TextField('text',
        required = False,
        searchable = True,
        primary = True,
        storage = AnnotationStorage(migrate=True),
        validators = ('isTidyHtmlWithCleanup',),
        default_output_type = 'text/x-html-safe',
        widget = RichWidget(
            label = 'Course Introduction',
            rows = 25,)
        ),

))

CourseSchema = ATContentTypeSchema.copy() + Schema((

    StringField('courseCode',
        required = True,
        searchable = False,
        storage = AnnotationStorage(),
        widget = StringWidget(
            label='Course Code',
        )
    ),

    StringField('courseType',
        required = True,
        searchable = True,
        vocabulary = COURSE_TYPE,
        storage = AnnotationStorage(),
        widget = SelectionWidget(
            label='Course Type',
        )
    ),

    StringField('courseSubject',
        required = True,
        searchable = True,
        multiValued = True,
        vocabulary = SUBJECT_CREDIT,
        storage = AnnotationStorage(),
        widget = MultiSelectionWidget(
            label='Subject Credit',
            format='checkbox',
        )
    ),

    StringField('courseAvailability',
        required = False,
        searchable = True,
        vocabulary = 'getCourseSemesters',
        multiValued = True,
        storage = AnnotationStorage(),
        widget = MultiSelectionWidget(
            label='Course Availability',
            description = """Select which semesters the course ia availabe in,
                if the new semesters are not listed here you can add them by editing the course folder""",
            format='checkbox',
        )
    ),

    TextField('text',
        required = False,
        searchable = True,
        primary = True,
        storage = AnnotationStorage(migrate=True),
        validators = ('isTidyHtmlWithCleanup',),
        default_output_type = 'text/x-html-safe',
        widget = RichWidget(
            label = 'Course Description',
            rows = 25,)
        ),

))

CourseSchema['title'].widget.label = 'Course Title'
CourseSchema['title'].edit_accessor = 'editTitle'
CourseSchema["description"].widget.visible = {"edit": "invisible" }
finalizeATCTSchema(CourseSchema)
