"""A collection of function for doing my project."""

import random
import vlc

def pick_database (number=1):
    """Returns a random word from the database name given as the parameter
    
    Parameters
    ----------
    word : number
        number that coordinates to a certain database
 
        
    Returns
    -------
    Returns a random word from the chosen database
    """
    
    # Databases
    artists = ['ILLENIUM', 'Seven Lions', 'Slander', 'Gryffin', 'Madeon', 'Dabin', 'Porter Robinson', 'Jai Wolf',
               'Boombox Cartel', 'NGHTMRE', 'Said The Sky', 'San Holo', 'Cash Cash', 'Galantis', 'Louis The Child',
               'RL Grime']
    songs = ['Good Things Fall Apart', 'Strangers', 'Potions', 'Tie Me Down', 'All My Friends', 'Part-Time Lover',
             'Shelter', 'Starlight', 'Whisper', 'Gud Vibrations', 'Just Us', 'Light', 'Take Me Home', 'Love On Me',
             'Better Not', 'I Wanna Know']
    
    # Checks which database was chosen
    if number == 1:
        return random.choice(artists)
    elif number == 2:
        return random.choice(songs)


def right_letter(word, letter):
    """Returns index(es) of the letter in the word
    
    Parameters
    ----------
    word : string
        word trying to guess
        
    letter : character
        character guessed if in word
 
        
    Returns
    -------
    Returns a list of index(es) of character, or an array of -1 if not found
    """
    
    # Lowercase version of word and character
    lower_word = word.lower()
    lower_letter = letter.lower()
    
    # List to track indexes
    index_list = []
    
    # Counter for list index
    list_counter = 0
    
    # Counter for word
    word_counter = 0
    
    # Keeps searching word for one or multiple occurances of character
    while word_counter < len(word):
        
        # Appends index to list
        word_index = lower_word.find(lower_letter, word_counter)
        index_list.append(word_index)
        
        # Updates word_counter to check rest of string for multiple occurances
        word_counter = word_index + 1
        
        # Checks to break loop if no character was found
        if word_index == -1:
            break
        
    return index_list


def print_word(word, guessed):
    """Prints the correctly guessed letters 
    
    Parameters
    ----------
    word : string
        word trying to guess
        
    guessed : string
        string of correctly guessed letters
 
        
    Returns
    -------
    Does not return anything, but prints out the correct letters and remaining ones as well
    """
    
    print('\n')
    
    # Goes through both strings to see if a letter should be printed
    for i in range(len(word)):
        
        # Checks to see if a letter was guessed correctly
        check_word = not word[i].isalpha()
        check_guess = not guessed[i].isalpha()
        
        if guessed[i] == ' ' and word[i] == ' ':
            print(' ', end="")
        elif check_guess and check_word:
            print(word[i] + ' ', end="")
        elif guessed[i] == ' ':
            print('_ ', end="")
        else:
            print(word[i] + ' ', end="")
            

def update_guessed(word, guessed, correct_index):
    """Updates the guessed word string
    
    Parameters
    ----------
    word : string
        word trying to guess
        
    guessed : string
        string of correctly guessed letters
        
    correct_index : list
        list of indexes correctly guessed
 
        
    Returns
    -------
    Returns an updated guessed word string
    """
    
    # Iterates through correct_index to update guessed
    for index in range(len(correct_index)):
        
        # Index of guessed character
        guessed_index = correct_index[index]
        
        # Checks for -1 as it signals failed search
        if correct_index[index] != -1:
            
            guessed = guessed[:guessed_index] + word[guessed_index] + guessed[guessed_index + 1:]
    
    return guessed


def guess_word(word):
    """Creates the guessWord string
    
    Parameters
    ----------
    word : string
        word trying to guess
 
        
    Returns
    -------
    Returns a newly created guessed word string
    """
    guessed = ' ' * len(word)
    
    # Iterates through correct_index to update guessed
    for index in range(len(word)):
        
        check_alpha = word[index].isalpha()
        
        # Checks for -1 as it signals failed search
        if check_alpha == False:
            
            guessed = guessed[:index] + word[index] + guessed[index + 1:]
    
    return guessed


