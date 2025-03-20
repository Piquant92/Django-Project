from django.urls  import path
from board.views import board_list, board_form, board_delete, board_edit

urlpatterns = [
    path('board/', board_list, name='board'),
    path('boardcreate/', board_form, name='boardcreate'),
    path('boarddel/<int:pk>/', board_delete, name='boarddel'),
    path('boardedit/<int:pk>/', board_edit, name='boardedit'),
]