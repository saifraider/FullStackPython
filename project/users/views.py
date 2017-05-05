from flask import redirect, render_template, url_for, Blueprint  # pragma: no cover
from flask_login import login_user, \
    login_required, logout_user  # pragma: no cover
from werkzeug.security import generate_password_hash, check_password_hash
from flask import request
from database import session, Session
from project.models.users import User
from project.users.login_form import LoginForm
from project.users.register_form import RegisterForm
from sqlalchemy import event

user_blueprint = Blueprint('user', __name__, template_folder='templates', static_folder='static')


# user = None
@user_blueprint.route('/')
def index():
    return redirect(url_for('.login'))


@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    # global user
    form = LoginForm()

    if form.validate_on_submit():
        user = session.query(User).filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)

                return redirect(url_for('home.dashboard'))

        return redirect(url_for('.login'))
        # return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'
    '''if user is not None:
        print(user.is_authenticated())
    else:
        print('False')'''

    return render_template('login.html', form=form)


@user_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        # check if user with same id exists
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(email=form.email.data, username=form.username.data, password=hashed_password)
        session.add(new_user)
        session.commit()

        return redirect(url_for('.login'))
        # return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form)


@user_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))


'''@event.listens_for(Session, 'after_commit')
def receive_after_commit(session):
    print("Hi new user created")'''