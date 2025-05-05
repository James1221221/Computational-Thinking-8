import random

# Pick a word at random
word_list = ["loopy","heart","audio","laugh","trial", "slate", "dream", "brain", "press", "vital", "yield", "envoi", "fadge", "drupe", "ouija", "rural", "ergot", "abuzz", "borts", "imbue","abide", "apple", "angel", "actor", "altar",
"brave", "beach", "brush", "baker", "bound",
"cabin", "candy", "clear", "crisp", "crawl",
"dance", "draft", "drain", "daisy", "ditch",
"eager", "eagle", "early", "elite", "entry",
"faith", "fancy", "feast", "flame", "front",
"giant", "globe", "grape", "greet", "guide",
"habit", "happy", "harsh", "hatch", "honor",
"ideal", "image", "imply", "index", "irony",
"jelly", "jolly", "joint", "judge", "jumpy",
"karma", "kayak", "kneel", "knock", "known",
"label", "latch", "learn", "light", "liver",
"magic", "maker", "march", "match", "moral",
"naive", "nasty", "noble", "noisy", "novel",
"ocean", "offer", "often", "onion", "orbit",
"paint", "panel", "party", "peace", "prior",
"quack", "quake", "queen", "query", "quick",
"raise", "ranch", "reach", "right", "river",
"scale", "score", "sheep", "sight", "spice",
"table", "taste", "teach", "thing", "trust",
"ultra", "uncle", "under", "union", "upper",
"valid", "value", "vapor", "vivid", "vocal",
"waist", "watch", "water", "weird", "wrist",
"xenon", "xylem", "xerox", "xenia", "xysti",
"yacht", "yearn", "yeast", "yield", "young",
"zebra", "zilch", "zesty", "zonal", "zoomy" ]
hidden_word = random.choice(word_list)

# Repeat for 6 guesses
for i in range(6):
    # Guess a word
    guess_word = input()
    output = ""

    # First letter (in python, counting starts at 0 not 1)
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    
    if guess_word[1] == hidden_word[1]:
        output += "🟩"
    elif guess_word[1] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    if guess_word[2] == hidden_word[2]:
        output += "🟩"
    elif guess_word[2] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    if guess_word[3] == hidden_word[3]:
        output += "🟩"
    elif guess_word[3] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    if guess_word[4] == hidden_word[4]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"

    # Result
    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("You win")
        break

print(f"You used {i+1} guesses")
