# Import base libraries
import numpy as np
import pandas as pn


# Define the file names
pe_file_name = "Physician_Compare_2015_Group_Public_Reporting_-_Patient_Experience.csv"
gps_file_name = "Physician_Compare_2015_Group_Public_Reporting___Performance_Scores.csv"
ips_file_name = "Physician_Compare_2015_Individual_EP_Public_Reporting___Performance_Scores.csv"
cn_file_name = "Physician_Compare_National_Downloadable_File.csv"

# Read in the data
pat_exp          = pn.read_csv( pe_file_name)
group_perf_score = pn.read_csv( gps_file_name)
indiv_perf_score = pn.read_csv( ips_file_name)
phys_comp        = pn.read_csv( cn_file_name)
