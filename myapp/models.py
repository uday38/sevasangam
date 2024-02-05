from email.policy import Policy
from django.db import models
from django.utils.safestring import mark_safe

STATUS_CHOICES = [
    ('active', 'Active'),
    ('inactive', 'Inactive'),
]
ROLE_CHOICES = [
    ('user', 'User'),
    ('admin', 'Admin'),
]
payment=[
    ("0","online"),
    ("1","offline")
]
paystatus=[
    ("0", "Inactive"),
    ("1", "Active")
]
complainstatus=[
    ("0", "Inactive"),
    ("1", "Active")
]
gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
disability_status_choices = [
        ('Y', 'Yes'),
        ('N', 'No'),
    ]
minority_status_choices = [
    ('Y', 'Yes'),
    ('N', 'No'),
]
bpl_status_choices = [
    ('Y', 'Yes'),
    ('N', 'No'),
]


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=15)
    occupation = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return self.name

class policy(models.Model):
    policy_name = models.CharField(max_length=255)
    policy_details = models.TextField()
    policy_type = models.CharField(max_length=50)
    policy_photo = models.ImageField(upload_to='photos')
    policy_agency = models.CharField(max_length=100)
    policy_publication_date = models.DateTimeField(max_length=100)
    policy_target_audience = models.CharField(max_length=100)
    policy_eligible_castes = models.CharField(max_length=100)
    policy_applicable_state = models.CharField(max_length=50)
    policy_residence_area = models.CharField(max_length=50)
    policy_disability_status = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')])
    policy_minority_status = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')])
    policy_bpl_status = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')])
    policy_url = models.URLField()

    def __str__(self):
        return self.policy_name
    
    # def policy_photo(self):
    #     return mark_safe('<img src="{}" width="100"/>'.format(self.policy_photo.url))
    # policy_photo.allow_tags = True

    
    
class category(models.Model):
    category_name=models.CharField(max_length=20)

class Payment(models.Model):
    payment_method=models.BigIntegerField(choices=payment)
    application_id=models.ForeignKey(policy,on_delete=models.CASCADE)
    user_id=models.BigIntegerField(primary_key=True)
    payment_status=models.IntegerField(choices=paystatus)

class feedback(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.IntegerField()
    comments=models.TextField(max_length=20)

class complain(models.Model):
    user_id=models.BigIntegerField(primary_key=True)
    complain_name=models.CharField(max_length=20)
    complain_message=models.TextField(max_length=25)
    complain_datetime=models.DateTimeField(max_length=10)
    complain_status=models.IntegerField(choices=complainstatus)


class aadhar(models.Model):
    aadhar_firstname=models.ForeignKey(User,on_delete=models.CASCADE)
    aadhar_number=models.BigIntegerField()
    aadhar_middlename=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    address=models.TextField(max_length=20)
    phonenumber=models.BigIntegerField()
    dob = models.DateField()
    cast = models.IntegerField()
    gender = models.CharField(max_length=1, choices=gender_choices)
    document = models.CharField(max_length=50)
    residencearea = models.CharField(max_length=50)
    disability_status = models.CharField(max_length=1, choices=disability_status_choices)
    minority_status = models.CharField(max_length=1, choices=minority_status_choices)
    bpl_status = models.CharField(max_length=1, choices=bpl_status_choices)

    def __str__(self):
        return self.aadhar_firstname

class ApplicationTable(models.Model):
    reg_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    policy_id = models.ForeignKey(policy, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.reg_id}"

class ContactTable(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    feedback_desk = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


def user():
    return None