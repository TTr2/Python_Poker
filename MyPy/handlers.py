import sys
sys.path.append("C:\\Users\\Tim\\Desktop\\Python\\Projects\\Poker\\Poker_Work\\MyPy")
import pyglet
import random
from handTypes import handTypes
from useful import useful
from GFX import GFX
import cfg


#///////////////////////////////////////////////////////////////////////////////
#// handlers CLASS
#/////////////////////////////////////////////////////////////////////////////// 
class handlers:

#///////////////////////////////////////////////////////////////////////////////
#// playout handler
#// Calls newHand,preFlop,flop,turn,river,onYourBacks
#/////////////////////////////////////////////////////////////////////////////// 
    def playout(self):
        phases.new_hand(phases,cfg.newDeck)
        phases.pre_flop(phases)
        phases.flop(phases)
        phases.turn(phases)
        phases.river(phases)
        phases.on_your_backs(phases,cfg.whwHands,cfg.whwCards)
        pyglet.app.run()

#/////////////////////////////////////////////////////////////////////////////// 
#// handlers.handCalc(cards) MODULE
#// thisHandp = thisHand[p] = [[9, 'Clubs'], [14, 'Spades'], [3, 'Clubs'],
#// [2, 'Hearts'], [13, 'Diamonds'], [7, 'Clubs'], [3, 'Hearts']]
#// Called individually per player by phases module.
#// Calls hand type functions in handTypes module.
#/////////////////////////////////////////////////////////////////////////////// 

    def hand_calc(self,thisHandp,p):
        thisHandp.sort(reverse=True)
        handTypes.high_card(handTypes,thisHandp,p)
        if len(thisHandp) >= 5: 
            handTypes.two_of_a_kind(handTypes,thisHandp,p)
            handTypes.two_pairs(handTypes,thisHandp,p)
            handTypes.three_of_a_kind(handTypes,thisHandp,p)
            handTypes.straight(handTypes,thisHandp,p)
            if cfg.CpFlush[1] >=3:  
                handTypes.flush(handTypes,thisHandp,p)
            handTypes.full_house(handTypes,thisHandp,p)
            handTypes.four_of_a_kind(handTypes,thisHandp,p)
            if cfg.CpFlush[1] >=3:  
                handTypes.str_flush(handTypes,thisHandp,p)
                handTypes.royal_flush(handTypes,thisHandp,p)

#///////////////////////////////////////////////////////////////////////////////
#// phases CLASS
#// new_hand,pre_flop,flop,turn,river,on_your_backs
#/////////////////////////////////////////////////////////////////////////////// 

class phases:

