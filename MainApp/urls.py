from django.urls import path
from . import views


urlpatterns = [
    path('first/', views.first_view),
    path('restaurant/', views.restaurant_view),
    path('restaurant2/', views.restaurant_views2),
    path('all_categories/', views.all_categories),
    path('create_category/', views.create_category),
    path('delete_category/<int:cat_id>/', views.delete_category),
]