"""hyo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from hyoapp import views

urlpatterns = [
    path('registration/login', views.login, name="login"),
    path('registration/signup/', views.signup, name = "signup"),
    path('registration/family_signup', views.family_signup, name="family_signup"),
    path('registration/logout', views.logout, name="logout"),
    path('admin/', admin.site.urls),
    path('new/', views.new, name="new"),
    path('home', views.home, name="home"),
    path('detail_url/<int:image_pk>', views.detail, name="detail"),
    path('delete_comment/<int:image_pk>/<int:comment_pk>', views.delete_comment, name="delete_comment"),
    path('edit_comment/<int:image_pk>/<int:comment_pk>', views.edit_comment, name="edit_comment"),
    path('indiv_home/<int:member_pk>', views.indiv_home, name="indiv_home"),
    path('todo', views.todo, name='todo'),
    path('todo_new',views.todo_new, name='todo_new'),
    path('todo_delete/<int:todo_pk>', views.todo_delete, name='todo_delete'),
    path('dday', views.dday, name='dday'),
    path('dday_new', views.dday_new, name='dday_new'),
    path('dday_delete', views.dday_delete, name='dday_delete'),
    path('shop',views.shop, name='shop'),
    path('account',views.account,name='account'),
    path('mission/', views.mission, name="mission"),
    path('',views.index, name='index')
]