#////////////////////////////////////////////////////////////////////////////////
#// newHand() FUNCTION
#// shuffles the deck (cfg.newDeck list) and deals to 8 players plus 5 secret
#// community cards.
#// thisHand (per player per phase) = [[[14, 'Diamonds'], [9, 'Diamonds']],etc]
#// cardString (from cfg.newDeck) = ['11Clubs.png', '7Clubs.png', '9Spades.png', '2Diamonds.png','11Hearts.png', '10Spades.png', '2Clubs.png', '6Hearts.png','5Hearts.png', '13Diamonds.png', '3Spades.png', '3Clubs.png','4Diamonds.png', '9Diamonds.png', '14Diamonds.png', '10Diamonds.png','6Clubs.png', '8Hearts.png', '8Clubs.png', '3Hearts.png','8Diamonds.png']
#///////////////////////////////////////////////////////////////////////////////
    def new_hand(self,newDeck):

        cfg.thisHand,handStr = [], []
        cfg.whwHands = [[]]*8
        cfg.whwCards = [[]]*8
        cfg.theBigReveal = []

        random.shuffle(cfg.newDeck)
                    
        # Generate 8x player thisHand list.
        cfg.thisHand = [[cfg.newDeck[q]] + [cfg.newDeck[q+8]] for q in range(0,8)]

        cfg.community = [cfg.newDeck[16], cfg.newDeck[17], cfg.newDeck[18], cfg.newDeck[19], cfg.newDeck[20]]
        cfg.thisHand.append(cfg.community)
        self.communityStr = [useful.card_2_png_conv(self,cfg.newDeck[c]) for c in range(16,21)]
 
        # Generate a list of cardname.jpeg strings to represent thisHand list,
        # for reading by drawDeal, using cardStrings() func.
        # e.g cardString = ['7Clubs.png', '2Hearts.png', '5Hearts.png',etc] 
        cfg.cardString = [useful.card_2_png_conv(self,cfg.newDeck[c]) for c in range(0,21)]
        print('newDeck =',cfg.newDeck[0:21])
        print('cardString =',cfg.cardString)


        cfg.card0 = pyglet.resource.image(str(cfg.cardString[0]))
        cfg.card1 = pyglet.resource.image(str(cfg.cardString[1]))
        cfg.card2 = pyglet.resource.image(str(cfg.cardString[2]))
        cfg.card3 = pyglet.resource.image(str(cfg.cardString[3]))
        cfg.card4 = pyglet.resource.image(str(cfg.cardString[4]))
        cfg.card5 = pyglet.resource.image(str(cfg.cardString[5]))
        cfg.card6 = pyglet.resource.image(str(cfg.cardString[6]))
        cfg.card7 = pyglet.resource.image(str(cfg.cardString[7]))

        cfg.card8 = pyglet.resource.image(str(cfg.cardString[8]))
        cfg.card9 = pyglet.resource.image(str(cfg.cardString[9]))
        cfg.card10 = pyglet.resource.image(str(cfg.cardString[10]))
        cfg.card11 = pyglet.resource.image(str(cfg.cardString[11]))
        cfg.card12 = pyglet.resource.image(str(cfg.cardString[12]))
        cfg.card13 = pyglet.resource.image(str(cfg.cardString[13]))
        cfg.card14 = pyglet.resource.image(str(cfg.cardString[14]))
        cfg.card15 = pyglet.resource.image(str(cfg.cardString[15]))

        cfg.card16 = pyglet.resource.image('b2fv.png')
        cfg.card17 = pyglet.resource.image('b2fv.png')
        cfg.card18 = pyglet.resource.image('b2fv.png')
        cfg.card19 = pyglet.resource.image('b2fv.png')
        cfg.card20 = pyglet.resource.image('b2fv.png')

        cfg.label_message = 'Shuffling the deck...'
#        cfg.label = pyglet.text.Label('Shuffling the deck...',
#                              font_name='Myriad Pro Cond',
#                              font_size=24,
#                              x=512, y=22,
#                              anchor_x='center', anchor_y='center',
#                              batch=main_batch)
        """ Run chk_3_com_suited only once at newDeck phase """ 
        useful.chk_3_com_suited(useful,cfg.newDeck)

#////////////////////////////////////////////////////////////////////////////////
#// preflop() FUNCTION
#// Draws each players hand.
#// Runs handCalc on hole cards.
#///////////////////////////////////////////////////////////////////////////////
    def pre_flop(self):
        for p in range(0,8):
            handlers.hand_calc(handlers,cfg.thisHand[p],p)

#////////////////////////////////////////////////////////////////////////////////
#// flop() FUNCTION
#// Appends the three community cards to each player's thisHand list
#// Assigns a cardID to the three community cards.
#// Draws the three community cards.
#// Runs handCalc on players cards.
#// Called by playout func in main body.
#// Calls handCalc in handlers.py 
#///////////////////////////////////////////////////////////////////////////////
    def flop(self):
        for p in range(0,8):
            cfg.thisHand[p].extend(cfg.community[0:3])
        cfg.card16 = pyglet.resource.image(str(cfg.cardString[16]))
        cfg.card17 = pyglet.resource.image(str(cfg.cardString[17]))
        cfg.card18 = pyglet.resource.image(str(cfg.cardString[18]))
        for p in range(0,8):
            handlers.hand_calc(handlers,cfg.thisHand[p],p)
        cfg.label_message = 'Now for the flop...'
#        cfg.label = pyglet.text.Label('Now for the flop...',
#                              font_name='Myriad Pro Cond',
#                              font_size=24,
#                              x=512, y=22,
#                              anchor_x='center', anchor_y='center',
#                              batch=phases.main_batch)

