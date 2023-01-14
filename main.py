import json

#lectura del json
with open (r"C:\Users\olive\OneDrive\Documents\GitHub\Templat Method\data.json") as J:
    dataJson= json.load(J)

#captura de datos del json
AveMessure = []
n = 0
for i in dataJson:
    AveMessure.append(i['meassure'])
    n = n + 1

def sumlist(AveMessure):
    average = 0.0
    for z in AveMessure:
        average += z 
    return average
a = (sumlist(AveMessure))
total= a/n
MaxValue = (max(AveMessure))
MinValue =(min(AveMessure))
print(total,MaxValue,MinValue)



jdata = json.dumps(dataJson)
with open('dataout.json', 'w') as outfile:
    json.dump(jdata, outfile)
