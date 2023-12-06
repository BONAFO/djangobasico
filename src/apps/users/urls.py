"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.users import views


urlpatterns = [
    path("delete/<int:id>", views.delete_confirm, name="delete user"),
    path("update/<int:id>", views.update_user, name="update user"),
    path("users/", views.get_user, name="get_user"),

    # path("test/<int:id>", views.test, name="update user"),
    # path("admin/", admin.site.urls),
    # path('home/', views.home.as_view(),name="home"),
    # path('signup/', views.signup,name="signup"),
    # path('login/', views.login,name="login"),
    # path('logout/', views.logout_view.as_view(),name="logout"),
    # #Returns a boolean if the user is logged or not
    # path('is_logged', views.is_logged_view, name="is_logged" )
    # path("home/", v    # path("app/", include("apps.usuarios.urls")),
    # iews.home, name="home page"),
]
