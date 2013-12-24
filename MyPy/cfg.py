#//////////////////////////////////////////////////////////////////////////////
#// cfg MODULE
#// Stores global variables between modules
#//////////////////////////////////////////////////////////////////////////////
import sys
sys.path.append("C:\\Users\\Tim\\Desktop\\Python\\Projects\\Poker\\Poker_Work\\MyPy")
from GFX import GFX
import pyglet
pyglet.resource.path = ['C:\\Users\Tim\Desktop\Python\Projects\Poker\Poker_Work\Assets']
pyglet.resource.reindex()


poker_window = pyglet.window.Window(1024,576)
@poker_window.event()
def on_draw():
    poker_window.clear()
    baize = pyglet.resource.image('redbaize.jpg')
    baize.blit(0,0)
    GFX.draw_cards(GFX)
    GFX.draw_text(GFX)
#    exit()
#    return

poker_window.push_handlers()

#pyglet.clock.schedule_interval(1/120.0)

thisHand = []
whwHands = []
whwCards = []
CpFlush = []
cardString = []
handString = []
newDeck = []
community = []
theBigReveal = []
card0 = pyglet.resource.image('b2fv.png')
card1 = pyglet.resource.image('b2fv.png')
card2 = pyglet.resource.image('b2fv.png')
card3 = pyglet.resource.image('b2fv.png')
card4 = pyglet.resource.image('b2fv.png')
card5 = pyglet.resource.image('b2fv.png')
card6 = pyglet.resource.image('b2fv.png')
card7 = pyglet.resource.image('b2fv.png')
card8 = pyglet.resource.image('b2fv.png')
card9 = pyglet.resource.image('b2fv.png')
card10 = pyglet.resource.image('b2fv.png')
card11 = pyglet.resource.image('b2fv.png')
card12 = pyglet.resource.image('b2fv.png')
card13 = pyglet.resource.image('b2fv.png')
card14 = pyglet.resource.image('b2fv.png')
card15 = pyglet.resource.image('b2fv.png')
card16 = pyglet.resource.image('b2fv.png')
card17 = pyglet.resource.image('b2fv.png')
card18 = pyglet.resource.image('b2fv.png')
card19 = pyglet.resource.image('b2fv.png')
card20 = pyglet.resource.image('b2fv.png')
main_batch = pyglet.graphics.Batch()
label_message = 'Temporary holding pattern message...'
label = pyglet.text.Label(label_message,
                          font_name='Myriad Pro Cond',
                          font_size=24,
                          x=512, y=22,
                          anchor_x='center', anchor_y='center',
                          batch=main_batch)
do_it_do_it_now = False