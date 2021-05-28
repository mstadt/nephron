import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os
import argparse

solute = ['Na','K','Cl','HCO3','H2CO3','CO2','HPO4','H2PO4','urea','NH3','NH4','H','HCO2','H2CO2','glu']

male_file = './Male_hum_normal'
female_file = './Female_hum_normal'

fig,axarr = plt.subplots(3,3)
fig.set_figheight(40)
fig.set_figwidth(40)

s = 'Na'

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
    file_sup = open(female_file+'/female_hum_'+seg+'_con_of_'+s+'_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    female_con_sup_early = female_con_sup_early+datalist_sup
for seg in segs_sup_later:
    file_sup = open(female_file+'/female_hum_'+seg+'_con_of_'+s+'_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    female_con_sup_later = female_con_sup_later+datalist_sup

for seg in segs_jux:
    file_jux = open(female_file+'/female_hum_'+seg+'_con_of_'+s+'_in_Lumen_jux4.txt','r')
    datalist_jux = []

    for i in file_jux:
        line = i.split(' ')
        datalist_jux.append(float(line[0]))
    female_con_jux = female_con_jux+datalist_jux

for seg in segs_cd:
    file_cd = open(female_file+'/female_hum_'+seg+'_con_of_'+s+'_in_Lumen.txt','r')
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
    file_sup = open(male_file+'/male_hum_'+seg+'_con_of_'+s+'_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    male_con_sup_early = male_con_sup_early+datalist_sup
for seg in segs_sup_later:
    file_sup = open(male_file+'/male_hum_'+seg+'_con_of_'+s+'_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    male_con_sup_later = male_con_sup_later+datalist_sup

for seg in segs_jux:
    file_jux = open(male_file+'/male_hum_'+seg+'_con_of_'+s+'_in_Lumen_jux4.txt','r')
    datalist_jux = []

    for i in file_jux:
        line = i.split(' ')
        datalist_jux.append(float(line[0]))
    male_con_jux = male_con_jux+datalist_jux

for seg in segs_cd:
    file_cd = open(male_file+'/male_hum_'+seg+'_con_of_'+s+'_in_Lumen.txt','r')
    datalist_cd = []
    for i in file_cd:
        line = i.split(' ')
        datalist_cd.append(float(line[0]))
    male_con_cd = male_con_cd+datalist_cd

pos_pt=[1.7*i/199 for i in range(181)]
pos_s3=[1.7*i/199 for i in range(180,200)]
pos_sdl=[1.7+0.33*i/199 for i in range(200)]
pos_ldl=[1.7+0.33+1.5*i/199 for i in range(200)]
pos_lal=[1.7+0.33+1.5+1.5*i/199 for i in range(200)]
pos_mtal=[1.7+0.33+1.5+1.5+0.5*i/199 for i in range(200)]
pos_ctal=[1.7+0.33+1.5+1.5+0.5+0.05*i/199 for i in range(200)]
pos_dct=[1.7+0.33+1.5+1.5+0.5+0.05+0.2*i/199 for i in range(200)]
pos_cnt=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4*i/199 for i in range(200)]
pos=pos_pt+pos_s3+pos_sdl+pos_ldl+pos_lal+pos_mtal+pos_ctal+pos_dct+pos_cnt

pos_ccd=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4+0.4*i/199 for i in range(200)]
pos_omcd=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4+0.4+0.5*i/199 for i in range(200)]
pos_imcd=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4+0.4+0.5+1.2*i/199 for i in range(200)]

#female_sup_early = axarr[0,0].plot(pos_pt+pos_s3+pos_sdl,female_con_sup_early,color = 'magenta',label = 'Female superficial')
#female_sup_later = axarr[0,0].plot(pos_mtal+pos_ctal+pos_dct+pos_cnt,female_con_sup_later,color = 'magenta')
female_jux = axarr[0,0].plot(pos,female_con_jux,color = 'magenta',label = 'Female',linewidth=2)
female_cd = axarr[0,0].plot(pos_ccd+pos_omcd+pos_imcd,female_con_cd,color = 'magenta',linewidth=2)

#male_sup_early = axarr[0,0].plot(pos_pt+pos_s3+pos_sdl,male_con_sup_early,color = 'royalblue',label = 'Male superficial')
#male_sup_later = axarr[0,0].plot(pos_mtal+pos_ctal+pos_dct+pos_cnt,male_con_sup_later,color = 'royalblue')
male_jux = axarr[0,0].plot(pos,male_con_jux,color = 'royalblue',label = 'Male',linewidth=2)
male_cd = axarr[0,0].plot(pos_ccd+pos_omcd+pos_imcd,male_con_cd,color = 'royalblue',linewidth=2)

pt_ht = 130
sdl_ht = 140
ldl_ht = 145
lal_ht = 140
tal_ht = 155
dct_ht = 55
cnt_ht = 0
cd_ht = 60

h = 2

axarr[0,0].plot(pos_pt+pos_s3,[pt_ht for i in pos_pt+pos_s3],'--',pos_sdl,[sdl_ht for i in pos_sdl],'--',pos_ldl,[ldl_ht for i in pos_ldl],'--',pos_lal,[lal_ht for i in pos_lal],'--',pos_mtal+pos_ctal,[tal_ht for i in pos_mtal+pos_ctal],'--',pos_dct,[dct_ht for i in pos_dct],'--',pos_cnt,[cnt_ht for i in pos_cnt],'--',pos_ccd+pos_omcd+pos_imcd,[cd_ht for i in pos_ccd+pos_omcd+pos_imcd],'--')
axarr[0,0].text(pos_pt[90],pt_ht+h,'PT',fontsize=20)
axarr[0,0].text(pos_sdl[50],sdl_ht+h,'SDL',fontsize=20)
axarr[0,0].text(pos_ldl[70],ldl_ht+h,'LDL',fontsize=20)
axarr[0,0].text(pos_lal[70],lal_ht+h,'LAL',fontsize=20)
axarr[0,0].text(pos_mtal[50],tal_ht+h,'TAL',fontsize=20)
axarr[0,0].text(pos_dct[10],dct_ht+h,'DCT',fontsize=20)
axarr[0,0].text(pos_cnt[10],cnt_ht+h,'CNT',fontsize=20)
axarr[0,0].text(pos_omcd[100],cd_ht+h,'CD',fontsize=20)
axarr[0,0].tick_params(labelsize = 30)
axarr[0,0].legend(fontsize = 25, markerscale = 25)
axarr[0,0].set_ylabel('[Na$^+$] (mM)',fontsize = 35)
axarr[0,0].get_xaxis().set_visible(False)

