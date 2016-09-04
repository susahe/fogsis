from django.conf.urls import url

from . import views

app_name = 'acount'

urlpatterns = [

    url(r'^$', views.PaymentView.as_view(), name='payment-list'),
    url(r'^(?P<pk>[0-9]+)/$', views.PaymentDetailView.as_view(), name='payment-details'),
    url(r'^payment/add/$', views.PaymentCreate.as_view(), name='payment-add'),
    url(r'^payment/(?P<pk>[0-9]+)/delete/$', views.PaymentDelete.as_view(), name='payment-delete'),

]
