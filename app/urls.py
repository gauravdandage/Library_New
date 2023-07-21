  
from django.urls import path
from app import views as library_views


urlpatterns = [
    path("home/", library_views.welcome_page, name="home_page"),
    path("show-books/", library_views.show_all_books, name="show_books"),
    path("show-single-books/<int:bid>/", library_views.show_single_book, name="show_single_books"),
    path("add-book/", library_views.add_single_book, name="add_single_books"),
    path("edit_book/<int:bid>/", library_views.edit_single_book, name="edit_single_books"),
    path("delete_book/<int:bid>/", library_views.delete_single_book, name="delete_single_book"),
    path("soft-delete_book/<int:bid>/", library_views.soft_delete_single_book, name="soft_delete_single_book"),
    path("form-view/", library_views.form_view, name="form_view"),


]