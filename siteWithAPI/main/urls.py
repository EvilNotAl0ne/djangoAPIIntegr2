from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('test_read_api', views.test_read_api, name='test_read_api'),
    # path('test_create_api', views.test_create_api, name='test_create_api')
]