from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from blog.models import Article
from mysite.forms import UserCreationForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
    objs = Article.objects.all()[:2]
    context = {
        'title': 'MySite',
        'articles': objs,
    }
    return render(request, 'list_gakuchika.html', context)

class Login(LoginView):
    template_name = 'mysite/auth.html'

    def form_valid(self, form):
        #messages.success(self.request, "ok")
        return super().form_valid(form)

    def form_invalid(self, form):
        #messages.error(self.request, "ERROR OCURRED")
        return super().form_invalid(form)


def signup(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            #messages.success(request, "register done")
            return redirect('/')
    
    return render(request, 'mysite/auth.html', context)



# redirect to users' individual pages after login
def login_redirect(request):
    return HttpResponseRedirect(reverse('home'))


# user's main page
@login_required
def home(request):
    return render(request, 'mysite/home.html')