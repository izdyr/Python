import random

# Characters
characters = ["James", "George", "Oliver", "Jack", "William", "Alexander", "Charles", "Michael", "David", "Daniel", "Oscar", "Thomas", "Joseph", "John", "Elizabeth", "Olivia", "Charlie", "Robert", "Martin", "Emma", "Jacob", "Emily", "Mary", "John"]
# What are they doing ?
settings = ["in a forest", "on a beach", "in a city", "on a spaceship", "in a haunted mansion", "in a downtown", "in the home", "in a gameroom", "reading a book", "in the ship", "on the social media", "asking to AI", "wanna get A+ for exam"]
# What are they wanna todo ?
plots = ["searching for a lost artifact", "solving a mystery", "escaping from danger", "winning a competition", "saving the world"]

character = random.choice(characters)
setting = random.choice(settings)
plot = random.choice(plots)

# Print story
print("{0} found themselves {1}, {2}. They were {3}!".format(character, setting, plot, random.choice(["excited", "scared", "curious", "determined"])))
