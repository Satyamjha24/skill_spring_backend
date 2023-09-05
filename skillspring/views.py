from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from . import models

def home(request):
    return HttpResponse("<h1>Welcome to Skill Spring Backend</h1>")



#Department Views

def get_departments(request):
    departments = models.Department.objects.all()
    # Convert departments to a list of dictionaries
    departments_data = [
        {
            '_id': str(department.id),
            'DepartmentID': department.DepartmentID,
            'DepartmentName': department.DepartmentName,
        }
        for department in departments
    ]
    
    return JsonResponse(departments_data, safe=False)

@csrf_exempt  # Disabling CSRF for demonstration purposes; you should handle CSRF properly in production
def add_department(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            department = models.Department(
                DepartmentID=data['DepartmentID'],
                DepartmentName=data['DepartmentName'],
            )
            department.save()  # Save the new department to MongoDB
            return JsonResponse({'message': 'New Department added successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
    
@require_http_methods(["PATCH"])
@csrf_exempt
def update_department(request, department_id):
    try:
        department = models.Department.objects.get(id=department_id)

        data = json.loads(request.body)
        if 'DepartmentName' in data:
            department.DepartmentName = data['DepartmentName']
        if 'DepartmentID' in data:
            department.DepartmentID = data['DepartmentID']

        department.save()
        return JsonResponse({'message': 'Department updated successfully'}, status=200)

    except models.Department.DoesNotExist:
        return JsonResponse({'error': 'Department not found'}, status=404)    


@csrf_exempt
def delete_department(request, department_id):
    if request.method == 'DELETE':
        try:
            department = models.Department.objects.get(id=department_id)
            department.delete()
            return JsonResponse({'message': 'Department deleted successfully'}, status=200)
        except models.Department.DoesNotExist:
            return JsonResponse({'error': 'Department not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    

### Announcement Views


def get_announcements(request):
    announcements = models.Announcement.objects.all()
    
    # Convert announcements to a list of dictionaries
    announcements_data = [
        {
            '_id': str(announcement.id),
            'AnnouncementID': announcement.AnnouncementID,
            'Title': announcement.Title,
            'Description': announcement.Description,
            'PublishDate': announcement.PublishDate
        }
        for announcement in announcements
    ]
    
    return JsonResponse(announcements_data, safe=False)




@csrf_exempt  # Disabling CSRF for demonstration purposes; you should handle CSRF properly in production
def add_announcement(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            announcement = models.Announcement(
                AnnouncementID=data['AnnouncementID'],
                Title=data['Title'],
                Description=data['Description'],
                PublishDate=data['PublishDate']
            )
            announcement.save()  # Save the new announcement to MongoDB
            return JsonResponse({'message': 'New Announcement added successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    

@require_http_methods(["PATCH"])
@csrf_exempt
def update_announcement(request, announcement_id):
    try:
        announcement = models.Announcement.objects.get(id=announcement_id)

        data = json.loads(request.body)
        if 'AnnouncementID' in data:
            announcement.AnnouncementID = data['AnnouncementID']
        if 'Title' in data:
            announcement.Title = data['Title']
        if 'Description' in data:
            announcement.Description = data['Description']
        if 'PublishDate' in data:
            announcement.PublishDate = data['PublishDate']

        announcement.save()
        return JsonResponse({'message': 'Announcement updated successfully'}, status=200)

    except models.Department.DoesNotExist:
        return JsonResponse({'error': 'Announcement not found'}, status=404)    


@csrf_exempt
def delete_announcement(request, announcement_id):
    if request.method == 'DELETE':
        try:
            announcement = models.Announcement.objects.get(id=announcement_id)
            announcement.delete()
            return JsonResponse({'message': 'Announcement deleted successfully'}, status=200)
        except models.Department.DoesNotExist:
            return JsonResponse({'error': 'Announcement not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)



# Instructor Views 


def get_instructors(request):
    instructors = models.Instructor.objects.all()
    
    # Convert instructors to a list of dictionaries
    instructors_data = [
        {
            '_id': str(instructor.id),
            'InstructorID': instructor.InstructorID,
            'Name': instructor.Name,
            'Gender': instructor.Gender,
            'DoB': instructor.DoB,
            'DepartmentID': instructor.DepartmentID,
            'Email': instructor.Email,
            'ContactNum': instructor.ContactNum,
        }
        for instructor in instructors
    ]
    
    return JsonResponse(instructors_data, safe=False)


@csrf_exempt  # Disabling CSRF for demonstration purposes; you should handle CSRF properly in production
def add_instructor(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            instructor = models.Instructor(
                InstructorID=data['InstructorID'],
                Name= data['Name'],
                Gender= data['Gender'],
                DoB= data['DoB'],
                DepartmentID= data['DepartmentID'],
                Email= data['Email'],
                ContactNum= data['ContactNum'],
            )
            instructor.save()  # Save the new instructor to MongoDB
            return JsonResponse({'message': 'New instructor added successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@require_http_methods(["PATCH"])
@csrf_exempt
def update_instructor(request, instructor_id):
    try:
        instructor = models.Instructor.objects.get(id=instructor_id)
        
        data = json.loads(request.body)
        if 'Name' in data:
            instructor.Name = data['Name']
        if 'Gender' in data:
            instructor.Gender = data['Gender']
        if 'DoB' in data:
            instructor.DoB = data['DoB']
        if 'DepartmentID' in data:
            instructor.DepartmentID = data['DepartmentID']
        if 'Email' in data:
            instructor.Email = data['Email']
        if 'ContactNum' in data:
            instructor.ContactNum = data['ContactNum']

        instructor.save()
        return JsonResponse({'message': 'Instructor updated successfully'}, status=200)

    except models.Instructor.DoesNotExist:
        return JsonResponse({'error': 'Instructor not found'}, status=404)


@csrf_exempt
def delete_instructor(request, instructor_id):
    if request.method == 'DELETE':
        try:
            instructor = models.Instructor.objects.get(id=instructor_id)
            instructor.delete()
            return JsonResponse({'message': 'Instructor deleted successfully'}, status=200)
        except models.Department.DoesNotExist:
            return JsonResponse({'error': 'Instructor not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

## Student Views


def get_students(request):
    students = models.Student.objects.all()
    
    # Convert instructors to a list of dictionaries
    students_data = [
        {
            '_id': str(student.id),
            'StudentID': student.StudentID,
            'Name': student.Name,
            'Gender': student.Gender,
            'DoB': student.DoB,
            'Major': student.Major,
            'Email': student.Email,
            'ContactNum': student.ContactNum,
        }
        for student in students
    ]
    
    return JsonResponse(students_data, safe=False)


@csrf_exempt  # Disabling CSRF for demonstration purposes; you should handle CSRF properly in production
def add_student(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            student = models.Student(
                StudentID=data['StudentID'],
                Name= data['Name'],
                Gender= data['Gender'],
                DoB= data['DoB'],
                Major= data['Major'],
                Email= data['Email'],
                ContactNum= data['ContactNum'],
            )
            student.save()  # Save the new student to MongoDB
            return JsonResponse({'message': 'New student added successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@require_http_methods(["PATCH"])
@csrf_exempt
def update_student(request, student_id):
    try:
        student = models.Student.objects.get(id=student_id)

        data = json.loads(request.body)
        if 'Name' in data:
            student.Name = data['Name']
        if 'Gender' in data:
            student.Gender = data['Gender']
        if 'DoB' in data:
            student.DoB = data['DoB']
        if 'Major' in data:
            student.Major = data['Major']
        if 'Email' in data:
            student.Email = data['Email']
        if 'ContactNum' in data:
            student.ContactNum = data['ContactNum']

        student.save()
        return JsonResponse({'message': 'Student updated successfully'}, status=200)

    except models.Student.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=404)


@csrf_exempt
def delete_student(request, student_id):
    if request.method == 'DELETE':
        try:
            student = models.Student.objects.get(id=student_id)
            student.delete()
            return JsonResponse({'message': 'Student deleted successfully'}, status=200)
        except models.Department.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

# Courses Views

def get_courses(request):
    courses = models.Course.objects.all()
    
    # Convert announcements to a list of dictionaries
    courses_data = [
        {
            '_id': str(course.id),
            "CourseCode": course.CourseCode,
            "Name": course.Name,
            "DepartmentID": course.DepartmentID,
            "Credits": course.Credits,
            "Description": course.Description,
            "InstructorID": course.InstructorID
        }
        for course in courses
    ]
    
    return JsonResponse(courses_data, safe=False)



@csrf_exempt  # Disabling CSRF for demonstration purposes; you should handle CSRF properly in production
def add_course(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            course = models.Course(
                CourseCode= data['CourseCode'],
                Name= data['Name'],
                DepartmentID= data['DepartmentID'],
                Credits= data['Credits'],
                Description= data['Description'],
                InstructorID= data['InstructorID']
            )
            course.save()  # Save the new course to MongoDB
            return JsonResponse({'message': 'New course added successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@require_http_methods(["PATCH"])
@csrf_exempt
def update_course(request, course_id):
    try:
        course = models.Course.objects.get(id=course_id)

        data = json.loads(request.body)
        if 'Name' in data:
            course.Name = data['Name']
        if 'DepartmentID' in data:
            course.DepartmentID = data['DepartmentID']
        if 'Credits' in data:
            course.Credits = data['Credits']
        if 'Description' in data:
            course.Description = data['Description']
        if 'InstructorID' in data:
            course.InstructorID = data['InstructorID']

        course.save()
        return JsonResponse({'message': 'Course updated successfully'}, status=200)

    except models.Course.DoesNotExist:
        return JsonResponse({'error': 'Course not found'}, status=404)
    

@csrf_exempt
def delete_course(request, course_id):
    if request.method == 'DELETE':
        try:
            course = models.Course.objects.get(id=course_id)
            course.delete()
            return JsonResponse({'message': 'Course deleted successfully'}, status=200)
        except models.Department.DoesNotExist:
            return JsonResponse({'error': 'Course not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

## Enrollment Views

def get_enrollments(request):
    enrollments = models.Enrollment.objects.all()
    
    # Convert announcements to a list of dictionaries
    enrollments_data = [
        {
            '_id': str(enrollment.id),
            'EnrollmentID': enrollment.EnrollmentID,
            'StudentID': enrollment.StudentID,
            'CourseCode': enrollment.CourseCode,
            'EnrollmentDate': enrollment.EnrollmentDate
        }
        for enrollment in enrollments
    ]
    
    return JsonResponse(enrollments_data, safe=False)


@csrf_exempt  # Disabling CSRF for demonstration purposes; you should handle CSRF properly in production
def add_enrollment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            enrollment = models.Enrollment(
                EnrollmentID=data['EnrollmentID'],
                StudentID=data['StudentID'],
                CourseCode=data['CourseCode'],
                EnrollmentDate=data['EnrollmentDate']
            )
            enrollment.save()  # Save the new enrollment to MongoDB
            return JsonResponse({'message': 'New Enrollment data added successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@require_http_methods(["PATCH"])
@csrf_exempt
def update_enrollment(request, enrollment_id):
    try:
        enrollment = models.Enrollment.objects.get(id=enrollment_id)

        data = json.loads(request.body)
        if 'StudentID' in data:
            enrollment.StudentID = data['StudentID']
        if 'CourseCode' in data:
            enrollment.CourseCode = data['CourseCode']
        if 'EnrollmentDate' in data:
            enrollment.EnrollmentDate = data['EnrollmentDate']

        enrollment.save()
        return JsonResponse({'message': 'Enrollment updated successfully'}, status=200)

    except models.Enrollment.DoesNotExist:
        return JsonResponse({'error': 'Enrollment not found'}, status=404)
    
@csrf_exempt
def delete_enrollment(request, enrollment_id):
    if request.method == 'DELETE':
        try:
            enrollment = models.Enrollment.objects.get(id=enrollment_id)
            enrollment.delete()
            return JsonResponse({'message': 'Enrollment deleted successfully'}, status=200)
        except models.Department.DoesNotExist:
            return JsonResponse({'error': 'Enrollment not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

## Assignment Views


def get_assignments(request):
    assignments = models.Assignment.objects.all()
    
    # Convert announcements to a list of dictionaries
    assignments_data = [
        {
            '_id': str(assignment.id),
            'AssignmentID': assignment.AssignmentID,
            'CourseCode': assignment.CourseCode,
            'Title': assignment.Title,
            'Description': assignment.Description,
            'DueDate': assignment.DueDate,
        }
        for assignment in assignments
    ]
    
    return JsonResponse(assignments_data, safe=False)



@csrf_exempt  # Disabling CSRF for demonstration purposes; you should handle CSRF properly in production
def add_assignment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            assignment = models.Assignment(
                AssignmentID=data['AssignmentID'],
                CourseCode=data['CourseCode'],
                Title=data['Title'],
                Description=data['Description'],
                DueDate=data['DueDate']
            )
            assignment.save()  # Save the new assignment to MongoDB
            return JsonResponse({'message': 'New assignment data added successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
    
@require_http_methods(["PATCH"])
@csrf_exempt
def update_assignment(request, assignment_id):
    try:
        assignment = models.Assignment.objects.get(id=assignment_id)

        data = json.loads(request.body)
        if 'CourseCode' in data:
            assignment.CourseCode = data['CourseCode']
        if 'Title' in data:
            assignment.Title = data['Title']
        if 'Description' in data:
            assignment.Description = data['Description']
        if 'DueDate' in data:
            assignment.DueDate = data['DueDate']

        assignment.save()
        return JsonResponse({'message': 'Assignment updated successfully'}, status=200)

    except models.Assignment.DoesNotExist:
        return JsonResponse({'error': 'Assignment not found'}, status=404)
    
@csrf_exempt
def delete_assignment(request, assignment_id):
    if request.method == 'DELETE':
        try:
            assignment = models.Assignment.objects.get(id=assignment_id)
            assignment.delete()
            return JsonResponse({'message': 'Assignment deleted successfully'}, status=200)
        except models.Department.DoesNotExist:
            return JsonResponse({'error': 'Assignment not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

## Submission Views

def get_submissions(request):
    submissions = models.Submission.objects.all()
    
    # Convert announcements to a list of dictionaries
    submissions_data = [
        {
            '_id': str(submission.id),
            'SubmissionID': submission.SubmissionID,
            'AssignmentID': submission.AssignmentID,
            'StudentID': submission.StudentID,
            'SubmissionDate': submission.SubmissionDate,
            'SubmissionLink': submission.SubmissionLink,
            'Status': submission.Status,
            'Remarks': submission.Remarks,
        }
        for submission in submissions
    ]
    
    return JsonResponse(submissions_data, safe=False)


@csrf_exempt  # Disabling CSRF for demonstration purposes; you should handle CSRF properly in production
def add_submission(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            submission = models.Submission(
                SubmissionID=data['SubmissionID'],
                AssignmentID=data['AssignmentID'],
                StudentID=data['StudentID'],
                SubmissionDate=data['SubmissionDate'],
                SubmissionLink=data['SubmissionLink'],
                Status=data['Status'],
                Remarks=data['Remarks']
            )
            submission.save()  # Save the new submission to MongoDB
            return JsonResponse({'message': 'New submission added successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@require_http_methods(["PATCH"])
@csrf_exempt
def update_submission(request, submission_id):
    try:
        submission = models.Submission.objects.get(id=submission_id)

        data = json.loads(request.body)
        if 'AssignmentID' in data:
            submission.AssignmentID = data['AssignmentID']
        if 'StudentID' in data:
            submission.StudentID = data['StudentID']
        if 'SubmissionDate' in data:
            submission.SubmissionDate = data['SubmissionDate']
        if 'SubmissionLink' in data:
            submission.SubmissionLink = data['SubmissionLink']    
        if 'Status' in data:
            submission.Status = data['Status']
        if 'Remarks' in data:
            submission.Remarks = data['Remarks']

        submission.save()
        return JsonResponse({'message': 'Submission updated successfully'}, status=200)

    except models.Submission.DoesNotExist:
        return JsonResponse({'error': 'Submission not found'}, status=404)
    

@csrf_exempt
def delete_submission(request, submission_id):
    if request.method == 'DELETE':
        try:
            submission = models.Submission.objects.get(id=submission_id)
            submission.delete()
            return JsonResponse({'message': 'Submission deleted successfully'}, status=200)
        except models.Department.DoesNotExist:
            return JsonResponse({'error': 'Submission not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)



    














