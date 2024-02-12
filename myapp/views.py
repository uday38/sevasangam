from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from .models import *
from .models import policy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404

# from django.core.exceptions import PermissionDenied



# Create your views here.
def aadhar(request):
    return render(request, 'aadhar.html')

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



def careers(request):
    return render(request, 'careers.html')

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
def logout(request):
    return render(request, 'logout.html')
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
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Welcome {username}")
                return redirect('indexo4b9.html')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def newsgrid(request):
    policydata=policy.objects.all()
    return render(request,"news-grid.html",{"policydata":policydata})

def policydetail(request,id):
    fetch=policy.objects.get(id=id)
    return render(request, 'policy-detail.html',{"data":fetch})

def logout(request):
    try:
        del request.session['u_name']
        del request.session['u_password']
    except:
        pass
    return redirect(index04b9)



# def policydetail(request, id):
#     data = get_object_or_404(data, id=id)
#     if not request.user.has_perm('policy.view_policy', data):
#         raise PermissionDenied
#     return render(request, 'policy_detail.html', {'policy': data})


def aadhar(request):
    if request.method == 'POST':
        form = aadhar(request.POST)
        if form.is_valid():
            aadhar = form.save(commit=False)
            aadhar.user = request.user
            aadhar.save()
            messages.success(request, 'Aadhaar card saved successfully.')
            return redirect(reverse('aadhar_detail'))
    else:
        form = aadhar()
    users = User.objects.all()
    return render(request, 'aadhar.html', {'form': form, 'users': users})

@login_required
def aadhar(request, aadhar_id):
    aadhar = aadhar.objects.get(id=aadhar_id)
    return render(request, 'aadhar.html', {'aadhar': aadhar})