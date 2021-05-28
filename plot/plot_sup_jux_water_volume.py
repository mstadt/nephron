import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np
import os
import argparse

solute = ['Na','K','Cl','HCO3','H2CO3','CO2','HPO4','H2PO4','urea','NH3','NH4','H','HCO2','H2CO2','glu']

male_file = './male_normal_check'
female_file = './female_normal_check'

fig,ax = plt.subplots()
fig.set_figheight(11)
fig.set_figwidth(11)

female_con_number = []
female_con_sup_early = []
female_con_sup_later = []
female_con_jux = []
female_con_cd = []

segs_sup_early = ['pt','s3','sdl']
segs_sup_later = ['mtal','ctal','dct','cnt']
segs_jux = ['pt','s3','sdl','ldl','lal','mtal','ctal','dct','cnt']
segs_cd = ['ccd','omcd','imcd']
for seg in segs_sup_early:
    file_sup = open(female_file+'/female'+seg+'_water_volume_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    female_con_sup_early = female_con_sup_early+datalist_sup
for seg in segs_sup_later:
    file_sup = open(female_file+'/female'+seg+'_water_volume_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    female_con_sup_later = female_con_sup_later+datalist_sup

for seg in segs_jux:
    file_jux = open(female_file+'/female'+seg+'_water_volume_in_Lumen_jux5.txt','r')
    datalist_jux = []

    for i in file_jux:
        line = i.split(' ')
        datalist_jux.append(float(line[0]))
    female_con_jux = female_con_jux+datalist_jux

for seg in segs_cd:
    file_cd = open(female_file+'/female'+seg+'_water_volume_in_Lumen.txt','r')
    datalist_cd = []
    for i in file_cd:
        line = i.split(' ')
        datalist_cd.append(float(line[0]))
    female_con_cd = female_con_cd+datalist_cd
#===============================================
# Male
#===============================================
male_con_number = []
male_con_sup_early = []
male_con_sup_later = []
male_con_jux = []
male_con_cd = []
for seg in segs_sup_early:
    file_sup = open(male_file+'/male'+seg+'_water_volume_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    male_con_sup_early = male_con_sup_early+datalist_sup
for seg in segs_sup_later:
    file_sup = open(male_file+'/male'+seg+'_water_volume_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    male_con_sup_later = male_con_sup_later+datalist_sup

for seg in segs_jux:
    file_jux = open(male_file+'/male'+seg+'_water_volume_in_Lumen_jux4.txt','r')
    datalist_jux = []

    for i in file_jux:
        line = i.split(' ')
        datalist_jux.append(float(line[0]))
    male_con_jux = male_con_jux+datalist_jux

for seg in segs_cd:
    file_cd = open(male_file+'/male'+seg+'_water_volume_in_Lumen.txt','r')
    datalist_cd = []
    for i in file_cd:
        line = i.split(' ')
        datalist_cd.append(float(line[0]))
    male_con_cd = male_con_cd+datalist_cd

pos_pt=[1.1*i/199 for i in range(176)]
pos_s3=[1.1*i/199 for i in range(175,200)]
pos_sdl=[1.1+0.14*i/199 for i in range(200)]
pos_ldl=[1.1+0.14+0.5*i/199 for i in range(200)]
pos_lal=[1.1+0.14+0.5+0.5*i/199 for i in range(200)]
pos_mtal=[1.1+0.14+0.5+0.5+0.2*i/199 for i in range(200)]
pos_ctal=[1.1+0.14+0.5+0.5+0.2+0.05*i/199 for i in range(200)]
pos_dct=[1.1+0.14+0.5+0.5+0.2+0.05+0.1*i/199 for i in range(200)]
pos_cnt=[1.1+0.14+0.5+0.5+0.2+0.05+0.1+0.3*i/199 for i in range(200)]
pos=pos_pt+pos_s3+pos_sdl+pos_ldl+pos_lal+pos_mtal+pos_ctal+pos_dct+pos_cnt

pos_ccd=[1.1+0.14+0.5+0.5+0.2+0.05+0.1+0.3+0.2*i/199 for i in range(200)]
pos_omcd=[1.1+0.14+0.5+0.5+0.2+0.05+0.1+0.3+0.2+0.2*i/199 for i in range(200)]
pos_imcd=[1.1+0.14+0.5+0.5+0.2+0.05+0.1+0.3+0.2+0.2+0.5*i/199 for i in range(200)]

#female_sup_early = ax.plot(pos_pt+pos_s3+pos_sdl,[i*36000*10e-7 for i in female_con_sup_early],color = 'magenta',label = 'Female superficial')
#female_sup_later = ax.plot(pos_mtal+pos_ctal+pos_dct+pos_cnt,[i*36000*10e-7 for i in female_con_sup_later],color = 'magenta')
female_jux = ax.plot(pos,[i*36000*10e-7 for i in female_con_jux],color = 'magenta',label = 'Female',linewidth=2)
female_cd = ax.plot(pos_ccd+pos_omcd+pos_imcd,[i*36000*10e-7 for i in female_con_cd],color = 'magenta',linewidth=2)

#male_sup_early = ax.plot(pos_pt+pos_s3+pos_sdl,[i*36000*10e-7 for i in male_con_sup_early],color = 'royalblue',label = 'Male superficial')
#male_sup_later = ax.plot(pos_mtal+pos_ctal+pos_dct+pos_cnt,[i*36000*10e-7 for i in male_con_sup_later],color = 'royalblue')
male_jux = ax.plot(pos,[i*36000*10e-7 for i in male_con_jux],color = 'royalblue',label = 'Male',linewidth=2)
male_cd = ax.plot(pos_ccd+pos_omcd+pos_imcd,[i*36000*10e-7 for i in male_con_cd],color = 'royalblue')

pt_ht = 5*36000*10e-7
sdl_ht = 3*36000*10e-7
ldl_ht = 3*36000*10e-7
lal_ht = 3*36000*10e-7
tal_ht = 6*36000*10e-7
dct_ht = 3*36000*10e-7
cnt_ht = 0.5*36000*10e-7
cd_ht = 1*36000*10e-7

ax.plot(pos_pt+pos_s3,[pt_ht for i in pos_pt+pos_s3],'--',pos_sdl,[sdl_ht for i in pos_sdl],'--',pos_ldl,[ldl_ht for i in pos_ldl],'--',pos_lal,[lal_ht for i in pos_lal],'--',pos_mtal+pos_ctal,[tal_ht for i in pos_mtal+pos_ctal],'--',pos_dct,[dct_ht for i in pos_dct],'--',pos_cnt,[cnt_ht for i in pos_cnt],'--',pos_ccd+pos_omcd+pos_imcd,[cd_ht for i in pos_ccd+pos_omcd+pos_imcd],'--')
ax.text(0.5,pt_ht+0.5*36000*10e-7,'PT',fontsize=20)
#ax.text(1.12,sdl_ht+0.5*36000*10e-7,'SDL',fontsize=20)
ax.text(1.42,ldl_ht+0.5*36000*10e-7,'DL',fontsize=20)
ax.text(1.92,lal_ht+0.5*36000*10e-7,'LAL',fontsize=20)
ax.text(2.26,tal_ht+0.5*36000*10e-7,'TAL',fontsize=20)
ax.text(2.5,dct_ht+0.5*36000*10e-7,'DCT',fontsize=20)
ax.text(2.6,cnt_ht+0.5*36000*10e-7,'CNT',fontsize=20)
ax.text(3.3,cd_ht+0.5*36000*10e-7,'CD',fontsize=20)
ax.tick_params(labelsize = 30)
ax.legend(fontsize = 25, markerscale = 25)
ax.set_ylabel('Volume flow (ml/min)',fontsize = 35)
ax.get_xaxis().set_visible(False)

axins = inset_axes(ax,width = 4,height=4,loc=7)
#female_sup_early = ax.plot(pos_pt+pos_s3+pos_sdl,[i*36000*10e-7 for i in female_con_sup_early],color = 'magenta',label = 'Female superficial')
#female_sup_later = ax.plot(pos_mtal+pos_ctal+pos_dct+pos_cnt,[i*36000*10e-7 for i in female_con_sup_later],color = 'magenta')
female_jux_ins = axins.plot(pos,[i*36000*10e-7 for i in female_con_jux],color = 'magenta',label = 'Female',linewidth=2)
female_cd_ins = axins.plot(pos_ccd+pos_omcd+pos_imcd,[i*36000*10e-7 for i in female_con_cd],color = 'magenta',linewidth=2)

#male_sup_early = ax.plot(pos_pt+pos_s3+pos_sdl,[i*36000*10e-7 for i in male_con_sup_early],color = 'royalblue',label = 'Male superficial')
#male_sup_later = ax.plot(pos_mtal+pos_ctal+pos_dct+pos_cnt,[i*36000*10e-7 for i in male_con_sup_later],color = 'royalblue')
male_jux_ins = axins.plot(pos,[i*36000*10e-7 for i in male_con_jux],color = 'royalblue',label = 'Male',linewidth=2)
male_cd_ins = axins.plot(pos_ccd+pos_omcd+pos_imcd,[i*36000*10e-7 for i in male_con_cd],color = 'royalblue')

axins.plot(pos_ccd+pos_omcd+pos_imcd,[0.01 for i in pos_ccd+pos_omcd+pos_imcd],'--')
axins.text(3.3,0.01+0.001,'CD',fontsize=20)
axins.get_xaxis().set_visible(False)
axins.set_xlim(pos_ccd[0],pos_imcd[-1])
axins.set_ylim(0,0.1)
axins.tick_params(axis='both',labelsize = 30)

plt.savefig('volume flow',bbox_inches='tight')