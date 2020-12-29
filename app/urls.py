from django.urls import path

# from app.views import todo_list, todo_detail_change_and_delete, TodoListAndCreate
from app.views import TodoListAndCreate,TodoDetailChangeAndDelete   

urlpatterns = [
    # path('', todo_list),
    # path('<int:pk>/', todo_detail_change_and_delete),
    path('', TodoListAndCreate.as_view()),
    path('<int:pk>/', TodoDetailChangeAndDelete.as_view())
]