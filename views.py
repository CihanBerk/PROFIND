# Every file or function that returns a webpage for viewing goes into this python file
from flask import Flask, render_template
from flask_login import LoginManager
from flask_login import login_required, login_user, current_user, logout_user
from flask_login import UserMixin

from user import get_user, User
from flask import flash
from passlib.hash import pbkdf2_sha256 as hasher

from flask_wtf import FlaskForm
from flask_wtf import *
from wtforms import StringField, PasswordField
from wtforms import *

from wtforms.validators import DataRequired, NumberRange, Optional
from wtforms_components import IntegerField


#from flask import Flask, current_app, render_template
from datetime import datetime

from flask import abort, current_app, render_template
from flask import request, redirect, url_for

from database import Database
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

from forms import *

import sqlite3 as dbapi2
#from flask import *

def home_page():
	
	today = datetime.today()
	day_name = today.strftime("%A")
	return render_template("home.html", day = day_name) 

def profs_page():
	# Here db is not the same as in server.py since we used another one there to add movies to movies class
	db = current_app.config["db"]
	#movies = db.get_movies()
	#return render_template("movies.html", movies = sorted(movies))
	if request.method == "GET":
		profs = db.get_profs()
		return render_template("profs.html", profs=sorted(profs))
	else:
		if not current_user.is_admin:
			abort(401)
		form_prof_keys = request.form.getlist("prof_keys")
		for form_prof_key in form_prof_keys:
			db.delete_prof(int(form_prof_key))
		flash("%(num)d professors deleted." % {"num": len(form_prof_keys)})
		return redirect(url_for("profs_page"))

def students_page():
	# Here db is not the same as in server.py since we used another one there to add movies to movies class
	db = current_app.config["db"]
	#movies = db.get_movies()
	#return render_template("movies.html", movies = sorted(movies))
	if request.method == "GET":
		students = db.get_students()
		return render_template("students.html", students=sorted(students))
	else:
		if not current_user.is_admin:
			abort(401)
		form_student_keys = request.form.getlist("student_keys")
		for form_student_key in form_student_keys:
			db.delete_student(int(form_student_key))
		flash("%(num)d students deleted." % {"num": len(form_student_keys)})
		return redirect(url_for("students_page"))

def papers_page():
	# Here db is not the same as in server.py since we used another one there to add movies to movies class
	db = current_app.config["db"]
	#movies = db.get_movies()
	#return render_template("movies.html", movies = sorted(movies))
	if request.method == "GET":
		papers = db.get_papers()
		return render_template("papers.html", papers=sorted(papers))
	else:
		if not current_user.is_admin:
			abort(401)
		form_paper_keys = request.form.getlist("paper_keys")
		for form_paper_key in form_paper_keys:
			db.delete_paper(int(form_paper_key))
		flash("%(num)d papers deleted." % {"num": len(form_paper_keys)})
		return redirect(url_for("papers_page"))

def projects_page():
	# Here db is not the same as in server.py since we used another one there to add movies to movies class
	db = current_app.config["db"]
	#movies = db.get_movies()
	#return render_template("movies.html", movies = sorted(movies))
	if request.method == "GET":
		projects = db.get_projects()
		return render_template("projects.html", projects=sorted(projects))
	else:
		if not current_user.is_admin:
			abort(401)
		form_project_keys = request.form.getlist("project_keys")
		for form_project_key in form_project_keys:
			db.delete_project(int(form_project_key))
		flash("%(num)d projects deleted." % {"num": len(form_project_keys)})
		return redirect(url_for("projects_page"))

def courses_page():
	# Here db is not the same as in server.py since we used another one there to add movies to movies class
	db = current_app.config["db"]
	#movies = db.get_movies()
	#return render_template("movies.html", movies = sorted(movies))
	if request.method == "GET":
		courses = db.get_courses()
		return render_template("courses.html", courses=sorted(courses))
	else:
		if not current_user.is_admin:
			abort(401)
		form_course_keys = request.form.getlist("course_keys")
		for form_course_key in form_course_keys:
			db.delete_course(int(form_course_key))
		flash("%(num)d courses deleted." % {"num": len(form_course_keys)})
		return redirect(url_for("courses_page"))

def evals_page():
	# Here db is not the same as in server.py since we used another one there to add movies to movies class
	db = current_app.config["db"]
	#movies = db.get_movies()
	#return render_template("movies.html", movies = sorted(movies))
	if request.method == "GET":
		evals = db.get_evals()
		return render_template("evals.html", evals=sorted(evals))
	else:
		if not current_user.is_admin:
			abort(401)
		form_eval_keys = request.form.getlist("eval_keys")
		for form_eval_key in form_eval_keys:
			db.delete_eval(int(form_eval_key))
		flash("%(num)d evals deleted." % {"num": len(form_eval_keys)})
		return redirect(url_for("evals_page"))

def openpositions_page():
	# Here db is not the same as in server.py since we used another one there to add movies to movies class
	db = current_app.config["db"]
	#movies = db.get_movies()
	#return render_template("movies.html", movies = sorted(movies))
	if request.method == "GET":
		openpositions = db.get_openpositions()
		return render_template("openpositions.html", openpositions=sorted(openpositions))
	else:
		if not current_user.is_admin:
			abort(401)
		form_openposition_keys = request.form.getlist("openposition_keys")
		for form_openposition_key in form_openposition_keys:
			db.delete_openposition(int(form_openposition_key))
		flash("%(num)d open positions deleted." % {"num": len(form_openposition_keys)})
		return redirect(url_for("openpositions_page"))

