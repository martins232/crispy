from django import forms
from . models import Candidate, SMOKER
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import date # used in birthday validation
import datetime # used to prevent future date

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
    # Job code always in uppercase for the server as done above and also here too in widget for client side
    job = UpperCase(
        label="Job code",
        min_length=5, max_length=5,
        error_messages= {"required": "Job cannot be empty"},

        widget=forms.TextInput(attrs={
            "placeholder":"Example : FR-22 | BA-10 | FU-22",
            "style": "font-size : 13px; text-transform: uppercase;",
            "data-mask": "AA-00"
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
            "style": "font-size : 13px; text-transform: lowercase;",
            # "autocomplete": "off" -----already done in supr func
            })
        )
    
    # Age must only be numbers and the length must not be less than 1 or greater than 3
    # age = forms.CharField(
    #     label="Age",
    #     min_length=1,
    #     max_length=3,
    #     # required=False,
    #     validators=[RegexValidator(r"^[0-9]{1,2}$", message="Enter a valid age")], 
    #     # widget=forms.TextInput(attrs={"placeholder":"Email Address",})
    #     widget=forms.TextInput(attrs={
    #         "placeholder":"Age",
    #         "style": "font-size : 13px;"})
    #     )
    
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
        label="Resume",
        required= True,
        widget=forms.ClearableFileInput(
            attrs={
                "style": "font-size : 13px;",
                # "accept": "application/pdf, application/msword, application/vnd.openxmlformats-officedocument.wordprocessingml.document, application/json"
            }
        )
    )
    # Image (Upload)
    image = forms.FileField(
        required= True,
        widget=forms.ClearableFileInput(
            attrs={
                "style": "font-size : 13px;",
                "accept": "image/png, image/jpeg"
            }
        )
    )
    
    # EDUCATION
    # Institution
    institution = forms.CharField(
        label="Institution",
        min_length= 2,
        max_length=50,
        widget=forms.TextInput(attrs={
            "placeholder":"Institution name",
            "style": "font-size : 13px;"
        })
    )
    
    
    # College Course
    course = forms.CharField(
        min_length= 2,
        max_length=50,
        widget=forms.TextInput(attrs={
            "placeholder":"Your college course",
            "style": "font-size : 13px;"
        })
    )
    
    # About_course
    about_course = forms.CharField(
        label="About your college course",
        max_length=300,
        widget=forms.Textarea(attrs={
            "placeholder":"Tell us about your course",
            "rows":4,
            "style": "font-size : 13px;"})
        
        )
    
     # About_job
    about_job = forms.CharField(
        label="About your last job",
        max_length=300,
        widget=forms.Textarea(attrs={
            "placeholder":"Tell us about your last job",
            "rows":4,
            "style": "font-size : 13px;"})
        
        )

    # PROFESSIONAL 
    # compnay (Last company)
    company = forms.CharField(
        label="Last company",
        min_length= 3,
        max_length=50,
        widget=forms.TextInput(attrs={
            "placeholder":"Campany name",
            "style": "font-size : 13px;"
        })
    )
    # compnay (Last company)
    position = forms.CharField(
        label="Postition",
        min_length= 3,
        max_length=50,
        widget=forms.TextInput(attrs={
            "placeholder":"Your position",
            "style": "font-size : 13px;"
        })
    )
    
    employed = forms.BooleanField(label="I am employed", required=False)
    remote = forms.BooleanField(label="I can work remotely", required=False)
    travel = forms.BooleanField(label="I am available to travel", required=False)
    
    
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
        labels ={
            "started_course":"Started",
            "finished_course":"finished",
            "started_job":"Started",
            "finished_job":"finished"
            # "phone":"Enter Phone",
            # "salary":"What is your salary expectation",
            # "personality":"What is your personality",
            # "gender":"Select your gender",
            # "smoker":"Do you smoke?"
        }
        
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
            # Birth date
            "birth": forms.DateInput(
                attrs={
                     "style": "font-size:14px; cursor:pointer",
                     "type":"date",
                     "onkeydown":"return false", # Javascript prevent typing
                     "min":"1958-01-01",
                     "max": str(date.today())
                }
            ),
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
            "smoker":forms.RadioSelect(choices=SMOKER ,attrs={"class":"btn-check"}),
            "status_course": forms.Select(attrs={"style": "font-size : 13px;"}),
            
            #started_course
            "started_course" :forms.DateInput(
                attrs={
                    "style": "font-size:13px; cursor:pointer",
                     "type":"date",
                     "onkeydown":"return false", # Javascript prevent typing
                     "min":"1950-01-01",
                     "max": str(date.today())
                }
            ),
            # finished_course
            "finished_course" :forms.DateInput(
                attrs={
                    "style": "font-size:13px; cursor:pointer",
                     "type":"date",
                     "onkeydown":"return false", # Javascript prevent typing
                     "min":"1950-01-01",
                     "max": str(date.today())
                }
            ),
            #started_job
            "started_job" :forms.DateInput(
                attrs={
                    "style": "font-size:13px; cursor:pointer",
                     "type":"date",
                     "onkeydown":"return false", # Javascript prevent typing
                     "min":"1950-01-01",
                     "max": str(date.today())
                }
            ),
            # finished_job
            "finished_job" :forms.DateInput(
                attrs={
                    "style": "font-size:13px; cursor:pointer",
                     "type":"date",
                     "onkeydown":"return false", # Javascript prevent typing
                     "min":"1950-01-01",
                     "max": str(date.today())
                }
            )
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
        
        # 4) FONT SIZE
        # font_size = ["firstname", "lastname", "job", "email", "age", "phone", "personality", "salary"]
        # for field in font_size:
        #     self.fields[field].widget.attrs.update({"style":"font-size: 15px;"}) 
        
        # 5) AUTO COMPLETE = OFF (Input History)
        # aut_complete = ["firstname", "lastname", "email", "phone"]
        # for field in aut_complete:
        #     self.fields[field].widget.attrs.update({"autocomplete":"off"}) 
            
                        
    #__________________________ END SUPERFUNCTION____________________
    
    
    #_______________________FUNCTION (METHOD CLEAN) ____________________
    
    # 1) FUNCTION TO PREVENT DUPLICATE ENTRIES
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
    
    
    # 2) JOB CODE (Job code validation)
    def clean_job(self):
        job = self.cleaned_data.get("job")
        if job == "FR-22" or job == "BA-10" or job == "FU-22":
            return job
        else: 
            raise forms.ValidationError(job +" role not presently available")
    
    # 3) AGE (Range: 15-35)
    # def clean_age(self):
    #     age = int(self.cleaned_data.get("age"))
    #     if age>15 and age<=35:
    #         return age
    #     else: 
    #         raise forms.ValidationError("Age must be between 15-35. Your age is: "+ str(age))
    
    # 4) PHONE (Prevent incomplete values):
    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if len(phone) != 20:
            raise forms.ValidationError("Incomplete number: +(234) 0000-0000-000")
        return phone
    
    # 5) RESTRICTION (File extensions - Method 2 via function )
    # METHOD 2
    # def clean_file(self):
    #     file = self.cleaned_data["file"]
    #     content_type = file.content_type
    #     if content_type == "application/pdf" or content_type == "application/msword":
    #         return file
    #     else:
    #         raise forms.ValidationError("Allowed files: PDF, DOC and DOCS")
        
    #  RESTRICTION (File extensions - Method 3 via function )
    #  # METHOD 3
    def clean_file(self):
        # get file 
        file = self.cleaned_data.get("file", False)
        #variables
        allowed_ext = ["pdf", "doc", "docx"]
        # get file ext
        ext = str(file).split(".")[-1]
        # a) accept only PDF, DOC and DOCS
        if ext.lower() in allowed_ext:
            if file.size <= 2 *1048576:
                # rename the file
                try:
                    new_name = (self.cleaned_data["firstname"]+"_"+self.cleaned_data["lastname"]+"."+ext).lower() 
                except KeyError:
                    return file
                else:
                    file.name = new_name
                    print(file.content_type)
                    print(file.name)
                    return file
            else:
                raise forms.ValidationError("Max. Upload: 2MB")
        else:
            raise forms.ValidationError("Allowed files: PDF, DOC and DOCS")
        
    # 6 IMAGE (Maximum upload size = 2mb)
    def clean_image(self):
        image = self.cleaned_data.get("image")
        ext = str(image).split(".")[-1]
        if image.size <= 2*1048576:
            try:
                new_name = (self.cleaned_data["firstname"]+"_"+self.cleaned_data["lastname"]+"."+ext).lower() 
            except KeyError:
                return image
            else:
                image.name = new_name
                return image
        else:
            raise forms.ValidationError("Max. Upload: 2MB")
    # 7) BIRTHDAY (Age: 18 and 65)
    def clean_birth(self):
        birth = self.cleaned_data.get("birth")
        # variables
        b = birth
        now = date.today()
        age = (now.year - b.year) - ((now.month, now.day) < (b.month, b.day))
        """ 
        age = (now.year - b.year) - ((now.month, now.day) < (b.month, b.day)) # i.e. 27 - ((9, 29) < (10, 26))
            
            ((now.month, now.day) < (b.month, b.day)) == ((9, 29) < (10, 26))
            
            Your answer will be True because (9, 29) is less than (10, 26) since 9(september) is less than 10(october) you haven't clocked 27 yet. The second elements of the tuples are not compared at all, as the first elements are enough to decide the result. You can think of it as comparing words in a dictionary: "apple" comes before "banana" because "a" comes before "b", regardless of the rest of the letters.
            
            Therefore (27 - True) is thesame as 27 -1 = 26
        """
        if age<18 or age >65:
            raise forms.ValidationError("Age must be between 18 and 65")
        
        return birth
    
    # 8) Prevent FUTURE date (card 3 and 4)
    #COLLEGE
    def clean_started_course(self):
        started_course = self.cleaned_data.get("started_course")
        if started_course > date.today():
            raise forms.ValidationError("Future dates is invalid")
        return started_course
        
        
    def clean_finished_course(self):
        try:
            started_course = self.cleaned_data.get("started_course")
            finished_course = self.cleaned_data.get("finished_course")
            if started_course>finished_course:
                raise forms.ValidationError("Date of started course cannot be greater than date of finished course")
        except TypeError:
            raise forms.ValidationError("Select a start date")
        else:
            return finished_course
    
    #COLLEGE
    def clean_started_job(self):
        started_job = self.cleaned_data.get("started_job")
        if started_job > date.today():
            raise forms.ValidationError("Future dates is invalid")
        return started_job
        
        
    def clean_finished_job(self):
        try:
            started_job = self.cleaned_data.get("started_job")
            finished_job = self.cleaned_data.get("finished_job")
            if started_job>finished_job:
                raise forms.ValidationError("Date of started job cannot be greater than date of finished job")
        except TypeError:
            raise forms.ValidationError("Select a start date")
        else:
            return finished_job