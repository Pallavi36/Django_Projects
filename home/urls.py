from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.show,name="show"),
    path('addstudent',views.addstudent,name="addstudent"),
    path('showstudents',views.showstudents,name="showstudents"),
    path('updatestudent',views.updatestudent,name="updatestudent"),
    path('searchstudent',views.searchstudent,name="searchstudent"),
    path('joinstudent',views.joinstudent,name="joinstudent"),
    path('showjoined',views.showjoined,name="showjoined"),
    path('updatejoined',views.updatejoined,name="updatejoined"),
    path('searchjoined',views.searchjoined,name="searchjoined"),
    path('addbatch',views.addbatch,name="addbatch"),
    path('showbatch',views.showbatch,name="showbatch"),
    path('updatebatch',views.updatebatch,name="updatebatch"),
    path('searchbatch',views.searchbatch,name="searchbatch"),
    path('addtrainer',views.addtrainer,name="addtrainer"),
    path('showtrainer',views.showtrainer,name="showtrainer"),
    path('searchtrainer',views.searchtrainer,name="searchtrainer"),
    
    
    
    
]
