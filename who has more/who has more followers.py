from data import data
from art import logo, vs
import random

__author__ = 'Nicolas de Moura'
__version__ = 0.9
__date__ = '03/04/2022'

def Show(data):
    a = random.randint(0, 49)
    b =  random.randint(0, 49)
    ad1 = data[a]
    ad2 = data[b]
    if ad2 == ad1:
        ad2 = data[b + 1]
    return ad1, ad2, a, b
def select(data, index1, index2):
    while True:
        pick = int(input("Type 1 or 2 to select a person: "))
        if pick == 1:
            return 1
            break
        elif pick == 2:
            return 2
            break
        else:
            print("Select 1 or 2")
def comparison(pick, index1, index2, data=data):
    if pick == data[index1]['follower_count']:
        if pick > data[index2]['follower_count']:
            print(f"Right! {data[index1]['name']} has more followers than {data[index2]['name']}")
            return 1
        else:
            print(f"Wrong! {data[index2]['name']} has more followers than {data[index1]['name']}")
            return 0
    elif pick == data[index2]['follower_count']:
        if pick > data[index1]['follower_count']:
            print(f"Right! {data[index2]['name']} has more followers than {data[index1]['name']}")
            return 1
        else:
            print(f"Wrong! {data[index1]['name']} has more followers than {data[index2]['name']}")
            return 0
def main():
    points = 0
    print(logo)
    while True:
        ad1, ad2, index1, index2 = Show(data)
        print("\nWhich one has more followers?: ")
        print(f"{ad1['name']}, {ad1['description']} from {ad1['country']}{vs}{ad2['name']}, {ad2['description']} from {ad2['country']}")    
        pick = select(data, index1, index2)
        if pick == 1:
            pick = data[index1]['follower_count']
            if comparison(pick, index1, index2) == 1:
                points += 1
            else:
                break
        if pick == 2:
            pick = data[index2]['follower_count']
            if comparison(pick, index1, index2) == 1:
                points += 1
            else:
                break
    print(f"You scored {points} points")
if __name__ == "__main__":
    main()
