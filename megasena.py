import pyautogui as pg
import time
import pyperclip as pc
import random
# Creating the lottery numbers:
games = [[], [], []]  # Where the numbers will be saved.

# Programmed to emit 3 sequences at a time
for x in range(0, 3):
    for each in range(0, 10):
        if len(games[x]) > 5:
            break
        else:
            lucky_number = random.randint(1, 60)
            if lucky_number in games[x]:
                continue
            else:
                games[x].append(lucky_number)

# Pause after each call.
pg.PAUSE = 1

# Opening Chrome and Gmail.
pg.press('win')
pg.write('chrome')
pg.press('Enter')
time.sleep(4)
# Click to select chrome profile
pg.click(x=776, y=427)
time.sleep(3)
# Open new tab
pg.hotkey('ctrl', 't')
pg.write('mail')
pg.press('Enter')
time.sleep(10)
# Compose mail option
pg.click(x=78, y=169)
time.sleep(8)
# Change e-mail accordingly.
pg.write('ajaymohaname@gmail.com')
pg.press('Tab')
pg.press('Tab')
pc.copy('Lottery - Lucky Numbers')
pg.hotkey('ctrl', 'v')
pg.press('Tab')
# Text for mail body
text = f'''
Hello Mr.Lucky,
    The 3 sets of lucky numbers are:
    Game 1: {games[0]}
    Game 2: {games[1]}
    Game 3: {games[2]}

Best of Luck!
'''
pc.copy(text)
pg.hotkey('ctrl', 'v')
time.sleep(3)
# Send
pg.hotkey('ctrl', 'enter')

