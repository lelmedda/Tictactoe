from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django import urls
from django.urls import reverse
from django.http import HttpResponse
from .models import Game

'''
def startpage(request):
    context = {'move':move}
    return render(request, 'game/game_create.html', context)

def detailpage(request):
    return render(request, 'game/game_detail.html')

def index(request):
    return render(request,'game/game_create.html', locals())

def play(request):
    return render(request, 'game/game_detail.html', locals())

'''
'''
class GameCreateView(CreateView):
    model = Game
    template_name = 'game/game_create.html'
    fields = ['board', 'move']

    def get_success_url(self, **kwargs):
        # redirecting to the url from reverse??
        return reverse('game:game_detail', kwargs={'pk' : self.object.pk}) #object

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(GameCreateView, self).get_form_kwargs(*args, **kwargs)
        return kwargs

class GameDetailView(DetailView):
    model = Game
    fields = ['board', 'move']
    template_name = 'game/game_detail.html'
    move = Game.objects.get('pk')
    context = {
        'game': game
    }
    return render(request,'game/game_detail.html', context)
