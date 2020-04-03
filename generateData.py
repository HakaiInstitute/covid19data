import csv
import os

def writeDataToFile (fileName: str, data: list):
   with open(fileName, 'w', newline='') as newFile:
    dataWriter = csv.DictWriter(newFile, delimiter=',', fieldnames=['metric','date', 'fraser', 'interior', 'vancouver_island', 'northern', 'vancouver_coastal', 'total_bc'])
    dataWriter.writeheader()
    dataWriter.writerows(data)

total_cases_chart = [] # total_cases
new_cases_chart = [] # new_cases
ever_hospitalized_chart = [] # ever_hospitalized
deaths_chart = [] # deaths
recovered_chart = [] # recovered
      
for filename in os.listdir(os.getcwd()):
  if filename.endswith(".csv") and filename != 'covid19data.csv' and filename != 'test.csv' and not filename.endswith('chart.csv'):
    with open(os.path.join(os.getcwd(), filename), mode='r', encoding='utf-8-sig') as csvFile:
      dataArray = csv.DictReader(csvFile, delimiter=',')
      # print(dataArray, filename)
      for row in dataArray:
        # print(filename, row)
        if (row['metric'] == 'total_cases'):
          total_cases_chart.append(row)
        if (row['metric'] == 'new_cases'):
          new_cases_chart.append(row)
        if (row['metric'] == 'ever_hospitalized'):
          ever_hospitalized_chart.append(row)
        if (row['metric'] == 'deaths'):
          deaths_chart.append(row)
        if (row['metric'] == 'recovered'):
          recovered_chart.append(row)
      
  print('total_cases_chart:', total_cases_chart)
  writeDataToFile('total_cases_chart.csv', total_cases_chart)
  writeDataToFile('new_cases_chart.csv', new_cases_chart)
  writeDataToFile('ever_hospitalized_chart.csv', ever_hospitalized_chart)
  writeDataToFile('deaths_chart.csv', deaths_chart)
  writeDataToFile('recovered_chart.csv', recovered_chart)


    
