from scipy import stats
import numpy as np
import sys
import statistics
import math
import matplotlib.pyplot as plt
from netCDF4 import Dataset

def han(filename,OBSTYPE,VarName):

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
   print(k2,p)

   k2,p=stats.ttest_ind(gsi_observer_noqc, gsi_observer_withqc)
#  k2,p=stats.ttest_ind(geopotential_height, geometric_height)

   print(len(gsi_observer_noqc))
   print(stats.describe(gsi_observer_noqc))
   print(stats.describe(gsi_observer_withqc))
   print("p = {:g}".format(p))

#=========================
#  plt.rcParams.update({'line.linewidth': 8})
   fig = plt.figure(figsize=(12.0,6))
   plt.rcParams.update({'font.size': 6})
   ax1=fig.add_subplot(121)
   ax1.scatter(gsi_observer_withqc,gsi_observer_noqc, color='blue',label="rw", marker='o', s=3)
   plt.title(thisobstype+':gsi_withqc and gsi_noqc')

   ax1=fig.add_subplot(122)
   ax1.scatter(geopotential_height,geometric_height, color='blue',label="rw", marker='o', s=3)
   plt.title(thisobstype+':gp_height and gm_height')

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

   print("get parameters")
   fileame=sys.argv[1]
   OBSTYPE=sys.argv[2]
   VarName=sys.argv[3]
   subtask=sys.argv[4]

   print("start Hypothesis Analysis")
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
