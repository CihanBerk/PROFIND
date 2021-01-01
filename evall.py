class Eval:
    def __init__(self, courseid, studentid, subject, evall):
        self.courseid = courseid
        self.studentid = studentid
        self.subject = subject
        self.evall = evall

class Eval_w_course_student:
    def __init__(self, student_name, student_surname, student_university, student_department, course_name, course_year, course_term, subject, evall):
		self.student_name = student_name
		self.student_surname = student_surname
		self.student_university = student_university
		self.student_department = student_department
		self.course_name = course_name
		self.course_year = course_year
		self.course_term = course_term
		self.subject = subject
		self.evall = evall
