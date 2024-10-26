from django.urls import path
from . import views


app_name = 'quoteapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('tag/<str:tag_id>/', views.tag_detail, name='tag_detail'),
    path('tag/', views.tag, name='tag'),
    path('author/<str:author_id>/', views.author_detail, name='author_detail'),
    path('author/', views.author, name='author'),
    path('quote/', views.quote, name='quote'),
    path('edit/<int:quote_id>/', views.edit_quote, name='edit_quote'),
    path('detail/<int:quote_id>', views.detail, name='detail'),
    path('delete/<int:quote_id>', views.delete_quote, name='delete'),

]
