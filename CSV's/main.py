import csv

with open("text.csv", newline = "\n") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    iterable_csv = iter(csvreader)
    next(iterable_csv)
    for row in iterable_csv:
        print(row[-1])




    # for row in csvreader:
    #     print(row)
    #
    # print(csvreader)