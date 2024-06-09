from django.urls import path
from Webapp import views

urlpatterns = [
    path('', views.home_page, name="home"),
    path('About/', views.about_page, name="About"),
    path('Contact/', views.contact_page, name="Contact"),
    path('Blog/', views.blog_page, name="Blog"),
    path('Shop/', views.shop_page, name="Shop"),
    path('Feedback/', views.feedback_page, name="Feedback"),
    path('Each_Products/<cat_name>', views.Product_filteredpage, name="Each_Products"),
    path('single_product/<int:p_id>', views.single_product, name="single_product"),
    path('user_register/', views.user_register, name="user_register"),
    path('user_save_register/', views.user_save_register, name="user_save_register"),
    path('User_Login/', views.User_Login, name="User_Login"),
    path('User_logout/', views.User_logout, name="User_logout"),
    path('cart/', views.cart_page, name="cart"),
    path('cart_save/', views.cart_save, name="cart_save"),
    path('user_login_page/', views.user_login_page, name="user_login_page"),
    path('delete_cart_page/<int:c_id>/', views.delete_cart_page, name="delete_cart_page"),
]