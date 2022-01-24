from django.contrib import admin
from django.urls import path
from django.conf.urls import include
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api_user.urls'), name='api_user'), # include 함수를 통해 api_user의 urls.py로 라우팅 해준다.
]