def messagetoprofs_page():
	# Here db is not the same as in server.py since we used another one there to add movies to movies class
	db = current_app.config["db"]
	#movies = db.get_movies()
	#return render_template("movies.html", movies = sorted(movies))
	if request.method == "GET":
		messagetoprofs = db.get_messagetoprofs()
		return render_template("messagetoprofs.html", messagetoprofs=sorted(messagetoprofs))
	else:
		if not current_user.is_admin:
			abort(401)
		form_messagetoprof_keys = request.form.getlist("messagetoprof_keys")
		for form_messagetoprof_key in form_messagetoprof_keys:
			db.delete_messagetoprof(int(form_messagetoprof_key))
		flash("%(num)d messages deleted." % {"num": len(form_messagetoprof_keys)})
		return redirect(url_for("messagetoprofs_page"))

def questions_page():
	# Here db is not the same as in server.py since we used another one there to add movies to movies class
	db = current_app.config["db"]
	#movies = db.get_movies()
	#return render_template("movies.html", movies = sorted(movies))
	if request.method == "GET":
		questions = db.get_questions()
		return render_template("questions.html", questions=sorted(questions))
	else:
		if not current_user.is_admin:
			abort(401)
		form_question_keys = request.form.getlist("question_keys")
		for form_question_key in form_question_keys:
			db.delete_question(int(form_question_key))
		flash("%(num)d questions deleted." % {"num": len(form_question_keys)})
		return redirect(url_for("questions_page"))

def alumnis_page():
	# Here db is not the same as in server.py since we used another one there to add movies to movies class
	db = current_app.config["db"]
	#movies = db.get_movies()
	#return render_template("movies.html", movies = sorted(movies))
	if request.method == "GET":
		alumnis = db.get_alumnis()
		return render_template("alumnis.html", alumnis=sorted(alumnis))
	else:
		if not current_user.is_admin:
			abort(401)
		form_alumni_keys = request.form.getlist("alumni_keys")
		for form_alumni_key in form_alumni_keys:
			db.delete_alumni(int(form_alumni_key))
		flash("%(num)d alumnis deleted." % {"num": len(form_alumni_keys)})
		return redirect(url_for("alumnis_page"))


def prof_page(prof_key):
	db = current_app.config["db"]
	prof = db.get_prof(prof_key)
	
	students = []
	students = db.get_prof_students(prof_key)
	papers = []
	papers = db.get_prof_papers(prof_key)
	projects = []
	projects = db.get_prof_projects(prof_key)	
	courses = []
	courses = db.get_prof_courses(prof_key)
	alumnis = []
	alumnis = db.get_prof_alumnis(prof_key)
	
	openpositions = []
	openpositions = db.get_prof_openpositions(prof_key)
	messagetoprofs = []
	messagetoprofs = db.get_prof_messagetoprofs(prof_key)
	questions = []
	questions = db.get_prof_questions(prof_key)
	
	if prof is None:
		abort(404)
	return render_template("prof.html", prof=prof, students=students, papers=papers, projects=projects, courses=courses, alumnis=alumnis, openpositions=openpositions, messagetoprofs=messagetoprofs, questions=questions)

def student_page(student_key):
    db = current_app.config["db"]
    student = db.get_student(student_key)
    if student is None:
		abort(404)
    return render_template("student.html", student=student)

def paper_page(paper_key):
    db = current_app.config["db"]
    paper = db.get_paper(paper_key)
    if paper is None:
		abort(404)
    return render_template("paper.html", paper=paper)

def project_page(project_key):
    db = current_app.config["db"]
    project = db.get_project(project_key)
    if project is None:
		abort(404)
    return render_template("project.html", project=project)

def course_page(course_key):
    db = current_app.config["db"]
    course = db.get_course(course_key)
    evals = []
    evals = db.get_course_evals(course_key)
    if course is None:
		abort(404)
    return render_template("course.html", course=course, evals=evals)

def eval_page(eval_key):
    db = current_app.config["db"]
    evall = db.get_eval(eval_key)
    if evall is None:
		abort(404)
    return render_template("eval.html", evall=evall)

def openposition_page(openposition_key):
	db = current_app.config["db"]
	openposition = db.get_openposition(openposition_key)

	students = []
	students = db.get_openposition_students(openposition_key)
	if openposition is None:
		abort(404)
	return render_template("openposition.html", openposition=openposition, students=students)

def messagetoprof_page(messagetoprof_key):
    db = current_app.config["db"]
    messagetoprof = db.get_messagetoprof(messagetoprof_key)
    if messagetoprof is None:
		abort(404)
    return render_template("messagetoprof.html", messagetoprof=messagetoprof)

def question_page(question_key):
    db = current_app.config["db"]
    question = db.get_question(question_key)
    if question is None:
		abort(404)
    return render_template("question.html", question=question)

def alumni_page(alumni_key):
    db = current_app.config["db"]
    alumni = db.get_alumni(alumni_key)
    if alumni is None:
		abort(404)
    return render_template("alumni.html", alumni=alumni)



@login_required
def prof_add_page():
	if not current_user.is_admin:
		abort(401)
	form = ProfEditForm()
	if form.validate_on_submit():
		name = form.data["name"]
		surname = form.data["surname"]
		university = form.data["university"]
		department = form.data["department"]
		prof = Prof(name, surname, university, department)
		db = current_app.config["db"]
		# add_movie function returns mmovie key at the end of the addition
		prof_key = db.add_prof(prof) 
		return redirect(url_for("prof_page", prof_key=prof_key))
	return render_template("prof_edit.html", form=form)

