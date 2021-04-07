from Question import Question

question_prompts = [
	"Q1: What characteristic of secure communication is asymmetric encryption not able to achieve?\n(a) Confidentiality\n(b) Integrity\n(c) Authentication\n(d) None - it can achieve all the above characteristics when implemented well\n\n",
	"Q2: What is a well known problem with symmetric encryption?\n(a) The key has to be shared with all entities\n(b) It is easily cracked\n(c) It is harder to crack\n(d) There is no well known problem with symmetric encryption\n\n",
	"Q3: What advantage does symmetric encryption have over asymmetric encryption?\n(a) It is always easier to implement\n(b) They key doesn't need to be kept secret\n(c) It functions slowly due to the mathematical complexity involved\n(d) It is faster\n\n",
	"Q4: In asymmetric encryption, which key is used to encrpyt a message?\n(a) Public key\n(b) Private key\n(c) Either the public key or private key\n(d) Both the public key and private key\n\n",
	"Q5: Which cryptographic algorithm uses a Feistel network?\n(a) AES\n(b) DES\n(c) RSA\n(d) None of the above\n\n",
	"Q6: Which statement is false?\n(a) Electronic Code Book (ECB) mode encryption is hard to crack\n(b) An Initialisation Vector (IV) is used in Cipher book Chaining (CBC)\n(c) Nonce's are used in Counter Mode (CTR)\n(d) All statements are false\n\n",
	"Q7: Which cryptographic algorithm is typically known for satisfying the avalanche effect?\n(a) Asymmetric algorithms\n(b) Stream ciphers\n(c) Hash functions\n(d) None of the above\n\n",
	"Q8: RSA key generation: Given the starting primes p=29 and q=23, the modulus N would be:\n(a) 720\n(b) 616\n(c) 667\n(d) 6\n\n",
	"Q9: RSA key generation: Given the starting primes p=29 and q=23, the Euler Totient is:\n(a) 720\n(b) 616\n(c) 667\n(d) 6\n\n",
	"Q10: RSA key generation: Given the starting primes p=29 and q=23, a valid public key would be:\n(a) 23\n(b) 11\n(c) 28\n(d) 44\n\n",
	"Q11: RSA key generation: Given the public key from the previous question, the corresponding private key is:\n(a) 427\n(b) 390\n(c) 283\n(d) 375\n\n"
]

question_info = [
	"Digital signatures can provide both authenticity and integrity, while encryption provides confidentiality.\n\n",
	"The same key that is used to encode/decode messages has to be shared with with all entities. This makes it more likely that the key will become compromised.\n\n",
	"Asymmetric encryption involves complex mathemtical functions, and therefore functions slower compared with symmetric encryption.\n\n",
	"Either can can be used. If a public key is used to encrypt a message, only the person with the private key can decrypt it. If a private key is used to encrypt a message, anyone with the public key can decrypt it (thus verifying the the sender).\n\n",
	"AES uses a substitution-permutation network, and RSA is an asymmetric cipher.\n\n",
	"ECB is NOT hard to crack. It is known as the weakest block mode and should not be used.\n\n",
	"Hash functions generally operate in a manner where a slight change in an input changes the output significantly (for example SHA-1).\n\n",
	"The modulus N = p*q\n\n",
	"The Euler Totient = (p-1)*(q-1)\n\n",
	"23 is co-prime with the 616 (Euler Totient).\n\n",
	"Go to wolframalpha.com to double check if you are still unsure.\n\n"
]

questions = [
	Question(question_prompts[0], "d", question_info[0]),
	Question(question_prompts[1], "a", question_info[1]),
	Question(question_prompts[2], "d", question_info[2]),
	Question(question_prompts[3], "c", question_info[3]),
	Question(question_prompts[4], "b", question_info[4]),
	Question(question_prompts[5], "a", question_info[5]),
	Question(question_prompts[6], "c", question_info[6]),
	Question(question_prompts[7], "c", question_info[7]),
	Question(question_prompts[8], "b", question_info[8]),
	Question(question_prompts[9], "a", question_info[9]),
	Question(question_prompts[10], "d", question_info[10])
]

def start_test(questions):
	score = 0
	valid_input = ['a', 'b', 'c', 'd']
	print('\nPlease enter a, b, c or d as your answer. Good luck!\n') # Initial instructions given so that users enter a valid answer.
	for question in questions:
		answer = input(question.prompt)
		while answer not in valid_input: # Handles invalid input from user.
			print('\nInvalid input. Please enter a, b, c or d.\n')
			answer = input(question.prompt)
			continue
		if answer == question.answer:
			score += 1
			print('\nCorrect. ' + question.info) # Add the reasoning as to why the question is correct.
		else:
			print('\nIncorrect. The correct answer is ' + question.answer + '. ' + question.info) # Add the reasoning as to why the user's answer is incorrect.
	print("You got " + str(score) + "/" + str(len(questions)) + " correct.")

start_test(questions)