#========================================================
# K
#========================================================
s = 'K'

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
    file_sup = open(female_file+'/female_hum_'+seg+'_con_of_'+s+'_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    female_con_sup_early = female_con_sup_early+datalist_sup
for seg in segs_sup_later:
    file_sup = open(female_file+'/female_hum_'+seg+'_con_of_'+s+'_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    female_con_sup_later = female_con_sup_later+datalist_sup

for seg in segs_jux:
    file_jux = open(female_file+'/female_hum_'+seg+'_con_of_'+s+'_in_Lumen_jux4.txt','r')
    datalist_jux = []

    for i in file_jux:
        line = i.split(' ')
        datalist_jux.append(float(line[0]))
    female_con_jux = female_con_jux+datalist_jux

for seg in segs_cd:
    file_cd = open(female_file+'/female_hum_'+seg+'_con_of_'+s+'_in_Lumen.txt','r')
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
    file_sup = open(male_file+'/male_hum_'+seg+'_con_of_'+s+'_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    male_con_sup_early = male_con_sup_early+datalist_sup
for seg in segs_sup_later:
    file_sup = open(male_file+'/male_hum_'+seg+'_con_of_'+s+'_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    male_con_sup_later = male_con_sup_later+datalist_sup

for seg in segs_jux:
    file_jux = open(male_file+'/male_hum_'+seg+'_con_of_'+s+'_in_Lumen_jux1.txt','r')
    datalist_jux = []

    for i in file_jux:
        line = i.split(' ')
        datalist_jux.append(float(line[0]))
    male_con_jux = male_con_jux+datalist_jux

for seg in segs_cd:
    file_cd = open(male_file+'/male_hum_'+seg+'_con_of_'+s+'_in_Lumen.txt','r')
    datalist_cd = []
    for i in file_cd:
        line = i.split(' ')
        datalist_cd.append(float(line[0]))
    male_con_cd = male_con_cd+datalist_cd

pos_pt=[1.7*i/199 for i in range(181)]
pos_s3=[1.7*i/199 for i in range(180,200)]
pos_sdl=[1.7+0.33*i/199 for i in range(200)]
pos_ldl=[1.7+0.33+1.5*i/199 for i in range(200)]
pos_lal=[1.7+0.33+1.5+1.5*i/199 for i in range(200)]
pos_mtal=[1.7+0.33+1.5+1.5+0.5*i/199 for i in range(200)]
pos_ctal=[1.7+0.33+1.5+1.5+0.5+0.05*i/199 for i in range(200)]
pos_dct=[1.7+0.33+1.5+1.5+0.5+0.05+0.2*i/199 for i in range(200)]
pos_cnt=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4*i/199 for i in range(200)]
pos=pos_pt+pos_s3+pos_sdl+pos_ldl+pos_lal+pos_mtal+pos_ctal+pos_dct+pos_cnt

pos_ccd=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4+0.4*i/199 for i in range(200)]
pos_omcd=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4+0.4+0.5*i/199 for i in range(200)]
pos_imcd=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4+0.4+0.5+1.2*i/199 for i in range(200)]

#female_sup_early = axarr[0,1].plot(pos_pt+pos_s3+pos_sdl,female_con_sup_early,color = 'magenta',label = 'Female superficial')
#female_sup_later = axarr[0,1].plot(pos_mtal+pos_ctal+pos_dct+pos_cnt,female_con_sup_later,color = 'magenta')
female_jux = axarr[0,1].plot(pos,female_con_jux,color = 'magenta',label = 'Female',linewidth=2)
female_cd = axarr[0,1].plot(pos_ccd+pos_omcd+pos_imcd,female_con_cd,color = 'magenta',linewidth=2)

#male_sup_early = axarr[0,1].plot(pos_pt+pos_s3+pos_sdl,male_con_sup_early,color = 'royalblue',label = 'Male superficial')
#male_sup_later = axarr[0,1].plot(pos_mtal+pos_ctal+pos_dct+pos_cnt,male_con_sup_later,color = 'royalblue')
male_jux = axarr[0,1].plot(pos,male_con_jux,color = 'royalblue',label = 'Male',linewidth=2)
male_cd = axarr[0,1].plot(pos_ccd+pos_omcd+pos_imcd,male_con_cd,color = 'royalblue',linewidth=2)

pt_ht = 10
sdl_ht = 5
ldl_ht = 10
lal_ht = 15
tal_ht = 10
dct_ht = 0
cnt_ht = 10
cd_ht = 60

h = 1

axarr[0,1].plot(pos_pt+pos_s3,[pt_ht for i in pos_pt+pos_s3],'--',pos_sdl,[sdl_ht for i in pos_sdl],'--',pos_ldl,[ldl_ht for i in pos_ldl],'--',pos_lal,[lal_ht for i in pos_lal],'--',pos_mtal+pos_ctal,[tal_ht for i in pos_mtal+pos_ctal],'--',pos_dct,[dct_ht for i in pos_dct],'--',pos_cnt,[cnt_ht for i in pos_cnt],'--',pos_ccd+pos_omcd+pos_imcd,[cd_ht for i in pos_ccd+pos_omcd+pos_imcd],'--')
axarr[0,1].text(pos_pt[90],pt_ht+h,'PT',fontsize=20)
axarr[0,1].text(pos_sdl[50],sdl_ht+h,'SDL',fontsize=20)
axarr[0,1].text(pos_ldl[70],ldl_ht+h,'LDL',fontsize=20)
axarr[0,1].text(pos_lal[70],lal_ht+h,'LAL',fontsize=20)
axarr[0,1].text(pos_mtal[50],tal_ht+h,'TAL',fontsize=20)
axarr[0,1].text(pos_dct[10],dct_ht+h,'DCT',fontsize=20)
axarr[0,1].text(pos_cnt[10],cnt_ht+h,'CNT',fontsize=20)
axarr[0,1].text(pos_omcd[100],cd_ht+h,'CD',fontsize=20)
axarr[0,1].tick_params(labelsize = 30)
axarr[0,1].legend(fontsize = 25, markerscale = 25)
axarr[0,1].set_ylabel('[K$^+$] (mM)',fontsize = 35)
axarr[0,1].get_xaxis().set_visible(False)

