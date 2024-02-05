from django.shortcuts import render
from django.contrib import messages
from .models import *
from .models import policy


# Create your views here.
def index04b9(request):
    return render(request, 'index04b9.html')

def index(request):
    return render(request, 'index.html')

def index2(request):
    return render(request, 'index-2.html')

def ourcompany(request):
    return render(request, 'about-company.html')

def aboutteam(request):
    return render(request, 'about-team.html')

def aboutpartners(request):
    return render(request, 'about-partners.html')

def services(request):
    return render(request, 'services.html')

def services2(request):
    return render(request, 'services-2.html')

def servicesdetail(request):
    return render(request, 'services-detail.html')

def faq(request):
    return render(request, 'faq.html')

def pricingtabel(request):
    return render(request, 'pricing-table.html')

def page(request):
    return render(request, '404page.html')

def career(request):
    return render(request, 'career.html')

def grid(request):
    return render(request, 'project-grid.html')

def detail(request):
    return render(request, 'project-detail.html')

def newsgrid(request):
    return render(request, 'news-grid.html')

def newssidebar(request):
    return render(request, 'news-sidebar.html')

def newsdetail(request):
    return render(request, 'news-detail.html')

def contact(request):
    return render(request, 'contact.html')

def contactus(request):
    return render(request, 'contact-us.html')

def contactquote(request):
    return render(request, 'contact-quote.html')

def boatinsurance(request):
    return render(request, 'service-boat-insurance.html')

def carinsurance(request):
    return render(request, 'service-car-insurance.html')

def houseinsurance(request):
    return render(request, 'service-house-insurance.html')

def lifeinsurance(request):
    return render(request, 'service-life-insurance.html')

def travelinsurance(request):
    return render(request, 'service-tarvel-insurance.html')

def vehicalinsurance(request):
    return render(request, 'service-vehical-insurance.html')

def insert(request):
    return render(request, 'insert.html')
def signup(request):
    return render(request, 'signup.html')
def login(request):
    return render(request, 'login.html')
def checklogin(request):
    return render(request, 'checklogin.html')


def insertdata(request):
    if request.method == "POST":
        username = request.POST.get('u_name')
        useremail = request.POST.get('u_email')
        userphonenumber = request.POST.get('u_phonenumber')
        userpassword = request.POST.get('u_password')
        useroccupation = request.POST.get('u_occupation')

        query= User(name=username, email=useremail, mobile_no=userphonenumber, password=userpassword,
                        occupation=useroccupation)
        query.save()
        messages.success(request," REGISTER SUCCESSFULL!!")
        return render(request, "login.html")
    else:
        messages.success(request,"UNABLE TO REGISTER!!")
        return render(request, "signup.html")

def checklogin(request):
    useremail=request.POST["u_email"]
    userpassword=request.POST["u_password"]
    try:
        query=User.objects.get(email=useremail)
        if check_password(userpassword=query.password):
            request.session['useremail']=query.email
            request.session['userid']=query.id
            print(request.session['userid'])
            return render(request, 'index04b9.html')
        else:
            messages.info(request, 'Incorrect email or password')
            return render(request, 'signup.html')
    except User.DoesNotExist:
        messages.info(request, 'Account does not exist!! Please Sign In')
        return render(request, 'signup.html')

def newsgrid(request):
    policydata=policy.objects.all()
    return render(request,"news-grid.html",{"policydata":policydata})


