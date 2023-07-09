"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('signup/',views.signup, name="signup"),
    path('login/',views.loguserin, name="login"),
    path('logout/',views.loguserout, name="logout"),
    
    path('tasks/',views.task, name="usertask"),
    path('tasks/end',views.taskend, name="task_end"),
    path('tasks/create/',views.createTask, name="createTask"),
    path('tasks/<int:task_id>/',views.task_detail, name="taskDetail"),
    path('tasks/<int:task_id>/complete',views.taskComplete, name="completeTask"),
    path('tasks/<int:task_id>/delete',views.taskDelete, name="deleteTask"),
    
    path('tasks/categories/',views.category, name="showCate"),
    path('tasks/create/cate/',views.createCategory, name="createcate"),
    path('tasks/categories/<int:category_id>/delete',views.deleteCategory, name="deleteCategory"),
    
    path('tasks/create/group/',views.createGroup, name="creategroup"),
    path('tasks/manage/group/task/<int:taskgroup_id>/',views.task_group_detail, name="groupTaskDetail"),
    path('tasks/manage/group/<int:group_id>/delete',views.deleteGroup, name="deleteGroup"),
    path('tasks/manage/group/',views.showGroup, name="managegroup"),
    path('tasks/create/group/task/<int:group_id>/create/',views.createGroupTask, name="createGroupTask"),
    path("tasks/manage/group/<int:group_id>/addMembers",views.addMembers, name="addMembers"),
    path('tasks/manage/group/<int:group_id>/modify',views.modifyGroup, name="modifyGroup"),
]
