from django.contrib import admin
from . models import Candidate
from .forms import CandidateForm
from django.utils.html import format_html

class CandidateAdmin(admin.ModelAdmin):
    radio_fields = {"smoker": admin.HORIZONTAL}
    form = CandidateForm
    exclude= ["status"] # remove status from admin form
    list_filter = ["situation"]
    list_display = ["name", "job","email" , "file", "created_at", "status", "_"]
    search_fields = ["firstname", "lastname","email", "situation"]
    list_per_page = 10
    
    
    #readonly section
    readonly_fields = ["firstname", "lastname", "experience", "gender","job","email" ,"phone","salary",'birth',"personality",  "smoker","file", "image", "frameworks", "languages", "databases", "libraries", "mobile", "others",'institution','status_course', 'course', 'started_course', 'finished_course', 'about_course',  'company', 'position', 'started_job', 'finished_job', 'about_job', 'employed', 'remote', 'travel', ]
    
    
    fieldsets = [
        #HR OPERATIONS
        ("HR OPERATIONS", {"fields": ["situation", "company_note"]}),
        
        ("PERSONAL", {"fields":["experience", "gender","job","email" ,"phone","salary",'birth',"personality",  "smoker", "image", "file"]}),
        
        ("CANDIDATE SKILLS", {"fields":["frameworks", "languages", "databases", "libraries", "mobile", "others"]}),
        
        ("EDUCATIONAL BACKGROUND", {"fields":['institution','status_course', 'course', 'started_course', 'finished_course', 'about_course']}),
        
        ("OTHERS",{"fields":['company', 'position', 'started_job', 'finished_job', 'about_job', ]}),
        
        ("NOTE",{"fields":["employed",'remote', 'travel']}),
    ]
    
    # Function to hide Fname and Lname when you click candidate
    def get_fields(self, request, obj):
        fields= super().get_fields(request, obj)
        if obj:
            fields.remove("firstname")
            fields.remove("lastname")
        return fields
    
    
    #Function to change the icons. N.B if you are assigning new values use (self, var)
    def _(self, obj): #_ was used so that you can get values for None
        if obj.situation == "Approved":
            return True
        elif obj.situation == "Pending":
            return None
        else:
            return False
    _.boolean = True
    
    #function to color the text
    def status(self, obj):
        if obj.situation == "Approved":
            color = "#28a745"
        elif obj.situation == "Pending":
            color = "#fea95e"
        else:
            color = "red"
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.situation))
    status.allow_tags = True
            
        
  
admin.site.register(Candidate, CandidateAdmin)



