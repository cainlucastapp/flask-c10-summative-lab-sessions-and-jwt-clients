#server/seeds.py

#server/seeds.py

from app import app
from extensions import db, bcrypt
from models.user import User
from models.quests import Quest

with app.app_context():
    # Clear existing data
    print("Clearing existing data...")
    Quest.query.delete()
    User.query.delete()
    db.session.commit()

    # Create users
    print("Seeding users...")

    howl = User(
        username='Howl',
        email='howl@tavernbook.com',
        character_class='Fighter',
        level=5,
        gold=450
    )
    howl.password_hash = 'swordfight1'

    jastor = User(
        username='Jastor',
        email='jastor@magetower.net',
        character_class='Mage',
        level=9,
        gold=1850
    )
    jastor.password_hash = '!expelliarmus'

    alistare = User(
        username='Alistare',
        email='sneakattackcrit@outlawlook.com',
        character_class='Rogue',
        level=3,
        gold=920
    )
    alistare.password_hash = '34n21poirrn!@$#21n4i32n42$#@M$ono32n1l2n4l321n4lnr3#@'

    kaiser = User(
        username='Kaiser',
        email='outh316@DeusVolt.com',
        character_class='Paladin',
        level=4,
        gold=180
    )
    kaiser.password_hash = 'forthelord'

    volstage = User(
        username='Volstage',
        email='kal@rockspace.org',
        character_class='Ranger',
        level=1,
        gold=35
    )
    volstage.password_hash = 'ilikesquires'

    db.session.add_all([howl, jastor, alistare, kaiser, volstage])
    db.session.commit()
    print("Users seeded!")
    

    # -- Howl (Fighter, Level 5) → 20 quests ---------------------------------
    howl_quests = [
        # Level 1
        dict(title='Clear the Cellar Rats',
             description='The innkeeper needs the cellar cleared of an infestation before they eat through the grain stores.',
             status='completed', difficulty='Easy', reward_gold=20),
        dict(title='Collect Overdue Rent',
             description='The landlord needs a firm hand to collect rent from three delinquent tenants in the market district.',
             status='completed', difficulty='Easy', reward_gold=15),
        dict(title='Spar with the Guard Captain',
             description='Prove your fighting mettle by landing at least one clean hit on the garrison captain.',
             status='completed', difficulty='Easy', reward_gold=10),
        dict(title='Escort the Supply Cart',
             description='Walk a merchant\'s cart of grain safely to the next village — bandits have been spotted on the road.',
             status='failed', difficulty='Easy', reward_gold=25),

        # Level 2
        dict(title='Break Up the Tavern Brawl',
             description='A drunken melee has broken out at the Rusty Flagon. Subdue the troublemakers without killing anyone.',
             status='completed', difficulty='Easy', reward_gold=40),
        dict(title='Hunt the Wolf Pack',
             description='A pack of wolves has grown bold and attacked a shepherd outside town. Cull the pack.',
             status='completed', difficulty='Medium', reward_gold=60),
        dict(title='Guard the Merchant Overnight',
             description='A wealthy spice merchant fears thieves. Stand watch outside his room until dawn.',
             status='completed', difficulty='Easy', reward_gold=35),
        dict(title='Retrieve the Lost Shipment',
             description='A shipment of weapons meant for the garrison was ambushed. Recover what remains.',
             status='failed', difficulty='Medium', reward_gold=80),

        # Level 3
        dict(title='Defeat the Dueling Champion',
             description='A travelling duelist has humiliated half the town guard. Restore their honor in single combat.',
             status='completed', difficulty='Medium', reward_gold=120),
        dict(title='Rout the Goblin Raiders',
             description='A goblin war band has been raiding farms on the eastern road. Drive them back into the hills.',
             status='completed', difficulty='Medium', reward_gold=100),
        dict(title='Smash the Smuggling Ring',
             description='Contraband weapons are being moved through the city sewers. Find the stash and arrest the ringleader.',
             status='completed', difficulty='Hard', reward_gold=175),
        dict(title='Hold the Bridge',
             description='Enemy forces are advancing. Hold the river bridge alone until reinforcements arrive.',
             status='failed', difficulty='Hard', reward_gold=200),

        # Level 4
        dict(title='Slay the Mountain Troll',
             description='A massive troll has been terrorizing the mountain pass. End its reign of terror.',
             status='completed', difficulty='Hard', reward_gold=200),
        dict(title='Liberate the Prisoners',
             description='A bandit fortress holds a dozen villagers captive. Storm the gates and bring them home.',
             status='completed', difficulty='Hard', reward_gold=220),
        dict(title='Survive the Colosseum Gauntlet',
             description='Five opponents, no breaks, no mercy. The crowd wants a show — give them one.',
             status='completed', difficulty='Hard', reward_gold=250),
        dict(title='Hunt the Wyvern',
             description='A wyvern has nested in the cliffs above the harbor, threatening ships. Drive it off or kill it.',
             status='failed', difficulty='Legendary', reward_gold=400),

        # Level 5 (current)
        dict(title='Defend the Village Gates',
             description='Bandits plan to raid Millhaven at dawn. Stand guard and repel the attack.',
             status='active', difficulty='Medium', reward_gold=150),
        dict(title='Retrieve the Stolen Shield',
             description='A legendary shield was stolen from the barracks. Track down the thief.',
             status='active', difficulty='Easy', reward_gold=75),
        dict(title='Challenge the Arena Champion',
             description='The arena champion has never been defeated. Prove your worth in single combat.',
             status='active', difficulty='Legendary', reward_gold=500),
        dict(title='Break the Siege Line',
             description='An enemy force has encircled a small keep. Find a gap in their lines and lead the defenders to safety.',
             status='active', difficulty='Hard', reward_gold=300),
    ]

    # -- Jastor (Mage, Level 9) → 36 quests -----------------------------------
    jastor_quests = [
        # Level 1
        dict(title='Identify the Strange Artifact',
             description='A farmer dug up a glowing stone in his field. Determine what it is before it causes harm.',
             status='completed', difficulty='Easy', reward_gold=20),
        dict(title='Light the Festival Lanterns',
             description='Use minor magic to ignite the hundred lanterns for the harvest festival before nightfall.',
             status='completed', difficulty='Easy', reward_gold=10),
        dict(title='Transcribe the Elder\'s Spellbook',
             description='The academy needs a clean copy of a deteriorating spellbook. Copy it before the ink fades entirely.',
             status='completed', difficulty='Easy', reward_gold=15),
        dict(title='Chase Off the Imp',
             description='A minor imp has been tormenting a cobbler\'s family. Banish it from their home.',
             status='failed', difficulty='Easy', reward_gold=25),

        # Level 2
        dict(title='Detect the Poisoned Well',
             description='Three villagers have fallen ill. Determine which of the town\'s wells has been contaminated.',
             status='completed', difficulty='Easy', reward_gold=40),
        dict(title='Translate the Ancient Inscription',
             description='An inscription on the old city gate has resisted translation for decades. Decipher it.',
             status='completed', difficulty='Medium', reward_gold=55),
        dict(title='Suppress the Wild Magic Zone',
             description='A patch of wild magic near the market has been causing accidents. Stabilize it.',
             status='completed', difficulty='Medium', reward_gold=70),
        dict(title='Counter the Hedge Witch\'s Hex',
             description='A local hedge witch placed a hex on the miller\'s family out of spite. Break it.',
             status='failed', difficulty='Medium', reward_gold=60),

        # Level 3
        dict(title='Summon and Bind the Scout Familiar',
             description='The council needs a long-range familiar to monitor the northern border. Summon and bind one.',
             status='completed', difficulty='Medium', reward_gold=100),
        dict(title='Unravel the Mind Maze',
             description='A nobleman\'s son has been mentally trapped by a cursed mirror. Free his mind.',
             status='completed', difficulty='Hard', reward_gold=160),
        dict(title='Retrieve the Stolen Spell Components',
             description='A thief made off with rare components from the academy vault. Track the magic residue.',
             status='completed', difficulty='Medium', reward_gold=90),
        dict(title='Survive the Arcane Trial',
             description='The academy demands that apprentices pass a dangerous test of magical aptitude. Endure it.',
             status='failed', difficulty='Hard', reward_gold=150),

        # Level 4
        dict(title='Destroy the Necromancer\'s Phylactery',
             description='A minor necromancer has hidden his phylactery somewhere in the catacombs. Find and destroy it.',
             status='completed', difficulty='Hard', reward_gold=220),
        dict(title='Shield the Town from the Firestorm',
             description='A rogue fire elemental is approaching the village. Erect a barrier to protect it.',
             status='completed', difficulty='Hard', reward_gold=200),
        dict(title='Uncover the Spy\'s Enchantment',
             description='Someone in the council has been magically coerced into passing secrets. Identify the compulsion.',
             status='completed', difficulty='Medium', reward_gold=180),
        dict(title='Contain the Summoning Gone Wrong',
             description='A student\'s summoning ritual backfired and opened a portal. Contain it before it expands.',
             status='failed', difficulty='Legendary', reward_gold=500),

        # Level 5
        dict(title='Recover the Lost Tome',
             description='An ancient spellbook was lost in the ruins of Valdermoor. Retrieve it before it falls into dark hands.',
             status='completed', difficulty='Hard', reward_gold=400),
        dict(title='Locate the Missing Archmage',
             description='High Archmage Delven vanished during a solo experiment. Scry his location.',
             status='completed', difficulty='Hard', reward_gold=350),
        dict(title='Purge the Haunted Library',
             description='Poltergeists have made the great library inaccessible. Exorcise every last one.',
             status='completed', difficulty='Medium', reward_gold=200),
        dict(title='Decode the Prophecy Fragment',
             description='A fragment of an ancient prophecy has surfaced. Decode it before the enemy does.',
             status='failed', difficulty='Hard', reward_gold=300),

        # Level 6
        dict(title='Dispel the Forest Curse',
             description='A dark curse has twisted the Elderwood. Find its source and break the enchantment.',
             status='completed', difficulty='Legendary', reward_gold=800),
        dict(title='Collapse the Enemy Ley Line',
             description='Enemy mages are drawing power from a ley line beneath the city. Cut them off.',
             status='completed', difficulty='Hard', reward_gold=450),
        dict(title='Reconstruct the Shattered Orb',
             description='The Orb of Seeing was shattered into seven pieces scattered across the realm. Reassemble it.',
             status='completed', difficulty='Legendary', reward_gold=700),
        dict(title='Resist the Siren\'s Enchantment',
             description='A powerful siren has bewitched an entire village. Break her hold without harming the captivated.',
             status='failed', difficulty='Hard', reward_gold=400),

        # Level 7
        dict(title='Anchor the Collapsing Demiplane',
             description='A demiplane used as a prison is collapsing. Stabilize it before the prisoners are lost to the void.',
             status='completed', difficulty='Legendary', reward_gold=900),
        dict(title='Sever the Soul Chain',
             description='A lich has bound three innocent souls to his own. Sever the chain without destroying the souls.',
             status='completed', difficulty='Legendary', reward_gold=950),
        dict(title='Avert the Astral Convergence',
             description='Two unstable planes are drifting toward convergence. Avert the collision before reality tears.',
             status='completed', difficulty='Legendary', reward_gold=1000),
        dict(title='Outwit the Sphinx',
             description='A sphinx guards the entrance to the ancient vault. Defeat it in a contest of riddles.',
             status='failed', difficulty='Hard', reward_gold=500),

        # Level 8
        dict(title='Bind the Storm Titan',
             description='A storm titan has broken free of its ancient binding. Reforge the seal before hurricanes destroy the coast.',
             status='completed', difficulty='Legendary', reward_gold=1200),
        dict(title='Unwrite the Cursed Edict',
             description='A cursed royal edict compels every citizen who reads it to attack their family. Nullify its magic.',
             status='completed', difficulty='Hard', reward_gold=600),
        dict(title='Navigate the Mirror Labyrinth',
             description='A powerful enchantress has trapped the king inside a mirror labyrinth. Find and free him.',
             status='completed', difficulty='Legendary', reward_gold=1100),
        dict(title='Purge the Mindflayer\'s Psychic Web',
             description='A mindflayer has extended a psychic web across an entire district. Tear it apart from the inside.',
             status='failed', difficulty='Legendary', reward_gold=1000),

        # Level 9 (current)
        dict(title='Brew the Arcane Elixir',
             description='Gather moonpetal flowers and dragon scales to brew a powerful elixir for the council.',
             status='active', difficulty='Medium', reward_gold=250),
        dict(title='Seal the Rift',
             description='A dimensional rift has opened near the city. Seal it before demons pour through.',
             status='active', difficulty='Legendary', reward_gold=1000),
        dict(title='Resurrect the Fallen Hero',
             description='The realm\'s greatest hero fell in the last war. The council wants her returned — at any cost.',
             status='active', difficulty='Legendary', reward_gold=1500),
        dict(title='Unmake the Cursed Crown',
             description='A crown of domination is driving the young queen to madness. Destroy it without destroying her.',
             status='active', difficulty='Legendary', reward_gold=1300),
    ]

    # -- Alistare (Rogue, Level 3) → 12 quests --------------------------------
    alistare_quests = [
        # Level 1
        dict(title='Lift the Baker\'s Purse',
             description='A simple training exercise from the guild: lift the baker\'s coin purse without him noticing.',
             status='completed', difficulty='Easy', reward_gold=10),
        dict(title='Eavesdrop on the Merchant Meeting',
             description='The guild wants to know what the spice merchants are planning. Get close enough to hear.',
             status='completed', difficulty='Easy', reward_gold=20),
        dict(title='Slip Past the Night Watch',
             description='A guild initiation test: move through the merchant quarter after curfew without being caught.',
             status='completed', difficulty='Easy', reward_gold=15),
        dict(title='Plant the Forged Letter',
             description='Leave a forged letter in the magistrate\'s desk without being detected.',
             status='failed', difficulty='Medium', reward_gold=35),

        # Level 2
        dict(title='Rob the Courier',
             description='A courier carrying sensitive documents for a corrupt official must be relieved of his cargo.',
             status='completed', difficulty='Medium', reward_gold=80),
        dict(title='Sabotage the Rival Guild\'s Heist',
             description='The Copper Knives are planning a job on our turf. Ruin their night without starting a war.',
             status='completed', difficulty='Medium', reward_gold=100),
        dict(title='Break into the Pawnbroker\'s Safe',
             description='A fence has been underpaying the guild for years. Retrieve the difference from his personal safe.',
             status='completed', difficulty='Medium', reward_gold=90),
        dict(title='Tail the City Guard Captain',
             description='Follow the guard captain all day and document his route and habits for the guild\'s records.',
             status='failed', difficulty='Hard', reward_gold=120),

        # Level 3 (current)
        dict(title='Steal the Merchant\'s Ledger',
             description='A corrupt merchant keeps records of his illegal dealings. Acquire them without being seen.',
             status='completed', difficulty='Medium', reward_gold=300),
        dict(title='Assassinate the Corrupt Lord',
             description='Lord Harwick has been extorting the poor for years. The guild wants him silenced.',
             status='active', difficulty='Hard', reward_gold=450),
        dict(title='Pickpocket the Prison Keys',
             description='A guild member is locked up in the city jail. Lift the keys from the warden.',
             status='active', difficulty='Easy', reward_gold=100),
        dict(title='Infiltrate the Noble\'s Gala',
             description='Blend in with the nobility and plant evidence on Duke Farenholdt.',
             status='failed', difficulty='Hard', reward_gold=350),
    ]

    # -- Kaiser (Paladin, Level 4) → 16 quests --------------------------------
    kaiser_quests = [
        # Level 1
        dict(title='Bless the Village Shrine',
             description='The village shrine has fallen into disrepair and the locals feel unprotected. Restore and bless it.',
             status='completed', difficulty='Easy', reward_gold=10),
        dict(title='Tend to the Wounded Soldiers',
             description='A skirmish left several soldiers injured in the field. Heal them and see them safely home.',
             status='completed', difficulty='Easy', reward_gold=15),
        dict(title='Drive Off the Grave Robbers',
             description='Desecrators have been looting the old cemetery. Confront and drive them off.',
             status='completed', difficulty='Easy', reward_gold=20),
        dict(title='Comfort the Dying Elder',
             description='An elder cleric is passing and asks for a holy companion at her side. Sit with her through the night.',
             status='completed', difficulty='Easy', reward_gold=5),

        # Level 2
        dict(title='Consecrate the Battlefield',
             description='Fallen soldiers from an old war haunt the battlefield as restless spirits. Perform the rites to set them free.',
             status='completed', difficulty='Medium', reward_gold=60),
        dict(title='Expose the False Priest',
             description='A charlatan is posing as a cleric of Auros and extorting the faithful. Unmask him publicly.',
             status='completed', difficulty='Medium', reward_gold=80),
        dict(title='Retrieve the Holy Relic',
             description='A relic of Saint Aldren has been stolen by cultists. Recover it from their hideout.',
             status='completed', difficulty='Medium', reward_gold=100),
        dict(title='Protect the Pilgrimage Route',
             description='Guard a group of pilgrims along a road known for ambushes.',
             status='failed', difficulty='Medium', reward_gold=70),

        # Level 3
        dict(title='Cleanse the Defiled Temple',
             description='The Temple of Auros has been desecrated by undead. Purify it in the light.',
             status='completed', difficulty='Hard', reward_gold=200),
        dict(title='Lay the Banshee to Rest',
             description='A grieving banshee haunts the ruins of a burned village. Discover her unfinished business and resolve it.',
             status='completed', difficulty='Hard', reward_gold=180),
        dict(title='Seal the Cursed Tomb',
             description='An ancient warlord\'s tomb has been disturbed. Reseal it before the undead army within escapes.',
             status='completed', difficulty='Hard', reward_gold=220),
        dict(title='Smite the Death Cult Leader',
             description='A cult devoted to a death god has been sacrificing townsfolk. Confront and destroy their leader.',
             status='failed', difficulty='Hard', reward_gold=250),

        # Level 4 (current)
        dict(title='Escort the Pilgrims',
             description='A group of pilgrims must reach the Holy Sanctum safely. Guard them on the journey.',
             status='active', difficulty='Easy', reward_gold=80),
        dict(title='Vanquish the Vampire Lord',
             description='A vampire lord terrorizes the countryside by night. Hunt him to his castle and end him.',
             status='active', difficulty='Legendary', reward_gold=600),
        dict(title='Protect the Innocent Farmer',
             description='A farmer has been falsely accused of witchcraft. Defend him before the tribunal.',
             status='failed', difficulty='Medium', reward_gold=120),
        dict(title='Break the Death Knight\'s Curse',
             description='A paladin of the old order was corrupted into a death knight. Find the source of his curse and free him.',
             status='active', difficulty='Legendary', reward_gold=550),
    ]

    # -- Volstage (Ranger, Level 1) → 4 quests --------------------------------
    volstage_quests = [
        dict(title='Map the Thornwood Forest',
             description='The Thornwood has never been fully charted. Venture in and create a reliable map.',
             status='active', difficulty='Medium', reward_gold=150),
        dict(title='Track the Missing Scout',
             description='A royal scout went missing three days ago in the Ashfield. Find them.',
             status='active', difficulty='Easy', reward_gold=90),
        dict(title='Hunt the Shadow Beast',
             description='A creature of darkness has been picking off livestock. Track it and bring back proof of its death.',
             status='failed', difficulty='Hard', reward_gold=280),
        dict(title='Set Snares Along the Border Trail',
             description='The garrison needs game for the winter stores. Set a line of snares along the northern border trail.',
             status='active', difficulty='Easy', reward_gold=30),
    ]

    # -------------------------------------------------------------------------
    # Build and insert all quests
    # -------------------------------------------------------------------------
    print("Seeding quests...")

    def make_quests(quest_data_list, user):
        return [
            Quest(user_id=user.id, **data)
            for data in quest_data_list
        ]

    all_quests = (
        make_quests(howl_quests, howl)
        + make_quests(jastor_quests, jastor)
        + make_quests(alistare_quests, alistare)
        + make_quests(kaiser_quests, kaiser)
        + make_quests(volstage_quests, volstage)
    )

    db.session.add_all(all_quests)
    db.session.commit()
    print(f"Quests seeded! ({len(all_quests)} total)")
    print("Done! Database seeded successfully.")