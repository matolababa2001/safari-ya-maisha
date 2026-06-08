from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('neno-la-mungu/', views.neno_la_mungu, name='neno'),
    path('tiba-lishe/', views.tiba_lishe, name='lishe'),
    path('siri-za-ndoa/', views.siri_za_ndoa, name='ndoa'),
    path('language/<str:lang>/', views.change_language, name='change_language'),
    path('lang/<str:lang>/', views.set_language, name='set_language'),
    path('search/', views.search, name='search'),
    path(
    'like/<int:post_id>/',
    views.like_post,
    name='like_post'
    ),

]