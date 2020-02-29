#dice_roller.py

    Module that contains the capability to roll any number of dice with any amount of sides and can have a modifier be added to every roll

    Ability to roll with advantage or disadvantage

#TODO List:

#Character sheet

    Level

    Proficiency Bonus

    Skill / Saving throw proficiency / expertise

    Armor class

    Health (max and current)

    Simple built in race / class feats (like Lucky for halflings)

    Class

    Race

    Size

    Age

    Alignment

    Weapon (damage, what skill to roll)

Character sheets will be saved as json files for easy storage and editing

Ability to make a specific roll (i.e. rollInsight, rollDamage, etc)


#Character generator

    Random class

    Random race

    Random background

    Weapons

    Armor

    Gold

    Skills

    Health

    Age

    Size

    Alignment

      Can be point bought using standard array or rolled using the roll 4 d6 drop lowest for each skill

      Skills will be assigned from highest to lowest based on predetermined "rankings" for best skill of each class

  Can generate up to any level but will not select any spells or specializations (like Circle of Moon druid or Swashbuckler rogue)
  
  Characters will be saved as json files
  

#Random encounter generator

    Can generate encounters based off of

        Player level

        Party size

        Intended difficulty level

        Type of enemy