@login_required
def student_add_page():
	if not current_user.is_admin:
		abort(401)
	form = StudentEditForm()
	if form.validate_on_submit():
		#profid = form.data["profid"]
		#name = form.data["name"]
		#surname = form.data["surname"]
		#university = form.data["university"]
		#department = form.data["department"]
		prof_name = form.data["prof_name"]
		prof_surname = form.data["prof_surname"]
		prof_university = form.data["prof_university"]
		prof_department = form.data["prof_department"]
		name = form.data["name"]
		surname = form.data["surname"]
		university = form.data["university"]
		department = form.data["department"]
		student = Student_w_prof(prof_name, prof_surname, prof_university, prof_department, name, surname, university, department)
		db = current_app.config["db"]
		student_key = db.add_student(student) 
		
		# add_movie function returns mmovie key at the end of the addition
		#student_key = db.add_student(student) 
		return redirect(url_for("student_page", student_key=student_key))
	return render_template("student_edit.html", form=form)

@login_required
def paper_add_page():
	if not current_user.is_admin:
		abort(401)
	form = PaperEditForm()
	if form.validate_on_submit():
		#profid = form.data["profid"]
		#name = form.data["name"]
		#surname = form.data["surname"]
		#university = form.data["university"]
		#department = form.data["department"]
		prof_name = form.data["prof_name"]
		prof_surname = form.data["prof_surname"]
		prof_university = form.data["prof_university"]
		prof_department = form.data["prof_department"]
		title = form.data["title"]
		pubyear = form.data["pubyear"]
		pubtype = form.data["pubtype"]
		pubsite = form.data["pubsite"]
		paper = Paper_w_prof(prof_name, prof_surname, prof_university, prof_department, title, pubyear, pubtype, pubsite)
		db = current_app.config["db"]
		paper_key = db.add_paper(paper) 
		
		# add_movie function returns mmovie key at the end of the addition
		#student_key = db.add_student(student) 
		return redirect(url_for("paper_page", paper_key=paper_key))
	return render_template("paper_edit.html", form=form)

@login_required
def project_add_page():
	if not current_user.is_admin:
		abort(401)
	form = ProjectEditForm()
	if form.validate_on_submit():
		#profid = form.data["profid"]
		#name = form.data["name"]
		#surname = form.data["surname"]
		#university = form.data["university"]
		#department = form.data["department"]
		prof_name = form.data["prof_name"]
		prof_surname = form.data["prof_surname"]
		prof_university = form.data["prof_university"]
		prof_department = form.data["prof_department"]
		title = form.data["title"]
		agency = form.data["agency"]
		appyear = form.data["appyear"]
		abstract = form.data["abstract"]
		duration = form.data["duration"]
		status = form.data["status"]
		totalamount = form.data["totalamount"]
		availableamount = form.data["availableamount"]
		project = Project_w_prof(prof_name, prof_surname, prof_university, prof_department, title, agency, appyear, abstract, duration, status, totalamount, availableamount)
		db = current_app.config["db"]
		project_key = db.add_project(project) 
		
		# add_movie function returns mmovie key at the end of the addition
		#student_key = db.add_student(student) 
		return redirect(url_for("project_page", project_key=project_key))
	return render_template("project_edit.html", form=form)

@login_required
def course_add_page():
	if not current_user.is_admin:
		abort(401)
	form = CourseEditForm()
	if form.validate_on_submit():
		#profid = form.data["profid"]
		#name = form.data["name"]
		#surname = form.data["surname"]
		#university = form.data["university"]
		#department = form.data["department"]
		prof_name = form.data["prof_name"]
		prof_surname = form.data["prof_surname"]
		prof_university = form.data["prof_university"]
		prof_department = form.data["prof_department"]
		name = form.data["name"]
		year = form.data["year"]
		term = form.data["term"]
		course = Course_w_prof(prof_name, prof_surname, prof_university, prof_department, name, year, term)
		db = current_app.config["db"]
		course_key = db.add_course(course) 
		
		# add_movie function returns mmovie key at the end of the addition
		#student_key = db.add_student(student) 
		return redirect(url_for("course_page", course_key=course_key))
	return render_template("course_edit.html", form=form)

@login_required
def eval_add_page():
	if not current_user.is_admin:
		abort(401)
	form = EvalEditForm()
	if form.validate_on_submit():
		#profid = form.data["profid"]
		#name = form.data["name"]
		#surname = form.data["surname"]
		#university = form.data["university"]
		#department = form.data["department"]
		course_name = form.data["course_name"]
		course_year = form.data["course_year"]
		course_term = form.data["course_term"]
		student_name = form.data["student_name"]
		student_surname = form.data["student_surname"]
		student_university = form.data["student_university"]
		student_department = form.data["student_department"]
		subject = form.data["subject"]
		evall = form.data["evall"]
		evall = Eval_w_course_student(student_name, student_surname, student_university, student_department,course_name, course_year, course_term, subject, evall)
		db = current_app.config["db"]
		eval_key = db.add_eval(evall) 
		
		# add_movie function returns mmovie key at the end of the addition
		#student_key = db.add_student(student) 
		return redirect(url_for("eval_page", eval_key=eval_key))
	return render_template("eval_edit.html", form=form)

