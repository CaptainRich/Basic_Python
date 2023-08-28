# This routine generates a random poem from five different lists of 
# component words.  This exercise is from "Python Basics", section 9.5.

import random

# Define the words in the sentence (poem) categories.
nouns        = [ "fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla" ]
verbs        = [ "kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles" ]
adjectives   = [ "furry", "balding", "incredulous", "fragrant", "exuberant", "glistening" ]
prepositions = [ "against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within" ]
adverbs      = [ "curiously", "extravagantly", "tantalizingly", "furiously", "sensuously" ]


#########################################################################################################
def select_words( category, number ):
    # This function returns a list containing "number" words from the provided category.
    words = []

    for i in range( number ):   # Loop to acquire the specified number of words
        new_word = random.choice( category ) 

        # If the (randomly selected) new_word is already in the list, ignore it and get another.
        duplicate = True                # Assume the new word is a duplicate
        while duplicate == True:

            if i == 0:                  # Always include the very first random word selected.
                break

            for j in range( i ):        # Check the new word against the existing list.

                if new_word == words[j]:
                    new_word = random.choice( category )
                    break
                else:
                    duplicate = False
                    break

        words.append( new_word )
            

    return( words )


#########################################################################################################
def get_all_words( ):

    # Acquire the various component (category) words.
    poem_nouns = select_words( nouns, 3 )
    print( "\nThe selected nouns are: ", poem_nouns )

    poem_verbs = select_words( verbs, 3 )
    print( "The selected verbs are: ", poem_verbs )

    poem_adjs = select_words( adjectives, 3 )
    print( "The selected adjectives are: ", poem_adjs )

    poem_preps = select_words( prepositions, 2 )
    print( "The selected prepositions are: ", poem_preps )

    poem_adverbs = select_words( adverbs, 1 )
    print( "The selected adverbs are: ", poem_adverbs )

    return( poem_nouns, poem_verbs, poem_adjs, poem_preps, poem_adverbs )


#########################################################################################################
# This is the main routine, which selects the words for the poem, and constructs the poem.

# Acquire the random poem words from the categories.
poem_nouns, poem_verbs, poem_adjs, poem_preps, poem_adverbs = get_all_words()

# Construct the poem, index values are given (specified) in the text.
print( " " )
print( f"A {poem_adjs[0]} {poem_nouns[0]} {poem_verbs[0]} {poem_preps[0]} the {poem_adjs[1]} {poem_nouns[1]} ")
print( f"{poem_adverbs[0]} the {poem_nouns[0]} {poem_verbs[1]} ")
print( f"the {poem_nouns[1]} {poem_verbs[2]} {poem_preps[1]} a {poem_adjs[2]} {poem_nouns[2]}. ")
print( " " )
