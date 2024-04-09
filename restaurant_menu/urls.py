from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name='home'),
    path('item/<int:pk>/', views.MenuItemDetail.as_view(), name="menu_item")
]
# when the viewer visits the root or the homepage
# the default page will be index.html
# views means the file where MenuList is coming from 