#////////////////////////////////////////////////////////////////////////////////
#// turn() FUNCTION
#// Appends the turn card to each player's thisHand list
#// Assigns a cardID to the turn card.
#// Draws the turn card.
#// Runs handCalc on players cards.
#///////////////////////////////////////////////////////////////////////////////
    def turn(self):
        for p in range(0,8):
            cfg.thisHand[p].append(cfg.community[3])
        cfg.card19 = pyglet.resource.image(str(cfg.cardString[19]))
        for p in range(0,8):
            handlers.hand_calc(handlers,cfg.thisHand[p],p)
        cfg.label_message = 'Now for the Turn card...'
#        cfg.label = pyglet.text.Label('Now for the Turn card...',
#                              font_name='Myriad Pro Cond',
#                              font_size=24,
#                              x=512, y=22,
#                              anchor_x='center', anchor_y='center')

#////////////////////////////////////////////////////////////////////////////////
#// river() FUNCTION
#// Appends the river card to each player's thisHand list
#// Assigns a cardID to the river card.
#// Draws the river card.
#// Runs handCalc on players cards.
#///////////////////////////////////////////////////////////////////////////////
    def river(self):
        for p in range(0,8):
            cfg.thisHand[p].append(cfg.community[4])
        cfg.card20 = pyglet.resource.image(str(cfg.cardString[20]))
        for p in range(0,8):
            handlers.hand_calc(handlers,cfg.thisHand[p],p)
        cfg.label_message = 'Now for the River card...'
#        cfg.label = pyglet.text.Label('Now for the River card...',
#                              font_name='Myriad Pro Cond',
#                              font_size=24,
#                              x=512, y=22,
#                              anchor_x='center', anchor_y='center')

#///////////////////////////////////////////////////////////////////////////////
#// on_your_backs FUNC
#// input = whwHands,whwCards
#// topHand = index of highest whwHands
#///////////////////////////////////////////////////////////////////////////////
    def on_your_backs(self,whwHands,whwCards):
        # Identify highest int in whwHands list.
        print('cfg.whwHands',cfg.whwHands)
        self.topHand = max(cfg.whwHands)
        self.whwCardStrings = []
        self.strippedwhwCS = []
        self.theBigReveal_IDs = []
        # Gen list of P indexes, if P's whwHand == topHand on the deck 
        self.playersWithTopHand = [n for n in range(8) if cfg.whwHands[n] 
                                                         == self.topHand]
        print('playersWithTopHand', self.playersWithTopHand)

        # Convert whwCard list of ids in to cards for P's with topHand
        for i in self.playersWithTopHand:
            self.foo = []
            self.bar = []
            for c in cfg.whwCards[i]:
                self.foo = useful.drawid_2_card_conv(useful,c)
                self.bar += [self.foo]
            self.whwCardStrings += [self.bar]
        print('whwCardStringsALL =',self.whwCardStrings)

        # Gen a list of whwCardStrings stripped of suit
        for w in self.whwCardStrings:
            fooA = []
            for x in w:
                fooA += [x[0]]
            self.strippedwhwCS += [fooA]
        print('strwhwCS =',self.strippedwhwCS)

        # Identify 'best of the best' hand from P's with topHand and 
        # check for duplicate top 5 cards (for split pot).  
        self.botb = max(self.strippedwhwCS)
        print('botb =',self.botb)
        self.winners = [self.playersWithTopHand[w]
                        for w in range (len(self.playersWithTopHand))
                        if self.strippedwhwCS[w] == self.botb]

        self.HandTypeStrings = ['a High Card',
                                'Two of a Kind',
                                'Two Pairs',
                                'Three of a Kind',
                                'a Straight',
                                'a Flush',
                                'a Full House',
                                'Four of a Kind',
                                'a Straight Flush',
                                'a Royal Flush']
        if len(self.winners) == 1:
            for y in cfg.whwCards[self.winners[0]]:
                self.barB = useful.card_2_png_conv(useful,useful.drawid_2_card_conv(useful,y))
                cfg.theBigReveal += [self.barB]
                self.theBigReveal_IDs += ['cfg.'+ y]

            self.label = ('Take down! Player '
                          + str(int(self.winners[0]) + 1) 
                          + ' is the Winner, with ' 
                          + str(self.HandTypeStrings[self.topHand]))
            print(self.label)
            cfg.label_message = self.label
