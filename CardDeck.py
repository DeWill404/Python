'''
John have infinite no. of rummy card,
	all sorted in order...
Crads are placed in the form of decks....
	and First deck have {hearts, clubs, spades, daimonds} types of cards...
		spades deck have {daimonds, hearts, clubs, spades}
		Third deck have {spades, daimonds, hearts, clubs}
		Forth deck have {clubs, spades, daimonds, hearts}
		Fifth deck have {hearts, clubs, spades, daimonds}
		..... and so on,
Each type of card consist of 13 card in this order...
	{one, two, three, four, five, six, seven, eight, nine, ten, joker, queen, king}

So Cards of heart is given by....
one of hearts
two of hearts
three of hearts
four of hearts
five of hearts
six of hearts
seven of hearts
eight of hearts
nine of hearts
ten of hearts
joker of hearts
queen of hearts
king of hearts

Given the no. of card, find its name....
e.g.
	40       => one of spades
	143      => king of hearts
	25000    => one of spades
	245      => joker of spades
	10000200 => two of diamonds
	30448    => two of clubs
	482722   => six of clubs
'''

deck = [[ "hearts", "clubs", "spades", "daimonds" ],
		[ "daimonds", "hearts", "clubs", "spades" ],
		[ "spades", "daimonds", "hearts", "clubs" ],
		[ "clubs", "spades", "daimonds", "hearts" ]]

card = ["one of ",
		"two of ",
		"three of ",
		"four of ",
		"five of ",
		"six of ",
		"seven of ",
		"eight of ",
		"nine of ",
		"ten of ",
		"joker of ",
		"queen of ",
		"king of "]

l = [40, 143, 25000, 245, 10000200, 30448, 482722]

for number in l:
	card_no = number-1
	deck_index = (card_no // 52) % 4
	card_no %= 52
	card_type = card_no // 13
	card_name = card_no % 13
	print( f"No {number} in deck {deck_index} of type {card_type} at card {card_name}" )
	print( "\t-> "+card[card_name] + deck[deck_index][card_type] )