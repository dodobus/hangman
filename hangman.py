aim = ["red", "green", "yellow", "blue", "purple", "principle"]

import random

pick = random.randint(0,6)
pick = int(pick)
word = aim[pick]

def hangman(word):
    wrong = 0
    stage = ["",
        "______________",
        "|             ",
        "|       |     ",
        "|       O     ",
        "|      /|\    ",
        "|      / \    ",
        "|             ",
        ]
    answer = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcom yo Hangman")

    while wrong < len(stage) - 1:
        print("\n")
        put = "Guess a letter"
        a = input(put)
        if a in answer:
            x = answer.index(a)
            board[x] = a
            answer[x] = "!"
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stage[0:e]))

        if "_" not in board:
            print("You Win")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stage[0:wrong]))
        print("You Lose! The word is {}.".format(word))
   
hangman(word)
