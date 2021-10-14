import csv
import json


def csv_trim(csvFilePath, newFilePath):
    newData = []

    # read csv file
    with open(csvFilePath, encoding="utf-8-sig") as csvf:
        dialect = csv.Sniffer().sniff(csvf.read(1024))

        csvf.seek(0)

        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf, dialect=dialect)

        # convert each csv row into python dict
        for row in csvReader:
            if row["Textbox26"] is "8":
                newData.append(row)
        print(newData)

    # convert python jsonArray to JSON String and write to file
    with open(newFilePath, "w", encoding="utf-8") as jsonf:
        jsonString = json.dumps(newData, indent=4)
        jsonf.write(jsonString)


csvFilePath = r"CCL Master Caseload Exporter.csv"
newFilePath = r"data.json"
csv_trim(csvFilePath, newFilePath)
