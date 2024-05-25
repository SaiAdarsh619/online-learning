from django.urls import path,include
from myapp import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    # Add other paths as needed
]
