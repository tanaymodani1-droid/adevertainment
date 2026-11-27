# Vault v4: SAME code for every team: 87384. Same numbers for every brand; only the names change.
# Every dial needs two steps and has a trap.
import sys; sys.path.insert(0,'../caps15')
from vault3 import FLAV as F15
from new29 import N
FLAV=dict(F15); FLAV.update({b:d['flav'] for b,d in N.items()})
CODE='87384'
def noise(brand,city):
    q,cr,kind=FLAV[brand]
    return [['Instagram poll','A '+city+' page','“'+q+'”|27,000 people voted. 4 out of every 9 said yes.|Of the people who said yes, 1 in 3 already owns one.|Posted 3 days ago · 2,100 comments.'],
            ['Creator profile',cr+', a '+city+' '+kind+' creator','Followers: 180K. Engagement: 6%.|Rate: ₹2,000 per post for every 60K followers.|The creator’s agency adds a flat fee of ₹1,000 to every post.|Offer: 1 free post for every 3 paid posts.'],
            ['Media quote',city+' Metro','Station billboard: ₹48,000 a week.|Bus-shelter posters: ₹4,000 each per week, sold only in packs of 4.|Auto-rickshaw back panels: ₹900 each per month.'],
            ['Launch budget memo','The new owners','Launch budget: ₹84,000.|Half of it goes to creators.|A quarter of it goes to posters.|Whatever is left pays for the launch party.']]
Q=[('Dial 1 · Clue #27. How many thousand people said yes but do NOT own one yet?',8),
   ('Dial 2 · Clue #28. What does ONE paid post cost us in total, in thousands of rupees?',7),
   ('Dial 3 · Clue #29. One week on the station billboard costs the same as how many packs of bus-shelter posters?',3),
   ('Dial 4 · Clues #28 and #30. Counting the free ones, how many posts will the creator budget get us?',8),
   ('Dial 5 · Clues #29 and #30. How many bus-shelter posters can the poster budget put up for one week?',4)]
def check():
    yes=27000*4//9; d1=(yes-yes//3)//1000
    post=180//60*2000+1000; d2=post//1000
    pack=4000*4; d3=48000//pack
    paid=(84000//2)//post; d4=paid+paid//3
    d5=((84000//4)//pack)*4
    v=[d1,d2,d3,d4,d5]
    assert v==[a for _,a in Q] and ''.join(map(str,v))==CODE,v
    assert 27000*4%9==0 and yes%3==0 and (84000//2)%post==0
    # traps give different answers
    assert (84000//2)//6000+(84000//2)//6000//3!=d4 and (84000//4)//4000!=d5
check()