def create_song_name (word, database_choice):
    """Creates a string of the song name location depending on which word was used
    
    Parameters
    ----------
    word : string
        word that was guessed
 
    database_choice : int
        which database was chosen to pick the random word from
    
        
    Returns
    -------
    Returns a string that is the location of the song to be played
    """
    
    # Databases
    artists = ['ILLENIUM', 'Seven Lions', 'Slander', 'Gryffin', 'Madeon', 'Dabin', 'Porter Robinson', 'Jai Wolf',
               'Boombox Cartel', 'NGHTMRE', 'Said The Sky', 'San Holo', 'Cash Cash', 'Galantis', 'Louis The Child',
               'RL Grime']
    songs = ['Good Things Fall Apart', 'Strangers', 'Potions', 'Tie Me Down', 'All My Friends', 'Part-Time Lover',
             'Shelter', 'Starlight', 'Whisper', 'Gud Vibrations', 'Just Us', 'Light', 'Take Me Home', 'Love On Me',
             'Better Not', 'I Wanna Know']
    
    # Sets index to figure out filename
    if database_choice == 1:
        song_index = artists.index(word)
    else:
        song_index = songs.index(word)
        
    # Special case made for artist name that started with 'n'
    if song_index == 9:
        return 'Songs\\' + songs[song_index] + '.mp3'
    
    return 'Songs\\' + artists[song_index] + '.mp3'


def pick_hint(word, database_choice, difficulty):
    """Plays a song depending on which song/artist word was chosen
    
    Parameters
    ----------
    word : string
        word that was guessed
 
    database_choice : int
        which database was chosen to pick the random word from
    
    difficulty : string
        difficulty of the game
    
        
    Returns
    -------
    Returns a string that is the location of the song to be played as the hint depending on the difficulty
    """
    
    # Databases
    artists = ['ILLENIUM', 'Seven Lions', 'Slander', 'Gryffin', 'Madeon', 'Dabin', 'Porter Robinson', 'Jai Wolf',
               'Boombox Cartel', 'NGHTMRE', 'Said The Sky', 'San Holo', 'Cash Cash', 'Galantis', 'Louis The Child',
               'RL Grime']
    songs = ['Good Things Fall Apart', 'Strangers', 'Potions', 'Tie Me Down', 'All My Friends', 'Part-Time Lover',
             'Shelter', 'Starlight', 'Whisper', 'Gud Vibrations', 'Just Us', 'Light', 'Take Me Home', 'Love On Me',
             'Better Not', 'I Wanna Know']
    easy_hints = ['Take You Down', 'Dreamin', 'Superhuman', 'obody Compares To You', "You're On", 'Alive',
                  'Sad Machine', 'Indian Summer', 'Whisper', 'Limelight', 'Show & Tell', 'We Rise', 'Matches',
                  'Runaway', 'Weekend', 'UCLA']
    med_hints = ["Where'd You Go", 'Ocean', 'All You Need To Know', 'Just For A Moment', 'Pay No Mind', 'In Flames',
                 'Divinity', 'Lose My Mind', 'How To Love', 'REDLIGHT', 'Rush Over Me', 'lift me from the ground', 'Belong',
                 'No Money', 'Last To Leave', 'Arcus']
    hard_hints = ['Feel Good', 'Freesol', 'First Time', 'Bye Bye', 'The City', 'Superstar',
                  'Flicker', 'Lost', 'ID', 'Needed You', "Sound Of Where'd You Go", 'show me', 'Millionaire',
                  'Tell Me You Love Me', 'Shake Something', 'Pressure']

    # Find index of word
    if database_choice == 1:
        song_index = artists.index(word)
    else:
        song_index = songs.index(word)
    
    # Return string depending on difficulty
    if difficulty.lower() == 'easy':
        return 'Songs\\' + easy_hints[song_index] + '.mp3'
    elif difficulty.lower() == 'medium':
        return 'Songs\\' + med_hints[song_index] + '.mp3'
    else:
        return 'Songs\\' + hard_hints[song_index] + '.mp3'