from time import sleep
from random import randint
def main():
    number_to_be_guessed = randint(0, 100)
    guessed_number = int(input("Guess a number:\n"))
    points = 100
    while guessed_number != number_to_be_guessed:
        if guessed_number > number_to_be_guessed:
            if (guessed_number - number_to_be_guessed) >= 50:
                print("The number is much lower than %s" %guessed_number)
                points -= 10
                sleep(1)
            elif(guessed_number - number_to_be_guessed) > 10 and (guessed_number - number_to_be_guessed) < 50:
                print("The number is lower than %s" %guessed_number)
                points -= 5
                sleep(1)
            elif(guessed_number - number_to_be_guessed) > 0 and (guessed_number - number_to_be_guessed) < 11:
                print("The number is a bit lower than %s" %guessed_number)
                points -= 2
                sleep(1)    
        elif (guessed_number < number_to_be_guessed):
            if (guessed_number - number_to_be_guessed) <= (-50):
                print("The number is much higher %s" %guessed_number)
                points -= 10
                sleep(1)
            elif(guessed_number - number_to_be_guessed) < (-10) and (guessed_number - number_to_be_guessed) > (-50) :
                print("The number is higher than %s" %guessed_number)
                points -= 5
                sleep(1)
            elif(guessed_number - number_to_be_guessed) < 0 and (guessed_number - number_to_be_guessed) > (-11):
                print("The number is a bit higher than %s" %guessed_number)
                points -= 2
                sleep(1)
        guessed_number = int(input("Guess a number:\n"))
    print("Right! %s is the correct number." %guessed_number)
    sleep(1)
    print("You did %s points" %points)
    sleep(2)


if __name__ == "__main__":
    main()