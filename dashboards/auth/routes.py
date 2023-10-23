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
    # Perform logout actions
    logout_user()  # Assuming you have Flask-Login set up
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))
