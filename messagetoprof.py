class Messagetoprof:
    def __init__(self, profid, studentid, mescontent):
        self.profid = profid
        self.studentid = studentid
        self.mescontent = mescontent

class Messagetoprof_w_prof_student:
    def __init__(self, prof_name, prof_surname, prof_university, prof_department, student_name, student_surname, student_university, student_department, mescontent):
		self.prof_name = prof_name
		self.prof_surname = prof_surname
		self.prof_university = prof_university
		self.prof_department = prof_department
		self.student_name = student_name
		self.student_surname = student_surname
		self.student_university = student_university
		self.student_department = student_department
		self.mescontent = mescontent
