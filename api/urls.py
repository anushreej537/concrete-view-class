from django.urls import path
from api import views
urlpatterns = [
    path('stulist/',views.StudentList.as_view()),
    path('createlist/',views.CreateStudentList.as_view()),
    path('fetchstu/<int:pk>/',views.RetrieveStudentList.as_view()),
    path('updatestu/<int:pk>/',views.UpdateStudentList.as_view()),
    path('delstu/<int:pk>/', views.DestroyStudata.as_view()),
    path('listcreatestu/',views.ListCreateStudata.as_view()),
    path('retrieveupdatestu/<int:pk>/',views.RetrieveUpdateStudata.as_view()),
    path('retrievedelstudata/<int:pk>/',views.RetrieveDestroyStudata.as_view()),
    path('retrieveupdatedelstudata/<int:pk>/',views.RetrieveUpdateDelStudata.as_view())
]
