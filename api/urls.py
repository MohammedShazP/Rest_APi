from django.urls import  path
from . import views

urlpatterns = [
    path('register/',views.Register.as_view(),name="register"),
    path('userdetail/<int:id>',views.UserDetail.as_view(),name="detail")
]