from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Institutions, Donations

class SignUpForm(UserCreationForm):

    class Meta:
            model = User
            fields = ('username', 'password1', 'password2', )


class AddInstitutionsForm(ModelForm):

    class Meta:
            model = Institutions
            fields = "__all__"


class AddDonationsForm(ModelForm):

    class Meta:
            model = Donations
            fields = "__all__"
