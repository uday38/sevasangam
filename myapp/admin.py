from django.contrib import admin
from .models import User, policy, category, Payment, feedback, complain, aadhar,ApplicationTable,ContactTable

# Register your models here

class show_User(admin.ModelAdmin):
    list_display = ['name','email','password','mobile_no','occupation','status',]
admin.site.register(User,show_User)
class show_Policy(admin.ModelAdmin):
    list_display = ['policy_name','policy_details','policy_type','policy_photo','policy_agency','policy_target_audience','policy_eligible_castes','policy_applicable_state','policy_residence_area','policy_disability_status','policy_minority_status','policy_bpl_status','policy_url']
admin.site.register(policy,show_Policy)
class show_Category(admin.ModelAdmin):
    list_display = ['category_name']
admin.site.register(category,show_Category)

class show_Payment(admin.ModelAdmin):
    list_display = ['payment_method','application_id','user_id','payment_status']
admin.site.register(Payment,show_Payment)

class show_Feedback(admin.ModelAdmin):
    list_display = ['user_id','rating']
admin.site.register(feedback,show_Feedback)

class show_Complain(admin.ModelAdmin):
    list_display = ['user_id','complain_name','complain_message','complain_datetime','complain_status']
admin.site.register(complain,show_Complain)

class show_Aadhar(admin.ModelAdmin):
    list_display = ['aadhar_firstname','aadhar_number','aadhar_middlename','lastname','address','phonenumber','dob','cast','gender','document','residencearea','disability_status','minority_status','bpl_status']
admin.site.register(aadhar,show_Aadhar)
class show_ApplicationTabel(admin.ModelAdmin):
    list_display = ['reg_id','name','policy_id','status','timestamp']
admin.site.register(ApplicationTable,show_ApplicationTabel)

class show_contactTabel(admin.ModelAdmin):
    list_display = ['email','subject','name','feedback_desk','timestamp']
admin.site.register(ContactTable,show_contactTabel)

