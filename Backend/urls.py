from django.urls import path
from Backend import views

urlpatterns = [
    path('index_page',views.index_page,name="index_page"),
    path('Categories_page/', views.Categories_page, name="Categories_page"),
    path('display_page/', views.display_page, name="display_page"),
    path('save_page/', views.save_page, name="save_page"),
    path('edit_categories/<int:cat_id>/', views.edit_categories, name="edit_categories"),
    path('update_categories/<int:cat_id>/', views.update_categories, name="update_categories"),
    path('delete_fun/<int:cat_id>/', views.delete_fun, name="delete_fun"),
    path('login_page/', views.login_page, name="login_page"),
    path('Admin_login/', views.Admin_login, name="Admin_login"),
    path('Admin_Logout/', views.Admin_Logout, name="Admin_Logout"),
    path('product_page/', views.product_page, name="product_page"),
    path('save_product/', views.save_product, name="save_product"),
    path('product_display/', views.product_display, name="product_display"),
    path('edit_products/<int:p_id>/', views.edit_products, name="edit_products"),
    path('delete_pro/<int:p_id>/', views.delete_pro, name="delete_pro"),
    path('update_products/<int:p_id>/', views.update_products, name="update_products"),

    path('contact_data/', views.contact_data, name="contact_data"),
    path('delete_feedback/<int:f_id>', views.delete_feedback, name="delete_feedback"),


]