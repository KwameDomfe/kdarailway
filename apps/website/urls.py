from django.urls import path

from . views import(
    index, 
    enrol, 
    courses, 
    course_instance,
    course_category,
    course_family,
    course_type,

    revit, revit_introduction, 
    revit_introduction_lesson_01,
    revit_introduction_lesson_02,
    revit_introduction_lesson_03,
    revit_introduction_lesson_04, 
    revit_introduction_lesson_05,

    revit, revit_intermediate, 
    revit_intermediate_lesson_01,
    revit_intermediate_lesson_02,
    revit_intermediate_lesson_03,
    revit_intermediate_lesson_04, 
    revit_intermediate_lesson_05,

    naviswork, 

    dynamo, 

    python, 

    discover, 
    
    contact_me, 
    
    faqs, 
    
    finance, 
    
    download, 

    style_guide, 

    layouts)

app_name = 'website'

urlpatterns = [
    path('', index, name='index'),
    path('enrol/', enrol, name='enrol'),
    path('courses/', courses, name='courses'),
    path('courses/course-category/', course_category, name='course-category'), # Revit
    path('courses/course-category/course-family/', course_family, name='course-family'), # REVIT Architecture, Revit Structure, Revit MEP
    path('courses/course-category/course-family/course-type/', course_type, name='course-type'),# Introdution, Intermediate, Mastery
    path('courses/course-category/course-family/course-type/course-instance/', course_instance, name='course-instance'),
    path('courses/revit/', revit, name='revit'),
    path('courses/revit/revit-introduction/', revit_introduction, name='revit-introduction'),
    path('courses/revit/revit-introduction/lesson-01/', revit_introduction_lesson_01, name='introduction-lesson-01'),
    path('courses/revit/revit-introduction/lesson-02/', revit_introduction_lesson_02, name='introduction-lesson-02'),
    path('courses/revit/revit-introduction/lesson-03/', revit_introduction_lesson_03, name='introduction-lesson-03'),
    path('courses/revit/revit-introduction/lesson-04/', revit_introduction_lesson_04, name='introduction-lesson-04'),
    path('courses/revit/revit-introduction/lesson-05/', revit_introduction_lesson_05, name='introduction-lesson-05'),
    path('courses/revit/revit-intermediate/', revit_intermediate, name='revit-intermediate'),
    path('courses/revit/revit-intermediate/lesson-01/', revit_intermediate_lesson_01, name='intermediate-lesson-01'),
    path('courses/revit/revit-intermediate/lesson-02/', revit_intermediate_lesson_02, name='intermediate-lesson-02'),
    path('courses/revit/revit-intermediate/lesson-03/', revit_intermediate_lesson_03, name='intermediate-lesson-03'),
    path('courses/revit/revit-intermediate/lesson-04/', revit_intermediate_lesson_04, name='intermediate-lesson-04'),
    path('courses/revit/revit-intermediate/lesson-05/', revit_intermediate_lesson_05, name='intermediate-lesson-05'),
    path('courses/naviswork', naviswork, name='naviswork'),
    path('courses/dynamo', dynamo, name='dynamo'),
    path('courses/python', python, name='python'),
    
    path('discover/', discover, name='discover'),
    path('discover/faqs', faqs, name='faqs'),
    path('discover/financing-options', finance, name='finance'),
    path('discover/contact-me', contact_me, name='contact-me'),
    path('discover/download', download, name='download'),
    path('discover/download/components/', download, name='download-components'),
    path('discover/download/documents/', download, name='download-documents'),
    path('discover/download/templates/', download, name='download-templates'),
    path('discover/style-guide', style_guide, name='style-guide'),
    path('layouts/', layouts, name='layouts'),
]