#            cfg.label = pyglet.text.Label(self.label,
#                                          font_name='Myriad Pro Cond',
#                                          font_size=24,
#                                          x=512, y=22,
#                                          anchor_x='center', anchor_y='center')
        else:
            self.winnersUp = []
            for x in self.winners:
                self.winnersUp += [int(x)+1]
#                self.fooB = []
                for y in cfg.whwCards[x]:
                    self.fooB = useful.card_2_png_conv(useful,useful.drawid_2_card_conv(useful,y))
                    cfg.theBigReveal += [self.fooB]
                    if y not in self.theBigReveal_IDs:
                        self.theBigReveal_IDs += ['cfg.'+ y]
            self.label = ('Split Pot! Players '
                         + str(self.winnersUp)
                         + ' are the Winners, with '
                         + str(self.HandTypeStrings[self.topHand]))
            print(self.label)
            cfg.label_message = self.label
#            cfg.label = pyglet.text.Label(self.label,
#                                      font_name='Myriad Pro Cond',
#                                      font_size=24,
#                                      x=512, y=22,
#                                      anchor_x='center', anchor_y='center')
        print(cfg.theBigReveal)
        
        if 'cfg.card0' not in self.theBigReveal_IDs:
            cfg.card0 = pyglet.resource.image('b2fv.png')
        if 'cfg.card1' not in self.theBigReveal_IDs:
            cfg.card1 = pyglet.resource.image('b2fv.png')
        if 'cfg.card2' not in self.theBigReveal_IDs:
            cfg.card2 = pyglet.resource.image('b2fv.png')
        if 'cfg.card3' not in self.theBigReveal_IDs:        
            cfg.card3 = pyglet.resource.image('b2fv.png')
        if 'cfg.card4' not in self.theBigReveal_IDs:        
            cfg.card4 = pyglet.resource.image('b2fv.png')
        if 'cfg.card5' not in self.theBigReveal_IDs:        
            cfg.card5 = pyglet.resource.image('b2fv.png')
        if 'cfg.card6' not in self.theBigReveal_IDs:        
            cfg.card6 = pyglet.resource.image('b2fv.png')
        if 'cfg.card7' not in self.theBigReveal_IDs:        
            cfg.card7 = pyglet.resource.image('b2fv.png')
           
        if 'cfg.card8' not in self.theBigReveal_IDs:        
            cfg.card8 = pyglet.resource.image('b2fv.png')
        if 'cfg.card9' not in self.theBigReveal_IDs:        
            cfg.card9 = pyglet.resource.image('b2fv.png')
        if 'cfg.card10' not in self.theBigReveal_IDs:        
            cfg.card10 = pyglet.resource.image('b2fv.png')
        if 'cfg.card11' not in self.theBigReveal_IDs:        
            cfg.card11 = pyglet.resource.image('b2fv.png')
        if 'cfg.card12' not in self.theBigReveal_IDs:        
            cfg.card12 = pyglet.resource.image('b2fv.png')
        if 'cfg.card13' not in self.theBigReveal_IDs:        
            cfg.card13 = pyglet.resource.image('b2fv.png')
        if 'cfg.card14' not in self.theBigReveal_IDs:        
            cfg.card14 = pyglet.resource.image('b2fv.png')
        if 'cfg.card15' not in self.theBigReveal_IDs:        
            cfg.card15 = pyglet.resource.image('b2fv.png')

        if 'cfg.card16' not in self.theBigReveal_IDs:        
            cfg.card16 = pyglet.resource.image('b2fv.png')
        if 'cfg.card17' not in self.theBigReveal_IDs:        
            cfg.card17 = pyglet.resource.image('b2fv.png')
        if 'cfg.card18' not in self.theBigReveal_IDs:        
            cfg.card18 = pyglet.resource.image('b2fv.png')
        if 'cfg.card19' not in self.theBigReveal_IDs:        
            cfg.card19 = pyglet.resource.image('b2fv.png')
        if 'cfg.card20' not in self.theBigReveal_IDs:        
            cfg.card20 = pyglet.resource.image('b2fv.png')
        
#//////////////////////////////////////////////////////////////////////////////