@login_required
def openposition_add_page():
	if not current_user.is_admin:
		abort(401)
	form = OpenpositionEditForm()
	if form.validate_on_submit():
		#profid = form.data["profid"]
		prof_name = form.data["prof_name"]
		prof_surname = form.data["prof_surname"]
		prof_university = form.data["prof_university"]
		prof_department = form.data["prof_department"]
		#course_name = form.data["course_name"]
		#course_year = form.data["course_year"]
		#course_term = form.data["course_term"]
		student_name = form.data["student_name"]
		student_surname = form.data["student_surname"]
		student_university = form.data["student_university"]
		student_department = form.data["student_department"]
		postype = form.data["postype"]
		requirements = form.data["requirements"]
		openposition = Openposition_w_prof_student(prof_name, prof_surname, prof_university, prof_department, student_name, student_surname, student_university, student_department, postype, requirements)
		db = current_app.config["db"]
		openposition_key = db.add_openposition(openposition) 
		
		# add_movie function returns mmovie key at the end of the addition
		#student_key = db.add_student(student) 
		return redirect(url_for("openposition_page", openposition_key=openposition_key))
	return render_template("openposition_edit.html", form=form)

@login_required
def messagetoprof_add_page():
	if not current_user.is_admin:
		abort(401)
	form = MessagetoprofEditForm()
	if form.validate_on_submit():
		#profid = form.data["profid"]
		prof_name = form.data["prof_name"]
		prof_surname = form.data["prof_surname"]
		prof_university = form.data["prof_university"]
		prof_department = form.data["prof_department"]
		#course_name = form.data["course_name"]
		#course_year = form.data["course_year"]
		#course_term = form.data["course_term"]
		student_name = form.data["student_name"]
		student_surname = form.data["student_surname"]
		student_university = form.data["student_university"]
		student_department = form.data["student_department"]
		mescontent = form.data["mescontent"]
		messagetoprof = Messagetoprof_w_prof_student(prof_name, prof_surname, prof_university, prof_department, student_name, student_surname, student_university, student_department, mescontent)
		db = current_app.config["db"]
		messagetoprof_key = db.add_messagetoprof(messagetoprof) 
		
		# add_movie function returns mmovie key at the end of the addition
		#student_key = db.add_student(student) 
		return redirect(url_for("messagetoprof_page", messagetoprof_key=messagetoprof_key))
	return render_template("messagetoprof_edit.html", form=form)

@login_required
def question_add_page():
	if not current_user.is_admin:
		abort(401)
	form = QuestionEditForm()
	if form.validate_on_submit():
		#profid = form.data["profid"]
		prof_name = form.data["prof_name"]
		prof_surname = form.data["prof_surname"]
		prof_university = form.data["prof_university"]
		prof_department = form.data["prof_department"]
		#course_name = form.data["course_name"]
		#course_year = form.data["course_year"]
		#course_term = form.data["course_term"]
		student_name = form.data["student_name"]
		student_surname = form.data["student_surname"]
		student_university = form.data["student_university"]
		student_department = form.data["student_department"]
		quescontent = form.data["quescontent"]
		question = Question_w_prof_student(prof_name, prof_surname, prof_university, prof_department, student_name, student_surname, student_university, student_department, quescontent)
		db = current_app.config["db"]
		question_key = db.add_question(question) 
		
		# add_movie function returns mmovie key at the end of the addition
		#student_key = db.add_student(student) 
		return redirect(url_for("question_page", question_key=question_key))
	return render_template("question_edit.html", form=form)

@login_required
def alumni_add_page():
	if not current_user.is_admin:
		abort(401)
	form = AlumniEditForm()
	if form.validate_on_submit():
		#profid = form.data["profid"]
		#name = form.data["name"]
		#surname = form.data["surname"]
		#university = form.data["university"]
		#department = form.data["department"]
		prof_name = form.data["prof_name"]
		prof_surname = form.data["prof_surname"]
		prof_university = form.data["prof_university"]
		prof_department = form.data["prof_department"]
		name = form.data["name"]
		surname = form.data["surname"]
		degree = form.data["degree"]
		years = form.data["years"]
		alumni = Alumni_w_prof(prof_name, prof_surname, prof_university, prof_department, name, surname, degree, years)
		db = current_app.config["db"]
		alumni_key = db.add_alumni(alumni) 
		
		# add_movie function returns mmovie key at the end of the addition
		#student_key = db.add_student(student) 
		return redirect(url_for("alumni_page", alumni_key=alumni_key))
	return render_template("alumni_edit.html", form=form)


@login_required
def prof_edit_page(prof_key):
	db = current_app.config["db"]
	prof = db.get_prof(prof_key)
	form = ProfEditForm()
	if form.validate_on_submit():
		name = form.data["name"]
		surname = form.data["surname"]
		university = form.data["university"]
		department = form.data["department"]
		prof = Prof(name, surname, university, department)
		#prof_key = db.add_prof(prof) 
		#prof_key = db.get_edit_prof(prof)
		db.update_prof(prof_key, prof)
		return redirect(url_for("prof_page", prof_key=prof_key))
	form.name.data = prof.name	
	form.surname.data = prof.surname
	form.university.data = prof.university
	form.department.data = prof.department
	return render_template("prof_edit.html", form=form)

