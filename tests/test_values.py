t1 = """Testing is this works
it should work
"""

t2 = """This is another test
it should also work.

So let us see
"""

l1 = """advantage: A useful trait that gives you an “edge” over another person
with comparable attributes and skills. See Chapter 2.
attributes: Four numbers – Strength, Dexterity, Intelligence, and Health
– that rate a character’s most basic abilities. Higher is always better!
See pp. 14-15.

cinematic: A style of play where the needs of the story outweigh those
of realism, even when that would produce improbable results. See
p. 488.

d: Short for “dice.” “Roll 3d” means “roll three ordinary six-sided dice
and add them up.” See p. 9.
Dexterity (DX): An attribute that measures agility and coordination.
See p. 15.

disadvantage: A problem that renders you less capable than your other
traits would indicate. See Chapter 3.
enhancement: An extra capability added to a trait. This increases the
point cost of the trait by a percentage. See pp. 102-109.

Fatigue Points (FP): A measure of resistance to exhaustion. See p. 16.
Health (HT): An attribute that measures physical grit and vitality. See
p. 15.

Hit Points (HP): A measure of ability to absorb punishment. See p. 16.
Intelligence (IQ): An attribute that measures brainpower. See p. 15.
limitation: A restriction on the use of a trait. This reduces the point cost
of the trait by a percentage. See pp. 110-117.
point: The unit of “currency” spent to buy traits for a character. The
more points you have, the more capable you are. Point costs for
traits are often written in brackets; e.g., “Combat Reflexes [15]”
means the Combat Reflexes trait costs 15 points. See p. 10.
prerequisite: A trait you must have to qualify for another trait. If the
prerequisite is a skill, you must have at least one point in it. See
p. 169.

skill: A number defining your trained ability in an area of knowledge
or broad class of tasks. See Chapter 4.
Strength (ST): An attribute that measures physical muscle and bulk.
See p. 14.

trait: An advantage, attribute, disadvantage, skill, or other character
“building block” that affects game play and costs points to add,
modify, or remove.
"""

l2 = """• GURPS Basic Set Characters. Everyone will need access to this
book in order to create characters and look up character abilities. A large
group will find it handy to have several copies available, especially during
character creation.
• GURPS Basic Set Campaigns. The GM will need a copy of this
book, which contains rules for success rolls, physical feats, combat,
injury, animals, and vehicles, as well as advice on how to run the game
and design a campaign.
•Character sheets. Each player will need a copy of the Character Sheet
(pp. 335-336) on which to record his PC’s statistics. You may make as
many copies as you like for your own use (but not for resale).
• Three six-sided dice. A set of three dice for each player, and another
set for the GM, is even better.
• Pencils and scratch paper. For taking notes, sketching maps, etc.
"""

l3 = """• Where was he born and where
did he grow up? Where does he live
now?
• Who were his parents? (Does he
know?) Are they still alive? If not,
what became of them? If so, does he
get along with them?
• What training does he have? Was
he an apprentice? A student? Or is he
self-taught?
• What is his current occupation?
What other jobs has he held?
• What social class does he belong
to? How wealthy is he?
• Who are his friends? His enemies?
His closest professional associates?
• What were the most important
moments of his life?
• What are his likes and dislikes?
Hobbies and interests? Morals and
beliefs?
• What are his motivations? Plans
for the future?
"""

l4 = """1. Quickly skim this book, just to
get the flavor of the game. Don’t worry
about the details yet.
2. Read the Mini-Glossary (p. 7) to
learn the basic terminology.
3. Read the Quick-Start and
Conventions sections to learn the basic
game concepts.
4. Read Creating a Character
(pp. 10-12) to get an idea of the different
things characters can do.
5. Read the rest of the rules in
detail, as your time permits.
"""

l5 = """Exotic. An alien, angel, robot,
“super” (a comic-book superhuman),
or other hero defined by his unusual
powers or nature. Most of his starting
points should go toward high attributes,
exotic or supernatural advantages
(see p. 32), or a racial template
(see p. 260). As a result, he probably
has fewer mundane abilities than his
fellow adventurers.
Jack-of-All-Trades. A many-skilled
hero: mercenary, bush pilot, reporter,
etc. DX and IQ are most important.
Advantages such as Talent and
Versatile can help. Pick one or two
skills from those suggested for each of
the other character types. A Jack-of-
All-Trades isn’t as good as a dedicated
expert, but he has some skill in many
areas.
Mouthpiece. A bard, con man, or
other person who exploits wit and
charm. IQ is crucial. Charisma,
Cultural Familiarity, Rapier Wit, Voice,
and a good appearance are all useful.
Most important are skills that emphasize
social interaction: Carousing,
Fast-Talk, Merchant, Public Speaking,
and so on.
Sage. A “wise man” – priest, professor,
scientist, etc. High IQ is essential.
Classic advantages are Eidetic
Memory, Intuition, Language Talent,
and Languages (and, in some campaigns, Illuminated!). He needs several
related IQ/Hard skills in obscure fields
(Expert Skills are especially suitable),
as well as Research, Teaching, and
Writing.
"""

table1 = """Imperial | Game Metric | Real Metric
1 inch (in.) | 2.5 cm | 2.54 cm
1 foot (ft.) | 30 cm | 30.48 cm
1 yard (yd.) | 1 meter | 0.914 meters
1 mile (mi.) | 1.5 km | 1.609 km
1 pound (lb.) | 0.5 kg | 0.454 kg
1 ton | 1 metric ton | 0.907 metric tons
1 gallon (gal.) | 4 liters | 3.785 liters
1 quart (qt.) | 1 liter | 0.946 liters
1 ounce (oz.) | 30 grams | 28.349 grams
1 cubic inch (ci) | 16 cubic cm | 16.387 cu. cm
1 cubic yard (cy) | 0.75 cubic m | 0.765 cubic m
"""

table2 = """ST | BL | Encumbrance Levels (lbs.) | Encumbrance Levels (lbs.) | Encumbrance Levels (lbs.) | Encumbrance Levels (lbs.) | Encumbrance Levels (lbs.) 
(lbs.) | | None (0) | Light (1) | Medium (2) | Heavy (3) | Extra-Heavy (4)
1 | 0.2 | 0.2 | 0.4 | 0.6 | 1.2 | 2
2 | 0.8 | 0.8 | 1.6 | 2.4 | 4.8 | 8
3 | 1.8 | 1.8 | 3.6 | 5.4 | 10.8 | 18
4 | 3.2 | 3.2 | 6.4 | 9.6 | 19.2 | 32
5 | 5 | 5 | 10 | 15 | 30 | 50
"""

table3 = """ST | Height Range | Weight Range by Build | Weight Range by Build | Weight Range by Build | Weight Range by Build | Weight Range by Build 
 | | Skinny | Average | Overweight | Fat | Very Fat
6 or less | 4’4”-5’2” | 40-80 lbs. | 60-120 lbs. | 80-160 lbs. | 90-180 lbs. | 120-240 lbs.
7 | 4’7”-5’5” | 50-90 lbs. | 75-135 lbs. | 100-175 lbs. | 115-205 lbs. | 150-270 lbs.
8 | 4’10”-5’8” | 60-100 lbs. | 90-150 lbs. | 120-195 lbs. | 135-225 lbs. | 180-300 lbs.
"""



######################################################################

page = 110


