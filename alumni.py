class Alumni:
    def __init__(self, profid, name, surname, degree, years):
        self.profid = profid
        self.name = name
        self.surname = surname
        self.degree = degree
        self.years = years

class Alumni_w_prof:
    def __init__(self, prof_name, prof_surname, prof_university, prof_department, name, surname, degree, years):
		self.prof_name = prof_name
		self.prof_surname = prof_surname
		self.prof_university = prof_university
		self.prof_department = prof_department
		self.name = name
		self.surname = surname
		self.degree = degree
		self.years = years