#========================================================
# Cl
#========================================================
s = 'Cl'

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
    file_sup = open(female_file+'/female_hum_'+seg+'_con_of_'+s+'_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    female_con_sup_early = female_con_sup_early+datalist_sup
for seg in segs_sup_later:
    file_sup = open(female_file+'/female_hum_'+seg+'_con_of_'+s+'_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    female_con_sup_later = female_con_sup_later+datalist_sup

for seg in segs_jux:
    file_jux = open(female_file+'/female_hum_'+seg+'_con_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_jux = []

    for i in file_jux:
        line = i.split(' ')
        datalist_jux.append(float(line[0]))
    female_con_jux = female_con_jux+datalist_jux

for seg in segs_cd:
    file_cd = open(female_file+'/female_hum_'+seg+'_con_of_'+s+'_in_Lumen.txt','r')
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
    file_sup = open(male_file+'/male_hum_'+seg+'_con_of_'+s+'_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    male_con_sup_early = male_con_sup_early+datalist_sup
for seg in segs_sup_later:
    file_sup = open(male_file+'/male_hum_'+seg+'_con_of_'+s+'_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    male_con_sup_later = male_con_sup_later+datalist_sup

for seg in segs_jux:
    file_jux = open(male_file+'/male_hum_'+seg+'_con_of_'+s+'_in_Lumen_jux4.txt','r')
    datalist_jux = []

    for i in file_jux:
        line = i.split(' ')
        datalist_jux.append(float(line[0]))
    male_con_jux = male_con_jux+datalist_jux

for seg in segs_cd:
    file_cd = open(male_file+'/male_hum_'+seg+'_con_of_'+s+'_in_Lumen.txt','r')
    datalist_cd = []
    for i in file_cd:
        line = i.split(' ')
        datalist_cd.append(float(line[0]))
    male_con_cd = male_con_cd+datalist_cd

pos_pt=[1.7*i/199 for i in range(181)]
pos_s3=[1.7*i/199 for i in range(180,200)]
pos_sdl=[1.7+0.33*i/199 for i in range(200)]
pos_ldl=[1.7+0.33+1.5*i/199 for i in range(200)]
pos_lal=[1.7+0.33+1.5+1.5*i/199 for i in range(200)]
pos_mtal=[1.7+0.33+1.5+1.5+0.5*i/199 for i in range(200)]
pos_ctal=[1.7+0.33+1.5+1.5+0.5+0.05*i/199 for i in range(200)]
pos_dct=[1.7+0.33+1.5+1.5+0.5+0.05+0.2*i/199 for i in range(200)]
pos_cnt=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4*i/199 for i in range(200)]
pos=pos_pt+pos_s3+pos_sdl+pos_ldl+pos_lal+pos_mtal+pos_ctal+pos_dct+pos_cnt

pos_ccd=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4+0.4*i/199 for i in range(200)]
pos_omcd=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4+0.4+0.5*i/199 for i in range(200)]
pos_imcd=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4+0.4+0.5+1.2*i/199 for i in range(200)]

#female_sup_early = axarr[0,2].plot(pos_pt+pos_s3+pos_sdl,female_con_sup_early,color = 'magenta',label = 'Female superficial')
#female_sup_later = axarr[0,2].plot(pos_mtal+pos_ctal+pos_dct+pos_cnt,female_con_sup_later,color = 'magenta')
female_jux = axarr[0,2].plot(pos,female_con_jux,color = 'magenta',label = 'Female',linewidth=2)
female_cd = axarr[0,2].plot(pos_ccd+pos_omcd+pos_imcd,female_con_cd,color = 'magenta',linewidth=2)

#male_sup_early = axarr[0,2].plot(pos_pt+pos_s3+pos_sdl,male_con_sup_early,color = 'royalblue',label = 'Male superficial')
#male_sup_later = axarr[0,2].plot(pos_mtal+pos_ctal+pos_dct+pos_cnt,male_con_sup_later,color = 'royalblue')
male_jux = axarr[0,2].plot(pos,male_con_jux,color = 'royalblue',label = 'Male',linewidth=2)
male_cd = axarr[0,2].plot(pos_ccd+pos_omcd+pos_imcd,male_con_cd,color = 'royalblue',linewidth=2)

pt_ht = 100
sdl_ht = 105
ldl_ht = 110
lal_ht = 105
tal_ht = 120
dct_ht = 0
cnt_ht = 15
cd_ht = 60

h = 2

axarr[0,2].plot(pos_pt+pos_s3,[pt_ht for i in pos_pt+pos_s3],'--',pos_sdl,[sdl_ht for i in pos_sdl],'--',pos_ldl,[ldl_ht for i in pos_ldl],'--',pos_lal,[lal_ht for i in pos_lal],'--',pos_mtal+pos_ctal,[tal_ht for i in pos_mtal+pos_ctal],'--',pos_dct,[dct_ht for i in pos_dct],'--',pos_cnt,[cnt_ht for i in pos_cnt],'--',pos_ccd+pos_omcd+pos_imcd,[cd_ht for i in pos_ccd+pos_omcd+pos_imcd],'--')
axarr[0,2].text(pos_pt[90],pt_ht+h,'PT',fontsize=20)
axarr[0,2].text(pos_sdl[50],sdl_ht+h,'SDL',fontsize=20)
axarr[0,2].text(pos_ldl[70],ldl_ht+h,'LDL',fontsize=20)
axarr[0,2].text(pos_lal[70],lal_ht+h,'LAL',fontsize=20)
axarr[0,2].text(pos_mtal[50],tal_ht+h,'TAL',fontsize=20)
axarr[0,2].text(pos_dct[10],dct_ht+h,'DCT',fontsize=20)
axarr[0,2].text(pos_cnt[10],cnt_ht+h,'CNT',fontsize=20)
axarr[0,2].text(pos_omcd[100],cd_ht+h,'CD',fontsize=20)
axarr[0,2].tick_params(labelsize = 30)
axarr[0,2].legend(fontsize = 25, markerscale = 25)
axarr[0,2].set_ylabel('[Cl$^-$] (mM)',fontsize = 35)
axarr[0,2].get_xaxis().set_visible(False)

#========================================================
# HCO3
#========================================================
s = 'HCO3'

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
    file_sup = open(female_file+'/female_hum_'+seg+'_con_of_'+s+'_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    female_con_sup_early = female_con_sup_early+datalist_sup
for seg in segs_sup_later:
    file_sup = open(female_file+'/female_hum_'+seg+'_con_of_'+s+'_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    female_con_sup_later = female_con_sup_later+datalist_sup

for seg in segs_jux:
    file_jux = open(female_file+'/female_hum_'+seg+'_con_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_jux = []

    for i in file_jux:
        line = i.split(' ')
        datalist_jux.append(float(line[0]))
    female_con_jux = female_con_jux+datalist_jux

for seg in segs_cd:
    file_cd = open(female_file+'/female_hum_'+seg+'_con_of_'+s+'_in_Lumen.txt','r')
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
    file_sup = open(male_file+'/male_hum_'+seg+'_con_of_'+s+'_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    male_con_sup_early = male_con_sup_early+datalist_sup
for seg in segs_sup_later:
    file_sup = open(male_file+'/male_hum_'+seg+'_con_of_'+s+'_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    male_con_sup_later = male_con_sup_later+datalist_sup

for seg in segs_jux:
    file_jux = open(male_file+'/male_hum_'+seg+'_con_of_'+s+'_in_Lumen_jux4.txt','r')
    datalist_jux = []

    for i in file_jux:
        line = i.split(' ')
        datalist_jux.append(float(line[0]))
    male_con_jux = male_con_jux+datalist_jux

for seg in segs_cd:
    file_cd = open(male_file+'/male_hum_'+seg+'_con_of_'+s+'_in_Lumen.txt','r')
    datalist_cd = []
    for i in file_cd:
        line = i.split(' ')
        datalist_cd.append(float(line[0]))
    male_con_cd = male_con_cd+datalist_cd

pos_pt=[1.7*i/199 for i in range(181)]
pos_s3=[1.7*i/199 for i in range(180,200)]
pos_sdl=[1.7+0.33*i/199 for i in range(200)]
pos_ldl=[1.7+0.33+1.5*i/199 for i in range(200)]
pos_lal=[1.7+0.33+1.5+1.5*i/199 for i in range(200)]
pos_mtal=[1.7+0.33+1.5+1.5+0.5*i/199 for i in range(200)]
pos_ctal=[1.7+0.33+1.5+1.5+0.5+0.05*i/199 for i in range(200)]
pos_dct=[1.7+0.33+1.5+1.5+0.5+0.05+0.2*i/199 for i in range(200)]
pos_cnt=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4*i/199 for i in range(200)]
pos=pos_pt+pos_s3+pos_sdl+pos_ldl+pos_lal+pos_mtal+pos_ctal+pos_dct+pos_cnt

pos_ccd=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4+0.4*i/199 for i in range(200)]
pos_omcd=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4+0.4+0.5*i/199 for i in range(200)]
pos_imcd=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4+0.4+0.5+1.2*i/199 for i in range(200)]

#female_sup_early = axarr[1,0].plot(pos_pt+pos_s3+pos_sdl,female_con_sup_early,color = 'magenta',label = 'Female superficial')
#female_sup_later = axarr[1,0].plot(pos_mtal+pos_ctal+pos_dct+pos_cnt,female_con_sup_later,color = 'magenta')
female_jux = axarr[1,0].plot(pos,female_con_jux,color = 'magenta',label = 'Female',linewidth=2)
female_cd = axarr[1,0].plot(pos_ccd+pos_omcd+pos_imcd,female_con_cd,color = 'magenta',linewidth=2)

#male_sup_early = axarr[1,0].plot(pos_pt+pos_s3+pos_sdl,male_con_sup_early,color = 'royalblue',label = 'Male superficial')
#male_sup_later = axarr[1,0].plot(pos_mtal+pos_ctal+pos_dct+pos_cnt,male_con_sup_later,color = 'royalblue')
male_jux = axarr[1,0].plot(pos,male_con_jux,color = 'royalblue',label = 'Male',linewidth=2)
male_cd = axarr[1,0].plot(pos_ccd+pos_omcd+pos_imcd,male_con_cd,color = 'royalblue',linewidth=2)

pt_ht = 20
sdl_ht = 25
ldl_ht = 25
lal_ht = 25
tal_ht = 10
dct_ht = 4
cnt_ht = 2.25
cd_ht = 0

h = 1

axarr[1,0].plot(pos_pt+pos_s3,[pt_ht for i in pos_pt+pos_s3],'--',pos_sdl,[sdl_ht for i in pos_sdl],'--',pos_ldl,[ldl_ht for i in pos_ldl],'--',pos_lal,[lal_ht for i in pos_lal],'--',pos_mtal+pos_ctal,[tal_ht for i in pos_mtal+pos_ctal],'--',pos_dct,[dct_ht for i in pos_dct],'--',pos_cnt,[cnt_ht for i in pos_cnt],'--',pos_ccd+pos_omcd+pos_imcd,[cd_ht for i in pos_ccd+pos_omcd+pos_imcd],'--')
axarr[1,0].text(pos_pt[90],pt_ht+h,'PT',fontsize=20)
axarr[1,0].text(pos_sdl[50],sdl_ht+h,'SDL',fontsize=20)
axarr[1,0].text(pos_ldl[70],ldl_ht+h,'LDL',fontsize=20)
axarr[1,0].text(pos_lal[70],lal_ht+h,'LAL',fontsize=20)
axarr[1,0].text(pos_mtal[50],tal_ht+h,'TAL',fontsize=20)
axarr[1,0].text(pos_dct[10],dct_ht+h,'DCT',fontsize=20)
axarr[1,0].text(pos_cnt[10],cnt_ht+h,'CNT',fontsize=20)
axarr[1,0].text(pos_omcd[100],cd_ht+h,'CD',fontsize=20)
axarr[1,0].tick_params(labelsize = 30)
axarr[1,0].legend(fontsize = 25, markerscale = 25)
axarr[1,0].set_ylabel('[HCO$_3^-$] (mM)',fontsize = 35)
axarr[1,0].get_xaxis().set_visible(False)

#========================================================
# NH4
#========================================================
s = 'NH4'

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
    file_sup = open(female_file+'/female_hum_'+seg+'_con_of_'+s+'_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    female_con_sup_early = female_con_sup_early+datalist_sup
for seg in segs_sup_later:
    file_sup = open(female_file+'/female_hum_'+seg+'_con_of_'+s+'_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    female_con_sup_later = female_con_sup_later+datalist_sup

for seg in segs_jux:
    file_jux = open(female_file+'/female_hum_'+seg+'_con_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_jux = []

    for i in file_jux:
        line = i.split(' ')
        datalist_jux.append(float(line[0]))
    female_con_jux = female_con_jux+datalist_jux

for seg in segs_cd:
    file_cd = open(female_file+'/female_hum_'+seg+'_con_of_'+s+'_in_Lumen.txt','r')
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
    file_sup = open(male_file+'/male_hum_'+seg+'_con_of_'+s+'_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    male_con_sup_early = male_con_sup_early+datalist_sup
for seg in segs_sup_later:
    file_sup = open(male_file+'/male_hum_'+seg+'_con_of_'+s+'_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    male_con_sup_later = male_con_sup_later+datalist_sup

for seg in segs_jux:
    file_jux = open(male_file+'/male_hum_'+seg+'_con_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_jux = []

    for i in file_jux:
        line = i.split(' ')
        datalist_jux.append(float(line[0]))
    male_con_jux = male_con_jux+datalist_jux

for seg in segs_cd:
    file_cd = open(male_file+'/male_hum_'+seg+'_con_of_'+s+'_in_Lumen.txt','r')
    datalist_cd = []
    for i in file_cd:
        line = i.split(' ')
        datalist_cd.append(float(line[0]))
    male_con_cd = male_con_cd+datalist_cd

pos_pt=[1.7*i/199 for i in range(181)]
pos_s3=[1.7*i/199 for i in range(180,200)]
pos_sdl=[1.7+0.33*i/199 for i in range(200)]
pos_ldl=[1.7+0.33+1.5*i/199 for i in range(200)]
pos_lal=[1.7+0.33+1.5+1.5*i/199 for i in range(200)]
pos_mtal=[1.7+0.33+1.5+1.5+0.5*i/199 for i in range(200)]
pos_ctal=[1.7+0.33+1.5+1.5+0.5+0.05*i/199 for i in range(200)]
pos_dct=[1.7+0.33+1.5+1.5+0.5+0.05+0.2*i/199 for i in range(200)]
pos_cnt=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4*i/199 for i in range(200)]
pos=pos_pt+pos_s3+pos_sdl+pos_ldl+pos_lal+pos_mtal+pos_ctal+pos_dct+pos_cnt

pos_ccd=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4+0.4*i/199 for i in range(200)]
pos_omcd=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4+0.4+0.5*i/199 for i in range(200)]
pos_imcd=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4+0.4+0.5+1.2*i/199 for i in range(200)]

#female_sup_early = axarr[1,1].plot(pos_pt+pos_s3+pos_sdl,female_con_sup_early,color = 'magenta',label = 'Female superficial')
#female_sup_later = axarr[1,1].plot(pos_mtal+pos_ctal+pos_dct+pos_cnt,female_con_sup_later,color = 'magenta')
female_jux = axarr[1,1].plot(pos,female_con_jux,color = 'magenta',label = 'Female',linewidth=2)
female_cd = axarr[1,1].plot(pos_ccd+pos_omcd+pos_imcd,female_con_cd,color = 'magenta',linewidth=2)

#male_sup_early = axarr[1,1].plot(pos_pt+pos_s3+pos_sdl,male_con_sup_early,color = 'royalblue',label = 'Male superficial')
#male_sup_later = axarr[1,1].plot(pos_mtal+pos_ctal+pos_dct+pos_cnt,male_con_sup_later,color = 'royalblue')
male_jux = axarr[1,1].plot(pos,male_con_jux,color = 'royalblue',label = 'Male',linewidth=2)
male_cd = axarr[1,1].plot(pos_ccd+pos_omcd+pos_imcd,male_con_cd,color = 'royalblue',linewidth=2)

pt_ht = 0
sdl_ht = 5
ldl_ht = 10
lal_ht = 5
tal_ht = 0
dct_ht = 5
cnt_ht = 10
cd_ht = 30

h = 1

axarr[1,1].plot(pos_pt+pos_s3,[pt_ht for i in pos_pt+pos_s3],'--',pos_sdl,[sdl_ht for i in pos_sdl],'--',pos_ldl,[ldl_ht for i in pos_ldl],'--',pos_lal,[lal_ht for i in pos_lal],'--',pos_mtal+pos_ctal,[tal_ht for i in pos_mtal+pos_ctal],'--',pos_dct,[dct_ht for i in pos_dct],'--',pos_cnt,[cnt_ht for i in pos_cnt],'--',pos_ccd+pos_omcd+pos_imcd,[cd_ht for i in pos_ccd+pos_omcd+pos_imcd],'--')
axarr[1,1].text(pos_pt[90],pt_ht+h,'PT',fontsize=20)
axarr[1,1].text(pos_sdl[50],sdl_ht+h,'SDL',fontsize=20)
axarr[1,1].text(pos_ldl[70],ldl_ht+h,'LDL',fontsize=20)
axarr[1,1].text(pos_lal[70],lal_ht+h,'LAL',fontsize=20)
axarr[1,1].text(pos_mtal[50],tal_ht+h,'TAL',fontsize=20)
axarr[1,1].text(pos_dct[10],dct_ht+h,'DCT',fontsize=20)
axarr[1,1].text(pos_cnt[10],cnt_ht+h,'CNT',fontsize=20)
axarr[1,1].text(pos_omcd[100],cd_ht+h,'CD',fontsize=20)
axarr[1,1].tick_params(labelsize = 30)
axarr[1,1].legend(fontsize = 25, markerscale = 25)
axarr[1,1].set_ylabel('[NH$_4^+$] (mM)',fontsize = 35)
axarr[1,1].get_xaxis().set_visible(False)

#========================================================
# TA
#========================================================
s = 'TA'

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
    file_sup_h2po4 = open(female_file+'/female_hum_'+seg+'_con_of_H2PO4_in_Lumen_sup.txt','r')
    file_sup_hpo4 = open(female_file+'/female_hum_'+seg+'_con_of_HPO4_in_Lumen_sup.txt','r')
    datalist_sup_h2po4 = []
    datalist_sup_hpo4 = []

    for i in file_sup_h2po4:
        line = i.split(' ')
        datalist_sup_h2po4.append(float(line[0]))
    for i in file_sup_hpo4:
        line = i.split(' ')
        datalist_sup_hpo4.append(float(line[0]))
    datalist_sup = [(10**(7.4-6.8)*datalist_sup_h2po4[i]-datalist_sup_hpo4[i])/(1+10**(7.4-6.8)) for i in range(len(datalist_sup_h2po4))]
    female_con_sup_early = female_con_sup_early+datalist_sup
for seg in segs_sup_later:
    file_sup_h2po4 = open(female_file+'/female_hum_'+seg+'_con_of_H2PO4_in_Lumen_sup.txt','r')
    file_sup_hpo4 = open(female_file+'/female_hum_'+seg+'_con_of_HPO4_in_Lumen_sup.txt','r')
    datalist_sup_h2po4 = []
    datalist_sup_hpo4 = []
    for i in file_sup_h2po4:
        line = i.split(' ')
        datalist_sup_h2po4.append(float(line[0]))
    for i in file_sup_hpo4:
        line = i.split(' ')
        datalist_sup_hpo4.append(float(line[0]))
    datalist_sup = [(10**(7.4-6.8)*datalist_sup_h2po4[i]-datalist_sup_hpo4[i])/(1+10**(7.4-6.8)) for i in range(len(datalist_sup_h2po4))]
    female_con_sup_later = female_con_sup_later+datalist_sup

for seg in segs_jux:
    file_jux_h2po4 = open(female_file+'/female_hum_'+seg+'_con_of_H2PO4_in_Lumen_jux5.txt','r')
    file_jux_hpo4 = open(female_file+'/female_hum_'+seg+'_con_of_HPO4_in_Lumen_jux5.txt','r')
    datalist_jux_h2po4 = []
    datalist_jux_hpo4 = []

    for i in file_jux_h2po4:
        line = i.split(' ')
        datalist_jux_h2po4.append(float(line[0]))
    for i in file_jux_hpo4:
        line = i.split(' ')
        datalist_jux_hpo4.append(float(line[0]))
    datalist_jux = [(10**(7.4-6.8)*datalist_jux_h2po4[i]-datalist_jux_hpo4[i])/(1+10**(7.4-6.8)) for i in range(len(datalist_jux_h2po4))]
    female_con_jux = female_con_jux+datalist_jux

for seg in segs_cd:
    file_cd_h2po4 = open(female_file+'/female_hum_'+seg+'_con_of_H2PO4_in_Lumen.txt','r')
    file_cd_hpo4 = open(female_file+'/female_hum_'+seg+'_con_of_HPO4_in_Lumen.txt','r')
    datalist_cd_h2po4 = []
    datalist_cd_hpo4 = []
    for i in file_cd_h2po4:
        line = i.split(' ')
        datalist_cd_h2po4.append(float(line[0]))
    for i in file_cd_hpo4:
        line = i.split(' ')
        datalist_cd_hpo4.append(float(line[0]))
    datalist_cd = [(10**(7.4-6.8)*datalist_cd_h2po4[i]-datalist_cd_hpo4[i])/(1+10**(7.4-6.8)) for i in range(len(datalist_cd_h2po4))]
    female_con_cd = female_con_cd+datalist_cd
#===============================================
# Male
#===============================================

male_con_number = []
male_con_sup_early = []
male_con_sup_later = []
male_con_jux = []
male_con_cd = []

segs_sup_early = ['pt','s3','sdl']
segs_sup_later = ['mtal','ctal','dct','cnt']
segs_jux = ['pt','s3','sdl','ldl','lal','mtal','ctal','dct','cnt']
segs_cd = ['ccd','omcd','imcd']
for seg in segs_sup_early:
    file_sup_h2po4 = open(male_file+'/male_hum_'+seg+'_con_of_H2PO4_in_Lumen_sup.txt','r')
    file_sup_hpo4 = open(male_file+'/male_hum_'+seg+'_con_of_HPO4_in_Lumen_sup.txt','r')
    datalist_sup_h2po4 = []
    datalist_sup_hpo4 = []

    for i in file_sup_h2po4:
        line = i.split(' ')
        datalist_sup_h2po4.append(float(line[0]))
    for i in file_sup_hpo4:
        line = i.split(' ')
        datalist_sup_hpo4.append(float(line[0]))
    datalist_sup = [(10**(7.4-6.8)*datalist_sup_h2po4[i]-datalist_sup_hpo4[i])/(1+10**(7.4-6.8)) for i in range(len(datalist_sup_h2po4))]
    male_con_sup_early = male_con_sup_early+datalist_sup
for seg in segs_sup_later:
    file_sup_h2po4 = open(male_file+'/male_hum_'+seg+'_con_of_H2PO4_in_Lumen_sup.txt','r')
    file_sup_hpo4 = open(male_file+'/male_hum_'+seg+'_con_of_HPO4_in_Lumen_sup.txt','r')
    datalist_sup_h2po4 = []
    datalist_sup_hpo4 = []
    for i in file_sup_h2po4:
        line = i.split(' ')
        datalist_sup_h2po4.append(float(line[0]))
    for i in file_sup_hpo4:
        line = i.split(' ')
        datalist_sup_hpo4.append(float(line[0]))
    datalist_sup = [(10**(7.4-6.8)*datalist_sup_h2po4[i]-datalist_sup_hpo4[i])/(1+10**(7.4-6.8)) for i in range(len(datalist_sup_h2po4))]
    male_con_sup_later = male_con_sup_later+datalist_sup

for seg in segs_jux:
    file_jux_h2po4 = open(male_file+'/male_hum_'+seg+'_con_of_H2PO4_in_Lumen_jux5.txt','r')
    file_jux_hpo4 = open(male_file+'/male_hum_'+seg+'_con_of_HPO4_in_Lumen_jux5.txt','r')
    datalist_jux_h2po4 = []
    datalist_jux_hpo4 = []

    for i in file_jux_h2po4:
        line = i.split(' ')
        datalist_jux_h2po4.append(float(line[0]))
    for i in file_jux_hpo4:
        line = i.split(' ')
        datalist_jux_hpo4.append(float(line[0]))
    datalist_jux = [(10**(7.4-6.8)*datalist_jux_h2po4[i]-datalist_jux_hpo4[i])/(1+10**(7.4-6.8)) for i in range(len(datalist_jux_h2po4))]
    male_con_jux = male_con_jux+datalist_jux

for seg in segs_cd:
    file_cd_h2po4 = open(male_file+'/male_hum_'+seg+'_con_of_H2PO4_in_Lumen.txt','r')
    file_cd_hpo4 = open(male_file+'/male_hum_'+seg+'_con_of_HPO4_in_Lumen.txt','r')
    datalist_cd_h2po4 = []
    datalist_cd_hpo4 = []
    for i in file_cd_h2po4:
        line = i.split(' ')
        datalist_cd_h2po4.append(float(line[0]))
    for i in file_cd_hpo4:
        line = i.split(' ')
        datalist_cd_hpo4.append(float(line[0]))
    datalist_cd = [(10**(7.4-6.8)*datalist_cd_h2po4[i]-datalist_cd_hpo4[i])/(1+10**(7.4-6.8)) for i in range(len(datalist_cd_h2po4))]
    male_con_cd = male_con_cd+datalist_cd

pos_pt=[1.7*i/199 for i in range(181)]
pos_s3=[1.7*i/199 for i in range(180,200)]
pos_sdl=[1.7+0.33*i/199 for i in range(200)]
pos_ldl=[1.7+0.33+1.5*i/199 for i in range(200)]
pos_lal=[1.7+0.33+1.5+1.5*i/199 for i in range(200)]
pos_mtal=[1.7+0.33+1.5+1.5+0.5*i/199 for i in range(200)]
pos_ctal=[1.7+0.33+1.5+1.5+0.5+0.05*i/199 for i in range(200)]
pos_dct=[1.7+0.33+1.5+1.5+0.5+0.05+0.2*i/199 for i in range(200)]
pos_cnt=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4*i/199 for i in range(200)]
pos=pos_pt+pos_s3+pos_sdl+pos_ldl+pos_lal+pos_mtal+pos_ctal+pos_dct+pos_cnt

pos_ccd=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4+0.4*i/199 for i in range(200)]
pos_omcd=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4+0.4+0.5*i/199 for i in range(200)]
pos_imcd=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4+0.4+0.5+1.2*i/199 for i in range(200)]

