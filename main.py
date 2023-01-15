import json
import os
from xml.dom import minidom
from abc import ABC, abstractmethod
import xmltodict
import pandas


class SuperClass:
    AveMessure = []

    def run(self):
        AveMessure = self.leer()
        self.Calc(AveMessure)

    @abstractmethod
    def leer(self):
        pass

    def Calc(self, AveMessure):
        n = len(AveMessure)
        sum = 0

        for i in range(0, len(AveMessure)):
            sum = sum + AveMessure[i]

        total = sum/len(AveMessure)
        MaxValue = (max(AveMessure))
        MinValue = (min(AveMessure))

        print(f'Avg {total}, Max {MaxValue}, Min {MinValue}')


class Json(SuperClass):
    def leer(self):
        AveMessure = []

        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'data.json'))) as J:
            dataJson = json.load(J)

            for i in dataJson:
                AveMessure.append(float(i['meassure']))

        print(AveMessure)
        return AveMessure


class Xml(SuperClass):
    def leer(self):
        AveMessure = []
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'data.xml')))as f:
            data = f.read()

        content = xmltodict.parse(data)['data']['row']

        for i in content:
            AveMessure.append(float(i['meassure']))

        print(AveMessure)
        return AveMessure

class Flat(SuperClass):
    def leer(self):
        AveMessure = []
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'data.xml')))as f:
            data = f.read()

        content = xmltodict.parse(data)['data']['row']

        for i in content:
            AveMessure.append(float(i['meassure']))

        print(AveMessure)
        return AveMessure

    def readFile(self):
        rawFlat = pandas.read_csv(os.path.abspath(os.path.join(os.path.dirname(__file__), 'data.flat')), delimiter=" ", header=None).to_dict()[0]
        dictionary = []
        AveMessure = []

        for i in rawFlat:
            res = {}
            if (i == 0):
                names = rawFlat[i].split("|")
                names = [element.lower() for element in names]
            else:
                values = rawFlat[i].split("|")

                for key in names:
                    for value in values:
                        res[key] = value
                        values.remove(value)
                        break

                dictionary.append(res)

        for i in dictionary:
            AveMessure.append(float(i['meassure']))

        print (AveMessure)
        return AveMessure
# j = Json()
# j.run()

# x =Xml()
# x.run()

f = Flat()
f.run()

