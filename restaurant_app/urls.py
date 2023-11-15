from django.urls import path
from . import views

urlpatterns = [
    # path function that with an empty string.
    # This is an empty string because this will be the homepage.
    #views.MenuList will be triggered 
    # and views.MenuList will send the index.html page 
    # to the user browser.
    # as_view, this is a method to which basically renders this class
    # as an actual view.
    path('',views.MenuList.as_view(),name='home'),
    # 127.0.0.1:8000/MenuItemDetail/
    path('item/<int:pk>/',views.MenuItemDetail.as_view(), name='menu_item')
]