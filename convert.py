import datetime
import time


def timeToStamp(StringTime):
    timeStamp = ""
    if StringTime != "":
        if not "/" in StringTime:
            StringTime = StringTime.replace("T", " ")
            timeArray = datetime.datetime.strptime(StringTime, "%Y-%m-%d %H:%M:%S.%f")
            timeStamp = int(time.mktime(timeArray.timetuple()))
        else:
            print("Oops!")
            StringTime = StringTime.split(" ")
            StringTimeArray = StringTime[0].split("/")
            if len(StringTimeArray[0]) == 1:
                StringTimeArray[0] = "0" + StringTimeArray[0]
            newStringTime = StringTimeArray[2] + "-" + StringTimeArray[1] + "-" + StringTimeArray[0]

            StringTimeArray2 = StringTime[1].split(":")
            if len(StringTimeArray2[0]) == 1:
                StringTimeArray2[0] = "0" + StringTimeArray2[0]
            ss = StringTimeArray2[0] + ":" + StringTimeArray2[1]

            newStringTime = newStringTime + " " + ss + ":00"
            timeArray = datetime.datetime.strptime(newStringTime, "%Y-%m-%d %H:%M:%S.%f")
            timeStamp = int(time.mktime(timeArray.timetuple()))

    return timeStamp


def main():
    time = "2016-08-02T15:39:14.957"
    result = timeToStamp(time)
    print(result)

if __name__ == "__main__":
    main()

    #1469973600
    #1472565600