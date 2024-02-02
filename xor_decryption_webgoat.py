#first step : base64 decode for this base64 encoded text 
#Oz4rPj0+LDovPiwsKDAtOw==
# lets begin

import base64

encoded_text ="Oz4rPj0+LDovPiwsKDAtOw=="

decoded_text = base64.b64decode(encoded_text)

print(decoded_text)

#alright lets we decrypt xor this ;>+>=>,:/>,,(0-; 
#before we need a key for xor decrypt but we dont have a key then we can try

possible_keys = range(256)

for key in possible_keys:
	decrypted = ""
	for byte in decoded_text:
		decrypted += chr(byte ^ key) #xor
	
	is_valid = True

	for c in decrypted:
		#we need only necessary chars else no valid
		if not(32<=ord(c)<=126 or c in '\n\t\r'):
			is_valid = False
			break

	if(is_valid):
		print(f"key:{key}")
		print(decrypted.lower())