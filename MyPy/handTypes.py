#///////////////////////////////////////////////////////////////////////////////
#// Version 1.0.0.2
#// handType MODULE - Contains a func for each type of hand:
#// 0 = royal_flush(), 1 = str_flush(), 2 = full_house(), 3 = four_of_a_kind(), 4 = flush()
#// 5 = straight(),   6 = three_of_a_kind(),    7 = two_pair(),   8 = two_of_a_kind(), 9 = high_card()
#// Input is always pHand == thisHand[p] and p (0-8) from phases.
#// Output is: whwCards = [card0,card1,card17,card19,card20]
#//       whsHand = [false,false,false,false,false,true,false,false,false,false]
#// Called by hand_calc function in handlers.py.
#// Uses functions in useful.py
#///////////////////////////////////////////////////////////////////////////////
import sys
sys.path.append("C:\\Users\\Tim\Desktop\\Python\\Projects\\Poker\\Poker_Work\\MyPy")
from useful import useful
import cfg

class handTypes:

#///////////////////////////////////////////////////////////////////////////////
#// royal_flush FUNCTION - Check for flush, then check for Royal Flush
#///////////////////////////////////////////////////////////////////////////////
    def royal_flush(self,thisHandp,p):
        self.foo = []
        for c in thisHandp:
            if c[1] == cfg.CpFlush[0]:
                self.foo += [c]
        # Count whether a players matching suit cards form a 5 card flush.
        if len(self.foo) >=5:
            self.foo.sort(reverse=True)
            if self.foo[0][0] == 14 and self.foo[4][0] == 10:
                cfg.whwHands[p] = 9
                cfg.whwCards[p] = [useful.card_2_cardid_conv(useful,self.foo[n]) for n in range(5)]
#                print('whwHands[p]',cfg.whwHands[p])
#                print('whwCards[p]',cfg.whwCards[p])
                    
#///////////////////////////////////////////////////////////////////////////////    
#// str_flush FUNC - Convert aces to 1 and add to list, check for Str Flushes.
#///////////////////////////////////////////////////////////////////////////////
    def str_flush(self,thisHandp,p):
        self.foo = []
        self.aceCheck = False
        for c in thisHandp:
            if c[1] == cfg.CpFlush[0]:
                self.foo += [c]
                self.aceCheck = True
        # Count whether a players matching suit cards form a 5 card flush.
        if len(self.foo) >=5:
            if self.aceCheck:
                for c in self.foo:
                    if c[0] == 14:
                        self.A1 = [1,cfg.CpFlush[0]]
                        self.A14 = [c]
                        self.foo.append(self.A1)
            self.foo.sort(reverse=True)
            for s in range(0,len(self.foo)-4):
                if self.foo[s][0]-4 == self.foo[s+4][0] and cfg.whwHands[p] != 1:
                    cfg.whwHands[p] = 1
                    if self.A1 in self.foo:
                        # Replace A1 with A14 at the end (duplicate) so that 
                        # the s range includes the ace card
                        self.foo.remove(self.A1)
                        self.foo.append(self.A14)
                    cfg.whwCards[p] = [useful.card_2_drawid_conv
                                   (useful,self.foo[s+t]) for t in range(0,5)]
#                print('whwHands[p]',cfg.whwHands[p])
#                print('whwCards[p]',cfg.whwCards[p])

#///////////////////////////////////////////////////////////////////////////////    
#// four_of_a_kind FUNC  - Search for 4 of a kind, plus assign highest kicker.
#///////////////////////////////////////////////////////////////////////////////
    def four_of_a_kind(self,thisHandp,p):
        self.F,self.foak = 0,[]
        for c in thisHandp:
            if useful.nested_count(useful,thisHandp,c) == 4:
                cfg.whwHands[p] = 7
                self.F = c[0]
                self.foak += [c]
        if self.F > 0:
            cfg.whwCards[p] = [useful.card_2_drawid_conv(useful,self.foak[n]) 
                                                           for n in range(4)]
            self.kicker = [thisHandp[k] for k in range(len(thisHandp)) 
                                     if thisHandp[k] not in self.foak]
            cfg.whwCards[p].append(useful.card_2_drawid_conv(useful,max(self.kicker)))

