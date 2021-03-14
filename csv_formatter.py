from os import name
import pandas as pd
# version - 1.2.3

from pathlib import Path, os
import csv

path = Path(Path.cwd(), 'Data')
# csv files are named as 'year-orgs.csv'

starting_yr = 2018
ending_yr = 2021


def csv_to_json(csvFilePath):
    jsonArray = []

    # read csv file
    with open(csvFilePath, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            jsonArray.append(row)

    # end point of the code execution
    return(jsonArray)


def save_excel(df, tech):
    final_file_path = Path(Path.cwd(), f"GSoC_org_list_{tech}.csv")
    df.to_csv(final_file_path, index=False)
    print(f"CSV file saved at {final_file_path}")
    return(final_file_path)


def search_by_year(year):
    filename = str(year)+'-orgs.csv'
    if os.path.exists(Path(path, filename)):
        print("File exist")
    else:
        print("404")


def search_by_tech(tech):
    files = loop_thru_files()
    techwise_df = pd.DataFrame()

    for file in files:
        df = pd.read_csv(file, index_col=0, header=0)
        row_df = pd.DataFrame()
        row_df = df[df['Technologies'].str.contains(tech, regex=False)]
        techwise_df = techwise_df.append(row_df)

    final_file_path = save_excel(techwise_df, tech)
    return(csv_to_json(final_file_path))
    # function to return the jsonArray


def loop_thru_files():
    existing_files = []

    for year in range(starting_yr, ending_yr+1):
        filename = str(year)+'-orgs.csv'
        file_path = Path(path, filename)

        # search_by_year(year)
        if os.path.exists(file_path):
            existing_files.append(Path(path, filename))

    return existing_files


def master_fn():
    tech = input("Enter the tech: ")
    return (search_by_tech(tech))


master_fn()
#print(master_fn())


# "D:\amFOSS\hack2.0\Data\2018-orgs.csv"

# output - returns a JSONArray
