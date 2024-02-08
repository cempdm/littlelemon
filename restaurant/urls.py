from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [ 
    path('', views.index, name='home'), 
    path('about/', views.about, name="about"),
    path('booking/', 
        views.BookingViewSet.as_view({'get':'list', 'post':'create'}), 
        name="booking"),

    path('menu/', 
        views.MenuItemView.as_view(), 
        name="menu"),

    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('menu-items/', views.MenuItemView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),

    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token)
]
