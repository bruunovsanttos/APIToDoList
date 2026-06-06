from flask import Blueprint, render_template

web_bp = Blueprint("web", __name__)

@web_bp.route("/")
def login_page():
    return render_template("login.html")

@web_bp.route("/register")
def register_page():
    return render_template("register.html")

@web_bp.route("/dashboard")
def dashboard_page():
    return render_template("/dashboard.html")
