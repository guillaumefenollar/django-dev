from django.shortcuts import render, redirect
from django.forms import ModelForm
from shorturls.config import *
from django.http import *
from shorturls.models import URL
import random
import string


class URLForm(ModelForm):
    class Meta:
        model = URL
        fields = ['path']


def generate_key(key_nb):
    char = string.ascii_letters + string.digits
    key = [random.choice(char) for _ in range(key_nb)]
    return ''.join(key)


def home(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            path = form.cleaned_data['path']
            while True:
                key = generate_key(KEY_LENGTH)
                if not URL.objects.filter(key=key): break

            newurl = URL()
            newurl.path = path
            newurl.key = key
            newurl.save()

            fullkey = ADDRESS + key
            added = True
    else:
        # Show the form code
        form = URLForm()

    return render(request, 'home.html', locals())


def redir(request, key):
    if request.method == 'GET':
        try:
            res = URL.objects.get(key=key)
            res.increment()
            return redirect(res.path)
        except URL.DoesNotExist:
            doesnt_exist = True
            form = URLForm()
            return render(request, 'home.html', locals())
