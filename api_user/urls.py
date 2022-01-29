from django.urls import path
from . import views

urlpatterns = [
    path('ing/', views.IngredientView.as_view()),
    path('ing/<int:ing_id>/', views.IngredientView.as_view()),
    path('san/', views.SandwichView.as_view()),
    path('san/<int:page>/', views.SandwichView.as_view()),
    path('san/id/<int:san_id>/', views.SandwichView.as_view()),
    path('san/kw/<int:san_kw>/', views.SandwichView.as_view()),
    path('san/up/<int:san_upper>/', views.SandwichView.as_view()),
    path('san/lo/<int:san_lower>/', views.SandwichView.as_view()),
    path('san/<int:page>/kw/<int:san_kw>/', views.SandwichView.as_view()),
    path('san/<int:page>/up/<int:san_upper>/', views.SandwichView.as_view()),
    path('san/<int:page>/lo/<int:san_lower>/', views.SandwichView.as_view()),
    path('san/bt/<int:san_upper>/<int:san_lower>/', views.SandwichView.as_view()),
    path('san/kw/<int:san_kw>/up/<int:san_upper>/', views.SandwichView.as_view()),
    path('san/kw/<int:san_kw>/lo/<int:san_lower>/', views.SandwichView.as_view()),
    path('san/kw/<int:san_kw>/bt/<int:san_upper>/<int:san_lower>/', views.SandwichView.as_view()),
    path('san/<int:page>/bt/<int:san_upper>/<int:san_lower>/', views.SandwichView.as_view()),
    path('san/<int:page>/kw/<int:san_kw>/up/<int:san_upper>/', views.SandwichView.as_view()),
    path('san/<int:page>/kw/<int:san_kw>/lo/<int:san_lower>/', views.SandwichView.as_view()),
    path('san/<int:page>/kw/<int:san_kw>/bt/<int:san_upper>/<int:san_lower>/', views.SandwichView.as_view()),
]