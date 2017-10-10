morse_code = {
    "A" : ".-", 
    "B" : "-...", 
    "C" : "-.-.", 
    "D" : "-..", 
    "E" : ".", 
    "F" : "..-.", 
    "G" : "--.", 
    "H" : "....", 
    "I" : "..", 
    "J" : ".---", 
    "K" : "-.-", 
    "L" : ".-..", 
    "M" : "--", 
    "N" : "-.", 
    "O" : "---", 
    "P" : ".--.", 
    "Q" : "--.-", 
    "R" : ".-.", 
    "S" : "...", 
    "T" : "-", 
    "U" : "..-", 
    "V" : "...-", 
    "W" : ".--", 
    "X" : "-..-", 
    "Y" : "-.--",
    "Z" : "--.."
}

def encode_morze(text):
	text = text.upper().strip()
	encoded = ''
	
	for char in text:
		if char in morse_code:
			encoded += morse_code[char] + '__'
		elif char == ' ':
			encoded += '____'
	
	encoded = encoded.replace('.', '^_').replace('-', '^^^_')
	
	while len(encoded) and encoded[-1] == '_':
		encoded = encoded[:-1]
	
	return encoded



print(encode_morze('Morze code') == '^^^_^^^___^^^_^^^_^^^___^_^^^_^___^^^_^^^_^_^___^_______^^^_^_^^^_^___^^^_^^^_^^^___^^^_^_^___^', encode_morze('Morze code'))
print(encode_morze('Prometheus') == '^_^^^_^^^_^___^_^^^_^___^^^_^^^_^^^___^^^_^^^___^___^^^___^_^_^_^___^___^_^_^^^___^_^_^', encode_morze('Prometheus'))
print(encode_morze('SOS') == '^_^_^___^^^_^^^_^^^___^_^_^', encode_morze('SOS'))
print(encode_morze('1') == '', encode_morze('1'))