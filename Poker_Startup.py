#///////////////////////////////////////////////////////////////////////////////
# Name:         PokerBody.py
# Purpose:      A Poker Simulation and Potential Game
# Version:      v1.1.0
#
# Author:       Tim Tyler
#
# Created:      2013-
# Copyright:    (c) 2013 by TT
# Licence:      Nah
#-------------------------------------------------------------------------------
# Release Notes:
# v1.0.1 (11/09/2013 @ 22:09) - Working copy of: NewHand, printNewHand,
# isFlush & playerFlushes functions.
# v1.0.2 (13/09/2013 @ 09:22) - Bug fix for PKR001. Flush function working.
# v1.0.3 (22/09/2013 @ 18:03) - Royal Flush and Straight Flushes added.  Broken
# Flush function in "isFlush", "playerFlush" and "winFlush".
# v1.0.4 (26/09/2013 @ 11:41) - Straight function added. Bug fix for PKR002.
# v1.0.5 (02/10/2013 @ 21:33) - Trip func fixed.  Bug fix for PKR003/005.
# v1.0.6 (08/10/2013 @ 22:14) - Reorganised flush functions to specific hands.
# v1.0.7 (11/10/2013 @ 16:28) - FullHouse func added.
# v1.0.8 (14/10/2013 @ 18:35) - TwoPair func added, refactored Royal Flush.
# v1.0.9 (16/10/2013 @ 14:45) - Pair func added, replaced xsorts with itemgetter
# v1.0.10 (17/10/2013 @ 15:35) - High Card added.
# v1.2.1 (21/11/2013 @ 08:45 - Re-architectured into seperate modules, checking
#                              each hand seperately.
# v1.3.0 (04/12/2013 @ 11:55) - Integrated with Pyglet, drawing on_your_backs()
#-------------------------------------------------------------------------------
# Bug tracker:
# PKR001 - playerFlush function. Multiple Flushes kicker calculation totally
# wrong. Multiple flushes reports wrong winner. Max community card calculated
# wrong. Line 315. **FIXED** 13/09/13 with lambda sorting.
# PKR002 - Community Flush crash. Lambda sort too specific, removed extra index.
# PKR004 - Multi Straights included lower value straights, added == highest
# value comparison to list comprehension.
# PKR003 & PKR005 - Shared trips weren't checking kickers, fixed by sorting on
# specific kicker index before each kicker check.
# PKR006 - drawing cards in wrong place.  Fixed in GFX draw_cards()
#-------------------------------------------------------------------------------
# To Do:
# Consider using dictionary keys for PX, and sets for hand lists.
# Logging
# add mySQL to record hand results
# Calculate prob %s
# Draw each phase in sequence.
#-------------------------------------------------------------------------------
# Dev Environment:
# \\LapBot\C:\ Users\Tim\Desktop\Python
# sys.path = "C:/Users/Tim/Desktop/Python/Projects/Poker/Poker_Work/)"
#-------------------------------------------------------------------------------
# NOTE: requires Python 3.3.0 or newer
# import the wxPython GUI package
# import wx
#////////////////////////////////////////////////////////////////////////////////
#// INIT FUNC
#// Load deck of cards in to memory and kick off handlers.playout().
#////////////////////////////////////////////////////////////////////////////////

import sys
sys.path.append("C:\\Users\\Tim\Desktop\\Python\\Projects\\Poker\\Poker_Work\\MyPy")
from handlers import handlers
import cfg

def init():
    # Generate a deck of cards in memory (the suits lists aren't modified
    # so can be referenced later) [number, 'suit'] = [0,1] - is modified 
    # (shuffled) by newHand() function
    cfg.newDeck = [[2,'Clubs'],[3,'Clubs'],[4,'Clubs'],[5,'Clubs'],
                   [6,'Clubs'],[7,'Clubs'],[8,'Clubs'],[9,'Clubs'],
                   [10,'Clubs'],[11,'Clubs'],[12,'Clubs'],[13,'Clubs'],
                   [14,'Clubs'],[2,'Diamonds'],[3,'Diamonds'],[4,'Diamonds'],
                   [5,'Diamonds'],[6,'Diamonds'],[7,'Diamonds'],[8,'Diamonds'],
                   [9,'Diamonds'],[10,'Diamonds'],[11,'Diamonds'],[12,'Diamonds'],
                   [13,'Diamonds'],[14,'Diamonds'],[2,'Hearts'],[3,'Hearts'],
                   [4,'Hearts'],[5,'Hearts'],[6,'Hearts'],[7,'Hearts'],
                   [8,'Hearts'],[9,'Hearts'],[10,'Hearts'],[11,'Hearts'],
                   [12,'Hearts'],[13,'Hearts'],[14,'Hearts'],[2,'Spades'],
                   [3,'Spades'],[4,'Spades'],[5,'Spades'],[6,'Spades'],
                   [7,'Spades'],[8,'Spades'],[9,'Spades'],[10,'Spades'],
                   [11,'Spades'],[12,'Spades'],[13,'Spades'],[14,'Spades']]


init()    
goes = 0
while goes < 1:
    handlers.playout(handlers)
    print('###############################################')
    goes += 1
