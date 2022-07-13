
import math
import json
from operator import itemgetter

def getPartners(fileName):
    partners = []
    file = open(fileName, "r")
    lines = file.readlines()
    
    for line in lines:
        partners.append(json.loads(line))
    return partners
        
    

def calculateDistance(x1, x2, y1, y2):
    d = 6371.01 * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x2)) + math.cos(math.radians(x1)) * math.cos(math.radians(x2)) * math.cos(abs(math.radians(y1) - math.radians(y2))))
    return d

partners = getPartners("partners.txt")

matchingPartners = []

for partner in partners:
    dist = calculateDistance(42.6665921, float(partner["latitude"]), 23.351723, float(partner["longitude"]))
    if(dist <= 100):
        matchingPartners.append(partner)
        
sortedPartners = sorted(matchingPartners, key=itemgetter("partner_id"))

print("Partners within 100 km")

print("----------------------")

for partner in sortedPartners:
    
    print("id: "+str(partner["partner_id"]) + ", name: "+partner["name"])
