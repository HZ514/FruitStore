from django.conf.urls import url, include

from user import views


urlpatterns = [
    url(r'^register/',views.register,name='register'),
    url(r'^login/',views.login,name='login'),
    url(r'^logout/',views.logout,name='logout'),
]