from Products.Archetypes.atapi import DisplayList

PROJECTNAME = 'cmrs.course'

ADD_PERMISSIONS = {
    'Course': 'CmrsCourse: Add Course',
    'CourseFolder': 'CmrsCourse: Add CourseFolder',
}

COURSE_TYPE = DisplayList((
    ('integral', 'Integral'),
    ('seminars', 'Seminars'),
    ('tutorials', 'Tutorials'),
))

SUBJECT_CREDIT = DisplayList((
    ('archaeology', 'Archaeology'),
    ('art', 'Art'),
    ('art_history', 'Art History'),
    ('classical_studies', 'Classical Studies'),
    ('creative_writing', 'Creative Writing'),
    ('dramatic_arts', 'Dramatic Arts'),
    ('gender_studies', 'Gender Studies'),
    ('history', 'History'),
    ('interdisciplinary', 'Interdisciplinary'),
    ('languages', 'Languages'),
    ('law', 'Law'),
    ('literature', 'Literature'),
    ('multidisciplinary', 'Multidisciplinary'),
    ('music', 'Music'),
    ('philosophy', 'Philosophy'),
    ('political_philosophy', 'Political Philosophy'),
    ('political_thought', 'Political Thought'),
    ('religious_studies', 'Religious Studies'),
    ('studio_art', 'Studio Art'),
    ('womens_studies', 'Women\'s Studies'),
))
