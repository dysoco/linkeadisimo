from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from .forms import SubmitForm, LoginForm, CommentForm
from .models import Publication


# Create your views here.
def index(request):
    publications = Publication.objects.order_by('-date')
    if request.user.is_authenticated:
        context = {
            'publications': publications,
            'authenticated': True,
            'user': request.user
        }
    else:
        context = {
            'publications': publications,
            'authenticated': False,
        }
    return render(request, 'website/index.html', context)


def publication(request, pub_id):
    pub = get_object_or_404(Publication, pk=pub_id)
    context = {
        'publication': pub,
        'form': CommentForm()
    }
    return render(request, 'website/publication.html', context)

def comment(request):



def user(request, user_id):
    return HttpResponse('user')


class Submit(View):
    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'website/submit.html', {'form': SubmitForm()})

    @method_decorator(login_required)
    def post(self, request):
        form = SubmitForm(request.POST)

        # TODO this probably should be checked in the frontend
        if not form.is_valid():
            return HttpResponseBadRequest('<p>Form was invalid</p>')

        pub = Publication(title=form.cleaned_data['title'], link=form.cleaned_data['url'],
                          text=form.cleaned_data['text'], created_by=request.user)

        pub.save()
        return HttpResponseRedirect(reverse('publication', args=(pub.id,)))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


class Login(View):
    def get(self, request):
        return render(request, 'website/login.html', {'form': LoginForm()})

    def post(self, request):
        form = LoginForm(request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest('<p>Login was invalid (server issue)</p>')

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(request, username=username, password=password)

        if user is None:
            return HttpResponseBadRequest('<p>Login invalid</p>')
        else:
            login(request, user)
            return HttpResponseRedirect('/')

        return HttpResponseBadRequest('<p>Not yet implemented</p>')

# def Register(View):
#    def get(self, request):
