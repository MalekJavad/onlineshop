from django.urls import path

from . import views
from .views import test_translation_message_view

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('comment/create/<int:product_id>', views.CommentCreateView.as_view(), name='comment_create'),
    path('hello', test_translation_message_view),
]