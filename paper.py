class Paper:
    def __init__(self, profid, title, pubyear, pubtype, pubsite):
        self.profid = profid
        self.title = title
        self.pubyear = pubyear
        self.pubtype = pubtype
        self.pubsite = pubsite

class Paper_w_prof:
    def __init__(self, prof_name, prof_surname, prof_university, prof_department, title, pubyear, pubtype, pubsite):
		self.prof_name = prof_name
		self.prof_surname = prof_surname
		self.prof_university = prof_university
		self.prof_department = prof_department
		self.title = title
		self.pubyear = pubyear
		self.pubtype = pubtype
		self.pubsite = pubsite
