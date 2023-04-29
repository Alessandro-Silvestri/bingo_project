'''
BINGO mini PROJECT game

The program generates a bingo card with random numbers between 1 and 90
It will ask you what number has been called.
It will cover the number in the card with an 'X' accordingly.

Made by Alessandro Silvestri © 2022 <alessandro.silvestri.work@gmail.com>
'''


import random

def pretty_print(t):
    ''' repairing the bingo card table in the final result'''
    t = str(t)
    if len(t) == 1:
        return f'0{t}'
    return t

def show_card():
    '''It shows the bingo card updated with the values'''
    print(f'''
    {bingo_nums[0]}  |   {bingo_nums[1]}  | {bingo_nums[2]}
    ----+-------+----
    {bingo_nums[3]}  | Bingo | {bingo_nums[4]}
    ----+-------+----
    {bingo_nums[5]}  |   {bingo_nums[6]}  | {bingo_nums[7]}
    ''')

def check_win(x: list):
    '''It checks if all numbers are covered with 'X', thus if you have won'''
    win = True
    for i in x:
        if i.strip() != 'X':
            win = False
            break
    return win

# creating a list with all the numbers between 1 to 90 
all_numbers = [i for i in range(1, 91)]

# shuffle them
random.shuffle(all_numbers)

# choose the first 8 (the ones will be used for the bingo card)
bingo_nums = list(map(pretty_print, all_numbers[0:8]))

# routine with an infinite loop until all the numbers ar covered with 'X'
while True:
    show_card()
    num_call = input('What number was called: ')
    
    # if the called number is in your bingo card will be covered with 'X'
    if num_call in bingo_nums:
        bingo_nums = list(map(lambda x: x.replace(num_call, ' X'), bingo_nums)) 
        
    # if there are only 'X' in the bingo card you have won 
    if check_win(bingo_nums):
        print('BINGO!!')
        break

