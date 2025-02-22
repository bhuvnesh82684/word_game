import uuid

from flask import jsonify

import model.response as response
from service import word_dictionary

id_dictionary = dict()

def word_selection(id):
    if not id_dictionary.__contains__(id):
        word = word_dictionary.random_word_selection()
        id_dictionary[id] = word
    return id_dictionary[id]


def word_check(id,word):
    user_win_status = False
    correct_char = 0
    correct_char_with_position = 0

    selected_word = word_selection(id)
    if len(word) != len(selected_word):
        print("incorrect input")

    if selected_word == word:
        print("Congrats you win this game, word is "+ selected_word)
        user_win_status = True

    for i in range(len(selected_word)):
        if selected_word[i] == word[i]:
            correct_char_with_position += 1

    counter = 0
    for i in word:
        if i in selected_word and selected_word[counter] != word[counter]:
            correct_char += 1
        counter += 1

    print("correct char with position: "+str(correct_char_with_position))
    print("correct char: "+str(correct_char))

    return jsonify({
        "win_status": user_win_status,
        "correct_char": correct_char,
        "correct_char_with_position": correct_char_with_position
    })


