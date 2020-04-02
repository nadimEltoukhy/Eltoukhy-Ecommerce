from django import forms


from django.contrib.auth import(

		authenticate,
		get_user_model,
		login,
		logout,


	)

User= get_user_model()

class userloginform(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)

	def clean(self,*args,**kwargs):
		username=self.cleaned_data.get("username")
		password=self.cleaned_data.get("password")
		user = authenticate(username=username,password=password)
		if not user:
			raise forms.ValidationError("You typied the username wrong or the user is not exist")

		if not user.check_password(password):
			raise ValidationError("The password you entered is wrong")

		if not user.is_active:
			raise ValidationError("The user doesn't exist")


		return super(userloginform,self).clean(*args,**kwargs)





class userregisterform(forms.ModelForm):
	class Meta:
		model =User
		email = forms.EmailField(label='Email')
		
		password = forms.CharField(widget=forms.PasswordInput)
		
		fields=[

			'username',
			'email',
			'password',


		]


	def clean_email(self):
		email=self.cleaned_data.get('email')
		

		return email
		
		email_gs=User.objects.filter(email=email)
		if email_gs.is_exist():
			raise forms.ValidationError("This email is already exist please try another email")
