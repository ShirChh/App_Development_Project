from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators

class CreateUserForms(Form):
    first_name = StringField('First Name', [validators.length(min=1, max=150),validators.DataRequired()])
    
    last_name = StringField('Last Name', [validators.length(min=1, max=150),validators.DataRequired()])
    
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'),('F', 'Female'),('M', 'Male')], default= '')
    
    membership = RadioField('Membership', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')], default='F')
    
    remarks = TextAreaField('Remarks', [validators.Optional()])
    