from django.urls import path
# from team import views
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('user_login', views.user_login, name='user_login'),
    path('signup', views.signup, name='signup'),
    path('user_homepage', views.user_homepage, name='user_homepage'),
    path('all_jobs', views.all_jobs, name='all_jobs'),
    path('job_detail/<str:id>', views.job_detail, name='job_detail'),
    # path('job_apply/id/', views.job_apply, name='job_apply')
    path('job_apply/<int:myid>/', views.job_apply, name='job_apply')
]


    
