from django.urls import path
from user import views

urlpatterns = [
    path('signup/', views.sign_up_view, name='sign-up'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout, name='logout'),
]
