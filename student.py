class Student:
    def __init__(self, profid, name, surname, university, department):
        self.profid = profid
        self.name = name
        self.surname = surname
        self.university = university
        self.department = department

class Student_w_prof:
    def __init__(self, prof_name, prof_surname, prof_university, prof_department, name, surname, university, department):
		self.prof_name = prof_name
		self.prof_surname = prof_surname
		self.prof_university = prof_university
		self.prof_department = prof_department
		self.name = name
		self.surname = surname
		self.university = university
		self.department = department
