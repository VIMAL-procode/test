from .views import *
app_name='post'
urlpatterns = [
    path('',post_list,name='post_list'),
    path('<int:pk>',post_detail,name='post_detail'),
]
