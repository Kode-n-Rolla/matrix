# In cmd for realism write 'color 02'. Terminal text change color will turn green

import random, shutil, sys, time

# Set up the constants
# min_length = int(input('Set the min length'))
# max_length = int(input('Set the max length'))
min_length = 6
max_length = 14
pause = 0.1
symbols = [0, 1, 'シ', '٢', '٠', '١', '٣', '٤', '٥', '٦', '٧', '٨', '٩', 'ン', 'ワ', 'ラ', 'ヤ',
           'マ', 'ハ', 'ナ', 'タ', 'サ', 'カ', 'ア', 'リ', 'ミ', 'ヒ', 'ニ', 'チ', 'キ', 'イ', 'ポ'
           'ル', 'ユ', 'ム', 'フ', 'ヌ', 'ツ', 'ス', 'ク', 'ウ', 'レ', 'メ', 'ヘ', 'ネ', 'テ', 'ズ'
           'セ', 'ケ', 'エ', 'ヲ', 'ロ', 'ヨ', 'モ', 'ホ', 'ノ', 'ト', 'ソ', 'コ', 'オ', 'ᖆᖇ', 'ゼ']

# Density can range from 0.0 to 1.0
density = 0.02

# Get the size of the terminal window
width = shutil.get_terminal_size()[0]
# Can`t print to the last column on Windows OS without it adding
# a newline automatically, so reduce the width by one:
width -= 1

print('Press Ctrl+C to quit (cmd).')
time.sleep(2)

try:
    # For the column, when the counter is 0, no stream is show.
    # Otherwise, it acts as a counter for how many times an one of the symbols
    # should de displayed in that columns
    columns = [0] * width
    while True:
        # Set up the counter for each columns
        for i in range(width):
            if columns[i] == 0:
                if random.random() <= density:
                    # Restart a stream on this column
                    columns[i] = random.randint(min_length, max_length)

            # Display an empty space or some another symbols
            if columns[i] > 0:
                print(random.choice(symbols), end='')
                columns[i] -= 1
            else:
                print(' ', end='')
        print() # Print a newline at the end of the row of columns
        sys.stdout.flush() # Make sure text appears on the screen
        time.sleep(pause)
except KeyboardInterrupt:
    sys.exit() # When Ctrl-C is pressed, end the program