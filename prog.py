items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"

count = 0
        
if ruleKey == "type":
  for i in range(len(items)):
    if items[i][0] == ruleValue:
      count = count + 1

elif ruleKey == "color":
  for i in range(len(items)):
    if items[i][1] == ruleValue:
      count = count + 1

elif ruleKey == "name":
  for i in range(len(items)):
    if items[i][2] == ruleValue:
      count = count + 1

print(count)
