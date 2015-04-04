from Products.Archetypes.atapi import DisplayList

PROJECTNAME = 'cmrs.course'

ADD_PERMISSIONS = {
    'Course': 'CmrsCourse: Add Course',
    'CourseFolder': 'CmrsCourse: Add CourseFolder',
}

COURSE_TYPE = DisplayList((
    ('research', 'Research'),
    ('seminars', 'Seminars'),
    ('tutorials', 'Tutorials'),
))

SUBJECT_CREDIT = DisplayList((
    ('american', 'American Studies'),
    ('arabic', 'Arabic'),
    ('chinese', 'Chinese'),
    ('classics', 'Classics'),
    ('comparative_literature', 'Comparative Literature'),
    ('economics', 'Economics'),
    ('literature', 'English & American Literature'),
    ('media', 'Film & Media Culture'),
    ('french', 'French'),
    ('gender', 'Gender Sexuality & Feminist Studies'),
    ('geography', 'Geography'),
    ('german', 'German'),
    ('greek', 'Greek'),
    ('classical_hebrew', 'Hebrew (Classical)'),
    ('modern_hebrew', 'Hebrew (Modern)'),
    ('history', 'History'),
    ('art_history', 'History of Art & Architecture'),
    ('italian', 'Italian'),
    ('japanese', 'Japanese'),
    ('latin', 'Latin'),
    ('literary_studies', 'Literary Studies'),
    ('music', 'Music'),
    ('philosophy', 'Philosophy'),
    ('portuguese', 'Portuguese'),
    ('politics', 'Political Science'),
    ('psychology', 'Psychology'),
    ('religion', 'Religion'),
    ('russian', 'Russian'),
    ('sociology', 'Sociology/Anthropology'),
    ('spanish', 'Spanish'),
    ('theatre', 'Theatre'),
    ('other', 'Other Subjects'),
))
