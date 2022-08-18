import random

major_arcana = ["The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor", "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit", "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance", "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "The World"]

card_one = random.randrange(22)
card_two = random.randrange(22)
card_three = random.randrange(22)

while card_one == card_two or card_one == card_three or card_two == card_three:
  card_one = random.randrange(22)
  card_two = random.randrange(22)
  card_three = random.randrange(22)


print(str(major_arcana[card_one]) + ", ")
print(str(major_arcana[card_two]) + ", ")
print(str(major_arcana[card_three]))
