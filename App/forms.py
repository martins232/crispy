from django import forms
from . models import Candidate, SMOKER
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# Every letters to lowercase
class LowerCase(forms.CharField):
    def to_python(self, value):
        return value.lower()

class UpperCase(forms.CharField):
    def to_python(self, value):
        return value.upper()

class CandidateForm(forms.ModelForm):
    
    #VALIDATION
    
    # firstname will automatically be capitalized. This already been done in the models.py class and also here too in widget
    firstname = forms.CharField(
        label="First name",
        min_length=3,
        max_length=50,
        # required=False,
        validators=[RegexValidator(r"^[a-zA-Z]*$", message="Only letters are allowed")], 
        error_messages= {"required": "Firstname cannot be empty"},
        widget=forms.TextInput(attrs={
            "placeholder":"Enter First name",
            "style": "font-size : 13px; text-transform: capitalize;"            
            })
        )  
    # Lastname will automatically be capitalized. This already been done in the models.py class and also here too in widget
    lastname = forms.CharField(
        label="Last name",
        min_length=3,
        max_length=50,
        # required=False,
        validators=[RegexValidator(r"^[a-zA-Z]*$", message="Only letters are allowed")], 
        widget=forms.TextInput(attrs={
            "placeholder":"Enter Last name",
            "style": "font-size : 13px; text-transform: capitalize;"            
            })
        )  
    # Job code always in uppercase for the server as done above and also here too in widget
    job = UpperCase(
        label="Job code",
        min_length=5, max_length=5,
        error_messages= {"required": "Job cannot be empty"},

        widget=forms.TextInput(attrs={
            "placeholder":"Example : FR-22",
            "style": "font-size : 13px; text-transform: uppercase;"
        })
    )
    
    # Email code always in lowercase for the server as done above and also here too in widget
    email = LowerCase(
        label="Email",
        min_length=10,
        max_length=50,
        # required=False,
        validators=[RegexValidator(r"^[a-zA-Z0-9.+-_]+@[a-zA-Z0-9.+-_]+\.[a-zA-Z]*$", message="Enter a valid email address")], 
        widget=forms.TextInput(attrs={
            "placeholder":"Email Address",
            "style": "font-size : 13px; text-transform: lowercase;"
            })
        )
    
    # Age must only be numbers and the length must not be less than 1 or greater than 3
    age = forms.CharField(
        label="Age",
        min_length=1,
        max_length=3,
        # required=False,
        validators=[RegexValidator(r"^[0-9]{1,2}$", message="Enter a valid age")], 
        # widget=forms.TextInput(attrs={"placeholder":"Email Address",})
        widget=forms.TextInput(attrs={
            "placeholder":"Age",
            "style": "font-size : 13px;"})
        )
    
    #Experience
    experience = forms.BooleanField(label="I have experience", required=False)
    
    #message
    message = forms.CharField(
        label="About You",
        max_length=300,
        required=False,
        widget=forms.Textarea(attrs={
            "placeholder":"Talk about yourself",
            "rows":4,
            "style": "font-size : 13px;"})
        
        )
    
    # File (Upload)
    file = forms.FileField(
        required= True,
        widget=forms.ClearableFileInput(
            attrs={
                "style": "font-size : 13px;"
            }
        )
    )
    
    #METHOD 1 {GENDER}
    # GENDER = (
    #     ("M","Male"),
    #     ("F","Female")
    # )
    # gender = forms.CharField(label="Gender", widget=forms.RadioSelect(choices=GENDER))
    
    
    class Meta:
        model = Candidate
        exclude =["created_at", "situation"]
        # fields = ["firstname", "lastname", "job", "email", "age","phone", "message"]
        
        #Creating a controll for labels
        # How to change labels of fields
        # labels ={
        #     "phone":"Enter Phone",
        #     "salary":"What is your salary expectation",
        #     "personality":"What is your personality",
        #     "gender":"Select your gender",
        #     "smoker":"Do you smoke?"
        # }
        
        SALARY = (
            ("", "Salary expectation {month}"),
            ("Between {$3000 and $4000}", "Between {$3000 and $4000}"),
            ("Between {$4000 and $5000}", "Between {$4000 and $5000}"),
            ("Between {$5000 and $7000}", "Between {$5000 and $7000}"),
            ("Between {$7000 and $10000}", "Between {$7000 and $10000}")
        )
        
        #METHOD 2 {GENDER}
        GENDER = (
            ("M","Male"),
            ("F","Female")
        )
     # OUTSIDE WIDGETS 
     # Using Jquery and Jquery script tag to mask the phone number
        widgets ={
            #Phone
            "phone" :forms.TextInput(
                attrs={
                    "style": "font-size:14px; ", #CSS
                    "placeholder": "E.g: 0703-0000-000",
                    "data-mask": "+(234) 0000-0000-000",
                }
            ),
            #Salary
            "salary" :forms.Select(
                choices=SALARY,
                attrs={
                    "class": "form-control", #BOOTSTRAP insde the form
                    "style": "font-size : 13px;",
                }
            ), 
            "personality": forms.Select(attrs={"style": "font-size : 13px;"}),
            "gender":forms.RadioSelect(choices=GENDER, attrs={"class":"btn-check",}),
            "smoker":forms.RadioSelect(choices=SMOKER ,attrs={"class":"btn-check"})
        }
    #'SUPER'   Function
    def __init__(self, *args, **kwargs):
        super(CandidateForm, self).__init__(*args, **kwargs)
        
        # ########### CONTROL PANEL (individual <inputs> )  ########## |            
        # 1)  INPUT REQUIRED
        # self.fields["message"].required = True
        
        # 2) INPUT DISABLE
        # self.fields["experience"].disabled = True
        
        # 3) INPUT READONLY
        # self.fields["job"].widget.attrs.update({"readonly":"readonly"})
        
        
        # 4) SELECT OPTION  
            #creating placeholder for select inputs
        # self.fields["personality"].choices = [("","Select a personality"),] +list(self.fields["personality"].choices)[1:]
        
        
        # 5) WIDGET PANEL  (inside/outside)
        # self.fields["phone"].widget.attrs.update({"style": "font-size:px;", "data-mask": "+(237) 0000-0000-000"})
        
        # 6) Erro messages
        # self.fields["firstname"].error_messages.update({
        #     "required": "Please your firstname is required"
        # })
        
        
       # ########### CONTROL PANEL (multiple <inputs> ) ########## |
        
        # 1) READONLY
        # readonly = ["firstname", "lastname", "job"]
        # for field in readonly:
            # self.fields[field].widget.attrs["readonly"] = True
        
        # 2) DISABLE
        # disabled = ["personality", "salary", "smoker", "gender", "experience"]
        # for field in disabled:
            # self.fields[field].widget.attrs["disabled"] = True
            
        # 3) ERROR MESSAGES
        # error_messages = ["firstname", "lastname", "job", "email", "age", "phone", "personality", "salary", "smoker", "gender", "smoker"]
        # for field in error_messages:
        #     self.fields[field].error_messages.update({
        #     "required": "Django field is required"
        # })
        
        # 2) FONT Size
        font_size = ["firstname", "lastname", "job", "email", "age", "phone", "personality", "salary"]
        for field in font_size:
            self.fields[field].widget.attrs.update({"style":"font-size: 15px;"}) 
            
                        
    #__________________________ END SUPERFUNCTION____________________
    
    # FUNCTION TO PREVENT DUPLICATE ENTRIES
    # Method 1 (loop for)
    # def clean_email(self):
    #     email= self.cleaned_data.get("email")
    #     for obj in Candidate.objects.all():
    #         if obj.email == email:
    #             raise forms.ValidationError("Denied! " + email + " is already registered")
    #     return email
    
    # Method 2 (If statement with filter)
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if Candidate.objects.filter(email=email).exists():
            raise forms.ValidationError("Denied! " + email + " is already registered")
        return email