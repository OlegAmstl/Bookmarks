from django.urls import path, include

from . import views


urlpatterns = [
    # path('login/', views.user_login, name='login'),
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('register/',  views.register, name='register'),

    # path('password-change/', PasswordChangeView.as_view(),
    #      name='password_change'),
    # path('password-change/done/', PasswordChangeDoneView.as_view(),
    #      name='password_change_done'),
    # path('password-reset/', PasswordResetView.as_view(),
    #      name='password_reset'),
    # path('password-reset/done/', PasswordResetDoneView.as_view(),
    #      name='password_reset_done'),
    # path('password-reset/<uid64>/<token>/',
    # PasswordResetConfirmView.as_view(),
    #      name='password_reset_confirm'),
    # path('password-reset/complete/', PasswordResetCompleteView.as_view(),
    #      name='password_reset_complete'),
]
