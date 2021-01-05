import requests
import json
import ast
import os
import csv

BASE_URL = ""
HOST = ""
JOURNEY_DETAILS_URL = ""

def returnRequestHeaders(): 
    return {
        "content-type": "application/x-www-form-urlencoded"
    }

def convertBytesToDictionary(content):
    dictStr = content.decode("utf-8")
    records =  ast.literal_eval(repr(dictStr))
    converted = json.loads(records)
    return converted

def generateToken():
    global BASE_URL
    headers = returnRequestHeaders()
    body = {
        "UserName": "",
        "Password": "",
        "area": "",
        "grant_type": ""
    }
    response = requests.post(BASE_URL, data=body, headers=headers)
    response = convertBytesToDictionary(response.content)
    print(response["access_token"])
    print("\n")
    return response["access_token"]

def returnAuthorizationHeaders(token):
    headers = {"Authorization": "Bearer %s"%token}
    return headers

def getJourneybyJourneyId(token, journeyId):
    global HOST, JOURNEY_DETAILS_URL
    headers = returnAuthorizationHeaders(token)
    # requestUrl = HOST + "/journey/get?journeyID=" + journeyId
    requestUrl = JOURNEY_DETAILS_URL + journeyId
    response = requests.get(requestUrl, headers=headers)
    # print(response.content)
    response = convertBytesToDictionary(response.content)
    return response

def readCsvAndGetJourneyIds():
    csvFilePath = os.getcwd() + "/csv_files/" + "IDscan_Records.csv"
    with open(csvFilePath, "r", encoding="utf8") as file: 
        records = csv.reader(file)
        journeyIds = []
        for record in records: 
            journeyIds.append(record[0])
        # journeyIds = journeyIds[1: (len(journeyIds) - 1)]
        return journeyIds 

def getJourneyDetails(journeyIds):
    global token
    allJourneyDetails = []
    counter = 0
    for journeyId in journeyIds: 
        if counter == 100: 
            return allJourneyDetails
        else:
            counter += 1 
            journeyDetails = getJourneybyJourneyId(token, journeyId)
            allJourneyDetails.append(journeyDetails)
            print(counter)
    # return allJourneyDetails

def writeCsvHeaders(): 
    csvFilePath = os.getcwd() + "/csv_files/output.csv"
    if os.path.isfile(csvFilePath):
        return
    else: 
        headers = [
            "JourneyId",
            "High Level Result",
            "Last Name",
            "First Name",
            "Date Of Birth",
            "Document Number",
            "Issue Date",
            "Document Category",
            "Document Type",
            "ValidationDetails.Name",
            "ValidationDetails.Description",
            "ValidationDetails.Result",
            "ValidationDetails.IdentityMeansScanId",
            "QualityCheckDetails.Name",
            "QualityCheckDetails.Description",
            "QualityCheckDetails.State",
            "QualityCheckDetails.IdentityMeansScanId",
            "QualityCheckDetails.ID"
        ]
        with open(csvFilePath,mode="w", newline='') as file: 
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(headers)


def getValForKey(val, dict): 
    if val in dict.keys():
        return dict[val]
    else: 
        return ""

def appendQualityCheckDetailsAndInsert(journeyDetails, recordList):
    finalRecords = []
    csvFilePath = os.getcwd() + "/csv_files/output.csv"
    with open(csvFilePath, mode="a", encoding="utf8", newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        qualityCheckDetails = journeyDetails["QualityCheckDetails"]
        if qualityCheckDetails == []:
            qualityCheckDetails = ["", "", "", "", ""]
            for record in recordList:
                row = record + qualityCheckDetails
                writer.writerow(row)
        else: 
            qualityCheckDetails = [detail for detail in qualityCheckDetails if detail["State"] > 1]
            for record in recordList:
                for qualityCheckDetail in qualityCheckDetails: 
                    updatedQualityCheckDetails =[
                        qualityCheckDetail["Name"], 
                        qualityCheckDetail["Description"], 
                        qualityCheckDetail["State"], 
                        qualityCheckDetail["IdentityMeansScanId"],
                        qualityCheckDetail["Id"]
                    ]
                    row = record + updatedQualityCheckDetails
                    writer.writerow(row)

def getValidationDetails(journeyDetails, recordList): 
    finalRecords = []
    validationDetails= journeyDetails["ValidationDetails"]
    if validatioDetails == []:
        validationDetails = ["", "", "", ""]
        finalRecords.append(recordList + validationDetails)
    else: 
        validationDetails = [validationDetail for validationDetail in validationDetails if validationDetail["Result"] > 1]
        for details in validationDetails: 
            updatedValidationDetails = [
                details["Name"], 
                details["Description"], 
                details["Result"], 
                details["IdentityMeansScanId"]
            ]
            finalRecords.append(recordList + updatedValidationDetails)
    return finalRecords

def writeJourneyDetailsToCSV(journeyDetails):
    outputFilePath = os.getcwd() + "/csv_files/output.csv"
    for journeyDetail in journeyDetails: 
        record = [
            getValForKey("EvaluatedPersonEntryId", journeyDetail),
            getValForKey("HighLevelResult", journeyDetail),
            getValForKey("LastName", journeyDetail),
            getValForKey("FirstName ", journeyDetail),
            getValForKey("BirthDate", journeyDetail),
            getValForKey("DocumentNumber", journeyDetail),
            getValForKey("IssueDate", journeyDetail),
            getValForKey("DocumentCategory", journeyDetail),
            getValForKey("DocumentType", journeyDetail),
        ]
        validationDetails = getValidationDetails(journeyDetail, record)
        appendQualityCheckDetailsAndInsert(journeyDetail, validationDetails)
        

token = generateToken()
writeCsvHeaders()
journeyDetails = getJourneyDetails(readCsvAndGetJourneyIds())
writeJourneyDetailsToCSV(journeyDetails)
