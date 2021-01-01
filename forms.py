from flask_wtf import FlaskForm
from flask_wtf import *
from wtforms import StringField, PasswordField
from wtforms import *

from wtforms.validators import DataRequired, NumberRange, Optional
from wtforms_components import IntegerField
from flask_login import LoginManager

from datetime import datetime


class ProfEditForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    surname = StringField("Surame", validators=[DataRequired()])
    university = StringField("University", validators=[DataRequired()])
    department = StringField("Department", validators=[DataRequired()])


class StudentEditForm(FlaskForm):
    #profid = StringField("Professor ID", validators=[DataRequired()])
    prof_name = StringField("Professor Name", validators=[DataRequired()])
    prof_surname = StringField("Professor Surname", validators=[DataRequired()])
    prof_university = StringField("Professor University", validators=[DataRequired()])
    prof_department = StringField("Professor Department", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    surname = StringField("Surame", validators=[DataRequired()])
    university = StringField("University", validators=[DataRequired()])
    department = StringField("Department", validators=[DataRequired()])


class PaperEditForm(FlaskForm):
    #profid = StringField("Professor ID", validators=[DataRequired()])
    prof_name = StringField("Professor Name", validators=[DataRequired()])
    prof_surname = StringField("Professor Surname", validators=[DataRequired()])
    prof_university = StringField("Professor University", validators=[DataRequired()])
    prof_department = StringField("Professor Department", validators=[DataRequired()])
    title = StringField("Title", validators=[DataRequired()])
    pubyear = StringField("Publication Year", validators=[DataRequired()])
    pubtype = StringField("Publication Type", validators=[DataRequired()])
    pubsite = StringField("Publication Site", validators=[DataRequired()])


class ProjectEditForm(FlaskForm):
	#profid = StringField("Professor ID", validators=[DataRequired()])
	prof_name = StringField("Professor Name", validators=[DataRequired()])
	prof_surname = StringField("Professor Surname", validators=[DataRequired()])
	prof_university = StringField("Professor University", validators=[DataRequired()])
	prof_department = StringField("Professor Department", validators=[DataRequired()])
	title = StringField("Title", validators=[DataRequired()])
	agency = StringField("Agency", validators=[DataRequired()])
	appyear = StringField("Application Year", validators=[DataRequired()])
	abstract = StringField("Abstract", validators=[DataRequired()])
	duration = StringField("Duration (Years)", validators=[DataRequired()])
	status = StringField("Status (Active / Completed)", validators=[DataRequired()])
	totalamount = StringField("Total Funding Amount (TL)", validators=[DataRequired()])
	availableamount = StringField("Available Funding Amount (TL)", validators=[DataRequired()])


class CourseEditForm(FlaskForm):
    #profid = StringField("Professor ID", validators=[DataRequired()])
    prof_name = StringField("Professor Name", validators=[DataRequired()])
    prof_surname = StringField("Professor Surname", validators=[DataRequired()])
    prof_university = StringField("Professor University", validators=[DataRequired()])
    prof_department = StringField("Professor Department", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    year = StringField("Year", validators=[DataRequired()])
    term = StringField("Term", validators=[DataRequired()])


class EvalEditForm(FlaskForm):
    #profid = StringField("Professor ID", validators=[DataRequired()])
    student_name = StringField("Student Name", validators=[DataRequired()])
    student_surname = StringField("Student Surname", validators=[DataRequired()])
    student_university = StringField("Student University", validators=[DataRequired()])
    student_department = StringField("Student Department", validators=[DataRequired()])
    course_name = StringField("Course Name", validators=[DataRequired()])
    course_year = StringField("Course Year", validators=[DataRequired()])
    course_term = StringField("Course Term", validators=[DataRequired()])
    subject = StringField("Subject", validators=[DataRequired()])
    evall = StringField("Comment / Evaluation", validators=[DataRequired()])


class OpenpositionEditForm(FlaskForm):
    #profid = StringField("Professor ID", validators=[DataRequired()])
	prof_name = StringField("Professor Name", validators=[DataRequired()])
	prof_surname = StringField("Professor Surname", validators=[DataRequired()])
	prof_university = StringField("Professor University", validators=[DataRequired()])
	prof_department = StringField("Professor Department", validators=[DataRequired()])
	student_name = StringField("Student Name", validators=[DataRequired()])
	student_surname = StringField("Student Surname", validators=[DataRequired()])
	student_university = StringField("Student University", validators=[DataRequired()])
	student_department = StringField("Student Department", validators=[DataRequired()])
	postype = StringField("Position Type", validators=[DataRequired()])
	requirements = StringField("Requirements", validators=[DataRequired()])


class MessagetoprofEditForm(FlaskForm):
    #profid = StringField("Professor ID", validators=[DataRequired()])
	prof_name = StringField("Professor Name", validators=[DataRequired()])
	prof_surname = StringField("Professor Surname", validators=[DataRequired()])
	prof_university = StringField("Professor University", validators=[DataRequired()])
	prof_department = StringField("Professor Department", validators=[DataRequired()])
	student_name = StringField("Student Name", validators=[DataRequired()])
	student_surname = StringField("Student Surname", validators=[DataRequired()])
	student_university = StringField("Student University", validators=[DataRequired()])
	student_department = StringField("Student Department", validators=[DataRequired()])
	mescontent = StringField("Message Content", validators=[DataRequired()])


class QuestionEditForm(FlaskForm):
    #profid = StringField("Professor ID", validators=[DataRequired()])
	prof_name = StringField("Professor Name", validators=[DataRequired()])
	prof_surname = StringField("Professor Surname", validators=[DataRequired()])
	prof_university = StringField("Professor University", validators=[DataRequired()])
	prof_department = StringField("Professor Department", validators=[DataRequired()])
	student_name = StringField("Student Name", validators=[DataRequired()])
	student_surname = StringField("Student Surname", validators=[DataRequired()])
	student_university = StringField("Student University", validators=[DataRequired()])
	student_department = StringField("Student Department", validators=[DataRequired()])
	quescontent = StringField("Question Content", validators=[DataRequired()])


class AlumniEditForm(FlaskForm):
    #profid = StringField("Professor ID", validators=[DataRequired()])
    prof_name = StringField("Professor Name", validators=[DataRequired()])
    prof_surname = StringField("Professor Surname", validators=[DataRequired()])
    prof_university = StringField("Professor University", validators=[DataRequired()])
    prof_department = StringField("Professor Department", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    surname = StringField("Surame", validators=[DataRequired()])
    degree = StringField("Degree Awarded", validators=[DataRequired()])
    years = StringField("Total years with professor", validators=[DataRequired()])

class LoginForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired()])

	password = PasswordField("Password", validators=[DataRequired()])
