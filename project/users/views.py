from flask import redirect, render_template, url_for, Blueprint  # pragma: no cover
from flask.ext.login import login_user, \
    login_required, logout_user  # pragma: no cover
from werkzeug.security import generate_password_hash, check_password_hash

from project import db
from project.models.users import User
from project.users.login_form import LoginForm
from project.users.register_form import RegisterForm

user_blueprint = Blueprint('user', __name__, template_folder='templates', static_folder='static')


@user_blueprint.route('/')
def index():
    return redirect(url_for('.login'))


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)

                return redirect(url_for('home.dashboard'))

        return redirect(url_for('.login'))
        # return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)


@user_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(email=form.email.data, username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('.login'))
        # return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form)


@user_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))
