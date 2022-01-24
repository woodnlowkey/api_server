from django.urls import path
from . import views
 
app_name = 'api_user'
urlpatterns = [
    path('bread/', views.BreadView.as_view()), # bread에 관한 API를 처리하는 view로 Request를 넘김
    path('bread/<int:bread_id>/', views.BreadView.as_view()), # bread pk id가 전달되는 경우
    path('topping/', views.ToppingView.as_view()),
    path('topping/<int:topping_id>/', views.ToppingView.as_view()),
    path('cheese/', views.CheeseView.as_view()),
    path('cheese/<int:cheese_id>/', views.CheeseView.as_view()),
    path('sauce/', views.SauceView.as_view()),
    path('sauce/<int:sauce_id>/', views.SauceView.as_view()),
    path('sandwich/', views.SandwichView.as_view()),
    path('sandwich/<int:page>/', views.SandwichView.as_view()),
    path('sandwich/<int:sandwich_id>/id', views.SandwichView.as_view()),
    path('sandwich/<int:page>/<str:sandwich_kw>/<int:kw_kn>/', views.SandwichView.as_view()),
]
