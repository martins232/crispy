from django.contrib import admin
from . models import Candidate
from .forms import CandidateForm
from django.utils.html import format_html

class CandidateAdmin(admin.ModelAdmin):
    radio_fields = {"smoker": admin.HORIZONTAL}
    form = CandidateForm
    readonly_fields = ["firstname", "lastname", "job","email" , "age","phone","personality","salary", "gender", "experience", "smoker","file", "frameworks", "languages", "databases", "libraries", "mobile", "others"]
    exclude= ["status"]
    list_filter = ["situation"]
    list_display = ["name", "job","email" , "file", "age", "created_at", "status", "_"]
    search_fields = ["firstname", "lastname","email", "situation"]
    list_per_page = 10
    
    # Function to hide Fname and Lname when you click candidate
    def get_fields(self, request, obj):
        fields= super().get_fields(request, obj)
        if obj:
            fields.remove("firstname")
            fields.remove("lastname")
        return fields
    
    
    #Function to change the icons
    def _(self, obj): #_ was used so that you can get values for none
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
