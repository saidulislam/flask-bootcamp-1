from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, 
                    RadioField, SelectField, TextField, 
                    TextAreaField, SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'asdfasdfasdfasdf'


class  StudentInfo(FlaskForm):

    name            = StringField("Full Name", validators=[DataRequired()])
    full_time       = BooleanField("Full time student?")
    student_year    = RadioField("Year", choices=[(1,1), (2,2), (3,3), (4,4)])
    major_choice    = SelectField("Major", choices=[('CIS', 'Computer Information Science'), ('CS', 'Computer Science')])
    comment         = TextAreaField()
    submit          = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():

    form = StudentInfo()
    if form.validate_on_submit():
        
        session['name']         = form.name.data
        session['full_time']    = form.full_time.data
        session['student_year'] = form.student_year.data
        session['major']        = form.major_choice.data
        session['comment']      = form.comment.data
        
        flash(f"Information saved for : {session['name']}")

        return redirect(url_for('thankyou'))

    return render_template('index.html', form=form)


@app.route('/thankyou')
def thankyou():

    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)