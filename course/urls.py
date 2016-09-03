from django.conf.urls import url

from . import views

app_name = 'course'

urlpatterns = [

    # url(r'^$', views.index , name = 'index'),
    url(r'^course/$', views.CourseListView.as_view(), name='course_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),
    # url(r'^(?P<course_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'^course/add/$', views.CourseCreate.as_view(), name='course-add'),
    url(r'^course/(?P<pk>[0-9]+)/update/$', views.CourseUpdate.as_view(), name='course-update'),
    url(r'^course/(?P<pk>[0-9]+)/delete/$', views.CourseDelete.as_view(), name='course-delete'),

    # ==========================================================================================================

    url(r'^module/add/$', views.CourseModuleCreate.as_view(), name='coursemodule-add'),
    url(r'^module/$', views.CourseModuleListView.as_view(), name='coursemodule_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailCourseModuleView.as_view(), name='moduledetails'),
    url(r'^module/(?P<pk>[0-9]+)/update/$', views.CourseModuleUpdate.as_view(), name='coursemodule-update'),
    url(r'^module/(?P<pk>[0-9]+)/delete/$', views.CourseModuleDelete.as_view(), name='coursemodule-delete'),

    # ==============================================================================================================

    url(r'^task/add/$', views.TaskCreate.as_view(), name='task-add'),
    url(r'^task/$', views.TaskListView.as_view(), name='task_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.TaskDetailView.as_view(), name='task_details'),
    url(r'^task/(?P<pk>[0-9]+)/update/$', views.TaskUpdate.as_view(), name='task-update'),
    url(r'^task/(?P<pk>[0-9]+)/delete/$', views.TaskDelete.as_view(), name='task-delete'),

    # ==============================================================================================================
    url(r'^activity/add/$', views.ActivityCreate.as_view(), name='activity-add'),
    url(r'^activity/$', views.ActivityListView.as_view(), name='activity_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.ActivityDetailView.as_view(), name='activity_details'),
    url(r'^activity/(?P<pk>[0-9]+)/update/$', views.ActivityUpdate.as_view(), name='activity-update'),
    url(r'^activity/(?P<pk>[0-9]+)/delete/$', views.ActivityDelete.as_view(), name='activity-delete'),
]
