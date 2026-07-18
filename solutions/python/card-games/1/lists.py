"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    Parameters:
        number (int): The current round number.

    Returns:
        list: The current round number and the two that follow.
    """

    return [number,number+1,number+2]



def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    Parameters:
        rounds_1 (list): The first rounds played.
        rounds_2 (list): The second group of rounds played.

    Returns:
        list:  All rounds played.
    """
    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    Parameters:
        rounds (list): The rounds played.
        number (int): The round number.

    Returns:
        bool: Was the round played?
    """

    return number in rounds 


def card_average(hand):
    """Calculate and returns the average card value from the list.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        float: The average value of the cards in the hand.
    """
    return sum(hand)/len(hand)




def approx_average_is_average(hand):
     # 1. Calculate the actual average
     actual_avg = sum(hand) / len(hand)
    
     # 2. Calculate the average of the first and last cards
     first_last_avg = (hand[0] + hand[-1]) / 2
    
     # 3. Find the middle card (median)
     # Using // gives us integer division so we get a whole number index
     middle_index = len(hand) // 2
     median = hand[middle_index]
    
     # 4. Check if the actual average matches either approximate average
     return actual_avg == first_last_avg or actual_avg == median


def average_even_is_average_odd(hand):
  #Slice out the card at evern indexes
  even_cards=hand[::2]

  #Slice out the cards at odd indexes
  odd_cards=hand[1::2]

  #Calculate the average of both slices
  even_avg = sum(even_cards)/len(even_cards)
  odd_avg = sum(odd_cards)/len(odd_cards)

  #Return whether they are equal
  return even_avg == odd_avg



def maybe_double_last(hand):
    # Check if the last card is an 11 using negative indexing
    if hand[-1] == 11:
        # Double the value of that specific card
        hand[-1] *= 2
        
    # Return the final list 
    return hand