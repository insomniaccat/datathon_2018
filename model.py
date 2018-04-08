# Import base libraries
import numpy             as np
import pandas            as pn
import matplotlib.pyplot as plt
import random            as rnd
import seaborn           as sns

# Import machine learning libraries
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.svm          import SVC, LinearSVC
from sklearn.ensemble     import RandomForestClassifier
from sklearn.neighbors    import KNeighborsClassifier
from sklearn.naive_bayes  import GaussianNB
from sklearn.tree         import DecisionTreeClassifier

# Define the file names
pe_file_name  = "Physician_Compare_2015_Group_Public_Reporting_-_Patient_Experience.csv"
gps_file_name = "Physician_Compare_2015_Group_Public_Reporting___Performance_Scores.csv"
ips_file_name = "Physician_Compare_2015_Individual_EP_Public_Reporting___Performance_Scores.csv"
cn_file_name  = "Physician_Compare_National_Downloadable_File.csv"

# Read in the data
pat_exp          = pn.read_csv( pe_file_name)
group_perf_score = pn.read_csv( gps_file_name)
indiv_perf_score = pn.read_csv( ips_file_name)
phys_comp        = pn.read_csv( cn_file_name)

# Plot correlations within and between data
colormap = plt.cm.RdBu
plt.figure()
## Currently broken, need to finish converting all data to floats first
sns.heatmap( phys_comp.astype(float).corr(), linewidths=0.1, vmax=1.0, square=True, cmap=colormap, linecolor='white', annot=True)
