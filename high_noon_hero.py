# High Noon Hero

import random
import sys
import time

print('"Lightning"')
print('It\'s Time to test your reflexes to see if you are \nThe Lightning Fast Shooter in the world.')
print('\nWhen you see \'SHOOT\',you have 0.3 seconds to press Enter.')
print('But you lose if you press Enter before\'SHOOT\' appears.\n')

input('Press Enter to begin...')

attempt = 1

while True:
    print('\nIt is high noon...')
    time.sleep(random.randint(20, 50)/10.0)
    print('SHOOT')
    draw_time = time.time()
    input()  # This function call doesn't return until Enter is pressed:
    time_elapsed = time.time() - draw_time

    if time_elapsed < 0.01:
        # If the player pressed Enter before DRAWN! appeared, the input() call returns almost instantly:
        print('You sling before "Shoot" appeared! You lose.')
    elif time_elapsed > 0.3:
        time_elapsed = round(time_elapsed, 4)
        print('you took', time_elapsed, 'seconds to shoot. Too slow!')
    else:
        time_elapsed = round(time_elapsed, 4)
        print('you took', time_elapsed, 'seconds to shoot. You wind!')

    print(f'\nAttempt #{attempt}')
    attempt += 1

    print('Enter (Q)uit to stop, or press Enter to play again.')
    response = input('>').upper()
    if response == 'Q':
        print('Goodbye Lightning!')
        sys.exit()