#                        print('whwHands[p]',whwHands[p])
#                        print('whwCards[p]',whwCards[p])

#///////////////////////////////////////////////////////////////////////////////    
#// full_house FUNC - Pick highest trips and pair.
#///////////////////////////////////////////////////////////////////////////////
    def full_house(self,thisHandp,p):
        self.trips = []
        self.pair = []
        self.T = 0
        self.P = 0
        for c in thisHandp:
            if useful.nested_count(useful,thisHandp,c) == 3 and c[0] > self.T:
                self.T = c[0]
        self.trips = [useful.card_2_drawid_conv(useful,thisHandp[i]) for i in 
                          range (len(thisHandp)) if thisHandp[i][0] == self.T]
        for c in thisHandp:
            if (useful.nested_count(useful,thisHandp,c) >= 2 and 
                                            c[0] != self.T and c[0] > self.P):
                self.P = c[0]
        self.pair = [useful.card_2_drawid_conv(useful,thisHandp[i]) for i in 
                          range (len(thisHandp)) if thisHandp[i][0] == self.P]
        if self.T and self.P > 0:
            cfg.whwHands[p] = 6
            cfg.whwCards[p] = self.trips + self.pair[0:2]

#/////////////////////////////////////////////////////////////////////////////    
#// flush FUNC - Check for Flush and gen list of flush cards then trim top
#// len of flush cards to == 5
#/////////////////////////////////////////////////////////////////////////////
    def flush(self,thisHandp,p):
        self.foo = []
        for c in thisHandp:
            if c[1] == cfg.CpFlush[0]:
                self.foo += [c]
        # Count whether a players matching suit cards form a 5 card flush.
        if len(self.foo) >=5:
            self.foo.sort(reverse=True)
            while len(self.foo) > 5:
                # check that pop removes last item ???
                self.foo.pop()
            cfg.whwHands[p] = 5
            cfg.whwCards[p] = [useful.card_2_drawid_conv(useful,self.foo[n])
                                                            for n in range(5)]
#            print('whwHands[p]',cfg.whwHands[p])
#            print('whwCards[p]',cfg.whwCards[p])

#/////////////////////////////////////////////////////////////////////////////
#// straight FUNCTION - Requires [p] from handCalc handler
#// Add Aces as [1,Suit]. Strip out duplicates. Check for sequential hands.
#/////////////////////////////////////////////////////////////////////////////
    def straight(self,thisHandp,p):
        self.foo = thisHandp[:]
        self.A1 = []
        for c in self.foo:
            if c[0] == 14:
                self.A14 = c
                self.A1 = [1,c[1]]
        if len(self.A1) > 0:
            self.foo.append(self.A1)
        for c in self.foo:
            if useful.nested_count(useful,self.foo,c) > 1:
                self.foo.remove(c)
        if len(self.foo) >= 5:
            for s in range(0,len(self.foo)-4):
                if (self.foo[s][0]-4 == self.foo[s+4][0] and 
                                                       cfg.whwHands[p] != 4):
                    cfg.whwHands[p] = 4
                    while self.A1 in self.foo:
                        self.foo.remove(self.A1)
                        self.foo.append(self.A14)
                    cfg.whwCards[p] = [useful.card_2_drawid_conv
                                          (useful,self.foo[t+s]) 
                                            for t in range(0,5)]
#        print('whwHands[p]',cfg.whwHands[p])
#        print('whwCards[p]',cfg.whwCards[p])

#/////////////////////////////////////////////////////////////////////////////
#// three_of_a_kind FUNCTION - Requires [p] from handCalc handler
#// Search for highest trips, plus two highest kickers.
#/////////////////////////////////////////////////////////////////////////////
    def three_of_a_kind(self,thisHandp,p):
        self.T = 0
        self.trips = []
        for c in thisHandp:
            if useful.nested_count(useful,thisHandp,c) == 3:
                self.T = c[0]
        if self.T > 0:
