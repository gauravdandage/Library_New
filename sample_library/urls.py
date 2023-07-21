"""
URL configuration for sample_library project.

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
from user_app import views as user_views
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #views url
    path("views-a", views.view_a, name="view_a"),
    
    # user app urls
    path('user/', include('user_app.urls')), #new

    # app urls
    path('book/', include('app.urls')), #new

]



# http://127.0.0.1:8000/admin/
# http://127.0.0.1:8000/home/
# http://127.0.0.1:8000/show-books/
# http://127.0.0.1:8000/show-single-books/1/
# http://127.0.0.1:8000/add-book/
# http://127.0.0.1:8000/edit_book/1/
# http://127.0.0.1:8000/delete_book/1/
# http://127.0.0.1:8000/soft-delete_book/<1/
# http://127.0.0.1:8000/form-view/

