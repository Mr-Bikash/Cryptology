def replace_multiple_characters(input_string, replacements):
    modified_string = ""
    for char in input_string:
        if char in replacements:
            modified_string += replacements[char]
        else:
            modified_string += char

    return modified_string

# Example usage
input_string = """Mewa wa mey twsam iepjoys gt mey ipbya. Pa xgn iph ayy, meysy wa hgmewhr gt whmysyam wh mey iepjoys. Agjy gt mey kpmys iepjoysa vwkk oy jgsy whmysyamwhr meph mewa ghy! Mey iguy nayu tgs mewa jyaapry wa p awjfky anoamwmnmwgh iwfeys wh vewie uwrwma epby oyyh aewtmyu ox 8 fkpiya. Mey fpaavgsu wa "mxSrN03uwdd" vwmegnm mey dngmya."""

replacements = {
    "Y": "E", #most frequent
    "y": "e",
    "M": "T", #Relevent because we can see mee word frequently. Which may be the
    "m": "t",
    "E": "H", # after replacing y and m we can see too many words changes from mey to tee. So guess possible word must be The
    "e": "h",
    "W": "I", # After replacement first two word looks Thwa wa. This looks similler to This is. 
    "w": "i",
    "A": "S", 
    "a": "s",
    # "T": "F",
    # "t": "f", # after replace ment 4th word looks like first : tisst - first
    # "S": "R",
    # "s": "r", 
    # "P": "A", # only p is there. So p have two possible option a and i. But prior to that word "is" word is there. So most relevant replacement for p will be a.
    # "p": "a",
    # "H": "N", # After replacing above ihterest looks like interest
    # "h": "n",
    # "I": "C", # After replacing above ian looks like can
    # "i": "c",
    # "G": "O", # After replacing above gf looks like of
    # "g": "o",

    # # vhich -> which, habe -> have, oeen-> been

    # "V": "W",
    # "v": "w", 
    # "B": "V",
    # "b": "v",
    # "O": "B",
    # "o": "b",

    # # chajber -> chamber, snbstitntion -> substitution, cifher->cipher

    # "J": "M",
    # "j": "m", 
    # "N": "U",
    # "n": "u",
    # "F": "P",
    # "f": "p",

    # # wikk -> will, nothinr -> nothing, xou -> you, coue useu -> code used

    # "K": "L",
    # "k": "l", 
    # "R": "G",
    # "r": "g",
    # "X": "Y",
    # "x": "y",
    # "U": "D",
    # "u": "d",

    # # duotes -> quotes

    # "D": "Q",
    # "d": "q"
}



modified_string = replace_multiple_characters(input_string, replacements)

print(input_string) 
print("\n")
print(modified_string)  # Output: "xaiiu, Wirud!"
