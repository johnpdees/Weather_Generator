"""These functions are used to extract weather station data from the total set and write them to a csv
Note that .data files for Rglimclim must follow this format:
Name of file containing daily weather / climate data (defaults to gaugvals.dat, for compatibility with previous versions
 of GLIMCLIM). This must be an ASCII file, and must be structured as follows:
Each line represents one day's data at one location.
The file is sorted by date, and within that by site code.
Each record is in fixed format, with fields as follows:
Positions 1-4
contain the year (e.g. 1978).
Positions 5-6
contain the month (1-12).
Positions 7-8
contain the day.
Positions 9-12
contain the four-character site identifier, as defined in siteinfo.
The remaining positions
contain the data values, in fields of width 6 and each with two decimal places.
The FORTRAN format for reading each record is I4,I2,I2,A4,NF6.2 where N is the number of variables in the data file.
 Thus, in a data file containing information on three variables, the records will have the form
 YYYYMMDD$$$$111.11222.22333.33 where YYYY is the year, MM the month, DD the day, $$$$ the site identifier and
 111.11 to 333.33 the data values.

"""

import csv
import os

w_dir = "C:\\Weather Generator\\Rglimclim_1.3-4\\TestData\\DailyTest"
years = list(range(2006, 2016))
stations = ["035", "039", "041","043","044","047","052","054","056","057","062","064","068","070","071","075","077","078",
            "080","083","084","086","087","088","090","091","092","099","103","104","105","106","107","109","113",
            "114","116","117","121","124","125","126","129","131","135","136","139","140","142","143","144","146","147","148",
            "150","151","152","153","155","157","158","159","160","161","163","165","167","169","170","171","173","174",
            "175","178","179","181","182","183","184","187","189","190","191","192","194","195","196","197","198","199",
            "002","006","007","012","013","015","019"]


#create a large csv
# open a directory full of csv files
#parse csv files
#look for csv files that end in the appropriate station number
#if station number is in list, add to complete csv

def write_csv(write_file, w_dir, stations, years):
    with open(os.path.join(w_dir, write_file), 'w') as csvfull:
        writer = csv.writer(csvfull, delimiter=",")
        for year in years:
            for station in stations:
                curr_path="dailyStns{}\\{}daily{}.csv".format(str(year),str(year), station)
                with open(os.path.join(w_dir, curr_path), 'r') as csvcurr:
                    reader = csv.reader(csvcurr, delimiter=",")
                    for row in reader:
                        writer.writerow(row)
                        print (row)
    return

def write_data_fortran(input_file, output_file="data_fort.txt"):
    first_row = 0
    with open(os.path.join(w_dir, input_file), 'r') as csvcurr:
        reader = csv.reader(csvcurr, delimiter=",")
        with open(os.path.join(w_dir, output_file), 'w') as data_fortran:
            for row in reader:
                if first_row == 0:
                    first_row = 1
                else:
                    ids, year, month, day, precip = row[0], row[1], row[2], row[3], row[4]
                    len_id = len(ids)
                    len_month = len(month)
                    len_day = len(day)
                    len_precip = len(precip)

                    if len_month < 2:
                        month = " " + month
                    if len_day < 2:
                        day = " " + day
                    if len_id == 3:
                        ids = " " + ids
                    elif len_id == 2:
                        ids = "  " + ids
                    elif len_id == 1:
                        ids = "   " + ids

                    num_spaces = 6 - len_precip
                    spaces = ""
                    if num_spaces > 0:
                        for each in range(0, num_spaces):
                            spaces = spaces + " "

                    precip = spaces + precip

                    newline = year + month + day + ids +  precip

                    data_fortran.write(newline + "\n")
    return


write_data_fortran("data.csv")