#            print('tripsT=',self.T)
            self.trips = [useful.card_2_drawid_conv(useful,thisHandp[i]) for
                        i in range(len(thisHandp)) if thisHandp[i][0] == self.T]
#        if len(self.trips) > 0:
            cfg.whwHands[p] = 3
            cfg.whwCards[p] = self.trips
            self.kicker = [thisHandp[k] for k in range(len(thisHandp)) 
                              if thisHandp[k][0] != self.T]
            self.a = max(self.kicker)
            self.kicker.remove(self.a)
            self.b = max(self.kicker)
            self.kicker = [self.a, self.b]
            self.bar = [useful.card_2_drawid_conv(useful,self.kicker[i])
                                                      for i in range(2)]
            cfg.whwCards[p].extend(self.bar)

#            print('whwHands[p]',cfg.whwHands[p])
#            print('whwCards[p]',cfg.whwCards[p])

#/////////////////////////////////////////////////////////////////////////////    
#// two_pairs FUNC - Requires [p] from handCalc handler.
#// Search for highest two Pair plus highest kicker.
#/////////////////////////////////////////////////////////////////////////////
    def two_pairs(self,thisHandp,p):
        self.bar = []
        for c in thisHandp:
            if useful.nested_count(useful,thisHandp,c) == 2:
                self.bar += [c]
        if len(self.bar) >= 4:
            self.bar.sort(reverse=True)
            self.pairs = self.bar[0:4]
            self.r = [thisHandp[i] for i in range(len(thisHandp)) if thisHandp[i] 
                                                           not in self.pairs]
            self.kicker = max(self.r)
            cfg.whwHands[p] = 2
            cfg.whwCards[p] = [useful.card_2_drawid_conv(useful,self.pairs[i]) 
                                               for i in range(4)]
            cfg.whwCards[p].append(useful.card_2_drawid_conv(useful,self.kicker))
#            print('whwCrds2pair',cfg.whwCards[p])
#            print('whwHands[p]',whwHands[p])
#            print('whwCards[p]',whwCards[p])
            
#///////////////////////////////////////////////////////////////////////////////    
#// two_of_a_kind FUNC - Requires [p] from handCalc handler
#// Search for highest Pair plus 3 highest kickers.
#///////////////////////////////////////////////////////////////////////////////
    def two_of_a_kind(self,thisHandp,p):
        self.pairs = []
        for c in thisHandp:
            if useful.nested_count(useful,thisHandp,c) == 2:
                self.pairs += [c]
                cfg.whwHands[p] = 1
        if len(self.pairs) == 2:
                    cfg.whwCards[p] = [useful.card_2_drawid_conv(useful,self.pairs[i]) for i in range(2)]
                    self.kicker = [thisHandp[k] for k in range(len(thisHandp)) 
                                        if thisHandp[k] not in self.pairs]
                    self.a = max(self.kicker)
                    self.kicker.remove(self.a)
                    self.b = max(self.kicker)
                    self.kicker.remove(self.b)
                    self.c = max(self.kicker)
                    self.kicker = [self.a, self.b, self.c]
                    cfg.whwCards[p] += [useful.card_2_drawid_conv(useful,self.kicker[j]) for j in range(3)]

#            print('whwHands[p]',cfg.whwHands[p])
#            print('whwCards[p]',cfg.whwCards[p])

#/////////////////////////////////////////////////////////////////////////////    
#// high_card FUNC - Requires [p] from handCalc handler.  Add 1st two cards 
#// from sorted thisHand[p], if >2 then add next 3 highest cards.
#/////////////////////////////////////////////////////////////////////////////
    def high_card(self,thisHandp,p):
        cfg.whwHands[p] = 0
        cfg.whwCards[p] = [useful.card_2_drawid_conv(useful,thisHandp[i]) 
                                                          for i in range(0,2)]
        if len(thisHandp) > 2:
            cfg.whwCards[p] += [useful.card_2_drawid_conv(useful,thisHandp[j]) 
                                                        for j in range(2,5)]
#        print('whwHands[p]',cfg.whwHands[p])
#        print('whwCards[p]',cfg.whwCards[p])
    
#/////////////////////////////////////////////////////////////////////////////    
