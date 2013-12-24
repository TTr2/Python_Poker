#///////////////////////////////////////////////////////////////////////////////
#// useful MODULE
#//
#// useful.card_2_png_conv FUNC - generate a cardname.png string to represent a card from
#// thisHand list,for reading by drawDeal. Input=[2,Hearts] Output='2Hearts.png'
#//
#// useful.png_2_card_conv FUNC - generate the original card string to represent original
#// cards in thisHand list,for onYourBacks. Input='2Hearts.png' Output=[2,Hearts]
#//
#// useful.card_2_drawid_Conv FUNC - generate 'card1', 'card2' etc from the original card 
#// string, using index in cardString for whwCards[0].  Input=[2,Hearts] Output=Card1
#//
#// useful.drawid_2_card_conv FUNC - generate card from drawID using index from cardString
#// Input= Card1 Output= [2,Hearts] 
#//
#// useful.chk_3_com_suited FUNC - check community cards for >=3 same suited cards.
#// Run after newHand to advise whether to search for flushes.
#// Generates CpFlush val, either ['Suit', N] or [False, 0]
#//
#// useful.nested_count FUNC - count a nested list of cards e.g. [6, 'Hearts']
#// for number of cards equal to c.  Input = thisHandp,c. Output = int
#///////////////////////////////////////////////////////////////////////////////

import sys
sys.path.append("C:\\Users\\Tim\Desktop\\Python\\Projects\\Poker\\Poker_Work\\MyPy")
#from phases import phases
import cfg
#import useful


class useful:


    def card_2_png_conv(self,card):
        return str(str(card[0])+str(card[1])+'.png')

    def png_2_card_conv(self,png):
        return cfg.newDeck[cfg.cardString.index(png)]

    def card_2_drawid_conv(self,card):
        return 'card'+str(cfg.cardString.index(str(useful.card_2_png_conv(useful,card))))

    def drawid_2_card_conv(self,drawID):
        return useful.png_2_card_conv(useful,cfg.cardString[int(drawID.lstrip('card'))])

    def chk_3_com_suited(self,newDeck):
#        global CpFlush
        self.foo = [cfg.newDeck[c][1] for c in range(16,21)]
        if self.foo.count('Clubs') > 2 :
            cfg.CpFlush = ['Clubs', self.foo.count('Clubs')]
        elif self.foo.count('Diamonds') > 2:
            cfg.CpFlush = ['Diamonds', self.foo.count('Diamonds')]
        elif self.foo.count('Hearts') > 2:
            cfg.CpFlush = ['Hearts', self.foo.count('Hearts')]
        elif self.foo.count('Spades') > 2:
            cfg.CpFlush = ['Spades', self.foo.count('Spades')] 
        else:
            cfg.CpFlush=[False,0]

    def nested_count(self,thisHandp,c):
        self.strip = [thisHandp[n][0] for n in range(len(thisHandp))]
        return self.strip.count(c[0])
