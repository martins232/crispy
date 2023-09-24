from django import forms
from . models import Candidate
from django.core.validators import RegexValidator

# Every letters to lowercase
class LowerCase(forms.CharField):
    def to_python(self, value):
        return value.lower()

class UpperCase(forms.CharField):
    def to_python(self, value):
        return value.upper()

class CandidateForm(forms.ModelForm):
    
    #VALIDATION
    
    # firstname will automatically be capitalized. This already been done in the models.py class
    firstname = forms.CharField(
        label="First name",
        min_length=3,
        max_length=50,
        # required=False,
        validators=[RegexValidator(r"^[a-zA-Z]*$", message="Only letters are allowed")], 
        widget=forms.TextInput(attrs={"placeholder":"Enter First name"})
        )  
    # lastname will automatically be capitalized. This already been done in the models.py class
    lastname = forms.CharField(
        label="Last name",
        min_length=3,
        max_length=50,
        # required=False,
        validators=[RegexValidator(r"^[a-zA-Z]*$", message="Only letters are allowed")], 
        widget=forms.TextInput(attrs={"placeholder":"Enter Lastname name"})
        )
    # job code always in uppercase
    job = UpperCase(
        label="Job code",
        min_length=5, max_length=5,
        widget=forms.TextInput(attrs={
            "placeholder":"Example : FR-22",
        })
    )
    
    # email code always in lowercase
    email = LowerCase(
        label="Email",
        min_length=10,
        max_length=50,
        # required=False,
        validators=[RegexValidator(r"^[a-zA-Z0-9.+-_]+@[a-zA-Z0-9.+-_]+\.[a-zA-Z]*$", message="Enter a valid email address")], 
        widget=forms.TextInput(attrs={"placeholder":"Email Address"})
        )
    
    # age must only be numbers and the length must not be less than 1 or greater than 3
    age = forms.CharField(
        label="Age",
        min_length=1,
        max_length=3,
        # required=False,
        validators=[RegexValidator(r"^[0-9]{1,2}$", message="Enter a valid age")], 
        # widget=forms.TextInput(attrs={"placeholder":"Email Address",})
        widget=forms.TextInput(attrs={"placeholder":"Email Address", "type":"number"})
        )
    message = forms.CharField(
        label="About You",
        max_length=300,
        widget=forms.Textarea(attrs={"placeholder":"Talk about yourself","rows":5})
        
        )
    
    
    class Meta:
        model = Candidate
        exclude =["created_at", "situation"]
        # fields = ["firstname", "lastname", "job", "email", "age","phone", "message"]
    
    
     # Outside Widget 
     # Using Jquery and Jquery script tag to mask the phone number
        widgets ={
            "phone" :forms.TextInput(
                attrs={
                    "style": "font-size:18px;",
                    "placeholder": "E.g: 0703-0000-000",
                    "data-mask": "+(234) 0000-0000-000",
                }
            )
        }
