#!/usr/bin/python3
""" Handle the user session routes """

from flask import request, redirect, url_for, flash, render_template, session
from flask_login import login_user, logout_user, current_app
from dashboards.auth.utils import custom_authentication
from models.optometrist import Optometrist
from models.receptionist import Receptionist

@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    if 'custom_user' in session:
        return redirect(url_for('custom_dashboard'))
    if current_user.is_authenticated:
        if isinstance(current_user, User):
            return redirect(url_for('main.home'))
        if isinstance(current_user, User):
            return redirect(url_for('main.home'))

    if request.method == 'POST':
        username = request.form.get('email')
        password = request.form.get('password')

        user = custom_authentication(email, password)

        if isinstance(user, Receptionist):
            login_user(user, remember=True)
            flash('Login successful.', 'success')
            return redirect(url_for('receptionist'))
        elif isinstance(user, Optometrist):
            login_user(user, remember=True)
            flash('Login successful.', 'success')
            return redirect(url_for('optometrist'))
        elif user:
            user = session.get('custom_user')
            flash('Login successful.', 'success')
            return redirect(url_for('administrator'))
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