@login_required
def student_edit_page(student_key):
	db = current_app.config["db"]
	student = db.get_student(student_key)
	form = StudentEditForm()
	if form.validate_on_submit():
		#profid = form.data["profid"]
		prof_name = form.data["prof_name"]
		prof_surname = form.data["prof_surname"]
		prof_university = form.data["prof_university"]
		prof_department = form.data["prof_department"]
		name = form.data["name"]
		surname = form.data["surname"]
		university = form.data["university"]
		department = form.data["department"]
		student = Student_w_prof(prof_name, prof_surname, prof_university, prof_department, name, surname, university, department)
		#student_key = db.add_student(student) 
		db.update_student(student_key, student)
		return redirect(url_for("student_page", student_key=student_key))
	form.prof_name.data = student.prof_name
	form.prof_surname.data = student.prof_surname
	form.prof_university.data = student.prof_university
	form.prof_department.data = student.prof_department
	form.name.data = student.name	
	form.surname.data = student.surname
	form.university.data = student.university
	form.department.data = student.department
	return render_template("student_edit.html", form=form)

@login_required
def paper_edit_page(paper_key):
	db = current_app.config["db"]
	paper = db.get_paper(paper_key)
	form = PaperEditForm()
	if form.validate_on_submit():
		#profid = form.data["profid"]
		prof_name = form.data["prof_name"]
		prof_surname = form.data["prof_surname"]
		prof_university = form.data["prof_university"]
		prof_department = form.data["prof_department"]
		title = form.data["title"]
		pubyear = form.data["pubyear"]
		pubtype = form.data["pubtype"]
		pubsite = form.data["pubsite"]
		paper = Paper_w_prof(prof_name, prof_surname, prof_university, prof_department, title, pubyear, pubtype, pubsite)
		#student_key = db.add_student(student) 
		db.update_paper(paper_key, paper)
		return redirect(url_for("paper_page", paper_key=paper_key))
	form.prof_name.data = paper.prof_name
	form.prof_surname.data = paper.prof_surname
	form.prof_university.data = paper.prof_university
	form.prof_department.data = paper.prof_department
	form.title.data = paper.title	
	form.pubyear.data = paper.pubyear
	form.pubtype.data = paper.pubtype
	form.pubsite.data = paper.pubsite
	return render_template("paper_edit.html", form=form)

@login_required
def project_edit_page(project_key):
	db = current_app.config["db"]
	project = db.get_project(project_key)
	form = ProjectEditForm()
	if form.validate_on_submit():
		#profid = form.data["profid"]
		prof_name = form.data["prof_name"]
		prof_surname = form.data["prof_surname"]
		prof_university = form.data["prof_university"]
		prof_department = form.data["prof_department"]
		title = form.data["title"]
		agency = form.data["agency"]
		appyear = form.data["appyear"]
		abstract = form.data["abstract"]
		duration = form.data["duration"]
		status = form.data["status"]
		totalamount = form.data["totalamount"]
		availableamount = form.data["availableamount"]
		project = Project_w_prof(prof_name, prof_surname, prof_university, prof_department, title, agency, appyear, abstract, duration, status, totalamount, availableamount) 
		db.update_project(project_key, project)
		return redirect(url_for("project_page", project_key=project_key))
	form.prof_name.data = project.prof_name
	form.prof_surname.data = project.prof_surname
	form.prof_university.data = project.prof_university
	form.prof_department.data = project.prof_department
	form.title.data = project.title	
	form.agency.data = project.agency
	form.appyear.data = project.appyear
	form.abstract.data = project.abstract
	form.duration.data = project.duration
	form.status.data = project.status
	form.totalamount.data = project.totalamount
	form.availableamount.data = project.availableamount
	return render_template("project_edit.html", form=form)

@login_required
def course_edit_page(course_key):
	db = current_app.config["db"]
	course = db.get_course(course_key)
	form = CourseEditForm()
	if form.validate_on_submit():
		#profid = form.data["profid"]
		prof_name = form.data["prof_name"]
		prof_surname = form.data["prof_surname"]
		prof_university = form.data["prof_university"]
		prof_department = form.data["prof_department"]
		name = form.data["name"]
		year = form.data["year"]
		term = form.data["term"]
		course = Course_w_prof(prof_name, prof_surname, prof_university, prof_department, name, year, term)
		#student_key = db.add_student(student) 
		db.update_course(course_key, course)
		return redirect(url_for("course_page", course_key=course_key))
	form.prof_name.data = course.prof_name
	form.prof_surname.data = course.prof_surname
	form.prof_university.data = course.prof_university
	form.prof_department.data = course.prof_department
	form.name.data = course.name	
	form.year.data = course.year
	form.term.data = course.term
	return render_template("course_edit.html", form=form)

@login_required
def eval_edit_page(eval_key):
	db = current_app.config["db"]
	evall = db.get_eval(eval_key)
	form = EvalEditForm()
	if form.validate_on_submit():
		#profid = form.data["profid"]
		course_name = form.data["course_name"]
		course_year = form.data["course_year"]
		course_term = form.data["course_term"]
		student_name = form.data["student_name"]
		student_surname = form.data["student_surname"]
		student_university = form.data["student_university"]
		student_department = form.data["student_department"]
		subject = form.data["subject"]
		evall = form.data["evall"]
		evall = Eval_w_course_student(student_name, student_surname, student_university, student_department,course_name, course_year, course_term, subject, evall)
		#student_key = db.add_student(student) 
		db.update_eval(eval_key, evall)
		return redirect(url_for("eval_page", eval_key=eval_key))
	form.course_name.data = evall.course_name
	form.course_year.data = evall.course_year
	form.course_term.data = evall.course_term
	form.student_name.data = evall.student_name
	form.student_surname.data = evall.student_surname
	form.student_university.data = evall.student_university
	form.student_department.data = evall.student_department
	form.subject.data = evall.subject	
	form.evall.data = evall.evall
	return render_template("eval_edit.html", form=form)

