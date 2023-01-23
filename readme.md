# RPG-ENGINE alpha 0.1

This is a text-adventure rpg engine written from scratch entirely in python. I don't know what level of python I am but it's surely not expert, so I am open to advice or comments. Additionally, I'm still new to git so everything is going to be a little weird until I learn the best practices.

I'm not a coder by trade, just by hobby (and will be for the foreseeable future) so I can't guarantee this will be completely bug-free. Just using this to keep the existential dread from setting in.

See "The Backend" for some technical descriptions.

## Current Features

Just a basic walking and item grabbing simulator.

## Planned Features

These are features that I plan to add for the next couple of versions. 

* Cleaning up existing code.
* Documenting features I've added but haven't commented (this will never go away)
* Item slots, weight, and container capacity
* Game Menu with Inventory, Status, Map (really not sure how to do this)
* Interactive roomspace items like switches, buttons, etc.
* Closed, Locked, and Hidden directions, items, and containers
* Searching and Pondering (pondering for hints)

## Future Features

These are features that will go in future iterations of the game, but haven't necessarily been planned yet. I am nothing if not ambitious.

Think of these features as major-version releases.

### Quests

* I want them
* Quests that progress the story (and world), side-questlines, and side-quests, like every other game.
* Different end-states to quests that will open up different paths
* **IDEALLY**: The ability to make a sandbox game with this.

### Dialogue

* You like morrowind? That's what I want. I know you're reinstalling it right now.
    * If you haven't played, dialogue works by having an NPC say something, and certain keywords appear.
    * Those keywords can be clicked on to get further context, and so on.
* In text-adventure-land, all the keywords will show up in a different color, and you are able to call on them.
    * Topics will be objects that can be called on by keywords. 
    * Going to use a key-value pair for this. key will be the keyword, value will be the dialogue.
    * Topics will be in an npc's "known topics"
* Keywords that appear will also be added to your journal, and you can ask other NPCs about keywords you know.
    * If the NPC doesn't know about the keyword, then there will be a default option.

### Character Creation

* Everything can be customized (it's your imagination)
* Classless (but templates will be available) and level-less (skill-based advancement, rip star wars galaxies)
* Some non-standard attribute system.
    * And an interactive way of setting these that explain what the attributes are and what they do.

### Combat

* Either automatic with *options* or turn-based (easiest) \
  I've never really liked turn based combat though, always feels a little gamey and unrealistic.
* Crunchy Combat Stats (because I'm *like that*)
* Vitality/Wound Point system (vitality regenerates on its own, wounds must be healed)
    * Vitality will decrease at its own rate, and can reduce your defense if too low.
    * Rate of decrease will depend on opponent and pc skill

## The Backend

Like I said above, this is all written in python. I'm using multiple inheritance to cut down on code repetition and to standardize methods. This is why both a player and a room are a container. They both have inventories. In some cases, that isn't really possible and I'll have to modify methods and stats. 