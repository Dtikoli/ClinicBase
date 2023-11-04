#!/usr/bin/python3
""" Handle the user session routes """

from dashboards.auth import bp_auth
from flask import request, redirect, url_for, flash, render_template, session
from flask_login import login_user, logout_user, current_user
from dashboards.auth.utils import custom_authentication
from models.optometrist import Optometrist
from models.receptionist import Receptionist
from models.custom_user import Admin


@bp_auth.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    """ handles session login """
    if current_user.is_authenticated:
        if isinstance(current_user, Receptionist):
            return redirect(url_for('recep.dashboard_recep'))
        elif isinstance(current_user, Optometrist):
            return redirect(url_for('optom.dashboard_optom'))
        else:
            return redirect(url_for('admin.dashboard_admin'))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = custom_authentication(email, password)

        if isinstance(user, Receptionist):
            login_user(user, remember=True)
            flash('Login successful.', 'success')
            return redirect(url_for('recep.dashboard_recep'))
        elif isinstance(user, Optometrist):
            login_user(user, remember=True)
            flash('Login successful.', 'success')
            return redirect(url_for('optom.dashboard_optom'))
        elif isinstance(user, Admin):
            login_user(user, remember=True)
            flash('Login successful.', 'success')
            return redirect(url_for('admin.dashboard_admin'))
        else:
            flash('Login failed. Please check your credentials.', 'danger')

    return render_template('login.html')


@bp_auth.route('/logout', strict_slashes=False)
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('main.home'))

