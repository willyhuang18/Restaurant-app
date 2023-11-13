from django.urls import path
from . import views

urlpatterns = [
    # 127.0.0.1:8000/index/
    path('',views.MenuList.as_view(),name='home'),
    # 127.0.0.1:8000/MenuItemDetail/
    path('login/',views.user_login,name="login"),
]