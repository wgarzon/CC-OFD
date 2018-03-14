#! /usr/bin/python3.5
# Created 20-June-2017 by Juan C. Correa and Wilmer Garzón
#This module is used to obtain the distance between two points.
#From each point it is necessary to know the latitude and longitude.
#The distance is obtained through the google API.
#For use this code is necessary provide the personal APIKEY
import urllib.request
import json
import csv


def loadData(file_csv):
    """This function read at file in format CSV
    Args:
        file_csv: The file_csv exists, with file extension .csv
    Returns:
        A list with information from the csv file
    """
    csvFile = csv.reader(open(file_csv), delimiter=',')
    return list(csvFile)


def getDistance(From, To, APIKey):
    """This function get the distance between two points, using google maps
    Args:
        From: Latitude and longitude the origin (separated by commas)
        To: Latitude and longitude the destination (separated by commas)
        APIKey: Your personal API key
    Returns:
        A list with information from the csv file
    """

    link = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+From+"&destinations="+To+"&mode=driving&language=en-EN&key="+APIKey

    with urllib.request.urlopen(link) as url:
        data = json.loads(url.read().decode())
        return(data['rows'][0]['elements'][0]['distance']['text'])


def main():
    """This function processes the csv file obtaining the distance for each record.
    The APIKey is valid
  
    Returns:
        Create the file out.txt with the distance for each record.
    """
    data=loadData('FileName.csv')
    APIKey = "put here your key"

    file = open('out.txt', 'w')

    for i in range(0,len(data)):
        line = list(data[i])
        #The index 13 corresponds to "From Provider"
        #The index 19 corresponds to "To Client"
        fromP = line[13].replace(" ",",")
        toCl = line[19].replace(" ",",")

        #Put the distance at the end of each line
        line.append(getDistance(fromP,toCl,APIKey))

        #Write the information in the file
        file.writelines(["%s;" % item  for item in line])
        file.write("\n")

    file.close()
    print("Completed task")

main()
