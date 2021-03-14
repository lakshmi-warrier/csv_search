import pandas as pd
# version - 1.2.3

from pathlib import Path, os
import csv 
import json 

path = Path(Path.cwd(), 'Data')
# csv files are named as 'year-orgs.csv'

starting_yr = 2018
ending_yr = 2021


def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)

        jsonf.write(jsonString)


def save_excel(df, tech):
    final_file_path = Path(Path.cwd(),f"GSoC_org_list_{tech}.csv")
    df.to_csv(final_file_path,index=False)
    print(f"File saved at {final_file_path}")
    final_json_path = Path(Path.cwd(),f"GSoC_org_list_{tech}.json")
    csv_to_json(final_file_path, final_json_path)

def make_df(filepath):
    df = pd.read_csv(filepath, index_col=0)
    print(df)
    return df


def search_by_year(year):
    filename = str(year)+'-orgs.csv'
    if os.path.exists(Path(path, filename)):
        print("File exist")
        make_df(Path(path, filename))
    else:
        print("404")

def mix_all_orgs(year):
    files = loop_thru_files
    filename = str(year)+'-orgs.csv'
    all_orgs = pd.DataFrame()

    for file in files: 
        if os.path.exists(file):
            print("File exist")
            df = pd.read_csv(Path(path, filename), index_col=0)
            all_orgs = all_orgs.append(df)

def search_by_tech(tech):
    files = loop_thru_files()
    techwise_df = pd.DataFrame()

    print(techwise_df)
    for file in files:
        df = pd.read_csv(file, index_col=0, header=0)
        row_df = pd.DataFrame()
        row_df =df[df['Technologies'].str.contains(tech, regex=False)]
        techwise_df = techwise_df.append(row_df)
    print(techwise_df)
    save_excel(techwise_df, tech)




def loop_thru_files():
    existing_files = []

    for year in range(starting_yr, ending_yr+1):
        filename = str(year)+'-orgs.csv'
        file_path = Path(path, filename)

        # search_by_year(year)
        if os.path.exists(file_path):
            existing_files.append(Path(path, filename))
    print(existing_files)

    return existing_files


search_by_tech(input("Enter the tech: "))
# "D:\amFOSS\hack2.0\Data\2018-orgs.csv"


# output - JSON file
