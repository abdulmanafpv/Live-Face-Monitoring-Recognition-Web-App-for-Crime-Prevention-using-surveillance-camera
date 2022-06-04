from django.contrib import admin
from django.urls import path
from django.urls import include, path
from face_biometric_app import views

urlpatterns = [
    path('', views.index,name='index'),
    path('video_feed', views.video_feed,name='video_feed'),
    path('refresh', views.refresh, name='refresh'),
    path('search_result', views.search_result, name='search_result'),
    path('unregisterd', views.unregisterd, name='unregisterd'),
    path('training', views.training, name='training'),
    path('registerd_people', views.registerd_people, name='registerd_people'),
    path('unknown-search', views.unknown_search, name='unknown_search'),
    path('checking_individual', views.checking_individual, name='checking_individual'),
    path('uncheck', views.uncheck, name='uncheck'),
    path('checking_one', views.checking_one, name='checking_one'),
    path('checking_two', views.checking_two, name='checking_two'),
    path('checking_three', views.checking_three, name='checking_three'),
    path('checking_four', views.checking_four, name='checking_four'),
    path('checking_five', views.checking_five, name='checking_five'),
    path('check_search', views.check_search, name='check_search'),
    path('uncheck_one', views.uncheck_one, name='uncheck_one'),
    path('uncheck_two', views.uncheck_two, name='uncheck_two'),
    path('uncheck_three', views.uncheck_three, name='uncheck_three'),
    path('uncheck_four', views.uncheck_four, name='uncheck_four'),
    path('uncheck_five', views.uncheck_five, name='uncheck_five'),
    path('one_search', views.one_search, name='one_search'),
    path('two_search', views.two_search, name='two_search'),
    path('three_search', views.three_search, name='three_search'),
    path('four_search', views.four_search, name='four_search'),
    path('five_search', views.five_search, name='five_search'),








]