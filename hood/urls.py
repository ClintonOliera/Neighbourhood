from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('', views.index, name='index'),
    url('signup/', views.signup, name='signup'),
    url('account/', include('django.contrib.auth.urls')),
    url('all-hoods/', views.hoods, name='hood'),
    url('new-hood/', views.create_hood, name='new-hood'),
    url('profile/<username>', views.profile, name='profile'),
    url('profile/<username>/edit/', views.edit_profile, name='edit-profile'),
    url('join_hood/<id>', views.join_hood, name='join-hood'),
    url('leave_hood/<id>', views.leave_hood, name='leave-hood'),
    url('single_hood/<hood_id>', views.single_hood, name='single-hood'),
    url('<hood_id>/new-post', views.create_post, name='post'),
    url('<hood_id>/members', views.hood_members, name='members'),
    url('search/', views.search_business, name='search'),
]