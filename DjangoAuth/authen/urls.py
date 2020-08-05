from django.urls import path
from . import views
 
app_name = 'authen'
 
urlpatterns = [
    path('signup/', views.signup_view, name='signup')
]