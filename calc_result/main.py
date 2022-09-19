from os import truncate
import pandas as pd
import numpy as np
from numpy import genfromtxt
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error
import subprocess

print("Parse result from file (C executable)")
subprocess.run(["make"])
subprocess.run(["./parsecsv", "input_files/va_affwild_validation.csv"])

# defines
COMMON_PATH = '/home/anjose-d/tg/tg-parser-emorecogn/'
TRUE_FILES_DIR = 'validation/'
PRED_FILES_DIR = 'predfiles/'
TRUE_PATH = COMMON_PATH + TRUE_FILES_DIR
PRED_PATH = COMMON_PATH + PRED_FILES_DIR

# files which hold valence and arousal values
# true files
	# with .txt extension and in the 'validation' folder
# pred files
	# with no extension and in the 'predfiles' folder

filenames = [
	['107-30-640x480'],
	['112-30-640x360'],				# DOESN'T MATCH
	['113-60-1280x720'],
	['114-30-1280x720'],			# DOESN'T MATCH
	['115-30-1280x720'],			# DOESN'T MATCH
	['118-30-640x480'],
	['12-24-1920x1080'],
	['126-30-1080x1920'],			# DOESN'T MATCH
	['127-30-1280x720'],
	['1-30-1280x720'],				# DOESN'T MATCH
	['132-30-426x240'],				# DOESN'T MATCH
	['13-30-1920x1080'],			# DOESN'T MATCH
	['16-30-1920x1080'],
	['21-24-1920x1080'],			# DOESN'T MATCH
	['25-25-600x480'],				# DOESN'T MATCH
	['26-60-1280x720'],
	['27-60-1280x720'],
	['48-30-720x1280'],				# DOESN'T MATCH
	['53-30-360x480'],				# DOESN'T MATCH
	['72-30-1280x720'],
	['76-30-640x280'],
	['77-30-1280x720'],
	['79-30-960x720'],				# DOESN'T MATCH
	['81-30-576x360'],				# DOESN'T MATCH
	['8-30-1280x720'],
	['84-30-1920x1080'],			# DOESN'T MATCH
	['video1'],						# DOESN'T MATCH
	['video54'],
	['video55_left'],				# DOESN'T MATCH
	['video55_right'],				# DOESN'T MATCH
	['video56'],					# DOESN'T MATCH
	['video57'],					# DOESN'T MATCH
	['video58'],					# DOESN'T MATCH
	['video59'],					# DOESN'T MATCH
	['video59_right'],				# DOESN'T MATCH
	['video60'],					# DOESN'T MATCH
	['video61'],					# DOESN'T MATCH
	['video62'],					# DOESN'T MATCH
	['video63'],					# DOESN'T MATCH
	['video64'],					# DOESN'T MATCH
	['video66'],					# DOESN'T MATCH
	['video67'],
	['video69'],					# DOESN'T MATCH
	['video70'],					# DOESN'T MATCH
	['video71'],
	['video74_left'],
	['video74_right'],				# DOESN'T MATCH
	['video75'],					# DOESN'T MATCH
	['video76'],					# DOESN'T MATCH
	['video77'],
	['video78'],
	['video79'],					# DOESN'T MATCH
	['video80'],					# DOESN'T MATCH
	['video81'],					# DOESN'T MATCH
	['video82'],					# DOESN'T MATCH
	['video83'],					# DOESN'T MATCH
	['video84'],
	['video85'],
	['video86_1'],					# DOESN'T MATCH
	['video86_2'],
	['video86_3'],
	['video87'],					# DOESN'T MATCH
	['video88'],					# DOESN'T MATCH
	['video89'],
	['video90'],					# DOESN'T MATCH
	['video91'],
	['video92'],					# DOESN'T MATCH
	['video93'],
	['video94'],
	['video95'],					# DOESN'T MATCH
	['video96']						# DOESN'T MATCH
]

def ccc(x_true, y_pred):
    ''' Concordance Correlation Coefficient'''
    sxy = np.sum((x_true - x_true.mean())*(y_pred - y_pred.mean()))/x_true.shape[0]
    rhoc = 2*sxy / (np.var(x_true) + np.var(y_pred) + (x_true.mean() - y_pred.mean())**2)
    return rhoc

# RMSE
def rmse(x_true, y_pred):
	return mean_squared_error(x_true, y_pred, squared=False)

# MAPE
def mape(x_true, y_pred):
    # ref: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_percentage_error.html#sklearn.metrics.mean_absolute_percentage_error
	return mean_absolute_percentage_error(x_true, y_pred)
 
df = pd.DataFrame(columns=["filename", "ccc_valence", "ccc_arousal",
                        	"rmse_valence", "rmse_arousal",
                         	"mape_valence", "mape_arousal", "status"])
print("Generating results...")
for fname in filenames:
	truefile = genfromtxt(TRUE_PATH + fname[0] + '.txt', delimiter=',')
	predfile = genfromtxt(PRED_PATH + fname[0], delimiter=',')
	
	# pular primeira linha (header)
	truefile = truefile[1:]
	predfile = predfile[1:]
	
	# get the size of the array
	if (truefile.shape[0] == predfile.shape[0]):
		# ccc calculation
		ccc_valence = ccc(truefile[:,0], predfile[:,0])
		ccc_arousal = ccc(truefile[:,1], predfile[:,1])
		# rmse calculation
		rmse_valence = rmse(truefile[:,0], predfile[:,0])
		rmse_arousal = rmse(truefile[:,1], predfile[:,1])
		# mape calculation
		mape_valence = mape(truefile[:,0], predfile[:,0])
		mape_arousal = mape(truefile[:,1], predfile[:,1])

		# construir planilha
		df = df.append({"filename": fname[0], 
                  		"ccc_valence": ccc_valence, "ccc_arousal": ccc_arousal,
                     	"rmse_valence": rmse_valence, "rmse_arousal": rmse_arousal,
                      	"mape_valence": mape_valence, "mape_arousal": mape_arousal,
						"status": "OK"}, ignore_index=True)
	else:
		df = df.append({"filename": fname[0],
						"ccc_valence": np.nan, "ccc_arousal": np.nan,
                     	"rmse_valence": np.nan, "rmse_arousal": np.nan,
                      	"mape_valence": np.nan, "mape_arousal": np.nan,
						"status": "pred and true files don't match the number of rows!"}, ignore_index=True)

file_name = 'calc_tg.xlsx'

# save the excelsheet
df.to_excel(file_name)
print('Spreedsheet worked just fine!')
