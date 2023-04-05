from django.urls import path
from . import views

urlpatterns = [
    path('activate/<email_token>/', views.activate, name='activate'),
    path('', views.index, name='home'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register_view, name='register_view'),
    path('addblog/', views.add_blog, name='add_blog'),
    path('logout/', views.logout, name='logout'),
    path('blog-detail/<slug>', views.blog_detail, name="blog_detail"),
    path('see-blog/', views.see_blog, name="see_blog"),
    path('blog-delete/<id>', views.blog_delete, name="blog_delete"),
    path('blog-update/<slug>/', views.blog_update, name="blog_update"),
]
