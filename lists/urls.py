from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (home_page,
                   show_all_todo_item,create_todo_item,
                    show_items_for_a_user,
                    add_items_for_an_existing_user,
            register_users,profile,register_users_with_profilepic,
                    start_page)
from django.conf import settings
from django.conf.urls.static import static
#from .forms import CustomEmailValidationForm
urlpatterns = [
    path('', start_page, name = 'start_page'),
    path('todo/', home_page, name = 'home_page'),
    path('todo/showall/', show_all_todo_item),
    path('todo/<int:id>/', show_items_for_a_user),
    path('todo/<int:user_id>/additem/', add_items_for_an_existing_user),
    path('todo/newtodoitem/', create_todo_item),
    path('register/', register_users_with_profilepic, name='register' ),
    path('profile/', profile, name='profile'),
    path('login/',
        auth_views.LoginView.as_view(template_name ='authsystem/login.html'),
         name='login' ),
     path('logout/',
         auth_views.LogoutView.as_view(template_name='authsystem/logout.html'),
         name='logout'),

      path('password_reset/',
    auth_views.PasswordResetView.as_view(
        #form_class=CustomEmailValidationForm,
         template_name='authsystem/password_reset.html',
         ),
         name='password_reset'),
        # path('password_reset/',
        #  auth_views.PasswordResetView.as_view(template_name='authsystem/password_reset.html' ),
        #  name='password_reset'),

    # path('password_reset/',
    #      #auth_views.PasswordResetView.as_view(template_name='authsystem/password_reset.html'),
    #      custom_view,
    #      name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='authsystem/password_reset_done.html'),
         name='password_reset_done'),

    path('password_reset/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.
         as_view(template_name='authsystem/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset/complete/',
         auth_views.PasswordResetCompleteView.
         as_view(template_name='authsystem/password_reset_complete.html'),
         name='password_reset_complete'),
    path('change_password/',
         auth_views.PasswordChangeView.
         as_view(template_name='authsystem/password_change.html'),
         name='password_change'),
    path('change_password/done',
         auth_views.PasswordChangeDoneView.
         as_view(template_name='authsystem/password_change_done.html'),
         name='password_change_done')


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
