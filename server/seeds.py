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

    # Create quests
    print("Seeding quests...")

    quests = [
        # Howl - Fighter
        Quest(
            title='Slay the Mountain Troll',
            description='A massive troll has been terrorizing the mountain pass. End its reign of terror.',
            status='completed',
            difficulty='Hard',
            reward_gold=200,
            user_id=howl.id
        ),
        Quest(
            title='Defend the Village Gates',
            description='Bandits plan to raid Millhaven at dawn. Stand guard and repel the attack.',
            status='active',
            difficulty='Medium',
            reward_gold=150,
            user_id=howl.id
        ),
        Quest(
            title='Retrieve the Stolen Shield',
            description='A legendary shield was stolen from the barracks. Track down the thief.',
            status='active',
            difficulty='Easy',
            reward_gold=75,
            user_id=howl.id
        ),
        Quest(
            title='Challenge the Arena Champion',
            description='The arena champion has never been defeated. Prove your worth in single combat.',
            status='failed',
            difficulty='Legendary',
            reward_gold=500,
            user_id=howl.id
        ),

        # Jastor - Mage
        Quest(
            title='Recover the Lost Tome',
            description='An ancient spellbook was lost in the ruins of Valdermoor. Retrieve it before it falls into dark hands.',
            status='completed',
            difficulty='Hard',
            reward_gold=400,
            user_id=jastor.id
        ),
        Quest(
            title='Dispel the Forest Curse',
            description='A dark curse has twisted the Elderwood. Find its source and break the enchantment.',
            status='completed',
            difficulty='Legendary',
            reward_gold=800,
            user_id=jastor.id
        ),
        Quest(
            title='Brew the Arcane Elixir',
            description='Gather moonpetal flowers and dragon scales to brew a powerful elixir for the council.',
            status='active',
            difficulty='Medium',
            reward_gold=250,
            user_id=jastor.id
        ),
        Quest(
            title='Seal the Rift',
            description='A dimensional rift has opened near the city. Seal it before demons pour through.',
            status='failed',
            difficulty='Legendary',
            reward_gold=1000,
            user_id=jastor.id
        ),

        # Alistare - Rogue
        Quest(
            title='Steal the Merchant\'s Ledger',
            description='A corrupt merchant keeps records of his illegal dealings. Acquire them without being seen.',
            status='completed',
            difficulty='Medium',
            reward_gold=300,
            user_id=alistare.id
        ),
        Quest(
            title='Assassinate the Corrupt Lord',
            description='Lord Harwick has been extorting the poor for years. The guild wants him silenced.',
            status='active',
            difficulty='Hard',
            reward_gold=450,
            user_id=alistare.id
        ),
        Quest(
            title='Pickpocket the Prison Keys',
            description='A guild member is locked up in the city jail. Lift the keys from the warden.',
            status='active',
            difficulty='Easy',
            reward_gold=100,
            user_id=alistare.id
        ),
        Quest(
            title='Infiltrate the Noble\'s Gala',
            description='Blend in with the nobility and plant evidence on Duke Farenholdt.',
            status='failed',
            difficulty='Hard',
            reward_gold=350,
            user_id=alistare.id
        ),

        # Kaiser - Paladin
        Quest(
            title='Cleanse the Defiled Temple',
            description='The Temple of Auros has been desecrated by undead. Purify it in the light.',
            status='completed',
            difficulty='Hard',
            reward_gold=200,
            user_id=kaiser.id
        ),
        Quest(
            title='Escort the Pilgrims',
            description='A group of pilgrims must reach the Holy Sanctum safely. Guard them on the journey.',
            status='active',
            difficulty='Easy',
            reward_gold=80,
            user_id=kaiser.id
        ),
        Quest(
            title='Vanquish the Vampire Lord',
            description='A vampire lord terrorizes the countryside by night. Hunt him to his castle and end him.',
            status='active',
            difficulty='Legendary',
            reward_gold=600,
            user_id=kaiser.id
        ),
        Quest(
            title='Protect the Innocent Farmer',
            description='A farmer has been falsely accused of witchcraft. Defend him before the tribunal.',
            status='failed',
            difficulty='Medium',
            reward_gold=120,
            user_id=kaiser.id
        ),

        # Volstage - Ranger
        Quest(
            title='Map the Thornwood Forest',
            description='The Thornwood has never been fully charted. Venture in and create a reliable map.',
            status='active',
            difficulty='Medium',
            reward_gold=150,
            user_id=volstage.id
        ),
        Quest(
            title='Track the Missing Scout',
            description='A royal scout went missing three days ago in the Ashfield. Find them.',
            status='active',
            difficulty='Easy',
            reward_gold=90,
            user_id=volstage.id
        ),
        Quest(
            title='Hunt the Shadow Beast',
            description='A creature of darkness has been picking off livestock. Track it and bring back proof of its death.',
            status='failed',
            difficulty='Hard',
            reward_gold=280,
            user_id=volstage.id
        ),
    ]

    db.session.add_all(quests)
    db.session.commit()
    print("Quests seeded!")
    print("Done! Database seeded successfully.")