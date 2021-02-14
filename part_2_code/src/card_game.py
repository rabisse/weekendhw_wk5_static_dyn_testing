### Testing task 2 code:

# Carry out dynamic testing on the code below.

# Correct the errors below that you spotted in task 1.

class CardGame:
  def __init__(self, card1, card2):
    self.card1 = card1
    self.card2 = card2

  def check_for_ace(self):
    if self.card1.value == 1 or self.card2.value == 1:
      return True
    else:
      return False

  def highest_card(self):
    if self.card1.value > self.card2.value:
      return self.card1
    elif self.card2.value > self.card1.value:
      return self.card2
    else:
      return "Tie"

  def cards_total(self):
    total = 0
    cards = [self.card1, self.card2]
    for card in cards:
      total += card.value
    return "You have a total of " + str(total)
