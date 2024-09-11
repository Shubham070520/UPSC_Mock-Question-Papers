from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from App import views
app_name= 'App'   # Define app name for namespacing

urlpatterns = [
    path('',views.welcome,name="welcome"),  #http://127.0.0.1:8000/
    path('candidateRegistration',views.candidateRegForm,name="candidateRegistration"),   #signup.html ,name="registrationForm"
    path('store-candidate',views.candidateRegistration,name="store-candidate"), #name='store-candidate'
    path('login/' ,views.loginView, name="login"), 
    path('otp',views.otp,name="otp-verification"),
    path('home',views.candidateHome,name="home"), #redirect after login
    path('test-Paper',views.testPaper,name="test-paper"),
    path('calc-Result',views.calcTestRes,name="calc-result"),
    path('test-History',views.testResHistory,name="test-history"),
    path('result',views.showTestRes,name="show-result"),
    path('logout',views.logoutView,name="logout"),

]