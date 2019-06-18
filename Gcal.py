import csv
class GCalCSV:
    def __init__(self, header = {"Subject":True, "Start Date":True, "Start Time":True, "End Date":True, "End Time":True, "All Day Event":True, "Description":True, "Location":True, "Private":True}):
        self.__list = []
        _header_base = ["Subject", "Start Date", "Start Time", "End Date", "End Time", "All Day Event", "Description", "Location", "Private"]
        for head in _header_base:
            if not head in header:
                header[head] = False
        self.__header = header
        
    def add(self, obj):
        self.__list.append(obj)

    def outputCSV(self, filename = "output.csv"):
        with open(filename, 'w') as f:
            writer = csv.writer(f, lineterminator='\n')
            ava = [e for e in self.__header if self.__header[e]]
            writer.writerow(ava)
            for elem in self.__list:
                writer.writerow([elem[e] for e in ava])
    


if __name__ == "__main__":
    a = GCalCSV({"Subject":True, "Start Date":True, "Start Time":True, "End Date":True})
    a.add({
        "Subject":"Hello",
        "Start Date":"04/12/2014",
        "Start Time":"12:00 PM",
        "End Date":"05/16/2015"
    }) 
    a.add({
        "Subject":"two",
        "Start Date":"04/11/2019",
        "Start Time":"4:00 AM",
        "End Date":"12/16/2020"
    })
    a.outputCSV("name.csv")