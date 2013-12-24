#///////////////////////////////////////////////////////////////////////////////
#// GFX MODULE
#// draw_cards(), draw_text(), on_draw()
#/////////////////////////////////////////////////////////////////////////////// 
import sys
sys.path.append("C:\\Users\\Tim\Desktop\\Python\\Projects\\Poker\\Poker_Work\\MyPy")
import cfg
import pyglet
pyglet.resource.path = ['C:\\Users\Tim\Desktop\Python\Projects\Poker\Poker_Work\Assets']
pyglet.resource.reindex()

class GFX:

    self.card0 = pyglet.sprite.Sprite(img=cfg.card0, 
                                   x=40, y=450,
                                   batch=main_batch)

    def draw_cards(self):
        cfg.card0.blit(40,450)

        cfg.card1.blit(294,450)
        cfg.card2.blit(570,450)
        cfg.card3.blit(826,450)
        cfg.card4.blit(40,70)
        cfg.card5.blit(294,70)
        cfg.card6.blit(570,70)
        cfg.card7.blit(826,70)

        cfg.card8.blit(132,450)
        cfg.card9.blit(386,450)
        cfg.card10.blit(662,450)
        cfg.card11.blit(918,450)
        cfg.card12.blit(132,70)
        cfg.card13.blit(386,70)
        cfg.card14.blit(662,70)
        cfg.card15.blit(918,70)

        cfg.card16.blit(294,256)
        cfg.card17.blit(386,256)
        cfg.card18.blit(478,256)
        cfg.card19.blit(570,256)
        cfg.card20.blit(662,256)
            
    def draw_text(self):
        self.player1 = pyglet.text.Label('Player 1',
                              font_name='Myriad Pro Cond',
                              font_size=24,
                              x=122, y=426,
                              anchor_x='center', anchor_y='center',
                              batch = cfg.main_batch)

        self.player2 = pyglet.text.Label('Player 2',
                              font_name='Myriad Pro Cond',
                              font_size=24,
                              x=376, y=426,
                              anchor_x='center', anchor_y='center',
                              batch = cfg.main_batch)

        self.player3 = pyglet.text.Label('Player 3',
                              font_name='Myriad Pro Cond',
                              font_size=24,
                              x=652, y=426,
                              anchor_x='center', anchor_y='center',
                              batch = cfg.main_batch)

        self.player4 = pyglet.text.Label('Player 4',
                              font_name='Myriad Pro Cond',
                              font_size=24,
                              x=908, y=426,
                              anchor_x='center', anchor_y='center',
                              batch = cfg.main_batch)

        self.player5 = pyglet.text.Label('Player 5',
                              font_name='Myriad Pro Cond',
                              font_size=24,
                              x=122, y=196,
                              anchor_x='center', anchor_y='center',
                              batch = cfg.main_batch)

        self.player6 = pyglet.text.Label('Player 6',
                              font_name='Myriad Pro Cond',
                              font_size=24,
                              x=376, y=196,
                              anchor_x='center', anchor_y='center',
                              batch = cfg.main_batch)

        self.player7 = pyglet.text.Label('Player 7',
                              font_name='Myriad Pro Cond',
                              font_size=24,
                              x=652, y=196,
                              anchor_x='center', anchor_y='center',
                              batch = cfg.main_batch)

        self.player8 = pyglet.text.Label('Player 8',
                              font_name='Myriad Pro Cond',
                              font_size=24,
                              x=908, y=196,
                              anchor_x='center', anchor_y='center',
                              batch = cfg.main_batch)
        cfg.label.draw()
        self.player1.draw()
        self.player2.draw()
        self.player3.draw()
        self.player4.draw()
        self.player5.draw()
        self.player6.draw()
        self.player7.draw()
        self.player8.draw()

#    poker_window = pyglet.window.Window(fullscreen=True)
