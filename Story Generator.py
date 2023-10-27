import random

def generate_story():
    # Define the elements of the story
    characters = ["Alice", "Bob", "Eve", "Charlie"]
    places = ["forest", "castle", "beach", "mountain"]
    actions = ["found a treasure", "saved a lost puppy", "discovered a secret passage", "won a singing contest"]

    # Generate random elements for the story
    character = random.choice(characters)
    place = random.choice(places)
    action = random.choice(actions)

    # Create the story
    story = f"Once upon a time, {character} went to the {place} and {action}."

    return story

# Generate and print a random story
random_story = generate_story()
print(random_story)
