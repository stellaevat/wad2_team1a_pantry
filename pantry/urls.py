
urlpatterns = [
    path('home/', views.home, name='home'),
    path('auth/', views.check_email, name='check_email'),
    path('auth/sign_up/', views.register, name='register'),
    path('auth/sign_in/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
    path('recipe/<slug:recipe_name_slug>/', views.show_recipe, name="show_recipe"),
    path('category/<slug:category_title_slug>/', views.show_category, name="show_category"),
    path('search_by_ingredient/', views.search_by_ingredient, name="search_by_ingredient",
    path('search_by_keyword/results/', views.keyword_search_results, name="keyword_search_results"),
    path('add_recipe/', views.add_recipe, name="add_recipe"),
]