#female_sup_early = axarr[1,2].plot(pos_pt+pos_s3+pos_sdl,female_con_sup_early,color = 'magenta',label = 'Female superficial')
#female_sup_later = axarr[1,2].plot(pos_mtal+pos_ctal+pos_dct+pos_cnt,female_con_sup_later,color = 'magenta')
female_jux = axarr[1,2].plot(pos,female_con_jux,color = 'magenta',label = 'Female',linewidth=2)
female_cd = axarr[1,2].plot(pos_ccd+pos_omcd+pos_imcd,female_con_cd,color = 'magenta',linewidth=2)

#male_sup_early = axarr[1,2].plot(pos_pt+pos_s3+pos_sdl,male_con_sup_early,color = 'royalblue',label = 'Male superficial')
#male_sup_later = axarr[1,2].plot(pos_mtal+pos_ctal+pos_dct+pos_cnt,male_con_sup_later,color = 'royalblue')
male_jux = axarr[1,2].plot(pos,male_con_jux,color = 'royalblue',label = 'Male',linewidth=2)
male_cd = axarr[1,2].plot(pos_ccd+pos_omcd+pos_imcd,male_con_cd,color = 'royalblue',linewidth=2)

pt_ht = 0
sdl_ht = 2
ldl_ht = 3
lal_ht = 2
tal_ht = 0
dct_ht = 2
cnt_ht = 5
cd_ht = 12

