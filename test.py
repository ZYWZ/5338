import csv
import time


def transform(StringTime):
    timeStamp=""
    if StringTime != "":
        if not "/" in StringTime:
            StringTime = StringTime.replace("T"," ")
            timeArray = time.strptime(StringTime, "%Y-%m-%d %H:%M:%S.%f")
            timeStamp = int(time.mktime(timeArray))
        else:
            print("Oops!")
            StringTime = StringTime.split(" ")
            StringTimeArray = StringTime[0].split("/")
            if len(StringTimeArray[0]) == 1:
                StringTimeArray[0] = "0"+ StringTimeArray[0]
            newStringTime = StringTimeArray[2]+"-"+StringTimeArray[1]+"-"+StringTimeArray[0]

            StringTimeArray2 = StringTime[1].split(":")
            if len(StringTimeArray2[0]) == 1:
                StringTimeArray2[0] = "0"+ StringTimeArray2[0]
            ss = StringTimeArray2[0]+":"+StringTimeArray2[1]

            newStringTime = newStringTime+" "+ss+":00.000"
            timeArray = time.strptime(newStringTime, "%Y-%m-%d %H:%M:%S.%f")
            timeStamp = int(time.mktime(timeArray))

    return timeStamp


def newPost():
    # Load csv file
    csvFile = open("csv/Posts.csv", "r")
    newCsvFile = open("csv/newPosts.csv", "w",encoding='utf8',newline='')
    reader = csv.reader(csvFile)
    writer = csv.writer(newCsvFile)

    for item in reader:
        if reader.line_num == 1:
            print(item)
            writer.writerow(item)
            continue

        item[3]=str(transform(item[3]))
        item[13]=str(transform(item[13]))
        writer.writerow(item)

    print("Making new User file!")
    csvFile.close()
    newCsvFile.close()


def newUser():
    # Load csv file
    csvFile = open("csv/Users.csv", "r")
    newCsvFile = open("csv/newUsers.csv", "w", encoding='utf8', newline='')
    reader = csv.reader(csvFile)
    writer = csv.writer(newCsvFile)

    for item in reader:
        if reader.line_num == 1:
            print(item)
            writer.writerow(item)
            continue

        item[2] = str(transform(item[2]))
        item[4] = str(transform(item[4]))
        writer.writerow(item)

    print("Making new User file!")
    csvFile.close()
    newCsvFile.close()


def newVote():
    # Load csv file
    csvFile = open("csv/Votes.csv", "r")
    newCsvFile = open("csv/newVotes.csv", "w", encoding='utf8', newline='')
    reader = csv.reader(csvFile)
    writer = csv.writer(newCsvFile)

    for item in reader:
        if reader.line_num == 1:
            print(item)
            writer.writerow(item)
            continue

        item[3] = str(transform(item[3]))
        writer.writerow(item)

    print("Making new Vote file!")
    csvFile.close()
    newCsvFile.close()


def main():
    newPost()
    newUser()
    newVote()


if __name__ == "__main__":
    main()




