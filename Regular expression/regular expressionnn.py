import re
# https://www.w3schools.com/python/python_regex.asp
mystr = '''Tata Motors Limited is an Indian multinational automotive manufacturing company, headquartered in Mumbai, Maharashtra which is part of Tata Group. The company produces passenger cars, trucks, vans, coaches, buses, luxury cars, sports cars, construction equipment and military vehicles. Wikipedia
Stock price: TATAMOTORS (NSE) ₹298.40 +3.15 (+1.07%)
9 Sep, 3:30 pm IST - Disclaimer
Customer service: 1800 209 7979
CEO: Guenter Butschek (15 Feb 2016–)
Headquarters: Mumbai
Founder: J. R. D. Tata
Subsidiaries: Jaguar Cars, Jaguar Land Rover, Tata Technologies, MORE
Parent organization: Tata Group
Video game: T1 Prima Run'''


# regular expression having findall(), search(), split(), sub(), finditer() functions
# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	Returns a list where the string has been split at each match
# sub	Replaces one or many matches with a string

#old way
# a = re.compile("Tata")
# matches = a.finditer(mystr)
# for match in matches:
#     print(match)

#new way
r = re.finditer(r"^.*fuckuman$", "ErMapshfuckuman")#return a iterator object we can iterate that object using
print(r)

r1 = re.findall(r"^.*fuckuman$", "ErMapshfuckuman")#return a list containing all matches
print(r1)

r2 = re.search(r"^.*man", "ErMapshfuckuman")#return match object
print(r2)

r3 = re.split(r" " , "ErMapsh fuckuman Er")#Returns a list where the string has been split at each match
print(r3)


r4 = re.finditer("Er|Mapsh", "ErMapsh fuckuman Er")
for i in r4:
    print(i)