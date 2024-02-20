from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index04b9, name="index04b9.html"),
    path('login/', views.login, name="login.html"),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name="signup.html"),
    path('insert', views.insertdata, name='insert'),
    path("index/", views.index, name="index.html"),
    path("index2/", views.index2, name="index-2.html"),
    path("about company/", views.ourcompany, name="about-company.html"),
    path("about team/", views.aboutteam, name="about-team.html"),
    path("about partners/", views.aboutpartners, name="about-partners.html"),
    path("services/", views.services, name="services.html"),
    path("services2/", views.services2, name="services-2.html"),
    path("servicesdetail/", views.servicesdetail, name="services-detail.html"),
    path("FAQ/", views.faq, name="faq.html"),
    path("pricing tabel/", views.pricingtabel, name="pricing-table.html"),
    path("404page/", views.page, name="404page.html"),
    path("careers/", views.careers, name="careers.html"),
    path("policydetail/<int:id>", views.policydetail, name="policy-detail.html"),
    path("relevent_policy", views.releventpolicy, name="releventpolicy"),

    path("project grid/", views.grid, name="project-grid.html"),
    path("project detail/", views.detail, name="project-detail.html"),
    path("news grid/", views.newsgrid, name="news-grid.html"),
    path("news sidebar/", views.newssidebar, name="news-sidebar.html"),
    path("news detail/", views.newsdetail, name="news-detail.html"),
    path("contact/", views.contact, name="contact.html"),
    path("contact us/", views.contactus, name="contact-us.html"),
    path("contact quote/", views.contactquote, name="contact-quote.html"),
    path("checklogin",views.checklogin, name="checklogin"),
    path("boatinsurance/",views.boatinsurance, name="service boat insurance.html"),
    path("carinsurance/",views.carinsurance, name="service car insurance.html"),
    path("houseinsurance/",views.houseinsurance, name="service house insurance.html"),
    path("lifeinsurance/",views.lifeinsurance, name="service life insurance.html"),
    path("travelinsurance/",views.travelinsurance, name="service travel insurance.html"),
    path("vehicalinsurance/",views.vehicalinsurance, name="service vehical insurance.html"),
    path('aadhars/', views.aadhars, name="aadhar.html"),
    path('aadhardata', views.aadhardata, name="aadhardata"),

]