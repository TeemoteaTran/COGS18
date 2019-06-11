import random
import vlc

from functions import pick_database, right_letter, print_word
from functions import update_guessed, guess_word, create_song_name, pick_hint

def test_pick_database():

    artists = ['ILLENIUM', 'Seven Lions', 'Slander', 'Gryffin', 'Madeon', 'Dabin', 'Porter Robinson', 'Jai Wolf',
               'Boombox Cartel', 'NGHTMRE', 'Said The Sky', 'San Holo', 'Cash Cash', 'Galantis', 'Louis The Child',
               'RL Grime']
    songs = ['Good Things Fall Apart', 'Strangers', 'Potions', 'Tie Me Down', 'All My Friends', 'Part-Time Lover',
             'Shelter', 'Starlight', 'Whisper', 'Gud Vibrations', 'Just Us', 'Light', 'Take Me Home', 'Love On Me',
             'Better Not', 'I Wanna Know']

    artist = pick_database()
    song = pick_database(2)
    
    assert (artist in artists) == True
    assert (song in songs) == True

def test_right_letter():
	
	assert right_letter('Dabin', 'd') == [0, -1]
	assert right_letter('San Holo', '') == [0, 1, 2, 3, 4, 5, 6, 7]
	assert right_letter('Gryffin', 'f') == [3, 4, -1]
	assert right_letter('NGHTMRE', 'x') == [-1]
	assert right_letter('RL Grime', 'e') == [7]

def test_print_word():
	
	assert print_word('Dabin', '     ') == None
	assert print_word('Seven Lions', 'S         s') == None

def test_update_guessed():

    assert update_guessed('Dabin', '     ', [0]) == 'D    '
    assert update_guessed('San Holo', 'San     ', [5, 7]) == 'San  o o'
    assert update_guessed('Seven Lions', '           ', [-1]) == '           '

def test_guess_word():

	assert guess_word('Part-Time Lover') == '    -          '
	assert guess_word('Better Not') == '          '
	assert guess_word('Dabin') == '     '

def test_create_song_name():
    
    assert create_song_name('ILLENIUM', 1) == 'Songs\\ILLENIUM.mp3'
    assert create_song_name('Potions', 2) == 'Songs\\Slander.mp3'
    assert create_song_name('I Wanna Know', 2) == 'Songs\\RL Grime.mp3'

def test_pick_hint():
    
    assert pick_hint('Dabin', 1, 'hard') == 'Songs\\Superstar.mp3'
    assert pick_hint('Shelter', 2, 'medium') == 'Songs\\Divinity.mp3'
    assert pick_hint('RL Grime', 1, 'easy') == 'Songs\\UCLA.mp3'
