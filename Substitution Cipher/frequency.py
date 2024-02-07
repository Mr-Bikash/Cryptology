def character_frequency(input_string):

    char_frequency = {}

    for char in input_string:
        if char.isalnum():
            char = char.lower()
            
            char_frequency[char] = char_frequency.get(char, 0) + 1

    sorted_frequency = dict(sorted(char_frequency.items(), key=lambda item: item[1], reverse=True))

    return sorted_frequency

# Example usage
input_string = """Mewa wa mey twsam iepjoys gt mey ipbya. Pa xgn iph ayy, meysy wa hgmewhr gt whmysyam wh mey iepjoys. Agjy gt mey kpmys iepjoysa vwkk oy jgsy whmysyamwhr meph mewa ghy! Mey iguy nayu tgs mewa jyaapry wa p awjfky anoamwmnmwgh iwfeys wh vewie uwrwma epby oyyh aewtmyu ox 8 fkpiya. Mey fpaavgsu wa "mxSrN03uwdd" vwmegnm mey dngmya."""
frequency = character_frequency(input_string)

# Print the character frequencies in descending order of frequency
for char, count in frequency.items():
    print(f"'{char}': {count}")
