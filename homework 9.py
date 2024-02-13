'''
#Homework Chapter 9
#Question 1
#import random module
import random
#create the dictionary
capital_dic={ 'Alabama': 'Montgomery', 'Alaska': 'Juneau',
             'Arizona':'Phoenix', 'Arkansas':'Little Rock',
             'California': 'Sacramento', 'Colorado':'Denver',
             'Connecticut':'Hartford', 'Delaware':'Dover',
             'Florida': 'Tallahassee', 'Georgia': 'Atlanta',
             'Hawaii': 'Honolulu', 'Idaho': 'Boise',
             'Illinios': 'Springfield', 'Indiana':
             'Indianapolis', 'Iowa': 'Des Monies',
             'Kansas': 'Topeka', 'Kentucky': 'Frankfort',
             'Louisiana': 'Baton Rouge', 'Maine': 'Augusta',
             'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
             'Michigan': 'Lansing', 'Minnesota': 'St. Paul',
             'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
             'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Neveda': 'Carson City',
             'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
             'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck',
             'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania':
             'Harrisburg', 'Rhoda Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakoda':
             'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
             'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':
             'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne' } 
#Variables that will track how many times the user answered,
#and whether those answers were correct or incorrect
answers=0
correctAnswers = 0
incorrectAnswers = 0
#created a while loop because i like them better
while True:
    #Convert to a str to make use random module and items to make iterable
    capital_dicList= list(capital_dic.keys())
    #Here I am using random.choice, I was unaware how to get 
    #this far with using random.randint without it being
    #super long and tedious
    randomKey=(random.choice(capital_dicList))
    #Input question for the key
    question = input("what is the capital of " + randomKey + "? ")
    #If the question is not correct
    if question != capital_dic.pop(randomKey):
        #print incorrect and tally up incorrect answers
        print("Incorrect")
        incorrectAnswers += 1
        answers+=1
        #tracks the amount of answers 
        if answers >= 5:
            break
    else:
        print("Correct!")
        correctAnswers += 0
        answers+=1
        if answers >= 5:
            break
print("The amount of correct answers you got was", correctAnswers)
print("The amount of incorrect answers you got was", incorrectAnswers)


#Question number 2
#create the code dictionary
codes = { 'a' : '!', 'b' : '*', 'c' : '(', 'd' : '&', 'e' : '#', 'f' : "^", 'g': '!', 'h' : '@',
         'i' : '#', 'j' : '$', 'k' : '%', 'l' : '^', 'm' : '&', 'n' : '*', 'o' : '*', 'p' : '(',
         'q' : ')', 'r' : '!', 's' : '@', 't' : '#', 'u' : '$', 'v' : '%', 'w' : '^', 'x' : '&'
         , 'y' : '*', 'z' : '('}

#ask user to enter a string
userString = str(input("Enter a string: "))
#make for loop to iterate through userString
for key in userString:
    #print keys associated
    print(codes.get(key))

#Question 3
#ask the user to enter a sentence
userSentence = str(input("Enter a sentence: "))
#split each part into separate words and update variable
userSentence = userSentence.split(' ')

#convert list into set
userSet = set(userSentence)
#sets print all unique words
print(userSet)
#i forgot sets automatically print all unique
#words and was searching for a function on
#the power point to do what otherwise was 
#already done haha
'''
# This program uses a dictionary as a deck of cards.
import random

def main():
    # Create a deck of cards.
    deck = create_deck()

    # Get the number of cards to deal.
    num_cards = int(5)

    
    # Deal the cards to 4 people.
    for i in range(1):
        print('Cards remaining: ',len(deck))
        print('Hand',i+1)
        score = deal_cards(deck, num_cards)
        print('Value of this hand:', score)
        score1 = score
    for i in range(1):
        print('Cards remaining: ',len(deck))
        print('Hand',i+1)
        score = deal_cards(deck, num_cards)
        print('Value of this hand:', score)
        score2 = score
    for i in range(1):
        print('Cards remaining: ',len(deck))
        print('Hand',i+1)
        score = deal_cards(deck, num_cards)
        print('Value of this hand:', score)
        score3 = score
    for i in range(1):
        print('Cards remaining: ',len(deck))
        print('Hand',i+1)
        score = deal_cards(deck, num_cards)
        print('Value of this hand:', score)
        score4 = score
        
        #says the highest for all that are the highest value
        if score1 > score2 and score3 and score4:
            print("The first hand was the highest")
        if score2 > score1 and score3 and score4:
            print("The second hand was the highest")
        if score3 > score1 and score2 and score4:
            print("The third hand was the highest")
        if score4 > score1 and score2 and score3:
            print("The fourth hand was the highest")
# The create_deck function returns a dictionary
# representing a deck of cards.
def create_deck():
    # Create a dictionary with each card and its value
    # stored as key-value pairs.
    deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3,
            '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
            '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
            '10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10, 'King of Spades': 10,
            
            'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
            '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
            '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
            '10 of Hearts':10, 'Jack of Hearts':10,
            'Queen of Hearts':10, 'King of Hearts': 10,
            
            'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,
            '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
            '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
            '10 of Clubs':10, 'Jack of Clubs':10,
            'Queen of Clubs':10, 'King of Clubs': 10,
            
            'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
            '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
            '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
            '10 of Diamonds':10, 'Jack of Diamonds':10,
            'Queen of Diamonds':10, 'King of Diamonds': 10}

    # Return the deck.
    return deck

# The deal_cards function deals a specified number of cards
# from the deck.

def deal_cards(deck, number):
    # Initialize an accumulator for the hand value.
    hand_value = 0

    # Make sure the number of cards to deal is not
    # greater than the number of cards in the deck.
    if number > len(deck):
        number = len(deck)

    temp_deck=list(deck.items())
    # Deal the cards and accumulate their values.
    for count in range(number):
        card_to_pop=random.randint(0,len(temp_deck)-1)
        card, value = temp_deck[card_to_pop]
        del temp_deck[card_to_pop]
        deck.pop(card,'Not found')
        print(card)
        hand_value += value

    # return the value of the hand.
    return hand_value

# Call the main function.
main()
