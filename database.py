#from sqlite3 import dbapi2 as sqlite3
#import sqlite3
import sqlite3 as dbapi2

from prof import Prof
from student import Student, Student_w_prof
from paper import Paper, Paper_w_prof
from project import Project, Project_w_prof
from alumni import Alumni, Alumni_w_prof
from course import Course, Course_w_prof
from evall import Eval, Eval_w_course_student
from openposition import Openposition, Openposition_w_prof_student
from messagetoprof import Messagetoprof, Messagetoprof_w_prof_student
from question import Question, Question_w_prof_student

class Database:
	def __init__(self, dbfile):
		self.dbfile = dbfile

	def add_prof(self, prof):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "INSERT INTO PROFESSOR (NAME, SURNAME, UNIVERSITY, DEPARTMENT) VALUES (?, ?, ?, ?)"
			cursor.execute(query, (prof.name, prof.surname, prof.university, prof.department))
			connection.commit()
			prof_key = cursor.lastrowid
		return prof_key

	def add_student(self, student):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "SELECT ID, NAME FROM PROFESSOR WHERE ((NAME = ?) AND (SURNAME = ?) AND (UNIVERSITY = ?) AND (DEPARTMENT = ?))"
			cursor.execute(query, (student.prof_name, student.prof_surname, student.prof_university, student.prof_department))
			#connection.commit()
			prof_key, prof_name = cursor.fetchone()
			
			#cursor = connection.cursor()
			query = "INSERT INTO STUDENT (PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT) VALUES (?, ?, ?, ?, ?)"
			cursor.execute(query, (prof_key, student.name, student.surname, student.university, student.department))
			connection.commit()
			student_key = cursor.lastrowid
		return student_key

	def add_paper(self, paper):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "SELECT ID, NAME FROM PROFESSOR WHERE ((NAME = ?) AND (SURNAME = ?) AND (UNIVERSITY = ?) AND (DEPARTMENT = ?))"
			cursor.execute(query, (paper.prof_name, paper.prof_surname, paper.prof_university, paper.prof_department))
			#connection.commit()
			prof_key, prof_name = cursor.fetchone()
			
			query = "SELECT PAPERID, PROFID FROM PAPER"
			cursor.execute(query)
			connection.commit()
			
			count = 0
			temp = []
			for temp_paper_key, temp_profid in cursor:
				temp.append(temp_paper_key)
				count = count + 1
			
			temp_paper_key= temp[count-1]
			temp_paper_key = temp_paper_key + 1
						
			cursor = connection.cursor()
			query = "INSERT INTO PAPER (PAPERID, PROFID, TITLE, PUBYEAR, PUBTYPE, PUBSITE) VALUES (?, ?, ?, ?, ?, ?)"
			cursor.execute(query, (temp_paper_key, prof_key, paper.title, paper.pubyear, paper.pubtype, paper.pubsite))
			connection.commit()
			paper_key = cursor.lastrowid
		return paper_key

	def add_project(self, project):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "SELECT ID, NAME FROM PROFESSOR WHERE ((NAME = ?) AND (SURNAME = ?) AND (UNIVERSITY = ?) AND (DEPARTMENT = ?))"
			cursor.execute(query, (project.prof_name, project.prof_surname, project.prof_university, project.prof_department))
			#connection.commit()
			prof_key, prof_name = cursor.fetchone()
			
			query = "SELECT PROJECTID, PROFID FROM PROJECT"
			cursor.execute(query)
			connection.commit()
			
			count = 0
			temp = []
			for temp_project_key, temp_profid in cursor:
				temp.append(temp_project_key)
				count = count + 1
			
			temp_project_key= temp[count-1]
			temp_project_key = temp_project_key + 1
						
			cursor = connection.cursor()
			query = "INSERT INTO PROJECT (PROJECTID, PROFID, TITLE, AGENCY, APPYEAR, ABSTRACT, DURATION, STATUS, TOTALAMOUNT, AVAILABLEAMOUNT) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
			cursor.execute(query, (temp_project_key, prof_key, project.title, project.agency, project.appyear, project.abstract, project.duration, project.status, project.totalamount, project.availableamount))
			connection.commit()
			project_key = cursor.lastrowid
		return project_key

	def add_course(self, course):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "SELECT ID, NAME FROM PROFESSOR WHERE ((NAME = ?) AND (SURNAME = ?) AND (UNIVERSITY = ?) AND (DEPARTMENT = ?))"
			cursor.execute(query, (course.prof_name, course.prof_surname, course.prof_university, course.prof_department))
			#connection.commit()
			prof_key, prof_name = cursor.fetchone()
			
			#cursor = connection.cursor()
			query = "INSERT INTO COURSE (PROFID, NAME, YEAR, TERM) VALUES (?, ?, ?, ?)"
			cursor.execute(query, (prof_key, course.name, course.year, course.term))
			connection.commit()
			course_key = cursor.lastrowid
		return course_key

	def add_eval(self, evall):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "SELECT COURSEID, NAME FROM COURSE WHERE ((NAME = ?) AND (YEAR = ?) AND (TERM = ?))"
			cursor.execute(query, (evall.course_name, evall.course_year, evall.course_term))
			#connection.commit()
			course_key, course_name = cursor.fetchone()

			#cursor = connection.cursor()
			query = "SELECT ID, NAME FROM STUDENT WHERE ((NAME = ?) AND (SURNAME = ?) AND (UNIVERSITY = ?) AND (DEPARTMENT = ?))"
			cursor.execute(query, (evall.student_name, evall.student_surname, evall.student_university, evall.student_department))
			#connection.commit()
			#student_key, student_name = cursor.fetchone()

			if cursor.fetchone() == None:

				prof_key = 0 # This line added since the student applied to the position does not need to be advised by an professor
				#cursor = connection.cursor()
				query = "INSERT INTO STUDENT (PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT) VALUES (?, ?, ?, ?, ?)"
				cursor.execute(query, (prof_key, evall.student_name, evall.student_surname, evall.student_university, evall.student_department))
				connection.commit()
				student_key = cursor.lastrowid
				
			else:
				query = "SELECT ID, NAME FROM STUDENT WHERE ((NAME = ?) AND (SURNAME = ?) AND (UNIVERSITY = ?) AND (DEPARTMENT = ?))"
				cursor.execute(query, (openposition.student_name, openposition.student_surname, openposition.student_university, openposition.student_department))
				student_key, student_name = cursor.fetchone()			
			
			#cursor = connection.cursor()
			query = "INSERT INTO COMMENT_EVAL (COURSEID, STUDENTID, SUBJECT, EVAL) VALUES (?, ?, ?, ?)"
			cursor.execute(query, (course_key, student_key, evall.subject, evall.evall))
			connection.commit()
			eval_key = cursor.lastrowid
		return eval_key

	def add_openposition(self, openposition):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "SELECT ID, NAME FROM PROFESSOR WHERE ((NAME = ?) AND (SURNAME = ?) AND (UNIVERSITY = ?) AND (DEPARTMENT = ?))"
			cursor.execute(query, (openposition.prof_name, openposition.prof_surname, openposition.prof_university, openposition.prof_department))
			#connection.commit()
			prof_key, prof_name = cursor.fetchone()

			#cursor = connection.cursor()
			query = "SELECT ID, NAME FROM STUDENT WHERE ((NAME = ?) AND (SURNAME = ?) AND (UNIVERSITY = ?) AND (DEPARTMENT = ?))"
			cursor.execute(query, (openposition.student_name, openposition.student_surname, openposition.student_university, openposition.student_department))
			#connection.commit()
			#student_key, student_name = cursor.fetchone()
			
			if cursor.fetchone() == None:
				
				#cursor = connection.cursor()
				temp_prof_key = 0 # This line added since the student applied to the position does not need to be advised by an professor
				query = "INSERT INTO STUDENT (PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT) VALUES (?, ?, ?, ?, ?)"
				cursor.execute(query, (temp_prof_key, openposition.student_name, openposition.student_surname, openposition.student_university, openposition.student_department))
				connection.commit()
				student_key = cursor.lastrowid
			else:
				query = "SELECT ID, NAME FROM STUDENT WHERE ((NAME = ?) AND (SURNAME = ?) AND (UNIVERSITY = ?) AND (DEPARTMENT = ?))"
				cursor.execute(query, (openposition.student_name, openposition.student_surname, openposition.student_university, openposition.student_department))
				student_key, student_name = cursor.fetchone()
			#cursor = connection.cursor()
			query = "INSERT INTO OPENPOSITION (PROFID, STUDENTID, POSTYPE, REQUIREMENTS) VALUES (?, ?, ?, ?)"
			cursor.execute(query, (prof_key, student_key, openposition.postype, openposition.requirements))
			connection.commit()
			openposition_key = cursor.lastrowid
		return openposition_key

	def add_messagetoprof(self, messagetoprof):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "SELECT ID, NAME FROM PROFESSOR WHERE ((NAME = ?) AND (SURNAME = ?) AND (UNIVERSITY = ?) AND (DEPARTMENT = ?))"
			cursor.execute(query, (messagetoprof.prof_name, messagetoprof.prof_surname, messagetoprof.prof_university, messagetoprof.prof_department))
			#connection.commit()
			prof_key, prof_name = cursor.fetchone()

			#cursor = connection.cursor()
			query = "SELECT ID, NAME FROM STUDENT WHERE ((NAME = ?) AND (SURNAME = ?) AND (UNIVERSITY = ?) AND (DEPARTMENT = ?))"
			cursor.execute(query, (messagetoprof.student_name, messagetoprof.student_surname, messagetoprof.student_university, messagetoprof.student_department))
			#connection.commit()
			#student_key, student_name = cursor.fetchone()
			
			if cursor.fetchone() == None:
				
				#cursor = connection.cursor()
				temp_prof_key = 0 # This line added since the student applied to the position does not need to be advised by an professor
				query = "INSERT INTO STUDENT (PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT) VALUES (?, ?, ?, ?, ?)"
				cursor.execute(query, (temp_prof_key, messagetoprof.student_name, messagetoprof.student_surname, messagetoprof.student_university, messagetoprof.student_department))
				connection.commit()
				student_key = cursor.lastrowid
			else:
				query = "SELECT ID, NAME FROM STUDENT WHERE ((NAME = ?) AND (SURNAME = ?) AND (UNIVERSITY = ?) AND (DEPARTMENT = ?))"
				cursor.execute(query, (messagetoprof.student_name, messagetoprof.student_surname, messagetoprof.student_university, messagetoprof.student_department))
				student_key, student_name = cursor.fetchone()
			#cursor = connection.cursor()
			query = "INSERT INTO MESSAGETOPROF (PROFID, STUDENTID, MESCONTENT) VALUES (?, ?, ?)"
			cursor.execute(query, (prof_key, student_key, messagetoprof.mescontent))
			connection.commit()
			messagetoprof_key = cursor.lastrowid
		return messagetoprof_key

	def add_question(self, question):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "SELECT ID, NAME FROM PROFESSOR WHERE ((NAME = ?) AND (SURNAME = ?) AND (UNIVERSITY = ?) AND (DEPARTMENT = ?))"
			cursor.execute(query, (question.prof_name, question.prof_surname, question.prof_university, question.prof_department))
			#connection.commit()
			prof_key, prof_name = cursor.fetchone()

			#cursor = connection.cursor()
			query = "SELECT ID, NAME FROM STUDENT WHERE ((NAME = ?) AND (SURNAME = ?) AND (UNIVERSITY = ?) AND (DEPARTMENT = ?))"
			cursor.execute(query, (question.student_name, question.student_surname, question.student_university, question.student_department))
			#connection.commit()
			#student_key, student_name = cursor.fetchone()
			
			if cursor.fetchone() == None:
				
				#cursor = connection.cursor()
				temp_prof_key = 0 # This line added since the student applied to the position does not need to be advised by an professor
				query = "INSERT INTO STUDENT (PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT) VALUES (?, ?, ?, ?, ?)"
				cursor.execute(query, (temp_prof_key, question.student_name, question.student_surname, question.student_university, question.student_department))
				connection.commit()
				student_key = cursor.lastrowid
			else:
				query = "SELECT ID, NAME FROM STUDENT WHERE ((NAME = ?) AND (SURNAME = ?) AND (UNIVERSITY = ?) AND (DEPARTMENT = ?))"
				cursor.execute(query, (question.student_name, question.student_surname, question.student_university, question.student_department))
				student_key, student_name = cursor.fetchone()
			#cursor = connection.cursor()
			query = "INSERT INTO QUESTION (PROFID, STUDENTID, QUESCONTENT) VALUES (?, ?, ?)"
			cursor.execute(query, (prof_key, student_key, question.quescontent))
			connection.commit()
			question_key = cursor.lastrowid
		return question_key

	def add_alumni(self, alumni):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "SELECT ID, NAME FROM PROFESSOR WHERE ((NAME = ?) AND (SURNAME = ?) AND (UNIVERSITY = ?) AND (DEPARTMENT = ?))"
			cursor.execute(query, (alumni.prof_name, alumni.prof_surname, alumni.prof_university, alumni.prof_department))
			#connection.commit()
			prof_key, prof_name = cursor.fetchone()
			
			#cursor = connection.cursor()
			query = "INSERT INTO ALUMNI (PROFID, NAME, SURNAME, DEGREE, TOTYEAR) VALUES (?, ?, ?, ?, ?)"
			cursor.execute(query, (prof_key, alumni.name, alumni.surname, alumni.degree, alumni.years))
			connection.commit()
			alumni_key = cursor.lastrowid
		return alumni_key


	def update_prof(self, prof_key, prof):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "UPDATE PROFESSOR SET NAME = ?, SURNAME = ?, UNIVERSITY = ?, DEPARTMENT = ? WHERE (ID = ?)"
			cursor.execute(query, (prof.name, prof.surname, prof.university, prof.department, prof_key))
			connection.commit()

	def update_student(self, student_key, student):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "SELECT ID, NAME FROM PROFESSOR WHERE ((NAME = ?) AND (SURNAME = ?) AND (UNIVERSITY = ?) AND (DEPARTMENT = ?))"
			cursor.execute(query, (student.prof_name, student.prof_surname, student.prof_university, student.prof_department))
			#connection.commit()
			prof_key, prof_name = cursor.fetchone()
						
			cursor = connection.cursor()
			query = "UPDATE STUDENT SET PROFID = ?, NAME = ?, SURNAME = ?, UNIVERSITY = ?, DEPARTMENT = ? WHERE (ID = ?)"
			cursor.execute(query, ( prof_key, student.name, student.surname, student.university, student.department, student_key))
			connection.commit()

	def update_paper(self, paper_key, paper):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "SELECT ID, NAME FROM PROFESSOR WHERE ((NAME = ?) AND (SURNAME = ?) AND (UNIVERSITY = ?) AND (DEPARTMENT = ?))"
			cursor.execute(query, (paper.prof_name, paper.prof_surname, paper.prof_university, paper.prof_department))
			#connection.commit()
			prof_key, prof_name = cursor.fetchone()
						
			cursor = connection.cursor()
			query = "UPDATE PAPER SET PROFID = ?, TITLE = ?, PUBYEAR = ?, PUBTYPE = ?, PUBSITE = ? WHERE (PAPERID = ?)"
			cursor.execute(query, ( prof_key, paper.title, paper.pubyear, paper.pubtype, paper.pubsite, paper_key))
			connection.commit()

	def update_project(self, project_key, project):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "SELECT ID, NAME FROM PROFESSOR WHERE ((NAME = ?) AND (SURNAME = ?) AND (UNIVERSITY = ?) AND (DEPARTMENT = ?))"
			cursor.execute(query, (project.prof_name, project.prof_surname, project.prof_university, project.prof_department))
			#connection.commit()
			prof_key, prof_name = cursor.fetchone()
						
			cursor = connection.cursor()
			query = "UPDATE PROJECT SET PROFID = ?, TITLE = ?, AGENCY = ?, APPYEAR = ?, ABSTRACT = ?, DURATION = ?, STATUS = ?, TOTALAMOUNT = ?, AVAILABLEAMOUNT = ? WHERE (PROJECTID = ?)"
			cursor.execute(query, ( prof_key, project.title, project.agency, project.appyear, project.abstract, project.duration, project.status, project.totalamount, project.availableamount, project_key))
			connection.commit()

	def update_course(self, course_key, course):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "SELECT ID, NAME FROM PROFESSOR WHERE ((NAME = ?) AND (SURNAME = ?) AND (UNIVERSITY = ?) AND (DEPARTMENT = ?))"
			cursor.execute(query, (course.prof_name, course.prof_surname, course.prof_university, course.prof_department))
			#connection.commit()
			prof_key, prof_name = cursor.fetchone()
						
			cursor = connection.cursor()
			query = "UPDATE COURSE SET PROFID = ?, NAME = ?, YEAR= ?, TERM = ? WHERE (COURSEID = ?)"
			cursor.execute(query, ( prof_key, course.name, course.year, course.term, course_key))
			connection.commit()

	def update_eval(self, eval_key, evall):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "SELECT ID, NAME FROM STUDENT WHERE ((NAME = ?) AND (SURNAME = ?) AND (UNIVERSITY = ?) AND (DEPARTMENT = ?))"
			cursor.execute(query, (evall.student_name, evall.student_surname, evall.student_university, evall.student_department))
			#connection.commit()
			student_key, student_name = cursor.fetchone()

			cursor = connection.cursor()
			query = "SELECT COURSEID, NAME FROM COURSE WHERE ((NAME = ?) AND (YEAR = ?) AND (TERM = ?))"
			cursor.execute(query, (evall.course_name, evall.course_year, evall.course_term))
			#connection.commit()
			course_key, course_name = cursor.fetchone()

			cursor = connection.cursor()
			query = "UPDATE COMMENT_EVAL SET COURSEID = ?, STUDENTID = ?, SUBJECT = ?, EVAL = ? WHERE (EVALID = ?)"
			cursor.execute(query, ( course_key, student_key, evall.subject, evall.evall, eval_key))
			connection.commit()

	def update_openposition(self, openposition_key, openposition):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "SELECT ID, NAME FROM PROFESSOR WHERE ((NAME = ?) AND (SURNAME = ?) AND (UNIVERSITY = ?) AND (DEPARTMENT = ?))"
			cursor.execute(query, (openposition.prof_name, openposition.prof_surname, openposition.prof_university, openposition.prof_department))
			#connection.commit()
			prof_key, prof_name = cursor.fetchone()

			#cursor = connection.cursor()
			query = "SELECT ID, NAME FROM STUDENT WHERE ((NAME = ?) AND (SURNAME = ?) AND (UNIVERSITY = ?) AND (DEPARTMENT = ?))"
			cursor.execute(query, (openposition.student_name, openposition.student_surname, openposition.student_university, openposition.student_department))
			#connection.commit()
			student_key, student_name = cursor.fetchone()

			cursor = connection.cursor()
			query = "UPDATE OPENPOSITION SET PROFID = ?, STUDENTID = ?, POSTYPE = ?, REQUIREMENTS = ? WHERE (POSITIONID = ?)"
			cursor.execute(query, ( prof_key, student_key, openposition.postype, openposition.requirements, openposition_key))
			connection.commit()

	def update_messagetoprof(self, messagetoprof_key, messagetoprof):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "SELECT ID, NAME FROM PROFESSOR WHERE ((NAME = ?) AND (SURNAME = ?) AND (UNIVERSITY = ?) AND (DEPARTMENT = ?))"
			cursor.execute(query, (messagetoprof.prof_name, messagetoprof.prof_surname, messagetoprof.prof_university, messagetoprof.prof_department))
			#connection.commit()
			prof_key, prof_name = cursor.fetchone()

			#cursor = connection.cursor()
			query = "SELECT ID, NAME FROM STUDENT WHERE ((NAME = ?) AND (SURNAME = ?) AND (UNIVERSITY = ?) AND (DEPARTMENT = ?))"
			cursor.execute(query, (messagetoprof.student_name, messagetoprof.student_surname, messagetoprof.student_university, messagetoprof.student_department))
			#connection.commit()
			student_key, student_name = cursor.fetchone()

			cursor = connection.cursor()
			query = "UPDATE MESSAGETOPROF SET PROFID = ?, STUDENTID = ?, MESCONTENT = ? WHERE (MESSAGEID = ?)"
			cursor.execute(query, ( prof_key, student_key, messagetoprof.mescontent, messagetoprof_key))
			connection.commit()

	def update_question(self, question_key, question):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "SELECT ID, NAME FROM PROFESSOR WHERE ((NAME = ?) AND (SURNAME = ?) AND (UNIVERSITY = ?) AND (DEPARTMENT = ?))"
			cursor.execute(query, (question.prof_name, question.prof_surname, question.prof_university, question.prof_department))
			#connection.commit()
			prof_key, prof_name = cursor.fetchone()

			#cursor = connection.cursor()
			query = "SELECT ID, NAME FROM STUDENT WHERE ((NAME = ?) AND (SURNAME = ?) AND (UNIVERSITY = ?) AND (DEPARTMENT = ?))"
			cursor.execute(query, (question.student_name, question.student_surname, question.student_university, question.student_department))
			#connection.commit()
			student_key, student_name = cursor.fetchone()

			cursor = connection.cursor()
			query = "UPDATE QUESTION SET PROFID = ?, STUDENTID = ?, QUESCONTENT = ? WHERE (QUESTIONID = ?)"
			cursor.execute(query, ( prof_key, student_key, question.quescontent, question_key))
			connection.commit()

	def update_alumni(self, alumni_key, alumni):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "SELECT ID, NAME FROM PROFESSOR WHERE ((NAME = ?) AND (SURNAME = ?) AND (UNIVERSITY = ?) AND (DEPARTMENT = ?))"
			cursor.execute(query, (alumni.prof_name, alumni.prof_surname, alumni.prof_university, alumni.prof_department))
			#connection.commit()
			prof_key, prof_name = cursor.fetchone()

			cursor = connection.cursor()
			query = "UPDATE ALUMNI SET PROFID = ?, NAME = ?, SURNAME = ?, DEGREE = ?, TOTYEAR = ? WHERE (ALUMNIID = ?)"
			cursor.execute(query, ( prof_key, alumni.name, alumni.surname, alumni.degree, alumni.years, alumni_key))
			connection.commit()


	def delete_prof(self, prof_key):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "DELETE FROM PROFESSOR WHERE (ID = ?)"
			cursor.execute(query, (prof_key,))
			connection.commit()

	def delete_student(self, student_key):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "DELETE FROM STUDENT WHERE (ID = ?)"
			cursor.execute(query, (student_key,))
			connection.commit()

	def delete_paper(self, paper_key):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "DELETE FROM PAPER WHERE (PAPERID = ?)"
			cursor.execute(query, (paper_key,))
			connection.commit()

	def delete_project(self, project_key):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "DELETE FROM PROJECT WHERE (PROJECTID = ?)"
			cursor.execute(query, (project_key,))
			connection.commit()

	def delete_course(self, course_key):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "DELETE FROM COURSE WHERE (COURSEID = ?)"
			cursor.execute(query, (course_key,))
			connection.commit()

	def delete_eval(self, eval_key):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "DELETE FROM COMMENT_EVAL WHERE (EVALID = ?)"
			cursor.execute(query, (eval_key,))
			connection.commit()

	def delete_openposition(self, openposition_key):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "DELETE FROM OPENPOSITION WHERE (POSITIONID = ?)"
			cursor.execute(query, (openposition_key,))
			connection.commit()

	def delete_messagetoprof(self, messagetoprof_key):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "DELETE FROM MESSAGETOPROF WHERE (MESSAGEID = ?)"
			cursor.execute(query, (messagetoprof_key,))
			connection.commit()

	def delete_question(self, question_key):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "DELETE FROM QUESTION WHERE (QUESTIONID = ?)"
			cursor.execute(query, (question_key,))
			connection.commit()

	def delete_alumni(self, alumni_key):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "DELETE FROM ALUMNI WHERE (ALUMNIID = ?)"
			cursor.execute(query, (alumni_key,))
			connection.commit()


	def get_prof(self, prof_key):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "SELECT NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM PROFESSOR WHERE (ID = ?)"
			cursor.execute(query, (prof_key,))
			name, surname, university, department = cursor.fetchone()
		prof_ = Prof(name, surname, university, department)
		return prof_

	def get_edit_prof(self, prof):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			#query = "SELECT ID FROM PROFESSOR WHERE (( NAME = ?) AND ( SURNAME = ?))"
			query = "SELECT ID, NAME FROM PROFESSOR WHERE ((NAME = ?) AND (SURNAME = ?) AND (UNIVERSITY = ?) AND (DEPARTMENT = ?))"
			cursor.execute(query, (prof.name, prof.surname, prof.university, prof.department))
			#connection.commit()
			prof_key, prof_name = cursor.fetchone()
		return prof_key

	def get_student(self, student_key):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			#query = "SELECT PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM STUDENT WHERE (ID = ?)"
			query = "SELECT PROFESSOR.NAME, PROFESSOR.SURNAME, PROFESSOR.UNIVERSITY, PROFESSOR.DEPARTMENT, STUDENT.NAME, STUDENT.SURNAME, STUDENT.UNIVERSITY, STUDENT.DEPARTMENT FROM STUDENT, PROFESSOR WHERE ((STUDENT.PROFID = PROFESSOR.ID) AND (STUDENT.ID = ?))"
			cursor.execute(query, (student_key,))
			prof_name, prof_surname, prof_university, prof_department, name, surname, university, department = cursor.fetchone()
			#profid, name, surname, university, department = cursor.fetchone()
		student_ = Student_w_prof(prof_name, prof_surname, prof_university, prof_department, name, surname, university, department)
		return student_

	def get_paper(self, paper_key):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			#query = "SELECT PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM STUDENT WHERE (ID = ?)"
			query = "SELECT PROFESSOR.NAME, PROFESSOR.SURNAME, PROFESSOR.UNIVERSITY, PROFESSOR.DEPARTMENT, PAPER.TITLE, PAPER.PUBYEAR, PAPER.PUBTYPE, PAPER.PUBSITE FROM PAPER, PROFESSOR WHERE ((PAPER.PROFID = PROFESSOR.ID) AND (PAPER.PAPERID = ?))"
			cursor.execute(query, (paper_key,))
			prof_name, prof_surname, prof_university, prof_department, title, pubyear, pubtype, pubsite = cursor.fetchone()
			#profid, name, surname, university, department = cursor.fetchone()
		paper_ = Paper_w_prof(prof_name, prof_surname, prof_university, prof_department, title, pubyear, pubtype, pubsite)
		return paper_

	def get_project(self, project_key):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			#query = "SELECT PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM STUDENT WHERE (ID = ?)"
			query = "SELECT PROFESSOR.NAME, PROFESSOR.SURNAME, PROFESSOR.UNIVERSITY, PROFESSOR.DEPARTMENT, PROJECT.TITLE, PROJECT.AGENCY, PROJECT.APPYEAR, PROJECT.ABSTRACT, PROJECT.DURATION, PROJECT.STATUS, PROJECT.TOTALAMOUNT, PROJECT.AVAILABLEAMOUNT FROM PROJECT, PROFESSOR WHERE ((PROJECT.PROFID = PROFESSOR.ID) AND (PROJECT.PROJECTID = ?))"
			cursor.execute(query, (project_key,))
			prof_name, prof_surname, prof_university, prof_department, title, agency, appyear, abstract, duration, status, totalamount, availableamount = cursor.fetchone()
			#profid, name, surname, university, department = cursor.fetchone()
		project_ = Project_w_prof(prof_name, prof_surname, prof_university, prof_department, title, agency, appyear, abstract, duration, status, totalamount, availableamount)
		return project_

	def get_course(self, course_key):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			#query = "SELECT PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM STUDENT WHERE (ID = ?)"
			query = "SELECT PROFESSOR.NAME, PROFESSOR.SURNAME, PROFESSOR.UNIVERSITY, PROFESSOR.DEPARTMENT, COURSE.NAME, COURSE.YEAR, COURSE.TERM FROM COURSE, PROFESSOR WHERE ((COURSE.PROFID = PROFESSOR.ID) AND  (COURSE.COURSEID = ?))"
			cursor.execute(query, (course_key,))
			prof_name, prof_surname, prof_university, prof_department, name, year, term = cursor.fetchone()
			#profid, name, surname, university, department = cursor.fetchone()
		course_ = Course_w_prof(prof_name, prof_surname, prof_university, prof_department, name, year, term)
		return course_

	def get_eval(self, eval_key):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			#query = "SELECT PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM STUDENT WHERE (ID = ?)"
			#query = "SELECT PROFESSOR.NAME, PROFESSOR.SURNAME, PROFESSOR.UNIVERSITY, PROFESSOR.DEPARTMENT, COURSE.NAME, COURSE.YEAR, COURSE.TERM FROM COURSE, PROFESSOR WHERE ((COURSE.PROFID = PROFESSOR.ID) AND  (COURSE.COURSEID = ?))"
			query = "SELECT STUDENT.NAME, STUDENT.SURNAME, STUDENT.UNIVERSITY, STUDENT.DEPARTMENT, COURSE.NAME, COURSE.YEAR, COURSE.TERM, COMMENT_EVAL.SUBJECT, COMMENT_EVAL.EVAL FROM STUDENT, COURSE, COMMENT_EVAL WHERE ((COMMENT_EVAL.STUDENTID = STUDENT.ID) AND (COMMENT_EVAL.COURSEID = COURSE.COURSEID) AND  (COMMENT_EVAL.EVALID = ?))"
			cursor.execute(query, (eval_key,))
			student_name, student_surname, student_university, student_department, course_name, course_year, course_term, subject, evall = cursor.fetchone()
			#profid, name, surname, university, department = cursor.fetchone()
		eval_ = Eval_w_course_student(student_name, student_surname, student_university, student_department, course_name, course_year, course_term, subject, evall)
		return eval_

	def get_openposition(self, openposition_key):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			#query = "SELECT PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM STUDENT WHERE (ID = ?)"
			#query = "SELECT PROFESSOR.NAME, PROFESSOR.SURNAME, PROFESSOR.UNIVERSITY, PROFESSOR.DEPARTMENT, COURSE.NAME, COURSE.YEAR, COURSE.TERM FROM COURSE, PROFESSOR WHERE ((COURSE.PROFID = PROFESSOR.ID) AND  (COURSE.COURSEID = ?))"
			query = "SELECT PROFESSOR.NAME, PROFESSOR.SURNAME, PROFESSOR.UNIVERSITY, PROFESSOR.DEPARTMENT, STUDENT.NAME, STUDENT.SURNAME, STUDENT.UNIVERSITY, STUDENT.DEPARTMENT, OPENPOSITION.POSTYPE, OPENPOSITION.REQUIREMENTS FROM PROFESSOR, STUDENT, OPENPOSITION WHERE ((OPENPOSITION.STUDENTID = STUDENT.ID) AND (OPENPOSITION.PROFID = PROFESSOR.ID) AND  (OPENPOSITION.POSITIONID = ?))"
			cursor.execute(query, (openposition_key,))
			prof_name, prof_surname, prof_university, prof_department, student_name, student_surname, student_university, student_department, postype, requirements = cursor.fetchone()
			#profid, name, surname, university, department = cursor.fetchone()
		openposition_ = Openposition_w_prof_student(prof_name, prof_surname, prof_university, prof_department, student_name, student_surname, student_university, student_department, postype, requirements)
		return openposition_

	def get_messagetoprof(self, messagetoprof_key):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			#query = "SELECT PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM STUDENT WHERE (ID = ?)"
			#query = "SELECT PROFESSOR.NAME, PROFESSOR.SURNAME, PROFESSOR.UNIVERSITY, PROFESSOR.DEPARTMENT, COURSE.NAME, COURSE.YEAR, COURSE.TERM FROM COURSE, PROFESSOR WHERE ((COURSE.PROFID = PROFESSOR.ID) AND  (COURSE.COURSEID = ?))"
			query = "SELECT PROFESSOR.NAME, PROFESSOR.SURNAME, PROFESSOR.UNIVERSITY, PROFESSOR.DEPARTMENT, STUDENT.NAME, STUDENT.SURNAME, STUDENT.UNIVERSITY, STUDENT.DEPARTMENT, MESSAGETOPROF.MESCONTENT FROM PROFESSOR, STUDENT, MESSAGETOPROF WHERE ((MESSAGETOPROF.STUDENTID = STUDENT.ID) AND (MESSAGETOPROF.PROFID = PROFESSOR.ID) AND  (MESSAGETOPROF.MESSAGEID = ?))"
			cursor.execute(query, (messagetoprof_key,))
			prof_name, prof_surname, prof_university, prof_department, student_name, student_surname, student_university, student_department, mescontent = cursor.fetchone()
			#profid, name, surname, university, department = cursor.fetchone()
		messagetoprof_ = Messagetoprof_w_prof_student(prof_name, prof_surname, prof_university, prof_department, student_name, student_surname, student_university, student_department, mescontent)
		return messagetoprof_

	def get_question(self, question_key):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			#query = "SELECT PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM STUDENT WHERE (ID = ?)"
			#query = "SELECT PROFESSOR.NAME, PROFESSOR.SURNAME, PROFESSOR.UNIVERSITY, PROFESSOR.DEPARTMENT, COURSE.NAME, COURSE.YEAR, COURSE.TERM FROM COURSE, PROFESSOR WHERE ((COURSE.PROFID = PROFESSOR.ID) AND  (COURSE.COURSEID = ?))"
			query = "SELECT PROFESSOR.NAME, PROFESSOR.SURNAME, PROFESSOR.UNIVERSITY, PROFESSOR.DEPARTMENT, STUDENT.NAME, STUDENT.SURNAME, STUDENT.UNIVERSITY, STUDENT.DEPARTMENT, QUESTION.QUESCONTENT FROM PROFESSOR, STUDENT, QUESTION WHERE ((QUESTION.STUDENTID = STUDENT.ID) AND (QUESTION.PROFID = PROFESSOR.ID) AND  (QUESTION.QUESTIONID = ?))"
			cursor.execute(query, (question_key,))
			prof_name, prof_surname, prof_university, prof_department, student_name, student_surname, student_university, student_department, quescontent = cursor.fetchone()
			#profid, name, surname, university, department = cursor.fetchone()
		question_ = Question_w_prof_student(prof_name, prof_surname, prof_university, prof_department, student_name, student_surname, student_university, student_department, quescontent)
		return question_

	def get_alumni(self, alumni_key):
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			#query = "SELECT PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM STUDENT WHERE (ID = ?)"
			query = "SELECT PROFESSOR.NAME, PROFESSOR.SURNAME, PROFESSOR.UNIVERSITY, PROFESSOR.DEPARTMENT, ALUMNI.NAME, ALUMNI.SURNAME, ALUMNI.DEGREE, ALUMNI.TOTYEAR FROM ALUMNI, PROFESSOR WHERE ((ALUMNI.PROFID = PROFESSOR.ID) AND  (ALUMNI.ALUMNIID = ?))"
			cursor.execute(query, (alumni_key,))
			prof_name, prof_surname, prof_university, prof_department, name, surname, degree, years = cursor.fetchone()
			#profid, name, surname, university, department = cursor.fetchone()
		alumni_ = Alumni_w_prof(prof_name, prof_surname, prof_university, prof_department,name, surname, degree, years)
		return alumni_


	def get_profs(self):
		profs = []
		with dbapi2.connect(self.dbfile) as connection:
			cursor = connection.cursor()
			query = "SELECT ID, NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM PROFESSOR ORDER BY ID"
			cursor.execute(query)
			for prof_key, name, surname, university, department in cursor:
				profs.append((prof_key, Prof(name, surname, university, department)))
		return profs

	def get_students(self):
		students = []
		with dbapi2.connect(self.dbfile) as connection:
			#cursor = connection.cursor()
			#query = "SELECT ID, PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM STUDENT ORDER BY ID"
			#cursor.execute(query)
			cursor = connection.cursor()
			query = "SELECT STUDENT.ID, PROFESSOR.NAME, PROFESSOR.SURNAME, PROFESSOR.UNIVERSITY, PROFESSOR.DEPARTMENT, STUDENT.NAME, STUDENT.SURNAME, STUDENT.UNIVERSITY, STUDENT.DEPARTMENT FROM STUDENT, PROFESSOR WHERE (STUDENT.PROFID = PROFESSOR.ID) ORDER BY STUDENT.ID"
			cursor.execute(query)
			for student_key, prof_name, prof_surname, prof_university, prof_department, name, surname, university, department in cursor:
				students.append((student_key, Student_w_prof(prof_name, prof_surname, prof_university, prof_department, name, surname, university, department)))
		return students

	def get_papers(self):
		papers = []
		with dbapi2.connect(self.dbfile) as connection:
			#cursor = connection.cursor()
			#query = "SELECT ID, PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM STUDENT ORDER BY ID"
			#cursor.execute(query)
			cursor = connection.cursor()
			query = "SELECT PAPER.PAPERID, PROFESSOR.NAME, PROFESSOR.SURNAME, PROFESSOR.UNIVERSITY, PROFESSOR.DEPARTMENT, PAPER.TITLE, PAPER.PUBYEAR, PAPER.PUBTYPE, PAPER.PUBSITE FROM PAPER, PROFESSOR WHERE (PAPER.PROFID = PROFESSOR.ID) ORDER BY PAPER.PAPERID"
			cursor.execute(query)
			for paper_key, prof_name, prof_surname, prof_university, prof_department, title, pubyear, pubtype, pubsite in cursor:
				papers.append((paper_key, Paper_w_prof(prof_name, prof_surname, prof_university, prof_department, title, pubyear, pubtype, pubsite)))
		return papers

	def get_projects(self):
		projects = []
		with dbapi2.connect(self.dbfile) as connection:
			#cursor = connection.cursor()
			#query = "SELECT ID, PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM STUDENT ORDER BY ID"
			#cursor.execute(query)
			cursor = connection.cursor()
			query = "SELECT PROJECT.PROJECTID, PROFESSOR.NAME, PROFESSOR.SURNAME, PROFESSOR.UNIVERSITY, PROFESSOR.DEPARTMENT, PROJECT.TITLE, PROJECT.AGENCY, PROJECT.APPYEAR, PROJECT.ABSTRACT, PROJECT.DURATION, PROJECT.STATUS, PROJECT.TOTALAMOUNT, PROJECT.AVAILABLEAMOUNT FROM PROJECT, PROFESSOR WHERE (PROJECT.PROFID = PROFESSOR.ID) ORDER BY PROJECT.PROJECTID"
			cursor.execute(query)
			for project_key, prof_name, prof_surname, prof_university, prof_department, title, agency, appyear, abstract, duration, status, totalamount, availableamount in cursor:
				projects.append((project_key, Project_w_prof(prof_name, prof_surname, prof_university, prof_department, title, agency, appyear, abstract, duration, status, totalamount, availableamount)))
		return projects

	def get_courses(self):
		courses = []
		with dbapi2.connect(self.dbfile) as connection:
			#cursor = connection.cursor()
			#query = "SELECT ID, PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM STUDENT ORDER BY ID"
			#cursor.execute(query)
			cursor = connection.cursor()
			query = "SELECT COURSE.COURSEID, PROFESSOR.NAME, PROFESSOR.SURNAME, PROFESSOR.UNIVERSITY, PROFESSOR.DEPARTMENT, COURSE.NAME, COURSE.YEAR, COURSE.TERM FROM COURSE, PROFESSOR WHERE (COURSE.PROFID = PROFESSOR.ID) ORDER BY COURSE.COURSEID"
			cursor.execute(query)
			for course_key, prof_name, prof_surname, prof_university, prof_department, name, year, term in cursor:
				courses.append((course_key, Course_w_prof(prof_name, prof_surname, prof_university, prof_department, name, year, term)))
		return courses

	def get_evals(self):
		evals = []
		with dbapi2.connect(self.dbfile) as connection:
			#cursor = connection.cursor()
			#query = "SELECT ID, PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM STUDENT ORDER BY ID"
			#cursor.execute(query)
			cursor = connection.cursor()
			query = "SELECT COMMENT_EVAL.EVALID, STUDENT.NAME, STUDENT.SURNAME, STUDENT.UNIVERSITY, STUDENT.DEPARTMENT, COURSE.NAME, COURSE.YEAR, COURSE.TERM, COMMENT_EVAL.SUBJECT, COMMENT_EVAL.EVAL FROM STUDENT, COURSE, COMMENT_EVAL WHERE ((COMMENT_EVAL.STUDENTID = STUDENT.ID) AND (COMMENT_EVAL.COURSEID = COURSE.COURSEID)) ORDER BY COMMENT_EVAL.EVALID"
			cursor.execute(query)
			for eval_key, student_name, student_surname, student_university, student_department, course_name, course_year, course_term, subject, evall in cursor:
				evals.append((eval_key, Eval_w_course_student(student_name, student_surname, student_university, student_department, course_name, course_year, course_term, subject, evall)))
		return evals

	def get_openpositions(self):
		openpositions = []
		with dbapi2.connect(self.dbfile) as connection:
			#cursor = connection.cursor()
			#query = "SELECT ID, PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM STUDENT ORDER BY ID"
			#cursor.execute(query)
			cursor = connection.cursor()
			query = "SELECT OPENPOSITION.POSITIONID, PROFESSOR.NAME, PROFESSOR.SURNAME, PROFESSOR.UNIVERSITY, PROFESSOR.DEPARTMENT, STUDENT.NAME, STUDENT.SURNAME, STUDENT.UNIVERSITY, STUDENT.DEPARTMENT, OPENPOSITION.POSTYPE, OPENPOSITION.REQUIREMENTS FROM PROFESSOR, STUDENT, OPENPOSITION WHERE ((OPENPOSITION.STUDENTID = STUDENT.ID) AND (OPENPOSITION.PROFID = PROFESSOR.ID)) ORDER BY OPENPOSITION.POSITIONID"
			cursor.execute(query)
			for openposition_key, prof_name, prof_surname, prof_university, prof_department, student_name, student_surname, student_university, student_department, postype, requirements in cursor:
				openpositions.append((openposition_key, Openposition_w_prof_student(prof_name, prof_surname, prof_university, prof_department, student_name, student_surname, student_university, student_department, postype, requirements)))
		return openpositions

	def get_messagetoprofs(self):
		messagetoprofs = []
		with dbapi2.connect(self.dbfile) as connection:
			#cursor = connection.cursor()
			#query = "SELECT ID, PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM STUDENT ORDER BY ID"
			#cursor.execute(query)
			cursor = connection.cursor()
			query = "SELECT MESSAGETOPROF.MESSAGEID, PROFESSOR.NAME, PROFESSOR.SURNAME, PROFESSOR.UNIVERSITY, PROFESSOR.DEPARTMENT, STUDENT.NAME, STUDENT.SURNAME, STUDENT.UNIVERSITY, STUDENT.DEPARTMENT, MESSAGETOPROF.MESCONTENT FROM PROFESSOR, STUDENT, MESSAGETOPROF WHERE ((MESSAGETOPROF.STUDENTID = STUDENT.ID) AND (MESSAGETOPROF.PROFID = PROFESSOR.ID)) ORDER BY MESSAGETOPROF.MESSAGEID"
			cursor.execute(query)
			for messagetoprof_key, prof_name, prof_surname, prof_university, prof_department, student_name, student_surname, student_university, student_department, mescontent in cursor:
				messagetoprofs.append((messagetoprof_key, Messagetoprof_w_prof_student(prof_name, prof_surname, prof_university, prof_department, student_name, student_surname, student_university, student_department, mescontent)))
		return messagetoprofs

	def get_questions(self):
		questions = []
		with dbapi2.connect(self.dbfile) as connection:
			#cursor = connection.cursor()
			#query = "SELECT ID, PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM STUDENT ORDER BY ID"
			#cursor.execute(query)
			cursor = connection.cursor()
			query = "SELECT QUESTION.QUESTIONID, PROFESSOR.NAME, PROFESSOR.SURNAME, PROFESSOR.UNIVERSITY, PROFESSOR.DEPARTMENT, STUDENT.NAME, STUDENT.SURNAME, STUDENT.UNIVERSITY, STUDENT.DEPARTMENT, QUESTION.QUESCONTENT FROM PROFESSOR, STUDENT, QUESTION WHERE ((QUESTION.STUDENTID = STUDENT.ID) AND (QUESTION.PROFID = PROFESSOR.ID)) ORDER BY QUESTION.QUESTIONID"
			cursor.execute(query)
			for question_key, prof_name, prof_surname, prof_university, prof_department, student_name, student_surname, student_university, student_department, quescontent in cursor:
				questions.append((question_key, Question_w_prof_student(prof_name, prof_surname, prof_university, prof_department, student_name, student_surname, student_university, student_department, quescontent)))
		return questions

	def get_alumnis(self):
		alumnis = []
		with dbapi2.connect(self.dbfile) as connection:
			#cursor = connection.cursor()
			#query = "SELECT ID, PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM STUDENT ORDER BY ID"
			#cursor.execute(query)
			cursor = connection.cursor()
			query = "SELECT ALUMNI.ALUMNIID, PROFESSOR.NAME, PROFESSOR.SURNAME, PROFESSOR.UNIVERSITY, PROFESSOR.DEPARTMENT, ALUMNI.NAME, ALUMNI.SURNAME, ALUMNI.DEGREE, ALUMNI.TOTYEAR FROM ALUMNI, PROFESSOR WHERE (ALUMNI.PROFID = PROFESSOR.ID) ORDER BY ALUMNI.ALUMNIID"
			cursor.execute(query)
			for alumni_key, prof_name, prof_surname, prof_university, prof_department, name, surname, degree, years in cursor:
				alumnis.append((alumni_key, Alumni_w_prof(prof_name, prof_surname, prof_university, prof_department, name, surname, degree, years)))
		return alumnis

		
	def get_prof_students(self, prof_key):
		students = []
		with dbapi2.connect(self.dbfile) as connection:
			#cursor = connection.cursor()
			#query = "SELECT ID, PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM STUDENT ORDER BY ID"
			#cursor.execute(query)
			cursor = connection.cursor()
			query = "SELECT STUDENT.ID, STUDENT.PROFID, STUDENT.NAME, STUDENT.SURNAME, STUDENT.UNIVERSITY, STUDENT.DEPARTMENT FROM STUDENT, PROFESSOR WHERE ((STUDENT.PROFID = PROFESSOR.ID) AND (PROFESSOR.ID = ?))"
			cursor.execute(query, (prof_key,))
			for student_key, profid, name, surname, university, department in cursor:
				students.append((student_key, Student(profid, name, surname, university, department)))
		return students

	def get_prof_papers(self, prof_key):
		papers = []
		with dbapi2.connect(self.dbfile) as connection:
			#cursor = connection.cursor()
			#query = "SELECT ID, PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM STUDENT ORDER BY ID"
			#cursor.execute(query)
			cursor = connection.cursor()
			query = "SELECT PAPER.PAPERID, PAPER.PROFID, PAPER.TITLE, PAPER.PUBYEAR, PAPER.PUBTYPE, PAPER.PUBSITE FROM PAPER, PROFESSOR WHERE ((PAPER.PROFID = PROFESSOR.ID) AND (PROFESSOR.ID = ?))"
			cursor.execute(query, (prof_key,))
			for paper_key, profid, title, pubyear, pubtype, pubsite in cursor:
				papers.append((paper_key, Paper(profid, title, pubyear, pubtype, pubsite)))
		return papers

	def get_prof_projects(self, prof_key):
		projects = []
		with dbapi2.connect(self.dbfile) as connection:
			#cursor = connection.cursor()
			#query = "SELECT ID, PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM STUDENT ORDER BY ID"
			#cursor.execute(query)
			cursor = connection.cursor()
			query = "SELECT PROJECT.PROJECTID, PROJECT.PROFID, PROJECT.TITLE, PROJECT.AGENCY, PROJECT.APPYEAR, PROJECT.ABSTRACT, PROJECT.DURATION, PROJECT.STATUS, PROJECT.TOTALAMOUNT, PROJECT.AVAILABLEAMOUNT FROM PROJECT, PROFESSOR WHERE ((PROJECT.PROFID = PROFESSOR.ID) AND (PROFESSOR.ID = ?))"
			cursor.execute(query, (prof_key,))
			for project_key, profid, title, agency, appyear, abstract, duration, status, totalamount, availableamount in cursor:
				projects.append((project_key, Project(profid, title, agency, appyear, abstract, duration, status, totalamount, availableamount)))
		return projects

	def get_prof_courses(self, prof_key):
		courses = []
		with dbapi2.connect(self.dbfile) as connection:
			#cursor = connection.cursor()
			#query = "SELECT ID, PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM STUDENT ORDER BY ID"
			#cursor.execute(query)
			cursor = connection.cursor()
			query = "SELECT COURSE.COURSEID, COURSE.PROFID, COURSE.NAME, COURSE.YEAR, COURSE.TERM FROM COURSE, PROFESSOR WHERE ((COURSE.PROFID = PROFESSOR.ID) AND (PROFESSOR.ID = ?))"
			cursor.execute(query, (prof_key,))
			for course_key, profid, name, year, term in cursor:
				courses.append((course_key, Course(profid, name, year, term)))
		return courses

	def get_prof_alumnis(self, prof_key):
		alumnis = []
		with dbapi2.connect(self.dbfile) as connection:
			#cursor = connection.cursor()
			#query = "SELECT ID, PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM STUDENT ORDER BY ID"
			#cursor.execute(query)
			cursor = connection.cursor()
			query = "SELECT ALUMNI.ALUMNIID, ALUMNI.PROFID, ALUMNI.NAME, ALUMNI.SURNAME, ALUMNI.DEGREE, ALUMNI.TOTYEAR FROM ALUMNI, PROFESSOR WHERE ((ALUMNI.PROFID = PROFESSOR.ID) AND (PROFESSOR.ID = ?))"
			cursor.execute(query, (prof_key,))
			for alumni_key, profid, name, surname, degree, years in cursor:
				alumnis.append((alumni_key, Alumni(profid, name, surname, degree, years)))
		return alumnis

	def get_prof_openpositions(self, prof_key):
		openpositions = []
		with dbapi2.connect(self.dbfile) as connection:
			#cursor = connection.cursor()
			#query = "SELECT ID, PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM STUDENT ORDER BY ID"
			#cursor.execute(query)
			cursor = connection.cursor()
			query = "SELECT OPENPOSITION.POSITIONID, PROFESSOR.NAME, PROFESSOR.SURNAME, PROFESSOR.UNIVERSITY, PROFESSOR.DEPARTMENT, STUDENT.NAME, STUDENT.SURNAME, STUDENT.UNIVERSITY, STUDENT.DEPARTMENT, OPENPOSITION.POSTYPE, OPENPOSITION.REQUIREMENTS FROM PROFESSOR, STUDENT, OPENPOSITION WHERE ((OPENPOSITION.STUDENTID = STUDENT.ID) AND (OPENPOSITION.PROFID = PROFESSOR.ID) AND (PROFESSOR.ID = ?))"
			cursor.execute(query, (prof_key,))
			for openposition_key, prof_name, prof_surname, prof_university, prof_department, student_name, student_surname, student_university, student_department, postype, requirements in cursor:
				openpositions.append((openposition_key, Openposition_w_prof_student(prof_name, prof_surname, prof_university, prof_department, student_name, student_surname, student_university, student_department, postype, requirements)))
		return openpositions

	def get_prof_messagetoprofs(self, prof_key):
		messagetoprofs = []
		with dbapi2.connect(self.dbfile) as connection:
			#cursor = connection.cursor()
			#query = "SELECT ID, PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM STUDENT ORDER BY ID"
			#cursor.execute(query)
			cursor = connection.cursor()
			query = "SELECT MESSAGETOPROF.MESSAGEID, PROFESSOR.NAME, PROFESSOR.SURNAME, PROFESSOR.UNIVERSITY, PROFESSOR.DEPARTMENT, STUDENT.NAME, STUDENT.SURNAME, STUDENT.UNIVERSITY, STUDENT.DEPARTMENT, MESSAGETOPROF.MESCONTENT FROM PROFESSOR, STUDENT, MESSAGETOPROF WHERE ((MESSAGETOPROF.STUDENTID = STUDENT.ID) AND (MESSAGETOPROF.PROFID = PROFESSOR.ID) AND (PROFESSOR.ID = ?))"
			cursor.execute(query, (prof_key,))
			for messagetoprof_key, prof_name, prof_surname, prof_university, prof_department, student_name, student_surname, student_university, student_department, mescontent in cursor:
				messagetoprofs.append((messagetoprof_key, Messagetoprof_w_prof_student(prof_name, prof_surname, prof_university, prof_department, student_name, student_surname, student_university, student_department, mescontent)))
		return messagetoprofs

	def get_prof_questions(self, prof_key):
		questions = []
		with dbapi2.connect(self.dbfile) as connection:
			#cursor = connection.cursor()
			#query = "SELECT ID, PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM STUDENT ORDER BY ID"
			#cursor.execute(query)
			cursor = connection.cursor()
			query = "SELECT QUESTION.QUESTIONID, PROFESSOR.NAME, PROFESSOR.SURNAME, PROFESSOR.UNIVERSITY, PROFESSOR.DEPARTMENT, STUDENT.NAME, STUDENT.SURNAME, STUDENT.UNIVERSITY, STUDENT.DEPARTMENT, QUESTION.QUESCONTENT FROM PROFESSOR, STUDENT, QUESTION WHERE ((QUESTION.STUDENTID = STUDENT.ID) AND (QUESTION.PROFID = PROFESSOR.ID) AND (PROFESSOR.ID = ?))"
			cursor.execute(query, (prof_key,))
			for question_key, prof_name, prof_surname, prof_university, prof_department, student_name, student_surname, student_university, student_department, quescontent in cursor:
				questions.append((question_key, Question_w_prof_student(prof_name, prof_surname, prof_university, prof_department, student_name, student_surname, student_university, student_department, quescontent)))
		return questions

	def get_course_evals(self, course_key):
		evals = []
		with dbapi2.connect(self.dbfile) as connection:
			#cursor = connection.cursor()
			#query = "SELECT ID, PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM STUDENT ORDER BY ID"
			#cursor.execute(query)
			cursor = connection.cursor()
			query = "SELECT COMMENT_EVAL.EVALID, STUDENT.NAME, STUDENT.SURNAME, STUDENT.UNIVERSITY, STUDENT.DEPARTMENT, COURSE.NAME, COURSE.YEAR, COURSE.TERM, COMMENT_EVAL.SUBJECT, COMMENT_EVAL.EVAL FROM STUDENT, COURSE, COMMENT_EVAL WHERE ((COMMENT_EVAL.STUDENTID = STUDENT.ID) AND (COMMENT_EVAL.COURSEID = COURSE.COURSEID) AND (COURSE.COURSEID = ?))"
			cursor.execute(query, (course_key,))
			for eval_key, student_name, student_surname, student_university, student_department, course_name, course_year, course_term, subject, evall in cursor:
				evals.append((eval_key, Eval_w_course_student(student_name, student_surname, student_university, student_department, course_name, course_year, course_term, subject, evall)))
		return evals

	def get_openposition_students(self, openposition_key):
		students = []
		with dbapi2.connect(self.dbfile) as connection:
			#cursor = connection.cursor()
			#query = "SELECT ID, PROFID, NAME, SURNAME, UNIVERSITY, DEPARTMENT FROM STUDENT ORDER BY ID"
			#cursor.execute(query)
			cursor = connection.cursor()
			query = "SELECT  STUDENT.ID, PROFESSOR.NAME, PROFESSOR.SURNAME, PROFESSOR.UNIVERSITY, PROFESSOR.DEPARTMENT, STUDENT.NAME, STUDENT.SURNAME, STUDENT.UNIVERSITY, STUDENT.DEPARTMENT FROM STUDENT, PROFESSOR, OPENPOSITION WHERE ((OPENPOSITION.STUDENTID = STUDENT.ID) AND (OPENPOSITION.PROFID = PROFESSOR.ID) AND (OPENPOSITION.POSITIONID = ?))"
			cursor.execute(query, (openposition_key,))
			for student_key, prof_name, prof_surname, prof_university, prof_department, name, surname, university, department in cursor:
				students.append((student_key, Student_w_prof(prof_name, prof_surname, prof_university, prof_department, name, surname, university, department)))
		return students
