from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired

class SubmitForm(Form):
    title = StringField('title', validators=[DataRequired()])
    bodytext = TextAreaField('bodytext', validators=[DataRequired()])
