from Utils import read_json as RJ
import os


def testData(attribute):
    testDataPath = os.path.abspath(r".\Util.json")
    testDataJsonFile = RJ.readJson(testDataPath)
    return testDataJsonFile[attribute]


# print(testData("username"))
# print(testData("password"))
# print(testData("environment"))
print(testData("browser"))
# print(testData("passconfirm"))
# print(testData("email"))
