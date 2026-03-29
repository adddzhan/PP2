import csv

with open("contacts.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["first_name", "phone"])
    writer.writerow(["Adilzhan", "87769748213"])
    writer.writerow(["Azimbek", "87000000000"])
    writer.writerow(["Ali", "87771234567"])