@login_required
def openposition_edit_page(openposition_key):
	db = current_app.config["db"]
	openposition = db.get_openposition(openposition_key)
	form = OpenpositionEditForm()
	if form.validate_on_submit():
		#profid = form.data["profid"]
		prof_name = form.data["prof_name"]
		prof_surname = form.data["prof_surname"]
		prof_university = form.data["prof_university"]
		prof_department = form.data["prof_department"]
		#course_name = form.data["course_name"]
		#course_year = form.data["course_year"]
		#course_term = form.data["course_term"]
		student_name = form.data["student_name"]
		student_surname = form.data["student_surname"]
		student_university = form.data["student_university"]
		student_department = form.data["student_department"]
		postype = form.data["postype"]
		requirements = form.data["requirements"]
		openposition = Openposition_w_prof_student(prof_name, prof_surname, prof_university, prof_department, student_name, student_surname, student_university, student_department, postype, requirements)
		#student_key = db.add_student(student) 
		db.update_openposition(openposition_key, openposition)
		return redirect(url_for("openposition_page", openposition_key=openposition_key))
	form.prof_name.data = openposition.prof_name
	form.prof_surname.data = openposition.prof_surname
	form.prof_university.data = openposition.prof_university
	form.prof_department.data = openposition.prof_department
	form.student_name.data = openposition.student_name
	form.student_surname.data = openposition.student_surname
	form.student_university.data = openposition.student_university
	form.student_department.data = openposition.student_department
	form.postype.data = openposition.postype	
	form.requirements.data = openposition.requirements
	return render_template("openposition_edit.html", form=form)

@login_required
def messagetoprof_edit_page(messagetoprof_key):
	db = current_app.config["db"]
	messagetoprof = db.get_messagetoprof(messagetoprof_key)
	form = MessagetoprofEditForm()
	if form.validate_on_submit():
		#profid = form.data["profid"]
		prof_name = form.data["prof_name"]
		prof_surname = form.data["prof_surname"]
		prof_university = form.data["prof_university"]
		prof_department = form.data["prof_department"]
		#course_name = form.data["course_name"]
		#course_year = form.data["course_year"]
		#course_term = form.data["course_term"]
		student_name = form.data["student_name"]
		student_surname = form.data["student_surname"]
		student_university = form.data["student_university"]
		student_department = form.data["student_department"]
		mescontent = form.data["mescontent"]
		messagetoprof = Messagetoprof_w_prof_student(prof_name, prof_surname, prof_university, prof_department, student_name, student_surname, student_university, student_department, mescontent)
		#student_key = db.add_student(student) 
		db.update_messagetoprof(messagetoprof_key, messagetoprof)
		return redirect(url_for("messagetoprof_page", messagetoprof_key=messagetoprof_key))
	form.prof_name.data = messagetoprof.prof_name
	form.prof_surname.data = messagetoprof.prof_surname
	form.prof_university.data = messagetoprof.prof_university
	form.prof_department.data = messagetoprof.prof_department
	form.student_name.data = messagetoprof.student_name
	form.student_surname.data = messagetoprof.student_surname
	form.student_university.data = messagetoprof.student_university
	form.student_department.data = messagetoprof.student_department
	form.mescontent.data = messagetoprof.mescontent	
	return render_template("messagetoprof_edit.html", form=form)


@login_required
def question_edit_page(question_key):
	db = current_app.config["db"]
	question = db.get_question(question_key)
	form = QuestionEditForm()
	if form.validate_on_submit():
		#profid = form.data["profid"]
		prof_name = form.data["prof_name"]
		prof_surname = form.data["prof_surname"]
		prof_university = form.data["prof_university"]
		prof_department = form.data["prof_department"]
		#course_name = form.data["course_name"]
		#course_year = form.data["course_year"]
		#course_term = form.data["course_term"]
		student_name = form.data["student_name"]
		student_surname = form.data["student_surname"]
		student_university = form.data["student_university"]
		student_department = form.data["student_department"]
		quescontent = form.data["quescontent"]
		question = Question_w_prof_student(prof_name, prof_surname, prof_university, prof_department, student_name, student_surname, student_university, student_department, quescontent)
		#student_key = db.add_student(student) 
		db.update_question(question_key, question)
		return redirect(url_for("question_page", question_key=question_key))
	form.prof_name.data = question.prof_name
	form.prof_surname.data = question.prof_surname
	form.prof_university.data = question.prof_university
	form.prof_department.data = question.prof_department
	form.student_name.data = question.student_name
	form.student_surname.data = question.student_surname
	form.student_university.data = question.student_university
	form.student_department.data = question.student_department
	form.quescontent.data = question.quescontent	
	return render_template("question_edit.html", form=form)

