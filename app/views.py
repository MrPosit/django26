from django.shortcuts import redirect
from .models import Author, Post
from django.contrib.auth.views import LoginView, LogoutView
from .forms import SignUpForm, PostForm
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

class SignUpView(CreateView):
    model = Author
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    
class Login(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('home')

class Logout(LogoutView):
    next_page = reverse_lazy('login')

class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid():
            post = form.save(commit=False)
            post.author = self.request.user
            bbcode_content = self.request.POST.get('bbcode_content', '')
            post.bbcode_content = bbcode_content

            post.save()
        return redirect(self.success_url)
