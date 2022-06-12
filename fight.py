import random

cards_p1 = 26
cards_p2 = 26
Round = 0

def calc():
    global cards_p1, \
        cards_p2, name_p1, name_p2
    num1 = random.randint(2, 14)
    num2 = random.randint(2, 14)
    if num1 > num2:
        cards_p1 += 1
        cards_p2 -= 1
        print(name_p1, "WON IN THIS ROUND!!!")
    elif num1 < num2:
        cards_p1 -= 1
        cards_p2 += 1
        print(name_p2, "WON IN THIS ROUND!!!")

    if num1 > 10 or num2 > 10:
        if num1 == 11 or num2 == 11:
            if num1 == 11:
                num1 = "J"
            if num2 == 11:
                num2 = "J"
        if num1 == 12 or num2 == 12:
            if num1 == 12:
                num1 = "Q"
            if num2 == 12:
                num2 = "Q"
        if num1 == 13 or num2 == 13:
            if num1 == 13:
                num1 = "K"
            if num2 == 13:
                num2 = "K"
        if num1 == 14 or num2 == 14:
            if num1 == 14:
                num1 = "A"
            if num2 == 14:
                num2 = "A"

    print(name_p1 + "_card :" + str(num1), name_p2 + "_card: " + str(num2))
    if num1 == num2:
        cards_p1 -= 1
        cards_p2 -= 1
        print("tie card! in war there are no winner. your card disappear ")


print("game start")
name_p1 = input("please enter your name(p1):")
name_p2 = input("please enter your name(p2):")
play = True
while play:
    Round += 1
    print(input("press enter to reveal.."))
    print('turn:' + str(Round))
    print(name_p1 + "_cards :" + str(cards_p1), name_p2 + "_cards : " +
          str(cards_p2))
    calc()
    if cards_p2 < 1:
        print(name_p1, "won!!! GG")
        play = False
    elif cards_p1 < 1:
        print(name_p2, "won!!! GG")
        play = False


