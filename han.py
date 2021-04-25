from scipy import stats
import numpy as np
import sys
import statistics
import math
import matplotlib.pyplot as plt
from netCDF4 import Dataset
import yaml

def han(filename,OBSTYPE,VarName):

#  stream = open("foo.yaml", 'r')
#  yamlconfig = yaml.safe_load(stream)

#  print(dictionary['doe'])
#  for key, value in yamlconfig.items():
#     print (key + " : " + str(value))

#  print(len(yamlconfig['variables']))
   exit()

   thisobstype=OBSTYPE
   thisvarname=VarName
   gsihofXBc=thisvarname+'@GsiHofXBc'
   gsihofX  =thisvarname+'@GsiHofX'
   ufohofX  =thisvarname+'@hofx'
   f=Dataset(filename, mode='r')
   gsi_observer_withqc=f.variables[gsihofXBc][:]
   gsi_observer_noqc  =f.variables[gsihofX][:]
   ufo                =f.variables[ufohofX][:]
   geopotential_height=f.variables['geopotential_height@MetaData'][:]
   geometric_height=f.variables['geometric_height@MetaData'][:]
   gsi_observer_withqc=f.variables['radial_velocity@GsiHofXBc'][:]
   f.close()

   k2,p=stats.normaltest(gsi_observer_noqc)
   print("normaltest::")
   print(k2,p)

   k2,p=stats.ttest_rel(gsi_observer_noqc, gsi_observer_withqc)
   print("two sample test gsi_observer::")
   print(k2,p)
   
   k2,p=stats.ttest_rel(ufo, gsi_observer_withqc)
   print("two sample test ufo-gsi with QC::")
   print(k2,p)

   k2,p=stats.ttest_rel(ufo, gsi_observer_noqc)
   print("two sample test ufo-gsi without QC::")
   print(k2,p)

#  print(stats.describe(ufo))
#  print(stats.describe(gsi_observer_withqc))

#  print(len(gsi_observer_noqc))
   print(stats.describe(gsi_observer_noqc))
   print(stats.describe(gsi_observer_withqc))
   print(stats.describe(ufo))
#  print("p = {:g}".format(p))

#=========================
#  plt.rcParams.update({'line.linewidth': 8})
   fig = plt.figure(figsize=(8,9))
   plt.rcParams.update({'font.size': 8})
   ax1=fig.add_subplot(221)
   ax1.scatter(ufo,gsi_observer_withqc, color='blue',label="rw", marker='o', s=3)
   plt.title(thisobstype+':ufo and gsi_withqc')

   ax1=fig.add_subplot(222)
   ax1.scatter(ufo,gsi_observer_noqc, color='blue',label="rw", marker='o', s=3)
   plt.title(thisobstype+':ufo and gsi_noqc')

   ax2=fig.add_subplot(223)
   ax2.hist(gsi_observer_withqc,bins=50,range=(-40.00,40.00))
   plt.title(thisobstype+':gsi_withqc')

   ax2=fig.add_subplot(224)
   ax2.hist(ufo,bins=50,range=(-40.00,40.00))
   plt.title(thisobstype+':ufo')

   figname='test.png'
   plt.savefig(figname,bbox_inches='tight',dpi=100)
   exit()
#=========================

#=========================
#  diff=gsi_observer_noqc
   diff=gsi_observer_withqc
   diff=diff - ufo
   print(diff)

   rms=float(0)
   for x in diff:
      rms=rms+x*x
   rms=math.sqrt(rms/len(diff))
   print("rms=",rms)

#  diff=diff*1000.0

   print(diff.max(),diff.min())

   fig1 = plt.figure(figsize=(8.0,7.5))
   ax=fig1.add_subplot(111)
#  plt.hist(diff,bins=50,range=(-0.10,0.10))
   plt.hist(diff,bins=50,range=(-2.00,2.00))
#  plt.xlim([-0.15,0.15])
   plt.xlabel('(gsi-ufo)*1')
   plt.title(thisobstype+':gsi and ufo diff histogram')
   figname='ufo_'+thisobstype+'_stage1_hist_'+subtask+'.png'
   plt.savefig(figname,bbox_inches='tight',dpi=100)
#=========================

#=========================
   fig2 = plt.figure(figsize=(8.0,7.5))
   ax=fig2.add_subplot(111)
   plt.scatter(diff,geopotential_height, color='b',label="rw", marker='o', s=3)
#  plt.xlim([-0.15,0.15])
   plt.xlabel('(gsi-ufo)*1')
   plt.ylabel('geop-height')
   plt.title(thisobstype+':gsi-ufo diff in vertical')
   figname='ufo_'+thisobstype+'_stage1_vdiff_scatter_'+subtask+'.png'
   plt.savefig(figname,bbox_inches='tight',dpi=100)
#=========================


#=====================================================================
#=====================================================================
if __name__ == '__main__':

   print("start Hypothesis Analysis")
   print("1. get config parameters")
   stream = open("config.yaml", 'r')
   config = yaml.safe_load(stream)

#  fileame=sys.argv[1]
#  OBSTYPE=sys.argv[2]
#  VarName=sys.argv[3]
#  subtask=sys.argv[4]

   fileame=config['paths']['inputdir']+'/'+config['inputfile']
   OBSTYPE=config['OBSTYPE']
   VarName=config['VarName']
   subtask=config['subtask']

   print(fileame)
   exit()

   han(fileame,OBSTYPE,VarName)



#  print(statistics.stdev(diff))
#plt.xticks(np.arange(0,25,3))
#ymin1=imos[0:8].min()
#ymin2=gfs.min()
#ymin=min(ymin1,ymin2)
#ymin=ymin-1.0
#print ymin
#ymax1=imos[0:8].max()
#ymax2=gfs.max()
#ymax=max(ymax1,ymax2)
#ymax=ymax+1.0
#plt.ylim([ymin,ymax])
#plt.xlim([-25,25])
#  plt.xticks(fontsize=15)
#  plt.yticks(fontsize=15)
