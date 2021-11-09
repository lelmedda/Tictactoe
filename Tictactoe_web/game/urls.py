
from django.urls import path
from game.views import GameCreateView, GameDetailView

app_name = 'game'
urlpatterns = [
    #path('', views.game, name='game'),

#    path('', views.startpage, name='startpage'),
#    path('detailpage/', views.detailpage, name='detailpage')
    #path('<int:pk>/detailpage', views.detailpage, name='detailpage')

    path('game_create/', GameCreateView.as_view(), name='game_create' ),
    path('<int:pk>/game_detail/$', GameDetailView.as_view(), name='game_detail'),
]
