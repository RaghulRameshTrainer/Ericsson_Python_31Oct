import csv

# with open(r'C:\Users\DELL\Desktop\emp.csv','r') as rcf:
#     data=csv.reader(rcf)
#     for row in data:
#         if row[0]!='EmpNo':
#             print(row[1] + " is from " + row[2] + " city")

with open("trans.csv","w",newline='') as wo:
    wf=csv.writer(wo)
    rows=[['Laptop',75000,"Dell"],
          ["Mobile",120000,"Apple"],
           ["TV",70000,"Samsung"],
          ]
    wf.writerows(rows)