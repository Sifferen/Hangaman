import random
word= ['abruptly', 'absurd', 'abyss', 'affix', 'askew', 'avenue', 'awkward', 'axiom', 'azure', 'bagpipes', 'bandwagon', 'banjo', 'bayou', 'beekeeper', 'bikini', 'blitz', 'blizzard', 'boggle', 'bookworm', 'boxcar', 'boxful', 'buckaroo', 'buffalo', 'buffoon', 'buxom', 'buzzard', 'buzzing', 'buzzwords', 'caliph', 'cobweb', 'cockiness', 'croquet', 'crypt', 'curacao', 'cycle', 'daiquiri', 'dirndl', 'disavow', 'dizzying', 'duplex', 'dwarves', 'embezzle', 'equip', 'espionage', 'euouae', 'exodus', 'faking', 'fishhook', 'fixable', 'fjord', 'flapjack', 'flopping', 'fluffiness', 'flyby', 'foxglove', 'frazzled', 'frizzled', 'fuchsia', 'funny', 'gabby', 'galaxy', 'galvanize', 'gazebo', 'giaour', 'gizmo', 'glowworm', 'glyph', 'gnarly', 'gnostic', 'gossip', 'grogginess', 'haiku', 'haphazard', 'hyphen', 'iatrogenic', 'icebox', 'injury', 'ivory', 'ivy', 'jackpot', 'jaundice', 'jawbreaker', 'jaywalk', 'jazziest', 'jazzy', 'jelly', 'jigsaw', 'jinx', 'jiujitsu', 'jockey', 'jogging', 'joking', 'jovial', 'joyful', 'juicy', 'jukebox', 'jumbo', 'kayak', 'kazoo', 'keyhole', 'khaki', 'kilobyte', 'kiosk', 'kitsch', 'kiwifruit', 'klutz', 'knapsack', 'larynx', 'lengths', 'lucky', 'luxury', 'lymph', 'marquis', 'matrix', 'megahertz', 'microwave', 'mnemonic', 'mystify', 'naphtha', 'nightclub', 'nowadays', 'numbskull', 'nymph', 'onyx', 'ovary', 'oxidize', 'oxygen', 'pajama', 'peekaboo', 'phlegm', 'pixel', 'pizazz', 'pneumonia', 'polka', 'pshaw', 'psyche', 'puppy', 'puzzling', 'quartz', 'queue', 'quips', 'quixotic', 'quiz', 'quizzes', 'quorum', 'razzmatazz', 'rhubarb', 'rhythm', 'rickshaw', 'schnapps', 'scratch', 'shiv', 'snazzy', 'sphinx', 'spritz', 'squawk', 'staff', 'strength', 'strengths', 'stretch', 'stronghold', 'stymied', 'subway', 'swivel', 'syndrome', 'thriftless', 'thumbscrew', 'topaz', 'transcript', 'transgress', 'transplant', 'twelfth', 'twelfths', 'unknown', 'unworthy', 'unzip', 'uptown', 'vaporize', 'vixen', 'vodka', 'voodoo', 'vortex', 'walkway', 'waltz', 'wave', 'wavy', 'waxy', 'wellspring', 'wheezy', 'whiskey', 'whizzing', 'whomever', 'wimpy', 'witchcraft', 'wizard', 'woozy', 'wristwatch', 'wyvern', 'xylophone', 'yachtsman', 'yippee', 'yoked', 'youthful', 'yummy', 'zephyr', 'zigzag', 'zigzagging', 'zilch', 'zipper', 'zodiac', 'zombie']
answer= random.choice(word)
display=['_' for _ in range(len(answer))]
wrong_count=0

while True:
    print(display)
    guess=input("enter letter here/answer here: ")
    
    #if guess in answer:




    position = 0
    found=False
    for letter in answer:
        if letter == guess:
            found=True
            display[position] = letter
        position += 1

    if not found:
        wrong_count +=1
        if wrong_count==1:
            print("0")
        if wrong_count==2:
            print("0")
            print('!')
            print('!')
            print('!')

        if wrong_count==3:
            print("0")
            print('!-_')
            print('!')
            print('!')
        if wrong_count==4:
            print("  0")
            print('_-!-__')
            print('  !')
            print('  !')

        if wrong_count==5:
            print("  0")
            print('_-!-__')
            print('  !')
            print('_-!')

        if wrong_count==6:
            print("  0")
            print('_-!-__')
            print('  !')
            print('_-!-_')

        if wrong_count==7:
            print("  ")
            print('_-!-__')
            print('  !')
            print('_-!-_')
            print(F"Game over you lose the word was {answer} ")
            break
    if "_"not in display:
        print(f'the word is {answer} you win')
        break





