# dojo_pets

# Objectives

- More practice with OOP and class association.

# Ninja Class

# Attributes

- first_name
- last_name
- pet
- treats
- pet_food

# Methods

- walk()
- feed()
- bathe()

```
class Ninja:
    # implement __init__( first_name , last_name , treats , pet_food , pet )
    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    # feed() - feeds the ninja's pet invoking the pet eat() method
    # bathe() - cleans the ninja's pet invoking the pet noise() method
```

# Pet Class

# Attributes

- name
- type
- tricks
- health
- energy

# Methods

- sleep()
- eat()
- play()
- noise()

```
class Pet:
    # implement __init__( name , type , tricks ):
    # implement the following methods:
    # sleep() - increases the pets energy by 25
    # eat() - increases the pet's energy by 5 & health by 10
    # play() - increases the pet's health by 5
    # noise() - prints out pet's sound
```

# Tasks

- [X] Create a Ninja class with the ninja attributes listed above.

- [X] Create a Pet class with the pet attributes listed above.

- [X] Implement walk(), feed(), bathe() on the ninja class.

- [X] Implement sleep(), eat(), play(), noise() methods on the pet class.

- [X] Make an instance of a Ninja and assign them an instance of a pet to the pet attribute.

- [X] Have the Ninja feed, walk , and bathe their pet.

- [X] NINJA BONUS: Use modules to separate out the classes into different files.

- [ ] SENSEI BONUS: Use Inheritance to create sub classes of pets.

- [X] Compress or zip up assignment and upload it.
