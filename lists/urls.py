from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import (home_page,
                   show_all_todo_item,create_todo_item,
                    show_items_for_a_user,
                    add_items_for_an_existing_user,
                   register_users,profile,
                    start_page)
urlpatterns = [
    path('start/', start_page, name = 'start_page'),
    path('todo/', home_page, name = 'home_page'),
    path('todo/showall/', show_all_todo_item),
    path('todo/<int:id>/', show_items_for_a_user),
    path('todo/<int:user_id>/additem/', add_items_for_an_existing_user),
    path('todo/newtodoitem/', create_todo_item),
    path('register/', register_users, name='register' ),
    path('profile/', profile, name='profile' ),
    path('login/',
        auth_views.LoginView.as_view(template_name ='authsystem/login.html'),
         name='login' ),
     path('logout/',
         auth_views.LogoutView.as_view(template_name='authsystem/logout.html'),
         name='logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
