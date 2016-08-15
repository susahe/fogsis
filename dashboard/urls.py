from django.conf.urls import url

from . import views

app_name = 'dashboard'

urlpatterns = [

    # url(r'^$', views.index , name = 'index'),
    url(r'^$', views.HomePageView.as_view(), name='index'),
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),
    # # url(r'^(?P<course_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    # url(r'^course/add/$', views.CourseCreate.as_view(), name='course-add'),
    # url(r'^module/add/$', views.ModuleCreate.as_view(), name='module-add'),
    # url(r'^course/(?P<pk>[0-9]+)/update/$', views.CourseUpdate.as_view(), name='course-update'),
    # url(r'^course/(?P<pk>[0-9]+)/delete/$', views.CourseDelete.as_view(), name='course-delete'),
    # url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', views.LogOutView.as_view(), name='logout'),

]
