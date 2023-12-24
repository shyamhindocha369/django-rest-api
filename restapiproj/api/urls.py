
from django.urls import path
from . import views

urlpatterns = [
    path("",views.endpoints),
    path("putdata/",views.create_fooddata),
    path("viewall/",views.list_fooddata),
    path('view/<int:pk>/', views.get_fooddata),
    
    path('delete/<int:id>/', views.delete_fooddata, name='fooddata-delete'),
    path('update/<int:id>/', views.update_fooddata, name='fooddata-update'),
    path('search/', views.search_fooddata, name='fooddata-search'),
]