h = 0.5

axarr[1,2].plot(pos_pt+pos_s3,[pt_ht for i in pos_pt+pos_s3],'--',pos_sdl,[sdl_ht for i in pos_sdl],'--',pos_ldl,[ldl_ht for i in pos_ldl],'--',pos_lal,[lal_ht for i in pos_lal],'--',pos_mtal+pos_ctal,[tal_ht for i in pos_mtal+pos_ctal],'--',pos_dct,[dct_ht for i in pos_dct],'--',pos_cnt,[cnt_ht for i in pos_cnt],'--',pos_ccd+pos_omcd+pos_imcd,[cd_ht for i in pos_ccd+pos_omcd+pos_imcd],'--')
axarr[1,2].text(pos_pt[90],pt_ht+h,'PT',fontsize=20)
axarr[1,2].text(pos_sdl[50],sdl_ht+h,'SDL',fontsize=20)
axarr[1,2].text(pos_ldl[70],ldl_ht+h,'LDL',fontsize=20)
axarr[1,2].text(pos_lal[70],lal_ht+h,'LAL',fontsize=20)
axarr[1,2].text(pos_mtal[50],tal_ht+h,'TAL',fontsize=20)
axarr[1,2].text(pos_dct[10],dct_ht+h,'DCT',fontsize=20)
axarr[1,2].text(pos_cnt[10],cnt_ht+h,'CNT',fontsize=20)
axarr[1,2].text(pos_omcd[100],cd_ht+h,'CD',fontsize=20)
axarr[1,2].tick_params(labelsize = 30)
axarr[1,2].legend(fontsize = 25, markerscale = 25)
axarr[1,2].set_ylabel('[TA] (mM)',fontsize = 35)
axarr[1,2].get_xaxis().set_visible(False)

