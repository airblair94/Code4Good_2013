from django.forms import *
from MHDC.models import *

class UserProfileForm(ModelForm):
    DOB = DateField(label=u'Date of Birth', input_formats=['%d/%m/%Y', '%m/%d/%Y', "%d/%m/%y"], widget=DateInput(format = '%d/%m/%Y'))
    class Meta:
        model = UserProfile
        app_label = "MHDC"
        exclude = {"user"}


class SelfHelpForm(ModelForm):
    co_DOB = DateField(label=u'Co-applicant\'s DOB', input_formats=['%d/%m/%Y', '%m/%d/%Y', "%d/%m/%y"], widget=DateInput(format = '%d/%m/%Y'))
    class Meta:
        model = SelfHelpApplication
        exclude = {"userProfile",  "status", "dateReceived"}

class HomeRepairForm(ModelForm):
	class Meta:
		model = HomeRepair
		exclude = {"status", "Contact_notes", "userProfile", "dateReceived","Package_mailed","Package_returned","Verified_Home_ownership","Total_Monthly","HRP_Approved","HRP_Denied","Denial_or_approval_explanation"}

class UserForm(ModelForm):
	password = CharField(label="Password", required=True,
		widget=PasswordInput(attrs={'class':'form_text'}))
	first_name = CharField(label="First Name", required=True,
		widget=TextInput(attrs={'class':'form_text'}))
	last_name = CharField(label="Last Name", required=True,
		widget=TextInput(attrs={'class':'form_text'}))
	email = EmailField(label="Email", required=True,
		widget=TextInput(attrs={'class':'form_text'}))

	class Meta:
		model = User
		fields = ("email",
			"first_name", "last_name",
			"password")

	#Hash the user's password upon save.
	def save(self, commit=True):
		user = super(UserForm, self).save(commit=False)
		user.set_password(self.cleaned_data["password"])
		user.username = user.email
		if commit:
			user.save()
		return user

class Internal_form(ModelForm):
	class Meta:
		model = SelfHelpStaffChecklist

