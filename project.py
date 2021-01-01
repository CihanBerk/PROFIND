class Project:
    def __init__(self, profid, title, agency, appyear, abstract, duration, status, totalamount, availableamount):
		self.profid = profid
		self.title = title
		self.agency = agency
		self.appyear = appyear
		self.abstract = abstract
		self.duration = duration
		self.status = status
		self.totalamount = totalamount        
		self.availableamount = availableamount

class Project_w_prof:
    def __init__(self, prof_name, prof_surname, prof_university, prof_department, title, agency, appyear, abstract, duration, status, totalamount, availableamount):
		self.prof_name = prof_name
		self.prof_surname = prof_surname
		self.prof_university = prof_university
		self.prof_department = prof_department
		self.title = title
		self.agency = agency
		self.appyear = appyear
		self.abstract = abstract
		self.duration = duration
		self.status = status
		self.totalamount = totalamount        
		self.availableamount = availableamount
