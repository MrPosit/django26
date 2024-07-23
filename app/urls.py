from django.urls import path
from .views import Home, SignUpView, Login, Logout, CreatePost

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('create/', CreatePost.as_view(), name='create')
]
