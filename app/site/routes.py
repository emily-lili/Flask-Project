from flask import Blueprint, render_template

site = Blueprint('site', __name__, template_folder='site_templates')

#homepage route
@site.route('/')
def home():
    return render_template('index.html')    

#profile
@site.route('/profile')
def profile():
    return render_template('profile.html') 