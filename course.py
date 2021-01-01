class Course:
    def __init__(self, profid, name, year, term):
        self.profid = profid
        self.name = name
        self.year = year
        self.term = term

class Course_w_prof:
    def __init__(self, prof_name, prof_surname, prof_university, prof_department, name, year, term):
		self.prof_name = prof_name
		self.prof_surname = prof_surname
		self.prof_university = prof_university
		self.prof_department = prof_department
		self.name = name
		self.year = year
		self.term = term
