from django.urls import path

from challenges.views.level_1.a_create_book import create_book_handler
from challenges.views.level_1.b_book_details import book_details_handler
from challenges.views.level_1.c_delete_book import delete_book_handler
from challenges.views.level_1.d_update_book import update_book_handler

urlpatterns = [
    path('book/create/', create_book_handler),
    path('book/<int:book_id>/', book_details_handler),
    path('book/<int:book_id>/delete/', delete_book_handler),
    path('book/<int:book_id>/update/', update_book_handler),
]
