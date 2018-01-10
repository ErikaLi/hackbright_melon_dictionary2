"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

salespeople = []
melons_sold = []

# open file and read in each salesperson and the number of melons they sold
f = open("sales-report.txt")
for line in f:
    line = line.rstrip()
    entries = line.split("|")
    salesperson = entries[0]
    melons = int(entries[2])

    # find the total number of melons each salesperson sold
    if salesperson in salespeople:
        position = salespeople.index(salesperson)
        melons_sold[position] += melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

# # print out the result
# for i in range(len(salespeople)):
#     print "{} sold {} melons".format(salespeople[i], melons_sold[i])


# using dictionary
melons_sold_by_salesperson = {}
f = open("sales-report.txt")
for line in f:
    line = line.rstrip()
    entries = line.split("|")
    salesperson = entries[0]
    melons = int(entries[2])
    melons_sold_by_salesperson[salesperson] = melons_sold_by_salesperson.get(salesperson, 0) + melons

for salesperson, melons_sold in melons_sold_by_salesperson.iteritems():
    print "{} sold {} melons".format(salesperson, melons_sold)


