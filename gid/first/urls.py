'''
wake me up when september end
'''
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
        path('crm/', views.crm, name='crm'),
        path('crm_insert/', views.crm_insert, name='crm_insert'),  
]
