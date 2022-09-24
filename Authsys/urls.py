from django.urls import path
from . import views


urlpatterns = [
    path('test/', views.test_view),
    path('sign_in/', views.sign_in),
    path('logout/', views.log_out)
]