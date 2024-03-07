from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from .models import *



# Create your views here.
def aadhars(request):
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
def aadhardata(request):
    return render(request, 'aadhardata.html')




def insertdata(request):
    if request.method == "POST":
        username = request.POST.get('u_name')
        useremail = request.POST.get('u_email')
        userphonenumber = request.POST.get('u_phonenumber')
        userpassword = request.POST.get('u_password')
        useroccupation = request.POST.get('u_occupation')

        query= register_user(name=username, email=useremail, mobile_no=userphonenumber, password=userpassword,
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
        query = register_user.objects.get(email=useremail, password=userpassword)
        request.session['user_email'] = query.email
        request.session['user_id'] = query.id
        print(request.session['user_id'])
    except register_user.DoesNotExist:
        query=None
    if query is not None:
        messages.success(request,'Login successful!!')
        return redirect(index04b9)
    else:
        messages.error(request,'Acount does not exist!! please sign in')
        return redirect(login)

def logout(request):
    try:
        del request.session['user_email']
        del request.session['user_id']
        messages.success(request,"LOGOUT SUCCESSFULL!!")
    except:
        pass
    return redirect(index04b9)

def dashboard(request):
    return render(request,'dashboard.html')

def newsgrid(request):
    policydata=policy.objects.all()
    return render(request,"news-grid.html",{"policydata":policydata})

def policydetail(request,id):
    data=policy.objects.get(id=id)
    return render(request, 'policy-detail.html',{"data":data})



def releventpolicy(request):
    uid = request.session['user_id']

    ocuu = register_user.objects.filter(id=uid).values('occupation')
    area=aadhar.objects.filter(user_id=uid).values('residencearea')
    area_filter=['Both',area]
    try:
        filters = aadhar.objects.get(user_id=uid)
    except aadhar.DoesNotExist:
        filters = None
    # print(aadhar_id)
    aadhar_avail = False
    print("Try 2",filters.bpl_status)

    if filters is not None:
        aadhar_avail = True
        if  filters.disability_status == 'Yes' and filters.minority_status == 'Yes' and filters.bpl_status == 'Yes':
            policy_data=policy.objects.filter(policy_type__in=ocuu, policy_residence_area__in=area_filter,policy_disability_status='Yes',policy_minority_status='Yes',policy_bpl_status='Yes')
            print(policy_data)
            contex = {
                    'policydata': policy_data,
                    'aadhar_avail': aadhar_avail,
                }
        elif  filters.disability_status == 'Yes' and filters.minority_status == 'No' and filters.bpl_status == 'No':
            policy_data=policy.objects.filter(policytype_icontains=ocuu, policy_residence_area_in=area_filter,policy_disability_status='Yes',status='No',policy_bpl_status='No')

            contex = {
                    'data': policy_data,
                    'aadhar_avail': aadhar_avail,
                }
        elif filters.disability_status == 'No' and filters.minority_status == 'Yes' and filters.bpl_status == 'No':
            policy_data = policy.objects.filter(policytype_icontains=ocuu, policy_residence_area_in=area_filter,policy_disability_status='No', policy_minority_status='Yes', policy_bpl_status='No')

            contex = {
                'data': policy_data,
                'aadhar_avail': aadhar_avail,
            }
        elif filters.disability_status == 'No' and filters.minority_status == 'No' and filters.bpl_status == 'Yes':
            policy_data = policy.objects.filter(policytype_icontains=ocuu, policy_residence_area_in=area_filter, policy_disability_status='No', policy_minority_status='No', policy_bpl_status='Yes')
            contex = {
                'data': policy_data,
                'aadhar_avail': aadhar_avail,
            }
        elif filters.disability_status == 'No' and filters.minority_status == 'Yes' and filters.bpl_status == 'Yes':
            policy_data = policy.objects.filter(policytype_icontains=ocuu, policy_residence_area_in=area_filter,policy_disability_status='No', policy_minority_status='Yes', policy_bpl_status='Yes')
            contex = {
                'data': policy_data,
                'aadhar_avail': aadhar_avail,
            }
        elif filters.disability_status == 'Yes' and filters.minority_status == 'No' and filters.bpl_status == 'Yes':
            policy_data = policy.objects.filter(policytype_icontains=ocuu, policy_residence_area_in=area_filter,policy_disability_status='Yes', policy_minority_status='No', policy_bpl_status='Yes')
            contex = {
                'data': policy_data,
                'aadhar_avail': aadhar_avail,
            }
        elif filters.disability_status == 'Yes' and filters.minority_status == 'Yes' and filters.bpl_status == 'No':
            policy_data = policy.objects.filter(policytype_icontains=ocuu, policy_residence_area_in=area_filter,policy_disability_status='Yes', policy_minority_status='Yes', policy_bpl_Status='No')
            contex = {
                'data': policy_data,
                'aadhar_avail': aadhar_avail,
            }
            
        else:
            # policies = policy.objects.filter(policytype_icontains=ocuu,policy_residence_area_in=area_filter)
            
            
            # occ_val = ocuu[0]['occupation']
            # print(occ_val)
            policies = policy.objects.filter(policy_type='Home')
            print("policydata",policies)
            contex = {
                'policydata': policies,
                'aadhar_avail': aadhar_avail,
            }
        # print("check upper")
        # print(aadhar_avail)
        # messages.success(request, 'AADHAR DETAILS ADDED SUCCESSFULLY!!')
        return render(request, 'relevent_policy.html', contex)
    else:
        aadhar_avail = False
        # print("check lower")
        # print(aadhar_avail)
        acontext = {
            'aadhar_avail': aadhar_avail
        }
        # messages.error(request, 'Add Aadhar Details')
        return render(request, 'relevent_policy.html', acontext)
    
    
    
def aadhardata(request):
    if request.method == 'POST':
        Aadharfirstname = request.session['user_id']
        Aadharnumber = request.POST.get('aadharnumber')
        Aadharmiddlename = request.POST.get('aadharmiddlename')
        Lastname = request.POST.get('lastname')
        Address = request.POST.get('address')
        Phonenumber = request.POST.get('phonenumber')
        Dob = request.POST.get('dob')
        Cast = request.POST.get('cast')
        Gender = request.POST.get('gender')
        Photo = request.FILES.get('photo')
        Residencearea = request.POST.get('residencearea')
        Disabilitystatus = request.POST.get('disabilitystatus')
        Minoritystatus = request.POST.get('minoritystatus')
        Bplstatus = request.POST.get('bplstatus')

        query = aadhar(user_id=register_user(id=Aadharfirstname), aadhar_number=Aadharnumber, aadhar_middlename=Aadharmiddlename, lastname=Lastname, address=Address, phonenumber=Phonenumber, dob=Dob, cast=Cast, gender=Gender, document=Photo, residencearea=Residencearea, disability_status=Disabilitystatus, minority_status=Minoritystatus, bpl_status=Bplstatus )
        query.save()
        messages.success(request, 'AADHAR DETAILS ADDED SUCCESSFULLY!!')
        return render(request, 'aadhar.html')
    else:
        messages.error(request, 'Unable to Add Aadhar Details')
        return render(request, 'aadhar.html')
    
def feedback(request):
    if request.method == "POST":
        star = request.POST.get("Rating")
        message = request.POST.get("p_message")

        insertdata = feedback(user_id=register_user(request.session['u_id']),rating=star,comments =message)
        insertdata.save()
        return redirect(reverse('index04b9'))
    
def Feedback(request):
    return render(request,'feedback.html')

def editpolicy(request):
    return render(request,'editpolicy.html')
def editpolicy(request,eid):
    data=policy.objects.get(id=eid)
    return render(request,'editpolicy.html',{"policydata":data})

def updatepolicy(request,uid):
    name = request.POST.get('name')
    price = request.POST.get('price')
    desc = request.POST.get('desc')
    data=policy.objects.get(id=uid)
    data.policy_name=name
    data.policy_publication_date=price
    data.policy_details=desc
    if "pimage" in request.FILES:
        image = request.FILES['pimage']
        data.policy_photo=image
    data.save()
    return redirect('index04b9')



    
