class Question:
    def __init__(self, profid, studentid, quescontent):
        self.profid = profid
        self.studentid = studentid
        self.quescontent = quescontent

class Question_w_prof_student:
    def __init__(self, prof_name, prof_surname, prof_university, prof_department, student_name, student_surname, student_university, student_department, quescontent):
		self.prof_name = prof_name
		self.prof_surname = prof_surname
		self.prof_university = prof_university
		self.prof_department = prof_department
		self.student_name = student_name
		self.student_surname = student_surname
		self.student_university = student_university
		self.student_department = student_department
		self.quescontent = quescontent
