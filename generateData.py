import csv

def writeDataToFile (fileName: str, data: list):
   with open(fileName, 'w', newline='') as newFile:
    dataWriter = csv.writer(newFile, delimiter=',')
    dataWriter.writerows(data)

with open('march23.csv', newline='', mode='r', encoding='utf-8-sig') as csvFile:
    dataArray = csv.DictReader(csvFile, delimiter=',')

    total_cases_chart = [['report_date', 'fraser', 'interior', 'vancouver_island', 'northern', 'vancouver_coastal', 'total_bc']] # total_cases
    new_cases_chart = [['report_date', 'fraser', 'interior', 'vancouver_island', 'northern', 'vancouver_coastal', 'total_bc']] # new_cases
    ever_hospitalized_chart = [['report_date', 'fraser', 'interior', 'vancouver_island', 'northern', 'vancouver_coastal', 'total_bc']] # ever_hospitalized
    deaths_chart = [['report_date', 'fraser', 'interior', 'vancouver_island', 'northern', 'vancouver_coastal', 'total_bc']] # deaths
    recovered_chart = [['report_date', 'fraser', 'interior', 'vancouver_island', 'northern', 'vancouver_coastal', 'total_bc']] # recovered

    for row in dataArray:
      print(row)
      # if (row['health_authority'] == 'fraser'):


      # Access the general and chart-specific properties from the csv data.
      # health_authority = row['health_authority']
      # report_date = row['report_date']
      # total_cases = row['total_cases']
      # new_cases = row['new_cases']
      # ever_hospitalized = row['ever_hospitalized']
      # deaths = row['deaths']
      # recovered = row['recovered']

      # Write the headers and data to the fileName
      # Total cases chart
      # total_cases_list.append([report_date, ])
      # new_cases_list.append()
      # ever_hospitalized_list.append()
      # deaths_list.append()
      # recovered_list.append()

    
