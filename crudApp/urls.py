from django.urls import path
from .views import home, create_post, edit_post, delete_post, detail_post,Home, Create_post,Edit_post,Delete_post,Detail_post, Product_home,Product_create,Product_edit,Product_delete,Product_detail

urlpatterns = [
    # path('home/',home,name='home'),
    # path('create_post/',create_post,name='create_post'),
    # path('edit_post/<int:post_pk>',edit_post,name='edit_post'),
    # path('delete_post/<int:post_pk>',delete_post,name='delete_post'),
    #path('detail_post/<int:post_pk>',detail_post,name='detail_post'),

    path('home/', Home.as_view(),name='home'),
    path('create_post/', Create_post.as_view(), name='create_post'),
    path('edit_post/<int:pk>', Edit_post.as_view(),name='edit_post'),
    path('delete_post/<int:pk>',Delete_post.as_view(),name='delete_post'),
    path('detail_post/<int:pk>',Detail_post.as_view(),name='detail_post'),

    path('product_home/', Product_home.as_view(),name='product_home'),
    path('product_create/', Product_create.as_view(), name='product_create'),
    path('product_edit/<int:pk>', Product_edit.as_view(),name='product_edit'),
    path('product_delete/<int:pk>',Product_delete.as_view(),name='product_delete'),
    path('product_detail/<int:pk>',Product_detail.as_view(),name='product_detail'),

]