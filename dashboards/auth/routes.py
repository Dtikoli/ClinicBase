from flask import request, redirect, url_for, flash, render_template, session
from flask_login import login_user, logout_user, current_app
from models import User
from dashboards.auth.utils import custom_authentication


@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('email')
        password = request.form.get('password')

        user = custom_authentication(email, password)

        if isinstance(user, User):
            login_user(user, remember=True)
            flash('Login successful.', 'success')
            return redirect(url_for('dashboard1'))
        elif user:
            user = session.get('custom_user')
            flash('Login successful.', 'success')
            return redirect(url_for('dashboard2'))
        else:
            flash('Login failed. Please check your credentials.', 'danger')

    return render_template('login.html')


@bp_auth.route('/logout')
def logout():
    if 'custom_user' in session:
        session.pop('custom_user')
    else:
        logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))

