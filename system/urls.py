from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="home"),
    path('<int:id>', views.driver, name='driver'),
    path('add/', views.addDriver, name='add'),
    path('edit/<int:id>', views.editDriver, name='edit'),
    path('delete/<int:id>', views.deleteDriver, name='delete'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile/<int:id>', views.profile, name='profile')

]
