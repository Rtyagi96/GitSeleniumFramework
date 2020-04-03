from Utils import read_json as RJ
import os


def testData(attribute):
    #testDataPath = os.path.abspath(r"C:\Users\Rohit\PycharmProjects\SeleniumFramework\Config\config.json")
    testDataPath = os.path.abspath(r"C:\Users\Rohit\PycharmProjects\SeleniumProject\data.json")
    testDataJsonFile = RJ.readJson(testDataPath)
    return testDataJsonFile[attribute]


print(testData("username"))
print(testData("password"))
print(testData("environment"))
print(testData("browser"))
print(testData("passconfirm"))
print(testData("email"))