#========================================================
# Urea
#========================================================
s = 'urea'

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
    file_sup = open(female_file+'/female_hum_'+seg+'_con_of_'+s+'_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    female_con_sup_early = female_con_sup_early+datalist_sup
for seg in segs_sup_later:
    file_sup = open(female_file+'/female_hum_'+seg+'_con_of_'+s+'_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    female_con_sup_later = female_con_sup_later+datalist_sup

for seg in segs_jux:
    file_jux = open(female_file+'/female_hum_'+seg+'_con_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_jux = []

    for i in file_jux:
        line = i.split(' ')
        datalist_jux.append(float(line[0]))
    female_con_jux = female_con_jux+datalist_jux

for seg in segs_cd:
    file_cd = open(female_file+'/female_hum_'+seg+'_con_of_'+s+'_in_Lumen.txt','r')
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
    file_sup = open(male_file+'/male_hum_'+seg+'_con_of_'+s+'_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    male_con_sup_early = male_con_sup_early+datalist_sup
for seg in segs_sup_later:
    file_sup = open(male_file+'/male_hum_'+seg+'_con_of_'+s+'_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    male_con_sup_later = male_con_sup_later+datalist_sup

for seg in segs_jux:
    file_jux = open(male_file+'/male_hum_'+seg+'_con_of_'+s+'_in_Lumen_jux4.txt','r')
    datalist_jux = []

    for i in file_jux:
        line = i.split(' ')
        datalist_jux.append(float(line[0]))
    male_con_jux = male_con_jux+datalist_jux

for seg in segs_cd:
    file_cd = open(male_file+'/male_hum_'+seg+'_con_of_'+s+'_in_Lumen.txt','r')
    datalist_cd = []
    for i in file_cd:
        line = i.split(' ')
        datalist_cd.append(float(line[0]))
    male_con_cd = male_con_cd+datalist_cd

pos_pt=[1.7*i/199 for i in range(181)]
pos_s3=[1.7*i/199 for i in range(180,200)]
pos_sdl=[1.7+0.33*i/199 for i in range(200)]
pos_ldl=[1.7+0.33+1.5*i/199 for i in range(200)]
pos_lal=[1.7+0.33+1.5+1.5*i/199 for i in range(200)]
pos_mtal=[1.7+0.33+1.5+1.5+0.5*i/199 for i in range(200)]
pos_ctal=[1.7+0.33+1.5+1.5+0.5+0.05*i/199 for i in range(200)]
pos_dct=[1.7+0.33+1.5+1.5+0.5+0.05+0.2*i/199 for i in range(200)]
pos_cnt=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4*i/199 for i in range(200)]
pos=pos_pt+pos_s3+pos_sdl+pos_ldl+pos_lal+pos_mtal+pos_ctal+pos_dct+pos_cnt

pos_ccd=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4+0.4*i/199 for i in range(200)]
pos_omcd=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4+0.4+0.5*i/199 for i in range(200)]
pos_imcd=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4+0.4+0.5+1.2*i/199 for i in range(200)]

#female_sup_early = axarr[2,0].plot(pos_pt+pos_s3+pos_sdl,female_con_sup_early,color = 'magenta',label = 'Female superficial')
#female_sup_later = axarr[2,0].plot(pos_mtal+pos_ctal+pos_dct+pos_cnt,female_con_sup_later,color = 'magenta')
female_jux = axarr[2,0].plot(pos,female_con_jux,color = 'magenta',label = 'Female',linewidth=2)
female_cd = axarr[2,0].plot(pos_ccd+pos_omcd+pos_imcd,female_con_cd,color = 'magenta',linewidth=2)

#male_sup_early = axarr[2,0].plot(pos_pt+pos_s3+pos_sdl,male_con_sup_early,color = 'royalblue',label = 'Male superficial')
#male_sup_later = axarr[2,0].plot(pos_mtal+pos_ctal+pos_dct+pos_cnt,male_con_sup_later,color = 'royalblue')
male_jux = axarr[2,0].plot(pos,male_con_jux,color = 'royalblue',label = 'Male',linewidth=2)
male_cd = axarr[2,0].plot(pos_ccd+pos_omcd+pos_imcd,male_con_cd,color = 'royalblue',linewidth=2)

pt_ht = 20
sdl_ht = 40
ldl_ht = 45
lal_ht = 40
tal_ht = 55
dct_ht = 30
cnt_ht = 50
cd_ht = 200

h = 2

axarr[2,0].plot(pos_pt+pos_s3,[pt_ht for i in pos_pt+pos_s3],'--',pos_sdl,[sdl_ht for i in pos_sdl],'--',pos_ldl,[ldl_ht for i in pos_ldl],'--',pos_lal,[lal_ht for i in pos_lal],'--',pos_mtal+pos_ctal,[tal_ht for i in pos_mtal+pos_ctal],'--',pos_dct,[dct_ht for i in pos_dct],'--',pos_cnt,[cnt_ht for i in pos_cnt],'--',pos_ccd+pos_omcd+pos_imcd,[cd_ht for i in pos_ccd+pos_omcd+pos_imcd],'--')
axarr[2,0].text(pos_pt[90],pt_ht+h,'PT',fontsize=20)
axarr[2,0].text(pos_sdl[50],sdl_ht+h,'SDL',fontsize=20)
axarr[2,0].text(pos_ldl[70],ldl_ht+h,'LDL',fontsize=20)
axarr[2,0].text(pos_lal[70],lal_ht+h,'LAL',fontsize=20)
axarr[2,0].text(pos_mtal[50],tal_ht+h,'TAL',fontsize=20)
axarr[2,0].text(pos_dct[10],dct_ht+h,'DCT',fontsize=20)
axarr[2,0].text(pos_cnt[10],cnt_ht+h,'CNT',fontsize=20)
axarr[2,0].text(pos_omcd[100],cd_ht+h,'CD',fontsize=20)

axarr[2,0].tick_params(labelsize = 30)
axarr[2,0].legend(fontsize = 25, markerscale = 25)
axarr[2,0].set_ylabel('[urea] (mM)',fontsize = 35)
axarr[2,0].get_xaxis().set_visible(False)

#========================================================
# H
#========================================================
s = 'H'

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
    file_sup = open(female_file+'/female_hum_'+seg+'_con_of_'+s+'_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    datalist_sup_ph = [-np.log(i/1000)/np.log(10) for i in datalist_sup]
    female_con_sup_early = female_con_sup_early+datalist_sup_ph
for seg in segs_sup_later:
    file_sup = open(female_file+'/female_hum_'+seg+'_con_of_'+s+'_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    datalist_sup_ph = [-np.log(i/1000)/np.log(10) for i in datalist_sup]
    female_con_sup_later = female_con_sup_later+datalist_sup_ph

for seg in segs_jux:
    file_jux = open(female_file+'/female_hum_'+seg+'_con_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_jux = []

    for i in file_jux:
        line = i.split(' ')
        datalist_jux.append(float(line[0]))
    datalist_jux_ph = [-np.log(i/1000)/np.log(10) for i in datalist_jux]
    female_con_jux = female_con_jux+datalist_jux_ph

for seg in segs_cd:
    file_cd = open(female_file+'/female_hum_'+seg+'_con_of_'+s+'_in_Lumen.txt','r')
    datalist_cd = []
    for i in file_cd:
        line = i.split(' ')
        datalist_cd.append(float(line[0]))
    datalist_cd_ph = [-np.log(i/1000)/np.log(10) for i in datalist_cd]
    female_con_cd = female_con_cd+datalist_cd_ph
#===============================================
# Male
#===============================================

male_con_number = []
male_con_sup_early = []
male_con_sup_later = []
male_con_jux = []
male_con_cd = []
for seg in segs_sup_early:
    file_sup = open(male_file+'/male_hum_'+seg+'_con_of_'+s+'_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    datalist_sup_ph = [-np.log(i/1000)/np.log(10) for i in datalist_sup]
    male_con_sup_early = male_con_sup_early+datalist_sup_ph
for seg in segs_sup_later:
    file_sup = open(male_file+'/male_hum_'+seg+'_con_of_'+s+'_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    datalist_sup_ph = [-np.log(i/1000)/np.log(10) for i in datalist_sup]
    male_con_sup_later = male_con_sup_later+datalist_sup_ph

for seg in segs_jux:
    file_jux = open(male_file+'/male_hum_'+seg+'_con_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_jux = []

    for i in file_jux:
        line = i.split(' ')
        datalist_jux.append(float(line[0]))
    datalist_jux_ph = [-np.log(i/1000)/np.log(10) for i in datalist_jux]
    male_con_jux = male_con_jux+datalist_jux_ph

for seg in segs_cd:
    file_cd = open(male_file+'/male_hum_'+seg+'_con_of_'+s+'_in_Lumen.txt','r')
    datalist_cd = []
    for i in file_cd:
        line = i.split(' ')
        datalist_cd.append(float(line[0]))
    datalist_cd_ph = [-np.log(i/1000)/np.log(10) for i in datalist_cd]
    male_con_cd = male_con_cd+datalist_cd_ph

pos_pt=[1.7*i/199 for i in range(181)]
pos_s3=[1.7*i/199 for i in range(180,200)]
pos_sdl=[1.7+0.33*i/199 for i in range(200)]
pos_ldl=[1.7+0.33+1.5*i/199 for i in range(200)]
pos_lal=[1.7+0.33+1.5+1.5*i/199 for i in range(200)]
pos_mtal=[1.7+0.33+1.5+1.5+0.5*i/199 for i in range(200)]
pos_ctal=[1.7+0.33+1.5+1.5+0.5+0.05*i/199 for i in range(200)]
pos_dct=[1.7+0.33+1.5+1.5+0.5+0.05+0.2*i/199 for i in range(200)]
pos_cnt=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4*i/199 for i in range(200)]
pos=pos_pt+pos_s3+pos_sdl+pos_ldl+pos_lal+pos_mtal+pos_ctal+pos_dct+pos_cnt

pos_ccd=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4+0.4*i/199 for i in range(200)]
pos_omcd=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4+0.4+0.5*i/199 for i in range(200)]
pos_imcd=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4+0.4+0.5+1.2*i/199 for i in range(200)]

#female_sup_early = axarr[2,1].plot(pos_pt+pos_s3+pos_sdl,female_con_sup_early,color = 'magenta',label = 'Female superficial')
#female_sup_later = axarr[2,1].plot(pos_mtal+pos_ctal+pos_dct+pos_cnt,female_con_sup_later,color = 'magenta')
female_jux = axarr[2,1].plot(pos,female_con_jux,color = 'magenta',label = 'Female',linewidth=2)
female_cd = axarr[2,1].plot(pos_ccd+pos_omcd+pos_imcd,female_con_cd,color = 'magenta',linewidth=2)

#male_sup_early = axarr[2,1].plot(pos_pt+pos_s3+pos_sdl,male_con_sup_early,color = 'royalblue',label = 'Male superficial')
#male_sup_later = axarr[2,1].plot(pos_mtal+pos_ctal+pos_dct+pos_cnt,male_con_sup_later,color = 'royalblue')
male_jux = axarr[2,1].plot(pos,male_con_jux,color = 'royalblue',label = 'Male',linewidth=2)
male_cd = axarr[2,1].plot(pos_ccd+pos_omcd+pos_imcd,male_con_cd,color = 'royalblue',linewidth=2)

pt_ht = 7
sdl_ht = 7.2
ldl_ht = 7
lal_ht = 7.2
tal_ht = 7
dct_ht = 6
cnt_ht = 5.8
cd_ht = 6.125

h = 0.05

axarr[2,1].plot(pos_pt+pos_s3,[pt_ht for i in pos_pt+pos_s3],'--',pos_sdl,[sdl_ht for i in pos_sdl],'--',pos_ldl,[ldl_ht for i in pos_ldl],'--',pos_lal,[lal_ht for i in pos_lal],'--',pos_mtal+pos_ctal,[tal_ht for i in pos_mtal+pos_ctal],'--',pos_dct,[dct_ht for i in pos_dct],'--',pos_cnt,[cnt_ht for i in pos_cnt],'--',pos_ccd+pos_omcd+pos_imcd,[cd_ht for i in pos_ccd+pos_omcd+pos_imcd],'--')
axarr[2,1].text(pos_pt[90],pt_ht+h,'PT',fontsize=20)
axarr[2,1].text(pos_sdl[50],sdl_ht+h,'SDL',fontsize=20)
axarr[2,1].text(pos_ldl[70],ldl_ht+h,'LDL',fontsize=20)
axarr[2,1].text(pos_lal[70],lal_ht+h,'LAL',fontsize=20)
axarr[2,1].text(pos_mtal[50],tal_ht+h,'TAL',fontsize=20)
axarr[2,1].text(pos_dct[10],dct_ht+h,'DCT',fontsize=20)
axarr[2,1].text(pos_cnt[10],cnt_ht+h,'CNT',fontsize=20)
axarr[2,1].text(pos_omcd[100],cd_ht+h,'CD',fontsize=20)

axarr[2,1].tick_params(labelsize = 30)
axarr[2,1].legend(fontsize = 25, markerscale = 25)
axarr[2,1].set_ylabel('pH',fontsize = 35)
axarr[2,1].set_ylim(5.5,8.25)
axarr[2,1].get_xaxis().set_visible(False)

#========================================================
# Osmolality
#========================================================

female_con_number = []
female_con_sup_early = []
female_con_sup_later = []
female_con_jux = []
female_con_cd = []

segs_sup_early = ['PT','S3','SDL']
segs_sup_later = ['mTAL','cTAL','DCT','CNT']
segs_jux = ['PT','S3','SDL','LDL','LAL','mTAL','cTAL','DCT','CNT']
segs_cd = ['CCD','OMCD','IMCD']
for seg in segs_sup_early:
    file_sup = open(female_file+'/female_hum_'+seg+'_osmolality_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    female_con_sup_early = female_con_sup_early+datalist_sup
for seg in segs_sup_later:
    file_sup = open(female_file+'/female_hum_'+seg+'_osmolality_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    female_con_sup_later = female_con_sup_later+datalist_sup

for seg in segs_jux:
    file_jux = open(female_file+'/female_hum_'+seg+'_osmolality_in_Lumen_jux5.txt','r')
    datalist_jux = []

    for i in file_jux:
        line = i.split(' ')
        datalist_jux.append(float(line[0]))
    female_con_jux = female_con_jux+datalist_jux

for seg in segs_cd:
    file_cd = open(female_file+'/female_hum_'+seg+'_osmolality_in_Lumen.txt','r')
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
    file_sup = open(male_file+'/male_hum_'+seg+'_osmolality_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    male_con_sup_early = male_con_sup_early+datalist_sup
for seg in segs_sup_later:
    file_sup = open(male_file+'/male_hum_'+seg+'_osmolality_in_Lumen_sup.txt','r')
    datalist_sup = []

    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    male_con_sup_later = male_con_sup_later+datalist_sup

for seg in segs_jux:
    file_jux = open(male_file+'/male_hum_'+seg+'_osmolality_in_Lumen_jux4.txt','r')
    datalist_jux = []

    for i in file_jux:
        line = i.split(' ')
        datalist_jux.append(float(line[0]))
    male_con_jux = male_con_jux+datalist_jux

for seg in segs_cd:
    file_cd = open(male_file+'/male_hum_'+seg+'_osmolality_in_Lumen.txt','r')
    datalist_cd = []
    for i in file_cd:
        line = i.split(' ')
        datalist_cd.append(float(line[0]))
    male_con_cd = male_con_cd+datalist_cd

pos_pt=[1.7*i/199 for i in range(181)]
pos_s3=[1.7*i/199 for i in range(180,200)]
pos_sdl=[1.7+0.33*i/199 for i in range(200)]
pos_ldl=[1.7+0.33+1.5*i/199 for i in range(200)]
pos_lal=[1.7+0.33+1.5+1.5*i/199 for i in range(200)]
pos_mtal=[1.7+0.33+1.5+1.5+0.5*i/199 for i in range(200)]
pos_ctal=[1.7+0.33+1.5+1.5+0.5+0.05*i/199 for i in range(200)]
pos_dct=[1.7+0.33+1.5+1.5+0.5+0.05+0.2*i/199 for i in range(200)]
pos_cnt=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4*i/199 for i in range(200)]
pos=pos_pt+pos_s3+pos_sdl+pos_ldl+pos_lal+pos_mtal+pos_ctal+pos_dct+pos_cnt

pos_ccd=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4+0.4*i/199 for i in range(200)]
pos_omcd=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4+0.4+0.5*i/199 for i in range(200)]
pos_imcd=[1.7+0.33+1.5+1.5+0.5+0.05+0.2+0.4+0.4+0.5+1.2*i/199 for i in range(200)]

#female_sup_early = axarr[2,2].plot(pos_pt+pos_s3+pos_sdl,female_con_sup_early,color = 'magenta',label = 'Female superficial')
#female_sup_later = axarr[2,2].plot(pos_mtal+pos_ctal+pos_dct+pos_cnt,female_con_sup_later,color = 'magenta')
female_jux = axarr[2,2].plot(pos,female_con_jux,color = 'magenta',label = 'Female',linewidth=2)
female_cd = axarr[2,2].plot(pos_ccd+pos_omcd+pos_imcd,female_con_cd,color = 'magenta',linewidth=2)

#male_sup_early = axarr[2,2].plot(pos_pt+pos_s3+pos_sdl,male_con_sup_early,color = 'royalblue',label = 'Male superficial')
#male_sup_later = axarr[2,2].plot(pos_mtal+pos_ctal+pos_dct+pos_cnt,male_con_sup_later,color = 'royalblue')
male_jux = axarr[2,2].plot(pos,male_con_jux,color = 'royalblue',label = 'Male',linewidth=2)
male_cd = axarr[2,2].plot(pos_ccd+pos_omcd+pos_imcd,male_con_cd,color = 'royalblue',linewidth=2)

pt_ht = 280
sdl_ht = 620
ldl_ht = 625
lal_ht = 620
tal_ht = 650
dct_ht = 50
cnt_ht = 310
cd_ht = 500

h = 2

axarr[2,2].plot(pos_pt+pos_s3,[pt_ht for i in pos_pt+pos_s3],'--',pos_sdl,[sdl_ht for i in pos_sdl],'--',pos_ldl,[ldl_ht for i in pos_ldl],'--',pos_lal,[lal_ht for i in pos_lal],'--',pos_mtal+pos_ctal,[tal_ht for i in pos_mtal+pos_ctal],'--',pos_dct,[dct_ht for i in pos_dct],'--',pos_cnt,[cnt_ht for i in pos_cnt],'--',pos_ccd+pos_omcd+pos_imcd,[cd_ht for i in pos_ccd+pos_omcd+pos_imcd],'--')
axarr[2,2].text(pos_pt[90],pt_ht+h,'PT',fontsize=20)
axarr[2,2].text(pos_sdl[50],sdl_ht+h,'SDL',fontsize=20)
axarr[2,2].text(pos_ldl[70],ldl_ht+h,'LDL',fontsize=20)
axarr[2,2].text(pos_lal[70],lal_ht+h,'LAL',fontsize=20)
axarr[2,2].text(pos_mtal[50],tal_ht+h,'TAL',fontsize=20)
axarr[2,2].text(pos_dct[10],dct_ht+h,'DCT',fontsize=20)
axarr[2,2].text(pos_cnt[10],cnt_ht+h,'CNT',fontsize=20)
axarr[2,2].text(pos_omcd[100],cd_ht+h,'CD',fontsize=20)
axarr[2,2].tick_params(labelsize = 30)
axarr[2,2].legend(fontsize = 25, markerscale = 25)
axarr[2,2].set_ylabel('Osmolality (mosm/kg H$_2$O)',fontsize = 35)
axarr[2,2].set_ylim(0,1100)
axarr[2,2].get_xaxis().set_visible(False)

plt.subplots_adjust(hspace=0.1)

axarr[0,0].text(-0.5,axarr[0,0].get_ylim()[1],'A',size=40,weight='bold')
axarr[0,1].text(-0.5,axarr[0,1].get_ylim()[1],'B',size=40,weight='bold')
axarr[0,2].text(-0.5,axarr[0,2].get_ylim()[1],'C',size=40,weight='bold')
axarr[1,0].text(-0.5,axarr[1,0].get_ylim()[1],'D',size=40,weight='bold')
axarr[1,1].text(-0.5,axarr[1,1].get_ylim()[1],'E',size=40,weight='bold')
axarr[1,2].text(-0.5,axarr[1,2].get_ylim()[1],'F',size=40,weight='bold')
axarr[2,0].text(-0.5,axarr[2,0].get_ylim()[1],'G',size=40,weight='bold')
axarr[2,1].text(-0.5,axarr[2,1].get_ylim()[1],'H',size=40,weight='bold')
axarr[2,2].text(-0.5,axarr[2,2].get_ylim()[1],'I',size=40,weight='bold')

plt.savefig('baseline_concentration',bbox_inches = 'tight')