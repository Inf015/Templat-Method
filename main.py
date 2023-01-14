import json
from xml.dom import minidom
from abc import ABC, abstractmethod


class Padre:
    AveMessure = []

    def run(self):
        AveMessure = self.leer()
        self.Calc(AveMessure)

    def leer(self):
        #lectura del json
        AveMessure = []

        with open (r"C:\Users\olive\OneDrive\Documents\GitHub\Templat Method\data.json") as J:
            dataJson= json.load(J)

            for i in dataJson:
                    AveMessure.append(i['meassure'])
            print(AveMessure)
            return AveMessure

#     def Calc(self,calc,AveMessure):
#         AveMessure = []

#         n = len(AveMessure)
#         total= (n(calc))/calc.len()
#         MaxValue = (max(calc))
#         MinValue =(min(calc))
#         print(total,MaxValue,MinValue)

# p1=Padre()
# p1.run()
#p1.Calc() 
#captura de datos del json





# datajs={
#    'data': [
#   {
#     'average': total,
#     'Max': MaxValue,
#     'Min': MinValue
#   }
# ]
# }

# jdata = json.dumps(datajs)


# with open ('dataout.json','w') as outfile:
#     json.dump(jdata, outfile)
class xml(Padre):
    def readxml(self):
        mydoc = minidom.parse('data.xml')
        items = mydoc.getElementsByTagName('meassure')

        print('\All attributes:')
    print(doc.nodeName)

    
    def run(self):
         self.readxml()
x1=xml()
x1.re()
    

