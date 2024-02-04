from django.urls import path
from . import views

urlpatterns = [
    path('', views.index04b9, name="index04b9.html"),
    path('login/', views.login, name="login.html"),
    path('signup/', views.signup, name="signup.html"),
    path('insert', views.insertdata, name='insert'),
    path("index/", views.index, name="index.html"),
    path("index2/", views.index2, name="index-2.html"),
    path("about company/", views.ourcompany, name="about-company.html"),
    path("about team/", views.aboutteam, name="about-team.html"),
    path("about partners/", views.aboutpartners, name="about-partners.html"),
    path("services/", views.services, name="services.html"),
    path("services2/", views.services2, name="services-2.html"),
    path("services detail/", views.servicesdetail, name="services-detail.html"),
    path("FAQ/", views.faq, name="faq.html"),
    path("pricingtabel/", views.pricingtabel, name="pricing-tabel.html"),
    path("404page/", views.page, name="404page.html"),
    path("careers/", views.career, name="careers.html"),
    path("project grid/", views.grid, name="project-grid.html"),
    path("project detail/", views.detail, name="project-detail.html"),
    path("news grid/", views.newsgrid, name="news-grid.html"),
    path("news sidebar/", views.newssidebar, name="news-sidebar.html"),
    path("news detail/", views.newsdetail, name="news-detail.html"),
    path("contact/", views.contact, name="contact.html"),
    path("contact us/", views.contactus, name="contact-us.html"),
    path("contact quote/", views.contactquote, name="contact-quote.html"),
    path('checklogin',views.checklogin, name="checklogin")
]