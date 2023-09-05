from django.db import models
from mongoengine import Document, StringField


class Department(Document):
    DepartmentID = StringField(max_length=50)
    DepartmentName = StringField(max_length=50)

class Announcement(Document):
    AnnouncementID = StringField(max_length=50)
    Title = StringField(max_length=50)
    Description = StringField(max_length=50)
    PublishDate = StringField(max_length=50)

class Instructor(Document):
    InstructorID = StringField(max_length=50)
    Name = StringField(max_length=50)
    Gender = StringField(max_length=50)
    DoB = StringField(max_length=50)
    DepartmentID = StringField(max_length=50)
    Email = StringField(max_length=50)
    ContactNum = StringField(max_length=50)

class Course(Document):
    CourseCode = StringField(max_length=50)
    Name = StringField(max_length=50)
    DepartmentID = StringField(max_length=50)
    Credits = StringField(max_length=50)
    Description = StringField(max_length=50)
    InstructorID = StringField(max_length=50)

class Student(Document):
    StudentID = StringField(max_length=50)
    Name = StringField(max_length=50)
    Gender = StringField(max_length=50)
    DoB = StringField(max_length=50)
    Major = StringField(max_length=50)
    Email = StringField(max_length=50)
    ContactNum = StringField(max_length=50)

class Enrollment(Document):
    EnrollmentID = StringField(max_length=50)
    StudentID = StringField(max_length=50)
    CourseCode = StringField(max_length=50)
    EnrollmentDate = StringField(max_length=50)

class Assignment(Document):
    AssignmentID = StringField(max_length=50)
    CourseCode = StringField(max_length=50)
    Title = StringField(max_length=50)
    Description = StringField(max_length=50)
    DueDate = StringField(max_length=50)

class Submission(Document):
    SubmissionID = StringField(max_length=50)
    AssignmentID = StringField(max_length=50)
    StudentID = StringField(max_length=50)
    Status = StringField(max_length=50)
    SubmissionDate = StringField(max_length=50)
    SubmissionLink = StringField(max_length=50)
    Remarks = StringField(max_length=50)


 
