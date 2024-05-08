import numpy as np
import random

mappings = {
 '0000': 'f', '0001': 'g', '0010': 'h', '0011': 'i',
 '0100': 'j', '0101': 'k', '0110': 'l', '0111': 'm',
 '1000': 'n', '1001': 'o', '1010': 'p', '1011': 'q',
 '1100': 'r', '1101': 's', '1110': 't', '1111': 'u'
}
rev_mappings = {
 'f': '0000', 'g': '0001', 'h': '0010', 'i': '0011',
 'j': '0100', 'k': '0101', 'l': '0110', 'm': '0111',
 'n': '1000', 'o': '1001', 'p': '1010', 'q': '1011',
 'r': '1100', 's': '1101', 't': '1110', 'u': '1111'
}

def input_gen(xor_value, input_file):

	binary_string = bin(xor_value)
	binary_string_padded = binary_string[2:].zfill(64)
	binary_list = list(binary_string_padded)
	intended_value = [int(bit) for bit in binary_list]


	plaintext_pairs=[]
	def generate_plaintext():
	    x = [random.choice(['f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u']) for _ in range(16)]
	    inp1 = ''.join(rev_mappings[char] for char in x) 
	    return [int(bit) for bit in inp1]


	def l2s(s):      
	    s1 = [str(x) for x in s] 
	    str1 = "".join(s1)   
	    return str1
	    

	for _ in range(1000):
	    random_plaintext = generate_plaintext()
	    xored_plaintext = list(np.bitwise_xor(random_plaintext, intended_value))
	    input1=""
	    for j in range(0,64,4):
	        temp1 = random_plaintext[j:j+4]
	       # print(temp1)
	        temp2 = l2s(temp1)
	       # print(temp2)
	        input1+=mappings[temp2]
	    plaintext_pairs+=[input1]
	    input2=""
	    for j in range(0,64,4):
	        temp1 = xored_plaintext[j:j+4]
	       # print(temp1)
	        temp2 = l2s(temp1)
	       # print(temp2)
	        input2+=mappings[temp2]
	    plaintext_pairs+=[input2]
	    #print(inputs)

	nw = open(input_file,"w")
	for plaintext in plaintext_pairs:
	    nw.write(plaintext+"\n")
	nw.close()

xor_value1 = 0x0000801000004000
input_file = 'input_strings1.txt'
input_gen(xor_value1, input_file)

xor_value2 = 0x0000080100100000
input_file = 'input_strings2.txt'
input_gen(xor_value2, input_file)