@login_required
def alumni_edit_page(alumni_key):
	db = current_app.config["db"]
	alumni = db.get_alumni(alumni_key)
	form = AlumniEditForm()
	if form.validate_on_submit():
		#profid = form.data["profid"]
		prof_name = form.data["prof_name"]
		prof_surname = form.data["prof_surname"]
		prof_university = form.data["prof_university"]
		prof_department = form.data["prof_department"]
		name = form.data["name"]
		surname = form.data["surname"]
		degree = form.data["degree"]
		years = form.data["years"]
		alumni = Alumni_w_prof(prof_name, prof_surname, prof_university, prof_department, name, surname, degree, years)
		#alumni_key = db.add_alumni(alumni) 
		db.update_alumni(alumni_key, alumni) 
		return redirect(url_for("alumni_page", alumni_key=alumni_key))
	form.prof_name.data = alumni.prof_name
	form.prof_surname.data = alumni.prof_surname
	form.prof_university.data = alumni.prof_university
	form.prof_department.data = alumni.prof_department
	form.name.data = alumni.name	
	form.surname.data = alumni.surname
	form.degree.data = alumni.degree
	form.years.data = alumni.years
	return render_template("alumni_edit.html", form=form)


def validate_prof_form(form):
    form.data = {}
    form.errors = {}

    form_name = form.get("name", "").strip()
    if len(form_name) == 0:
        form.errors["name"] = "Name can not be blank."
    else:
        form.data["name"] = form_name

    form_surname = form.get("surname", "").strip()
    if len(form_surname) == 0:
        form.errors["surname"] = "Surname can not be blank."
    else:
        form.data["surname"] = form_surname
        
    form_university = form.get("university", "").strip()
    if len(form_university) == 0:
        form.errors["university"] = "University can not be blank."
    else:
        form.data["university"] = form_university

    form_department = form.get("department", "").strip()
    if len(form_department) == 0:
        form.errors["department"] = "Department can not be blank."
    else:
        form.data["department"] = form_department


    return len(form.errors) == 0

def validate_student_form(form):
    form.data = {}
    form.errors = {}

    form_profid = form.get("profid", "").strip()
    if len(form_profid) == 0:
        form.errors["profid"] = "Profid can not be blank."
    else:
        form.data["name"] = form_name

    form_name = form.get("name", "").strip()
    if len(form_name) == 0:
        form.errors["name"] = "Name can not be blank."
    else:
        form.data["name"] = form_name

    form_surname = form.get("surname", "").strip()
    if len(form_surname) == 0:
        form.errors["surname"] = "Surname can not be blank."
    else:
        form.data["surname"] = form_surname
        
    form_university = form.get("university", "").strip()
    if len(form_university) == 0:
        form.errors["university"] = "University can not be blank."
    else:
        form.data["university"] = form_university

    form_department = form.get("department", "").strip()
    if len(form_department) == 0:
        form.errors["department"] = "Department can not be blank."
    else:
        form.data["department"] = form_department


    return len(form.errors) == 0

def validate_paper_form(form):
    form.data = {}
    form.errors = {}

    form_profid = form.get("profid", "").strip()
    if len(form_profid) == 0:
        form.errors["profid"] = "Profid can not be blank."
    else:
        form.data["profid"] = form_profid

    form_title = form.get("title", "").strip()
    if len(form_title) == 0:
        form.errors["title"] = "Title can not be blank."
    else:
        form.data["title"] = form_title

    form_pubyear = form.get("pubyear", "").strip()
    if len(form_pubyear) == 0:
        form.errors["pubyear"] = "Publication year can not be blank."
    else:
        form.data["pubyear"] = form_pubyear
        
    form_pubtype = form.get("pubtype", "").strip()
    if len(form_pubtype) == 0:
        form.errors["pubtype"] = "Publication type can not be blank."
    else:
        form.data["pubtype"] = form_pubtype

    form_pubsite = form.get("pubsite", "").strip()
    if len(form_pubsite) == 0:
        form.errors["pubsite"] = "Publication site can not be blank."
    else:
        form.data["pubsite"] = form_pubsite


    return len(form.errors) == 0

def validate_project_form(form):
    form.data = {}
    form.errors = {}

    form_profid = form.get("profid", "").strip()
    if len(form_profid) == 0:
        form.errors["profid"] = "Profid can not be blank."
    else:
        form.data["profid"] = form_profid

    form_title = form.get("title", "").strip()
    if len(form_title) == 0:
        form.errors["title"] = "Title can not be blank."
    else:
        form.data["title"] = form_title

    form_agency = form.get("agency", "").strip()
    if len(form_agency) == 0:
        form.errors["agency"] = "Agency can not be blank."
    else:
        form.data["agency"] = form_agency
        
    form_appyear = form.get("appyear", "").strip()
    if len(form_appyear) == 0:
        form.errors["appyear"] = "Application year can not be blank."
    else:
        form.data["appyear"] = form_appyear

    form_abstract = form.get("abstract", "").strip()
    if len(form_abstract) == 0:
        form.errors["abstract"] = "Application can not be blank."
    else:
        form.data["abstract"] = form_abstract

    form_duration = form.get("duration", "").strip()
    if len(form_duration) == 0:
        form.errors["duration"] = "Duration can not be blank."
    else:
        form.data["duration"] = form_duration

    form_status = form.get("status", "").strip()
    if len(form_status) == 0:
        form.errors["status"] = "Status can not be blank."
    else:
        form.data["status"] = form_status

    form_totalamount = form.get("totalamount", "").strip()
    if len(form_totalamount) == 0:
        form.errors["totalamount"] = "Total funding amount can not be blank."
    else:
        form.data["totalamount"] = form_totalamount

    form_availableamount = form.get("availableamount", "").strip()
    if len(form_availableamount) == 0:
        form.errors["availableamount"] = "Available funding amount can not be blank."
    else:
        form.data["availableamount"] = form_totalamount

    return len(form.errors) == 0

