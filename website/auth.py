from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/sign-up', methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm = request.form.get('confirm')

        user = User.query.filter_by(email = email).first()
        if user: 
            flash('Email alreedy exists', category='error')
        elif len(email) < 4: 
            flash('Email must be greater the 3 characters.', category='error')
        elif len(name) < 2: 
            flash('name must be greater the 1 character.', category='error')
        elif len(password) < 6: 
            flash('Password must be greater the 5 characters.', category='error')
        elif confirm != password: 
            flash('Passwords don\'t match.', category='error')
        else: 
            # add user to DB
            hashPass = generate_password_hash(password, method='sha256')
            new_user = User(name = name, email = email, password = hashPass)
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created!.', category='success')

            return redirect(url_for('views.home'))

    return render_template('signUp.html', user=current_user)

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # email is a unique fild
        user = User.query.filter_by(email = email).first()
        if user:
            if check_password_hash(user.password, password):
                flash(f'Welcome back, {user.name}!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else: 
                flash('Incorrect password, try again', category='error')
        else: 
            flash('User does not exists. Please register first', category='error')

    return render_template('login.html', user=current_user)

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


# obj = User.query.filter_by(id=2).one()
# db.session.delete(obj)
# db.session.commit()