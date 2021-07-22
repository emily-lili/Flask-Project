from flask import Blueprint, render_template, request, flash, redirect, url_for

from flask_login import current_user, login_required

# import any database model we're using
from app.models import Character, db

# import our form that we're using
from app.forms import newCharacterForm
site = Blueprint('site', __name__, template_folder='site_templates')

#homepage route
@site.route('/', methods=['GET', 'POST'])
def home():
    form = newCharacterForm()
    try:
        if request.method == 'POST' and form.validate_on_submit():
            moviedata = form.movie.data
            genredata = form.genre.data
            ratingdata = form.rating.data
            yeardata = form.year.data
            namedata = form.name.data

            print(moviedata, namedata)

            new_character = Character(movie=moviedata,genre=genredata, rating=ratingdata, year=yeardata, name=namedata)

            db.session.add(new_character)
            db.session.commit()

            #flash messages 
            flash(f'You have successfully added the character {namedata} to your database.')

            return redirect(url_for('site.home'))
    except:
        flash(f'Invalid form input, try again.')
        return redirect(url_for('site.home'))
    return render_template('index.html',form=form)    

#profile
@site.route('/profile')
def profile():
    return render_template('profile.html') 

@site.route('/character')
def displayCharacter():
    c = Character.query.all()
    return render_template('display_character.html', Character=c)