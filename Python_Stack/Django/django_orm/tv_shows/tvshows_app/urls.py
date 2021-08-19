from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('shows/new', views.new_show),
    path('shows/create', views.add_show),
    path('shows/<int:show_id>/', views.show),
    path('shows', views.all_shows),
    path('shows/<int:show_id>/edit', views.edit_show),
    path('shows/<int:show_id>/update', views.update_show),
    path('shows/<int:show_id>/destroy', views.delete_show),
	]