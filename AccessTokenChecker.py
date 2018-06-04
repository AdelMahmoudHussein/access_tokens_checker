import requests
import time
print("Coder -> Mostafa M. Mead")
print("Github -> Github/AimMead")
print("FB -> FB/100010261237574")
print("")
def checkToken(tokensTxt):
	with open(tokensTxt) as f:
		lines = f.read().split("\n")
	count = 0
	for token in lines:
		url = requests.get("https://graph.facebook.com/me?access_token={0}".format(token))
		source = url.content
		count += 1
		if "first_name" in source.decode("utf-8"):
			goodTokens = open("goodTokens.txt" , 'a+')
			goodTokens.write(token + "\n")
			goodTokens.close()
			print("Checking Token Number -> {0}".format(count) , end="\r")
checkToken(input("Enter Tokens Path : "))
print("Done [+]")
time.sleep(500)
