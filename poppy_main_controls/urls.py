from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.poppyMainController.index, name='index'),
    ]