def validate_course_form(form):
    form.data = {}
    form.errors = {}

    form_profid = form.get("profid", "").strip()
    if len(form_profid) == 0:
        form.errors["profid"] = "Profid can not be blank."
    else:
        form.data["name"] = form_name

    form_name = form.get("name", "").strip()
    if len(form_name) == 0:
        form.errors["name"] = "Name can not be blank."
    else:
        form.data["name"] = form_name

    form_year = form.get("year", "").strip()
    if len(form_year) == 0:
        form.errors["year"] = "Year can not be blank."
    else:
        form.data["year"] = form_year
        
    form_term = form.get("term", "").strip()
    if len(form_term) == 0:
        form.errors["term"] = "Term can not be blank."
    else:
        form.data["term"] = form_term

    return len(form.errors) == 0

def validate_eval_form(form):
    form.data = {}
    form.errors = {}

    form_courseid = form.get("courseid", "").strip()
    if len(form_courseid) == 0:
        form.errors["courseid"] = "Courseid can not be blank."
    else:
        form.data["courseid"] = form_courseid

    form_studentid = form.get("studentid", "").strip()
    if len(form_studentid) == 0:
        form.errors["studentid"] = "Studentid can not be blank."
    else:
        form.data["studentid"] = form_studentid

    form_subject = form.get("subject", "").strip()
    if len(form_subject) == 0:
        form.errors["subject"] = "Subject can not be blank."
    else:
        form.data["subject"] = form_subject
        
    form_eval = form.get("eval", "").strip()
    if len(form_eval) == 0:
        form.errors["eval"] = "Eval can not be blank."
    else:
        form.data["eval"] = form_eval

    return len(form.errors) == 0

def validate_openposition_form(form):
    form.data = {}
    form.errors = {}

    form_profid = form.get("profid", "").strip()
    if len(form_profid) == 0:
        form.errors["profid"] = "Profid can not be blank."
    else:
        form.data["profid"] = form_profid

    form_studentid = form.get("studentid", "").strip()
    if len(form_studentid) == 0:
        form.errors["studentid"] = "Studentid can not be blank."
    else:
        form.data["studentid"] = form_studentid

    form_postype = form.get("postype", "").strip()
    if len(form_postype) == 0:
        form.errors["postype"] = "Position type can not be blank."
    else:
        form.data["postype"] = form_postype
        
    form_requirements = form.get("requirements", "").strip()
    if len(form_requirements) == 0:
        form.errors["requirements"] = "Requirements can not be blank."
    else:
        form.data["requirements"] = form_requirements

    return len(form.errors) == 0

def validate_messagetoprof_form(form):
    form.data = {}
    form.errors = {}

    form_profid = form.get("profid", "").strip()
    if len(form_profid) == 0:
        form.errors["profid"] = "Profid can not be blank."
    else:
        form.data["profid"] = form_profid

    form_studentid = form.get("studentid", "").strip()
    if len(form_studentid) == 0:
        form.errors["studentid"] = "Studentid can not be blank."
    else:
        form.data["studentid"] = form_studentid

    form_mescontent = form.get("mescontent", "").strip()
    if len(form_mescontent) == 0:
        form.errors["mescontent"] = "Message Content can not be blank."
    else:
        form.data["mescontent"] = form_mescontent

    return len(form.errors) == 0

def validate_question_form(form):
    form.data = {}
    form.errors = {}

    form_profid = form.get("profid", "").strip()
    if len(form_profid) == 0:
        form.errors["profid"] = "Profid can not be blank."
    else:
        form.data["profid"] = form_profid

    form_studentid = form.get("studentid", "").strip()
    if len(form_studentid) == 0:
        form.errors["studentid"] = "Studentid can not be blank."
    else:
        form.data["studentid"] = form_studentid

    form_quescontent = form.get("quescontent", "").strip()
    if len(form_quescontent) == 0:
        form.errors["quescontent"] = "Question Content can not be blank."
    else:
        form.data["quescontent"] = form_quescontent

    return len(form.errors) == 0

def validate_alumni_form(form):
    form.data = {}
    form.errors = {}

    form_profid = form.get("profid", "").strip()
    if len(form_profid) == 0:
        form.errors["profid"] = "Profid can not be blank."
    else:
        form.data["name"] = form_name

    form_name = form.get("name", "").strip()
    if len(form_name) == 0:
        form.errors["name"] = "Name can not be blank."
    else:
        form.data["name"] = form_name

    form_surname = form.get("surname", "").strip()
    if len(form_surname) == 0:
        form.errors["surname"] = "Surname can not be blank."
    else:
        form.data["surname"] = form_surname
        
    form_degree = form.get("degree", "").strip()
    if len(form_degree) == 0:
        form.errors["degree"] = "Degree Awarded can not be blank."
    else:
        form.data["degree"] = form_degree

    form_years = form.get("years", "").strip()
    if len(form_years) == 0:
        form.errors["years"] = "Total years with professor can not be blank."
    else:
        form.data["years"] = form_years


    return len(form.errors) == 0


def login_page():
	form = LoginForm()
	if form.validate_on_submit():
		username = form.data["username"]
		user = get_user(username)
		if user is not None:
			password = form.data["password"]
			if hasher.verify(password, user.password):
				login_user(user)
				flash("You have logged in.")
				next_page = request.args.get("next", url_for("home_page"))
				return redirect(next_page)
		flash("Invalid credentials.")
	return render_template("login.html", form=form)


def logout_page():
	logout_user()
	flash("You have logged out.")
	return redirect(url_for("home_page"))
