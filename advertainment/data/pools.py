# Lock 2 value pools: value -> (two ways to say it on a card, near-miss value, evidence [type, src, body])
# Each evidence fits its value and rules out its near-miss value.
W='From our customer’s week'
LIVE={
 'friends':(["Rents a flat with two friends from college.","Shares a rented flat with two old college friends."],'pg',['Group chat',W,'“302 🏠 (3 members)”: “Rent is due Friday. Also, WHO finished the milk?”|The group photo: three people in graduation gowns, arms around each other.']),
 'pg':(["Lives in a PG with people they met on moving day.","Rents a bed in a paying-guest house full of strangers-turned-friends."],'friends',['House rules',W,'“No guests after 9 pm. Tiffin at 8. Rent to Aunty by the 5th.”|Bed 3 of 4 in the room. The other three were strangers until moving day.']),
 'parents':(["Lives at home with their parents.","Still lives in the family home with mum and dad."],'joint',['Sticky note',W,'On the fridge: “Beta, Papa and I are at Nani’s till Sunday. Dinner is in the microwave. The house is all yours!”']),
 'joint':(["Lives in a big joint family with grandparents, uncles and aunts.","Shares a house with three generations of family."],'parents',['Kitchen wall',W,'In chalk: “Tonight: 9 plates. Dadi: no salt. Chachu: home late.”']),
 'spouse':(["Lives with their partner. No kids yet.","Married, and it is just the two of them at home."],'inlaws',['Calendar reminder',W,'“Our anniversary! Table for two. No babysitter needed.”|“The in-laws live in another city. It’s just us at home.”']),
 'inlaws':(["Lives with their partner and their partner’s parents.","Shares a home with their partner and in-laws."],'spouse',['Kitchen note',W,'“Beta, I made extra rotis for you two. My son says you will be late tonight. — Mummy-ji”']),
 'kids':(["Lives with their partner and two school-going children.","Has two children in school and a partner at home."],'spouse',['School diary',W,'“Parent–teacher meeting on Saturday. Please bring both report cards: Class 4 and Class 6.”']),
 'spparents':(["Lives with their partner and their own parents.","Married, and still in the family home with mum and dad."],'inlaws',['Kitchen note',W,'“Your wife and I made poha. Eat before you leave. Papa needs the scooter today. — Aai”']),
 'hostel':(["Lives in the college hostel with a roommate.","Shares a hostel room on campus."],'pg',['Notice',W,'“Room 214: gates close at 10 pm. Show your college ID at the gate. Late arrivals sign the warden’s register.”']),
 'alone':(["Has a small flat all to themselves.","Lives alone and likes the quiet."],'friends',['Food app',W,'Saved address: “Home: 1RK, 4th floor”.|Not one order this month was split with anyone.']),
 'grand':(["Lives with their partner; their children have moved to other cities.","Shares a quiet home with their partner now that the children live elsewhere."],'joint',['Train ticket',W,'Two names, booked for May: the grandchildren, coming from far away.|On the back: “The house will be noisy again! Since the children moved away, it is just the two of us.”']),
 'toddler':(["Lives with their partner and a 4-year-old.","Has a partner and one child in playschool."],'kids',['Fridge door',W,'A playschool notice: “Nursery A: bring one toy from home on Friday.”|Only one child’s name on the pick-up card.']),
}
MEDIA={
 'insta':(["Spends most of their phone time on Instagram reels.","Can scroll reels for hours."],'youtube',['Screen-time report',W,'No. 1 app: the pink-and-orange camera icon.|No. 2, far behind: the red play button.']),
 'youtube':(["Watches long YouTube videos before buying anything.","Spends most of their phone time on YouTube."],'insta',['Browser history',W,'“full review”, “part 2”, “watch till the end”, “unboxing”.|Most-used app: the red play button. The camera-icon app was deleted in March.']),
 'tv':(["Never misses the evening TV serial.","Watches TV with the family every night."],'youtube',['TV remote',W,'The volume button is worn out. A channel guide has 8 pm circled in red.|Phone data used this month: 1.2 GB. “Videos eat my data.”']),
 'paper':(["Reads the morning newspaper cover to cover.","Trusts only the printed newspaper."],'tv',['Doormat',W,'Three newspapers, folded, every crossword finished in pen.|The TV cable was cut in March. Nobody asked for it back.']),
 'whatsapp':(["Gets all their news from WhatsApp groups.","Lives in family and neighbourhood WhatsApp groups."],'fb',['Phone storage',W,'“Storage full.” 2,341 “Good morning” images from 14 groups.|The blue app with the white ‘f’: never installed.']),
 'fb':(["Spends most phone time on Facebook groups.","Reads everything on Facebook."],'whatsapp',['Phone screen',W,'Most-used app: the blue one with the white ‘f’. Member of 22 groups there.|The green chat app: muted for weeks.']),
}
SHOP={
 'middle':(["Picks the mid-priced option: good-looking, but never the costliest.","Pays a little extra for looks, within reason."],'cheap',['Price list',W,'Compared 5 options and sorted them by price.|Bought No. 3.']),
 'cheap':(["Always picks the cheapest option that works.","Buys whatever costs least."],'middle',['Price app',W,'Alert: “Price dropped by ₹4. This is now the lowest price anywhere!”|Bought within 1 minute.']),
 'premium':(["Always buys the most expensive version.","Only buys top-of-the-range."],'middle',['Shopping filter',W,'“Sort by: Price, high to low.”|Bought the very first result. Every time.']),
 'lasts':(["Pays more once rather than buying cheap twice.","Buys the one that lasts, even if it costs more."],'cheap',['Phone note',W,'“Bought the ₹150 one twice last year. Never again.”|“Check the warranty first.”']),
}
RHYTHM={
 'office':(["Works fixed office hours and logs off on time.","Keeps a strict 9-to-6 and switches off after."],'flexi',['Auto-reply',W,'“I’m offline after 6 pm. I’ll reply first thing tomorrow.”']),
 'flexi':(["Works flexible hours, often late into the night.","Starts late, finishes late, no fixed hours."],'office',['Calendar',W,'First meeting: noon. Last call: 10:30 pm.|No two days start at the same time.']),
 'wfh':(["Works from home and sets their own hours.","Has no office to go to."],'office',['Office badge',W,'Never needed one: every meeting this week happened at the dining table.']),
 'shifts':(["Works rotating shifts: days one week, nights the next.","Has a different shift every week."],'office',['Roster',W,'This week: nights. Next week: days. Week after: nights again.']),
 'early':(["Is up before sunrise most days.","Starts the day before 6 am."],'night',['Gym card',W,'Every check-in this month is stamped while it is still dark outside.|Lights out by 10.']),
 'night':(["Does their best thinking after midnight.","Is wide awake at 2 am."],'early',['Food app',W,'Every order this week was delivered long after midnight.']),
}
MOVE={
 'metro':(["Takes the metro everywhere.","Swipes a metro card twice a day."],'bus',['Travel card',W,'Swipe history: “Entry: Gate 2 … Exit: Gate 4”, twice a day.|No bus conductor has ever seen this card.']),
 'bus':(["Takes the city bus everywhere.","Rides the bus to work and back."],'metro',['Monthly pass',W,'Punched by a conductor every morning.|A route number written on the back.']),
 'scooter':(["Rides a two-wheeler everywhere.","Zips around on their own scooter."],'cab',['Keys',W,'A helmet hook by the door. A fuel receipt: ₹200, every 4 days.|The cab app was deleted months ago.']),
 'cab':(["Books a cab for every trip.","Never drives; always takes a cab."],'scooter',['Ride app',W,'“You took 46 rides this month. You are now a Gold rider!”|No helmet, no driving licence.']),
 'car':(["Drives their own car everywhere.","Has a car and drives it daily."],'cab',['Windscreen',W,'A parking sticker for the society basement.|SMS: “FASTag recharged: ₹500.”']),
 'walks':(["Walks everywhere.","Goes everywhere on foot."],'cycle',['Step counter',W,'14,000 steps a day.|The parking slot at home is empty: not even a bicycle.']),
 'cycle':(["Cycles everywhere.","Pedals to work and back every day."],'walks',['Bag',W,'A small air pump and a lock key on the key ring.|Trouser cuffs tucked into the socks every morning.']),
 'train':(["Takes the local train every day.","Rides the suburban train to work."],'bus',['Season ticket',W,'“First class, Thane to Kurla. Valid for 3 months.”']),
 'auto':(["Takes an auto-rickshaw everywhere.","Hops into an auto for every trip."],'bus',['Purse',W,'A slip with three auto drivers’ numbers: “Raju: market. Ramesh: temple.”|Has never waited at a bus stop.']),
}
POOL={'live':LIVE,'media':MEDIA,'shop':SHOP,'rhythm':RHYTHM,'move':MOVE}
