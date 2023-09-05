from django.urls import path
from . import views
urlpatterns = [

    # Home route
    path("", views.home, name="home"),
    
    # Department URLs
    path('departments/', views.get_departments, name='departments-list'),
    path('add_department/', views.add_department, name='add_department'),
    path('departments/update/<str:department_id>/', views.update_department, name='update_department'),
    path('departments/<str:department_id>/', views.delete_department, name='delete_department'),

    #Announcement URLs
    path('announcements/', views.get_announcements, name='announcements-list'),
    path('add_announcement/', views.add_announcement, name='add_announcement'),
    path('announcements/update/<str:announcement_id>/', views.update_announcement, name='update_announcement'),
    path('announcements/<str:announcement_id>/', views.delete_announcement, name='delete_announcement'),

    #Instructor URLs
    path('instructors/', views.get_instructors, name='instructors-list'),
    path('add_instructor/', views.add_instructor, name='add_instructor'),
    path('instructors/update/<str:instructor_id>/', views.update_instructor, name='update_instructor'),
    path('instructors/<str:instructor_id>/', views.delete_instructor, name='delete_instructor'),

    #Student URLs
    path('students/', views.get_students, name='students-list'),
    path('add_student/', views.add_student, name='add_student'),
    path('students/update/<str:student_id>/', views.update_student, name='update_student'),
    path('students/<str:student_id>/', views.delete_student, name='delete_student'),

    #Course URLs
    path('courses/', views.get_courses, name='courses-list'),
    path('add_course/', views.add_course, name='add_course'),
    path('courses/update/<str:course_id>/', views.update_course, name='update_student'),
    path('courses/<str:course_id>/', views.delete_course, name='delete_student'),

    #Enrollment URLs
    path('enrollments/', views.get_enrollments, name='enrollments-list'),
    path('add_enrollment/', views.add_enrollment, name='add_enrollment'),
    path('enrollments/update/<str:enrollment_id>/', views.update_enrollment, name='update_enrollment'),
    path('enrollments/<str:enrollment_id>/', views.delete_enrollment, name='delete_enrollment'),

    #Assignment URLs
    path('assignments/', views.get_assignments, name='assignments-list'),
    path('add_assignment/', views.add_assignment, name='add_assignment'),
    path('assignments/update/<str:assignment_id>/', views.update_assignment, name='update_assignment'),
    path('assignments/<str:assignment_id>/', views.delete_assignment, name='delete_assignment'),


    #Submission URLs
    path('submissions/', views.get_submissions, name='submissions-list'),
    path('add_submission/', views.add_submission, name='add_submission'),
    path('submissions/update/<str:submission_id>/', views.update_submission, name='update_submission'),
    path('submissions/<str:submission_id>/', views.delete_submission, name='delete_submission'),


]
