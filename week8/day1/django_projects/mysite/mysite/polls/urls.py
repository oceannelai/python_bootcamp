from django.urls import path #path function
from . import views # . is shorthand for the current directory

urlpatterns = [
    path('profile',views.profile_user),

]
