from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView
from django.conf import settings
from pantry import views

app_name = 'pantry'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('auth/', views.check_email, name='check_email'),
    path('auth/sign_up/', views.sign_up, name='sign_up'),
    path('auth/sign_in/', views.sign_in, name='sign_in'),
    path('sign_out/', views.sign_out, name='sign_out'),
    path('user/<str:username>/', views.user_profile, name="user_profile"),
    path('user/<str:username>/edit_profile/', views.edit_profile, name="edit_profile"),
    path('user/<str:username>/my_recipes/', views.show_my_recipes, name="my_recipes"),
    path('user/<str:username>/my_recipes/<slug:sort>', views.show_my_recipes, name="my_recipes"),
    path('user/<str:username>/starred_recipes/', views.show_starred_recipes, name="starred_recipes"),
    path('user/<str:username>/starred_recipes/<slug:sort>', views.show_starred_recipes, name="starred_recipes"),
    
    path('recipe/<slug:recipe_name_slug>/', views.show_recipe, name="show_recipe"),
    path('category/<slug:category_title_slug>/', views.show_category, name="show_category"),
    path('category/<slug:category_title_slug>/<slug:sort>', views.show_category, name="show_category"),
    path('search_by_ingredient/', views.search_by_ingredient, name="search_by_ingredient"),
    path('search_by_ingredient/results/', views.search_by_ingredient_results, name="search_by_ingredient_results"),
    path('search_by_ingredient/results/<slug:sort>', views.search_by_ingredient_results, name="search_by_ingredient_results"),
    path('search_results/', views.search_results, name="search_results"),
    path('search_results/<slug:sort>', views.search_results, name="search_results"),
    path('add_recipe/ingredients', views.add_recipe_ingredients, name="add_recipe_ingredients"),
    path('add_recipe/method', views.add_recipe_method, name="add_recipe_method"),

    
    path('favicon.ico/', RedirectView.as_view(url=staticfiles_storage.url("img/favicon.ico"))),
]
