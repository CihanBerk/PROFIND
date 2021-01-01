from flask import Flask, render_template
from flask_login import LoginManager

from flask import *
#from datetime import datetime
import views
import os

#import os.path

import sqlite3 as dbapi2
#from database import *  this is the way to import all functions inside of the database.py file
from database import *
from prof import Prof
from student import Student
from user import get_user
from passlib.hash import pbkdf2_sha256 as hasher

lm = LoginManager()

@lm.user_loader
def load_user(user_id):
	return get_user(user_id)
    
#function call to initialize the application
def create_app():
	app = Flask(__name__)
	# we can set configuration of app instead of inside of app.run() function
	#we can put config options inside of the another file such as settings.py
	#app.config["DEBUG"] = True 
	app.config.from_object("settings")
	# the following means when you see "/" do the call of home_page from view.py
	app.add_url_rule("/", view_func = views.home_page)
	
	# Login and logout pages
	app.add_url_rule(
		"/login", view_func=views.login_page, methods=["GET", "POST"]
	)
	app.add_url_rule("/logout", view_func=views.logout_page)
	
	#app.add_url_rule("/movies", view_func = views.movies_page)
	app.add_url_rule("/profs", view_func=views.profs_page, methods=["GET", "POST"])

	app.add_url_rule("/profs/<int:prof_key>", view_func=views.prof_page)
	
	# We added new url for movie editing
	app.add_url_rule("/profs/<int:prof_key>/edit", view_func=views.prof_edit_page,methods=["GET", "POST"],)
	
	# Addition of the new movies from the form interface
	# We allows both GET and POST methods
	app.add_url_rule("/new-prof", view_func=views.prof_add_page, methods=["GET", "POST"])
	
	
	app.add_url_rule("/students", view_func=views.students_page, methods=["GET", "POST"])
	app.add_url_rule("/students/<int:student_key>", view_func=views.student_page)
	app.add_url_rule("/students/<int:student_key>/edit", view_func=views.student_edit_page,methods=["GET", "POST"],)
	app.add_url_rule("/new-student", view_func=views.student_add_page, methods=["GET", "POST"])
	
	app.add_url_rule("/alumnis", view_func=views.alumnis_page, methods=["GET", "POST"])
	app.add_url_rule("/alumnis/<int:alumni_key>", view_func=views.alumni_page)
	app.add_url_rule("/alumnis/<int:alumni_key>/edit", view_func=views.alumni_edit_page,methods=["GET", "POST"],)
	app.add_url_rule("/new-alumni", view_func=views.alumni_add_page, methods=["GET", "POST"])
	
	app.add_url_rule("/courses", view_func=views.courses_page, methods=["GET", "POST"])
	app.add_url_rule("/courses/<int:course_key>", view_func=views.course_page)
	app.add_url_rule("/courses/<int:course_key>/edit", view_func=views.course_edit_page,methods=["GET", "POST"],)
	app.add_url_rule("/new-course", view_func=views.course_add_page, methods=["GET", "POST"])
	
	app.add_url_rule("/evals", view_func=views.evals_page, methods=["GET", "POST"])
	app.add_url_rule("/evals/<int:eval_key>", view_func=views.eval_page)
	app.add_url_rule("/evals/<int:eval_key>/edit", view_func=views.eval_edit_page,methods=["GET", "POST"],)
	app.add_url_rule("/new-eval", view_func=views.eval_add_page, methods=["GET", "POST"])

	app.add_url_rule("/openpositions", view_func=views.openpositions_page, methods=["GET", "POST"])
	app.add_url_rule("/openpositions/<int:openposition_key>", view_func=views.openposition_page)
	app.add_url_rule("/openpositions/<int:openposition_key>/edit", view_func=views.openposition_edit_page,methods=["GET", "POST"],)
	app.add_url_rule("/new-openposition", view_func=views.openposition_add_page, methods=["GET", "POST"])

	app.add_url_rule("/messagetoprofs", view_func=views.messagetoprofs_page, methods=["GET", "POST"])
	app.add_url_rule("/messagetoprofs/<int:messagetoprof_key>", view_func=views.messagetoprof_page)
	app.add_url_rule("/messagetoprofs/<int:messagetoprof_key>/edit", view_func=views.messagetoprof_edit_page,methods=["GET", "POST"],)
	app.add_url_rule("/new-messagetoprof", view_func=views.messagetoprof_add_page, methods=["GET", "POST"])
	
	app.add_url_rule("/questions", view_func=views.questions_page, methods=["GET", "POST"])
	app.add_url_rule("/questions/<int:question_key>", view_func=views.question_page)
	app.add_url_rule("/questions/<int:question_key>/edit", view_func=views.question_edit_page,methods=["GET", "POST"],)
	app.add_url_rule("/new-question", view_func=views.question_add_page, methods=["GET", "POST"])	
		
	app.add_url_rule("/papers", view_func=views.papers_page, methods=["GET", "POST"])
	app.add_url_rule("/papers/<int:paper_key>", view_func=views.paper_page)
	app.add_url_rule("/papers/<int:paper_key>/edit", view_func=views.paper_edit_page,methods=["GET", "POST"],)
	app.add_url_rule("/new-paper", view_func=views.paper_add_page, methods=["GET", "POST"])
			
	app.add_url_rule("/projects", view_func=views.projects_page, methods=["GET", "POST"])
	app.add_url_rule("/projects/<int:project_key>", view_func=views.project_page)
	app.add_url_rule("/projects/<int:project_key>/edit", view_func=views.project_edit_page,methods=["GET", "POST"],)
	app.add_url_rule("/new-project", view_func=views.project_add_page, methods=["GET", "POST"])
		

	lm.init_app(app)
	lm.login_view = "login_page"

	# new database decleration with SQLlite
	#home_dir = os.path.expanduser("~")
	#db = Database(os.path.join(home_dir, "PROFESSOR.sqlite"))
	db = Database("PROFESSOR_STUDENT_SQLITE_V2.sqlite")
	app.config["db"] = db
	
	#db = Database()
	# We don't need these sample movies anymore since the user can add a movie
	#db.add_prof(Prof("Husnu", "cavus", "ITU", "CS"))
	#db.add_prof(Prof("Husnuye", "cavusan", "ITU", "ECE"))
	#app.config["db"] = db
		
	return app

#@app.route("/") when we define url_rule we don't need these routings
# we can move definitions to another file but in that case, 
# we need to define app as a global variable. Instead of that we can add url rules

#def home_page():	
#	today = datetime.today()
#	day_name = today.strftime("%A")
#	return render_template("home.html", day = day_name)

#Route function
#@app.route("/movies") when we define url_rule we don't need these routings
#view function
#def movies_page():
#	return render_template("movies.html")

if __name__ == "__main__":
	app = create_app()
	app.run(host="0.0.0.0", port = 8080)

