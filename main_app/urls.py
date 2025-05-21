from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    # Routes will be added here
    path('', views.home, name='home'), # Home page route
    path('about/', views.about, name='about'), # About page route
    path('cats/', views.cat_index, name='cat_index'),
]
