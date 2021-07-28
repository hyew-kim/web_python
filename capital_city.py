import sys

def findcapital():
	states = {
	"Oregon" : "OR",
	"Alabama" : "AL",
	"New Jersey": "NJ",
	"Colorado" : "CO"
	}
	capital_cities = {
	"OR": "Salem",
	"AL": "Montgomery",
	"NJ": "Trenton",
	"CO": "Denver"
	}

	if len(sys.argv) != 1:
		sys.exit()
	if sys.argv[0] in states == False:
		print("Unknown State")
	print(capital_cities[states[sys.argv[0]]])

if __name__ == '__main__':
	findcapital()
