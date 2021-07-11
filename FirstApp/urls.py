from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.clients, name='clients'),
    path('clients/<int:id>', views.get_clients_id, name='get_clients_id'),
    path('projects/', views.projects, name='projects'),
    path('clients/<int:id>/projects', views.create_project, name='create_project'),
    # path('get_api/<str:fileType>/', views.get_api, name='get_api'),
    # path('get_api_id/<str:fileType>/<int:id>', views.get_api_id, name='get_api_id'),
    # path('update_api/<str:fileType>/<int:id>', views.update_api, name='update_api'),
    # path('delete_api/<str:fileType>/<int:id>', views.delete_api, name='delete_api'),
]