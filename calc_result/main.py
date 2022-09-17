import numpy as np
from numpy import genfromtxt

# create an array of arrays
dirs = [
	['/home/anjose-d/tg/tg-parser-emorecogn/output/107-30-640x480'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/112-30-640x360'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/113-60-1280x720'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/114-30-1280x720'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/115-30-1280x720'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/118-30-640x480'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/12-24-1920x1080'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/126-30-1080x1920'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/127-30-1280x720'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/1-30-1280x720'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/132-30-426x240'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/13-30-1920x1080'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/16-30-1920x1080'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/21-24-1920x1080'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/25-25-600x480'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/26-60-1280x720'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/27-60-1280x720'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/48-30-720x1280'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/53-30-360x480'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/72-30-1280x720'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/76-30-640x280'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/77-30-1280x720'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/79-30-960x720'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/81-30-576x360'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/8-30-1280x720'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/84-30-1920x1080'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video1'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video54'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video55_left'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video55_right'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video56'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video57'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video58'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video59'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video59_right'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video60'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video61'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video62'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video63'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video64'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video66'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video67'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video69'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video70'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video71'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video74_left'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video74_right'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video75'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video76'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video77'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video78'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video79'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video80'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video81'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video82'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video83'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video84'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video85'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video86_1'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video86_2'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video86_3'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video87'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video88'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video89'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video90'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video91'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video92'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video93'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video94'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video95'],
	['/home/anjose-d/tg/tg-parser-emorecogn/output/video96']
]

def ccc(x,y):
    ''' Concordance Correlation Coefficient'''
    sxy = np.sum((x - x.mean())*(y - y.mean()))/x.shape[0]
    rhoc = 2*sxy / (np.var(x) + np.var(y) + (x.mean() - y.mean())**2)
    return rhoc


my_data = genfromtxt(dirs[1][0], delimiter=',')

print(dirs[1][0])



my_data = my_data[1:]
n = ccc(my_data[:,0], my_data[:,1])

print(n)
