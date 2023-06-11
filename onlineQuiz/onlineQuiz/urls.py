"""onlineQuiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Quiz.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('studentlogin/', Studentlogin, name='studentlogin'),
    path('tutorlogin/', Tutorlogin, name='tutorlogin'),
    path('userdashboard/', Userdashboard, name='userdashboard'),
    path('addtopic/', addTopic, name='addtopic'),
    path('addcourse/', addCourse, name='addcourse'),
    path('addquestion/', addQuestion, name='addquestion'),
    path('adduser/', addUser, name='adduser'),
    path('tutorreport/', TutorReport, name='tutorreport'),
    path('studentreport/', StudentReport, name='studentreport'),
    path('topicreport/', TopicDetail, name='topicreport'),
    path('coursereport/', CourseReport, name='coursereport'),
    path('questionreport/', QuestionReport, name='questionreport'),
    path('changepassword/<int:pid>', ChangePassword, name='changepassword'),
    path('changepassword2/<int:pid>', ChangePassword2, name='changepassword2'),
    path('logout/', Logout, name='logout'),
    path('courselist/', CourseList, name='courselist'),
    path('myresult/<int:pid>', MyResult, name='myresult'),
    path('viewtopic/<int:pid>', ViewTopic, name='viewtopic'),
    path('studentdashboard/', StudentDashboard, name='studentdashboard'),
    path('startquiz/<int:pid>', StartQuiz, name='startquiz'),
    path('signuptutor/', Signup_Tutor, name='signuptutor'),
    path('signupstudent/', Signup_Student, name='signupstudent'),
    path('myaccount/<int:pid>',MyAccount, name='myaccount'),
    path('deletetutor/<int:pid>',DeleteTutor, name='deletetutor'),
    path('deletecourse/<int:pid>',DeleteCourse, name='deletecourse'),
    path('deletequestion/<int:pid>',DeleteQuestion, name='deletequestion'),
    path('deletestudent/<int:pid>',DeleteStudent, name='deletestudent'),
    path('deletetopic/<int:pid>',DeleteTopic, name='deletetopic'),
    path('edittopic/<int:pid>',EditTopic, name='edittopic'),
    path('editcourse/<int:pid>',EditCourse, name='editcourse'),
    path('editstudent/<int:pid>',EditStudent, name='editstudent'),
    path('edittutor/<int:pid>',EditTutor, name='edittutor'),
    path('editquestion/<int:pid>',EditQuestion, name='editquestion'),
    path('viewresult/<int:pid>',View_Result, name='viewresult'),
    path('myaccountstudent/<int:pid>',MyAccountStudent, name='myaccountstudent'),
    path('resultreport/',ResultReport, name='resultreport'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
