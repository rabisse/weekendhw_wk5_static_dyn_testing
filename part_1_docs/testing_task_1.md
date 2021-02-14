### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
# needs to have a 'def __init__' to initialize the class with attributes

  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
# else needs a colon

  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
# should be 'def' not dif
# everything below should be indented
# missing a comma between card1 and card2
# 'card' should be 'card1'
# returns card2 as highest even when it's a tie

def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
# everything should be indented one level
# should say that total = 0
# the last line should be indented to the level of total and for (1 less level than it's written)
# there should be a space after 'of'
# total is an int and needs to be converted to a string
```
