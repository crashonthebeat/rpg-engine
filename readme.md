# RPG-ENGINE alpha 0.3

This repo is deprecated, there's too much spaghetti. Please see [ifrpg-engine](https://github.com/crashonthebeat/ifrpg-engine). 

This is an old version of the code that I have started rewriting as of 1/25/2023. The way I wrote items and containers proved to be way too much work and I belive that if I rewrite the item code, I can make things much more smoother down the road. I've also decided to add more travel methods and look methods before I start on items, and flesh out all kinds of "foot and eyeball" interactions before I move on to "hand stuff".

This is a text-adventure rpg engine written from scratch entirely in python. I don't know what level of python I am but it's surely not expert, so I am open to advice or comments. Additionally, I'm still new to git so everything is going to be a little weird until I learn the best practices.

I'm not a coder by trade, just by hobby (and will be for the foreseeable future) so I can't guarantee this will be completely bug-free. Just using this to keep the existential dread from setting in.

See "The Backend" for some technical descriptions.

## Current Features

* Walk between rooms! 
* Pick up and put down items!
* Equippable items!
* Look at yourself!
* Backpacks! You can put things in them, take things out, and look inside them.

## Planned Features

These are features that will be in the game engine as of version 1. 

* Documenting features I've added but haven't commented (this will never go away)
* Refactor the item find methods for better efficiency and reusability

* Item slots, weight, and container capacity
* Game Menu with Inventory, Status, Map (really not sure how to do this)
* Interactive roomspace items like switches, buttons, etc.
* Closed, Locked, and Hidden directions, items, and containers
* Searching and Pondering (pondering for hints)
* Basic dialogue and fetch-quests
* Puzzles

I may also end up doing a code rewrite before version 1.

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

### Combat

* Armor and Weapons
* Either automatic with *options* or turn-based (easiest) \
  I've never really liked turn based combat though, always feels a little gamey and unrealistic.
* Crunchy Combat Stats (because I'm *like that*)
* Vitality/Wound Point system (vitality regenerates on its own, wounds must be healed)
    * Vitality will decrease at its own rate, and can reduce your defense if too low.
    * Rate of decrease will depend on opponent and pc skill

### Character Creation

* Everything can be customized (it's your imagination)
* Classless (but templates will be available) and level-less (skill-based advancement, rip star wars galaxies)
* Some non-standard attribute system.
    * And an interactive way of setting these that explain what the attributes are and what they do.

## The Backend

Like I said above, this is all written in python. I'm using multiple inheritance to cut down on code repetition and to standardize methods. This is why both a player and a room are a container. They both have inventories. In some cases, that isn't really possible and I'll have to modify methods and stats. 

If you dig into the player methods, you'll see that I have several methods to "find" an item. This is because the player inputs a string, while the actual "item id" is an object. So, the program has to loop through the name attributes of every item in an inventory and look for a match, which will then return the object that matches.

I also have a lot of "return True" on these methods in order to keep them from passing an invalid variable to another if statement or loop in the same method. Since I'm using this also to get better at python and programming in general, these will be cleaned up in the future, unless that's just *how it's done* in which case the spaghetti stays.
