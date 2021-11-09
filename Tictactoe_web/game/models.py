from django.db import models
from . import tictactoe as ttt

class Game(models.Model):
    board = models.CharField(max_length=9, blank=True)
    move =  models.IntegerField(null=True, blank=False, help_text='Enter field documentation')

    def get_absolute_url(self):
        print("self.pk", self.pk)
        return reverse('game:game_detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        human_turn, self.board= initialize()
        game_result = None

        while True:
            if game_result != None:
                break
            else:
                if human_turn = True:
                    game_result, filled_cell_player = play_in_django(human_turn, self.move)

                else:
                    game_result, filled_cell_player = play_in_django(False, None)
        return game_result

    def __str__(self):
        return self.board
