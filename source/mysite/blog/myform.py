from wtforms import Form, TextField, validators

class EmailForm(Form):
	#email = TextField("Email Addres",[validators.Required()])
	email = StringField('Email Addres', validators.Required())
	message = TextAreaField("Message",[validators.Required()])
	#StringField类表示一个type="text"属性的<input>标签
	submit = SubmitField("Send",[validators.Required()])
	#SubmitField类表示一个type="submit"属性的<input>标签
