import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np
import os
import argparse

segment = ['PT','DL','mTAL','DCT','CNT','CCD','urine']

female_normal_file = './Female_hum_N_diab'
female_nhe50_file = './Female_hum_Y_diab'
#female_nhe80_file = './female_nhe80_check'

male_normal_file = './Male_hum_N_diab'
male_nhe50_file = './Male_hum_Y_diab'
#male_nhe80_file = './male_nhe80_check'

neph_weight = [0.85,(0.15)*0.4,(0.15)*0.3,(0.15)*0.15,(0.15)*0.1,(0.15)*0.05]

solute = ['Na','K','Cl','HCO3','H2CO3','CO2','HPO4','H2PO4','urea','NH3','NH4','H','HCO2','H2CO2','glu']
segment_early = ['pt','sdl','mtal','dct','cnt']
segment_late = ['ccd','imcd']

bar_width = 0.2
fig,axarr = plt.subplots(3,2)
fig.set_figheight(45)
fig.set_figwidth(40)
fig.subplots_adjust(hspace = 0.06)

volume_conversion = 1.44
solute_conversion = 1.44*10e-4

#=================================================================
# Na
#=================================================================

s = 'Na'
female_delivery_number = []
female_delivery_sup = []
female_delivery_jux1 = []
female_delivery_jux2 = []
female_delivery_jux3 = []
female_delivery_jux4 = []
female_delivery_jux5 = []
for seg in segment_early:
    file_sup = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    for i in file_jux1:
        line = i.split(' ')
        datalist_jux1.append(float(line[0]))
    for i in file_jux2:
        line = i.split(' ')
        datalist_jux2.append(float(line[0]))
    for i in file_jux3:
        line = i.split(' ')
        datalist_jux3.append(float(line[0]))
    for i in file_jux4:
        line = i.split(' ')
        datalist_jux4.append(float(line[0]))
    for i in file_jux5:
        line = i.split(' ')
        datalist_jux5.append(float(line[0]))
    number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    female_delivery_number.append(0)
    female_delivery_sup.append(neph_weight[0]*datalist_sup[0]*solute_conversion)
    female_delivery_jux1.append(neph_weight[1]*datalist_jux1[0]*solute_conversion)
    female_delivery_jux2.append(neph_weight[2]*datalist_jux2[0]*solute_conversion)
    female_delivery_jux3.append(neph_weight[3]*datalist_jux3[0]*solute_conversion)
    female_delivery_jux4.append(neph_weight[4]*datalist_jux4[0]*solute_conversion)
    female_delivery_jux5.append(neph_weight[5]*datalist_jux5[0]*solute_conversion)
    if seg == 'cnt':
        female_delivery_number.append(0)
        female_delivery_sup.append(neph_weight[0]*datalist_sup[-1]*solute_conversion)
        female_delivery_jux1.append(neph_weight[1]*datalist_jux1[-1]*solute_conversion)
        female_delivery_jux2.append(neph_weight[2]*datalist_jux2[-1]*solute_conversion)
        female_delivery_jux3.append(neph_weight[3]*datalist_jux3[-1]*solute_conversion)
        female_delivery_jux4.append(neph_weight[4]*datalist_jux4[-1]*solute_conversion)
        female_delivery_jux5.append(neph_weight[5]*datalist_jux5[-1]*solute_conversion)
for seg in segment_late:
    file_data = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        female_delivery_number.append(number_of_delivery*solute_conversion)
    else:
        number_of_delivery = datalist[0]  

male_delivery_number = []
male_delivery_sup = []
male_delivery_jux1 = []
male_delivery_jux2 = []
male_delivery_jux3 = []
male_delivery_jux4 = []
male_delivery_jux5 = []
for seg in segment_early:
    file_sup = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    for i in file_jux1:
        line = i.split(' ')
        datalist_jux1.append(float(line[0]))
    for i in file_jux2:
        line = i.split(' ')
        datalist_jux2.append(float(line[0]))
    for i in file_jux3:
        line = i.split(' ')
        datalist_jux3.append(float(line[0]))
    for i in file_jux4:
        line = i.split(' ')
        datalist_jux4.append(float(line[0]))
    for i in file_jux5:
        line = i.split(' ')
        datalist_jux5.append(float(line[0]))
    number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_delivery_number.append(0)
    male_delivery_sup.append(neph_weight[0]*datalist_sup[0]*solute_conversion)
    male_delivery_jux1.append(neph_weight[1]*datalist_jux1[0]*solute_conversion)
    male_delivery_jux2.append(neph_weight[2]*datalist_jux2[0]*solute_conversion)
    male_delivery_jux3.append(neph_weight[3]*datalist_jux3[0]*solute_conversion)
    male_delivery_jux4.append(neph_weight[4]*datalist_jux4[0]*solute_conversion)
    male_delivery_jux5.append(neph_weight[5]*datalist_jux5[0]*solute_conversion)
    if seg == 'cnt':
        male_delivery_number.append(0)
        male_delivery_sup.append(neph_weight[0]*datalist_sup[-1]*solute_conversion)
        male_delivery_jux1.append(neph_weight[1]*datalist_jux1[-1]*solute_conversion)
        male_delivery_jux2.append(neph_weight[2]*datalist_jux2[-1]*solute_conversion)
        male_delivery_jux3.append(neph_weight[3]*datalist_jux3[-1]*solute_conversion)
        male_delivery_jux4.append(neph_weight[4]*datalist_jux4[-1]*solute_conversion)
        male_delivery_jux5.append(neph_weight[5]*datalist_jux5[-1]*solute_conversion)
for seg in segment_late:
    file_data = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        male_delivery_number.append(number_of_delivery*solute_conversion)
    else:
        number_of_delivery = datalist[0]
    
    #===================================
    # NHE3 50% inhibited
    #===================================
female_delivery_number_nhe50 = []
female_delivery_sup_nhe50 = []
female_delivery_jux1_nhe50 = []
female_delivery_jux2_nhe50 = []
female_delivery_jux3_nhe50 = []
female_delivery_jux4_nhe50 = []
female_delivery_jux5_nhe50 = []
for seg in segment_early:
    file_sup = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    for i in file_jux1:
        line = i.split(' ')
        datalist_jux1.append(float(line[0]))
    for i in file_jux2:
        line = i.split(' ')
        datalist_jux2.append(float(line[0]))
    for i in file_jux3:
        line = i.split(' ')
        datalist_jux3.append(float(line[0]))
    for i in file_jux4:
        line = i.split(' ')
        datalist_jux4.append(float(line[0]))
    for i in file_jux5:
        line = i.split(' ')
        datalist_jux5.append(float(line[0]))
    number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    female_delivery_number_nhe50.append(0)
    female_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[0]*solute_conversion)
    female_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[0]*solute_conversion)
    female_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[0]*solute_conversion)
    female_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[0]*solute_conversion)
    female_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[0]*solute_conversion)
    female_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[0]*solute_conversion)
    if seg == 'cnt':
        female_delivery_number_nhe50.append(0)
        female_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[-1]*solute_conversion)
        female_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[-1]*solute_conversion)
        female_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[-1]*solute_conversion)
        female_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[-1]*solute_conversion)
        female_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[-1]*solute_conversion)
        female_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[-1]*solute_conversion)
for seg in segment_late:
    file_data = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        female_delivery_number_nhe50.append(number_of_delivery*solute_conversion)
    else:
        number_of_delivery = datalist[0]
    

male_delivery_number_nhe50 = []
male_delivery_sup_nhe50 = []
male_delivery_jux1_nhe50 = []
male_delivery_jux2_nhe50 = []
male_delivery_jux3_nhe50 = []
male_delivery_jux4_nhe50 = []
male_delivery_jux5_nhe50 = []
for seg in segment_early:
    file_sup = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    for i in file_jux1:
        line = i.split(' ')
        datalist_jux1.append(float(line[0]))
    for i in file_jux2:
        line = i.split(' ')
        datalist_jux2.append(float(line[0]))
    for i in file_jux3:
        line = i.split(' ')
        datalist_jux3.append(float(line[0]))
    for i in file_jux4:
        line = i.split(' ')
        datalist_jux4.append(float(line[0]))
    for i in file_jux5:
        line = i.split(' ')
        datalist_jux5.append(float(line[0]))
    number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_delivery_number_nhe50.append(0)
    male_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[0]*solute_conversion)
    male_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[0]*solute_conversion)
    male_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[0]*solute_conversion)
    male_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[0]*solute_conversion)
    male_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[0]*solute_conversion)
    male_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[0]*solute_conversion)
    if seg == 'cnt':
        male_delivery_number_nhe50.append(0)
        male_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[-1]*solute_conversion)
        male_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[-1]*solute_conversion)
        male_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[-1]*solute_conversion)
        male_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[-1]*solute_conversion)
        male_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[-1]*solute_conversion)
        male_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[-1]*solute_conversion)
for seg in segment_late:
    file_data = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        male_delivery_number_nhe50.append(number_of_delivery*solute_conversion)
    else:
        number_of_delivery = datalist[0]

segment = ['PT','DL','mTAL','DCT','CNT','CCD','urine']
#bar_width = 0.15

#print(segment[:6],male_delivery_sup)

male_sup=axarr[0,0].bar(np.arange(len(segment[:6])),male_delivery_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Men, Healthy')
male_jux=axarr[0,0].bar(np.arange(len(segment[:6])),[male_delivery_jux1[i]+male_delivery_jux2[i]+male_delivery_jux3[i]+male_delivery_jux4[i]+male_delivery_jux5[i] for i in range(len(male_delivery_sup))],bar_width,bottom=male_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later=axarr[0,0].bar(np.arange(len(segment)),male_delivery_number,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

male_sup_nhe50=axarr[0,0].bar(np.arange(len(segment[:6]))+bar_width,male_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue',label='Men, Diabetic')
male_jux_nhe50=axarr[0,0].bar(np.arange(len(segment[:6]))+bar_width,[male_delivery_jux1_nhe50[i]+male_delivery_jux2_nhe50[i]+male_delivery_jux3_nhe50[i]+male_delivery_jux4_nhe50[i]+male_delivery_jux5_nhe50[i] for i in range(len(male_delivery_sup_nhe50))],bar_width,bottom=male_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later_nhe50=axarr[0,0].bar(np.arange(len(segment))+bar_width,male_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

Female_sup=axarr[0,0].bar(np.arange(len(segment[:6]))+2*bar_width,female_delivery_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')
Female_jux=axarr[0,0].bar(np.arange(len(segment[:6]))+2*bar_width,[female_delivery_jux1[i]+female_delivery_jux2[i]+female_delivery_jux3[i]+female_delivery_jux4[i]+female_delivery_jux5[i] for i in range(len(female_delivery_sup))],bar_width,bottom=female_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
Female_later=axarr[0,0].bar(np.arange(len(segment))+2*bar_width,female_delivery_number,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

Female_sup_nhe50=axarr[0,0].bar(np.arange(len(segment[:6]))+3*bar_width,female_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')
Female_jux_nhe50=axarr[0,0].bar(np.arange(len(segment[:6]))+3*bar_width,[female_delivery_jux1_nhe50[i]+female_delivery_jux2_nhe50[i]+female_delivery_jux3_nhe50[i]+female_delivery_jux4_nhe50[i]+female_delivery_jux5_nhe50[i] for i in range(len(female_delivery_sup_nhe50))],bar_width,bottom=female_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
Female_later_nhe50=axarr[0,0].bar(np.arange(len(segment))+3*bar_width,female_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')
axarr[0,0].set_xticks(np.arange(len(segment))+1.5*bar_width)
axarr[0,0].set_xticklabels(segment,fontsize=30)
axarr[0,0].tick_params(axis='both',labelsize=30)
#ax.set_xlabel('Segment',fontsize=20)
axarr[0,0].set_ylabel('Na$^+$ delivery (mol/Day)',fontsize=30)
axarr[0,0].legend(fontsize=30,markerscale=30)

bar_width_ins = bar_width
axins = inset_axes(axarr[0,0],width=5,height=5,loc=7)

male_sup_inset=axins.bar(np.arange(len(segment[:6])),male_delivery_sup,bar_width_ins,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')
male_jux_inset=axins.bar(np.arange(len(segment[:6])),[male_delivery_jux1[i]+male_delivery_jux2[i]+male_delivery_jux3[i]+male_delivery_jux4[i]+male_delivery_jux5[i] for i in range(len(male_delivery_sup))],bar_width_ins,bottom=male_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later_inset=axins.bar(np.arange(len(segment)),male_delivery_number,bar_width_ins,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

male_sup_nhe50_inset=axins.bar(np.arange(len(segment[:6]))+bar_width_ins,male_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')
male_jux_nhe50_inset=axins.bar(np.arange(len(segment[:6]))+bar_width_ins,[male_delivery_jux1_nhe50[i]+male_delivery_jux2_nhe50[i]+male_delivery_jux3_nhe50[i]+male_delivery_jux4_nhe50[i]+male_delivery_jux5_nhe50[i] for i in range(len(male_delivery_sup_nhe50))],bar_width,bottom=male_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later_nhe50_inset=axins.bar(np.arange(len(segment))+bar_width_ins,male_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

Female_sup_inset=axins.bar(np.arange(len(segment[:6]))+2*bar_width_ins,female_delivery_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')
Female_jux_inset=axins.bar(np.arange(len(segment[:6]))+2*bar_width_ins,[female_delivery_jux1[i]+female_delivery_jux2[i]+female_delivery_jux3[i]+female_delivery_jux4[i]+female_delivery_jux5[i] for i in range(len(female_delivery_sup))],bar_width,bottom=female_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
Female_later_inset=axins.bar(np.arange(len(segment))+2*bar_width_ins,female_delivery_number,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

Female_sup_nhe50_inset=axins.bar(np.arange(len(segment[:6]))+3*bar_width,female_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')
Female_jux_nhe50_inset=axins.bar(np.arange(len(segment[:6]))+3*bar_width,[female_delivery_jux1_nhe50[i]+female_delivery_jux2_nhe50[i]+female_delivery_jux3_nhe50[i]+female_delivery_jux4_nhe50[i]+female_delivery_jux5_nhe50[i] for i in range(len(female_delivery_sup_nhe50))],bar_width,bottom=female_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
Female_later_nhe50_inset=axins.bar(np.arange(len(segment))+3*bar_width,female_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')

axins.set_xticks(np.arange(len(segment))+1.5*bar_width_ins)
axins.set_xticklabels(segment,fontsize=30)
axins.set_xlim(3-1.5*bar_width_ins,6+4*bar_width_ins)
axins.set_ylim(0,1.5)
axins.tick_params(axis='both',labelsize=30)

#=================================================================
# K
#=================================================================

s = 'K'
female_delivery_number = []
female_delivery_sup = []
female_delivery_jux1 = []
female_delivery_jux2 = []
female_delivery_jux3 = []
female_delivery_jux4 = []
female_delivery_jux5 = []
for seg in segment_early:
    file_sup = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    for i in file_jux1:
        line = i.split(' ')
        datalist_jux1.append(float(line[0]))
    for i in file_jux2:
        line = i.split(' ')
        datalist_jux2.append(float(line[0]))
    for i in file_jux3:
        line = i.split(' ')
        datalist_jux3.append(float(line[0]))
    for i in file_jux4:
        line = i.split(' ')
        datalist_jux4.append(float(line[0]))
    for i in file_jux5:
        line = i.split(' ')
        datalist_jux5.append(float(line[0]))
    number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    female_delivery_number.append(0)
    female_delivery_sup.append(neph_weight[0]*datalist_sup[0]*solute_conversion)
    female_delivery_jux1.append(neph_weight[1]*datalist_jux1[0]*solute_conversion)
    female_delivery_jux2.append(neph_weight[2]*datalist_jux2[0]*solute_conversion)
    female_delivery_jux3.append(neph_weight[3]*datalist_jux3[0]*solute_conversion)
    female_delivery_jux4.append(neph_weight[4]*datalist_jux4[0]*solute_conversion)
    female_delivery_jux5.append(neph_weight[5]*datalist_jux5[0]*solute_conversion)
    if seg == 'cnt':
        female_delivery_number.append(0)
        female_delivery_sup.append(neph_weight[0]*datalist_sup[-1]*solute_conversion)
        female_delivery_jux1.append(neph_weight[1]*datalist_jux1[-1]*solute_conversion)
        female_delivery_jux2.append(neph_weight[2]*datalist_jux2[-1]*solute_conversion)
        female_delivery_jux3.append(neph_weight[3]*datalist_jux3[-1]*solute_conversion)
        female_delivery_jux4.append(neph_weight[4]*datalist_jux4[-1]*solute_conversion)
        female_delivery_jux5.append(neph_weight[5]*datalist_jux5[-1]*solute_conversion)
for seg in segment_late:
    file_data = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        female_delivery_number.append(number_of_delivery*solute_conversion)
    else:
        number_of_delivery = datalist[0]
    

male_delivery_number = []
male_delivery_sup = []
male_delivery_jux1 = []
male_delivery_jux2 = []
male_delivery_jux3 = []
male_delivery_jux4 = []
male_delivery_jux5 = []
for seg in segment_early:
    file_sup = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    for i in file_jux1:
        line = i.split(' ')
        datalist_jux1.append(float(line[0]))
    for i in file_jux2:
        line = i.split(' ')
        datalist_jux2.append(float(line[0]))
    for i in file_jux3:
        line = i.split(' ')
        datalist_jux3.append(float(line[0]))
    for i in file_jux4:
        line = i.split(' ')
        datalist_jux4.append(float(line[0]))
    for i in file_jux5:
        line = i.split(' ')
        datalist_jux5.append(float(line[0]))
    number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_delivery_number.append(0)
    male_delivery_sup.append(neph_weight[0]*datalist_sup[0]*solute_conversion)
    male_delivery_jux1.append(neph_weight[1]*datalist_jux1[0]*solute_conversion)
    male_delivery_jux2.append(neph_weight[2]*datalist_jux2[0]*solute_conversion)
    male_delivery_jux3.append(neph_weight[3]*datalist_jux3[0]*solute_conversion)
    male_delivery_jux4.append(neph_weight[4]*datalist_jux4[0]*solute_conversion)
    male_delivery_jux5.append(neph_weight[5]*datalist_jux5[0]*solute_conversion)
    if seg == 'cnt':
        male_delivery_number.append(0)
        male_delivery_sup.append(neph_weight[0]*datalist_sup[-1]*solute_conversion)
        male_delivery_jux1.append(neph_weight[1]*datalist_jux1[-1]*solute_conversion)
        male_delivery_jux2.append(neph_weight[2]*datalist_jux2[-1]*solute_conversion)
        male_delivery_jux3.append(neph_weight[3]*datalist_jux3[-1]*solute_conversion)
        male_delivery_jux4.append(neph_weight[4]*datalist_jux4[-1]*solute_conversion)
        male_delivery_jux5.append(neph_weight[5]*datalist_jux5[-1]*solute_conversion)
for seg in segment_late:
    file_data = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        male_delivery_number.append(number_of_delivery*solute_conversion)
    else:
        number_of_delivery = datalist[0]

    #===================================
    # NHE3 50% inhibited
    #===================================
female_delivery_number_nhe50 = []
female_delivery_sup_nhe50 = []
female_delivery_jux1_nhe50 = []
female_delivery_jux2_nhe50 = []
female_delivery_jux3_nhe50 = []
female_delivery_jux4_nhe50 = []
female_delivery_jux5_nhe50 = []
for seg in segment_early:
    file_sup = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    for i in file_jux1:
        line = i.split(' ')
        datalist_jux1.append(float(line[0]))
    for i in file_jux2:
        line = i.split(' ')
        datalist_jux2.append(float(line[0]))
    for i in file_jux3:
        line = i.split(' ')
        datalist_jux3.append(float(line[0]))
    for i in file_jux4:
        line = i.split(' ')
        datalist_jux4.append(float(line[0]))
    for i in file_jux5:
        line = i.split(' ')
        datalist_jux5.append(float(line[0]))
    number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    female_delivery_number_nhe50.append(0)
    female_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[0]*solute_conversion)
    female_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[0]*solute_conversion)
    female_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[0]*solute_conversion)
    female_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[0]*solute_conversion)
    female_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[0]*solute_conversion)
    female_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[0]*solute_conversion)
    if seg == 'cnt':
        female_delivery_number_nhe50.append(0)
        female_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[-1]*solute_conversion)
        female_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[-1]*solute_conversion)
        female_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[-1]*solute_conversion)
        female_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[-1]*solute_conversion)
        female_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[-1]*solute_conversion)
        female_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[-1]*solute_conversion)
for seg in segment_late:
    file_data = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        female_delivery_number_nhe50.append(number_of_delivery*solute_conversion)
    else:
        number_of_delivery = datalist[0]
    

male_delivery_number_nhe50 = []
male_delivery_sup_nhe50 = []
male_delivery_jux1_nhe50 = []
male_delivery_jux2_nhe50 = []
male_delivery_jux3_nhe50 = []
male_delivery_jux4_nhe50 = []
male_delivery_jux5_nhe50 = []
for seg in segment_early:
    file_sup = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    for i in file_jux1:
        line = i.split(' ')
        datalist_jux1.append(float(line[0]))
    for i in file_jux2:
        line = i.split(' ')
        datalist_jux2.append(float(line[0]))
    for i in file_jux3:
        line = i.split(' ')
        datalist_jux3.append(float(line[0]))
    for i in file_jux4:
        line = i.split(' ')
        datalist_jux4.append(float(line[0]))
    for i in file_jux5:
        line = i.split(' ')
        datalist_jux5.append(float(line[0]))
    number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_delivery_number_nhe50.append(0)
    male_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[0]*solute_conversion)
    male_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[0]*solute_conversion)
    male_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[0]*solute_conversion)
    male_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[0]*solute_conversion)
    male_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[0]*solute_conversion)
    male_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[0]*solute_conversion)
    if seg == 'cnt':
        male_delivery_number_nhe50.append(0)
        male_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[-1]*solute_conversion)
        male_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[-1]*solute_conversion)
        male_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[-1]*solute_conversion)
        male_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[-1]*solute_conversion)
        male_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[-1]*solute_conversion)
        male_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[-1]*solute_conversion)
for seg in segment_late:
    file_data = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        male_delivery_number_nhe50.append(number_of_delivery*solute_conversion)
    else:
        number_of_delivery = datalist[0]

segment = ['PT','DL','mTAL','DCT','CNT','CCD','urine']
#bar_width = 0.15

#print(segment[:6],male_delivery_sup)

male_sup=axarr[0,1].bar(np.arange(len(segment[:6])),male_delivery_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')
male_jux=axarr[0,1].bar(np.arange(len(segment[:6])),[male_delivery_jux1[i]+male_delivery_jux2[i]+male_delivery_jux3[i]+male_delivery_jux4[i]+male_delivery_jux5[i] for i in range(len(male_delivery_sup))],bar_width,bottom=male_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later=axarr[0,1].bar(np.arange(len(segment)),male_delivery_number,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

male_sup_nhe50=axarr[0,1].bar(np.arange(len(segment[:6]))+bar_width,male_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')
male_jux_nhe50=axarr[0,1].bar(np.arange(len(segment[:6]))+bar_width,[male_delivery_jux1_nhe50[i]+male_delivery_jux2_nhe50[i]+male_delivery_jux3_nhe50[i]+male_delivery_jux4_nhe50[i]+male_delivery_jux5_nhe50[i] for i in range(len(male_delivery_sup_nhe50))],bar_width,bottom=male_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later_nhe50=axarr[0,1].bar(np.arange(len(segment))+bar_width,male_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

Female_sup=axarr[0,1].bar(np.arange(len(segment[:6]))+2*bar_width,female_delivery_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta',label='Women, Healthy')
Female_jux=axarr[0,1].bar(np.arange(len(segment[:6]))+2*bar_width,[female_delivery_jux1[i]+female_delivery_jux2[i]+female_delivery_jux3[i]+female_delivery_jux4[i]+female_delivery_jux5[i] for i in range(len(female_delivery_sup))],bar_width,bottom=female_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
Female_later=axarr[0,1].bar(np.arange(len(segment))+2*bar_width,female_delivery_number,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

Female_sup_nhe50=axarr[0,1].bar(np.arange(len(segment[:6]))+3*bar_width,female_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink',label='Women, Diabetic')
Female_jux_nhe50=axarr[0,1].bar(np.arange(len(segment[:6]))+3*bar_width,[female_delivery_jux1_nhe50[i]+female_delivery_jux2_nhe50[i]+female_delivery_jux3_nhe50[i]+female_delivery_jux4_nhe50[i]+female_delivery_jux5_nhe50[i] for i in range(len(female_delivery_sup_nhe50))],bar_width,bottom=female_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
Female_later_nhe50=axarr[0,1].bar(np.arange(len(segment))+3*bar_width,female_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')
axarr[0,1].set_xticks(np.arange(len(segment))+1.5*bar_width)
axarr[0,1].set_xticklabels(segment,fontsize=30)
axarr[0,1].tick_params(axis='both',labelsize=30)
#ax.set_xlabel('Segment',fontsize=20)
axarr[0,1].set_ylabel('K$^+$ delivery (mol/Day)',fontsize=30)
axarr[0,1].legend(fontsize=30,markerscale=30)
bar_width_ins = bar_width
#axins = inset_axes(ax,width=2,height=2,loc=7)
#Male_inset=axins.bar(np.arange(len(segment)),male_list,bar_width_ins,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='black',label='Male')
#Female_inset=axins.bar(np.arange(len(segment))+bar_width_ins,female_list,bar_width_ins,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white',label='Female')
#axins.set_xticks(np.arange(len(segment))+0.5*bar_width_ins)
#axins.set_xticklabels(segment,fontsize=20)
#axins.set_xlim(5-1.5*bar_width_ins,6+2*bar_width)
#axins.set_ylim(0,2)
#axins.tick_params(axis='both',labelsize=20)
#autolabel(Male,'left')
#autolabel(Female,'right')

#=================================================================
# Cl
#=================================================================

s = 'Cl'
female_delivery_number = []
female_delivery_sup = []
female_delivery_jux1 = []
female_delivery_jux2 = []
female_delivery_jux3 = []
female_delivery_jux4 = []
female_delivery_jux5 = []
for seg in segment_early:
    file_sup = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    for i in file_jux1:
        line = i.split(' ')
        datalist_jux1.append(float(line[0]))
    for i in file_jux2:
        line = i.split(' ')
        datalist_jux2.append(float(line[0]))
    for i in file_jux3:
        line = i.split(' ')
        datalist_jux3.append(float(line[0]))
    for i in file_jux4:
        line = i.split(' ')
        datalist_jux4.append(float(line[0]))
    for i in file_jux5:
        line = i.split(' ')
        datalist_jux5.append(float(line[0]))
    number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    female_delivery_number.append(0)
    female_delivery_sup.append(neph_weight[0]*datalist_sup[0]*solute_conversion)
    female_delivery_jux1.append(neph_weight[1]*datalist_jux1[0]*solute_conversion)
    female_delivery_jux2.append(neph_weight[2]*datalist_jux2[0]*solute_conversion)
    female_delivery_jux3.append(neph_weight[3]*datalist_jux3[0]*solute_conversion)
    female_delivery_jux4.append(neph_weight[4]*datalist_jux4[0]*solute_conversion)
    female_delivery_jux5.append(neph_weight[5]*datalist_jux5[0]*solute_conversion)
    if seg == 'cnt':
        female_delivery_number.append(0)
        female_delivery_sup.append(neph_weight[0]*datalist_sup[-1]*solute_conversion)
        female_delivery_jux1.append(neph_weight[1]*datalist_jux1[-1]*solute_conversion)
        female_delivery_jux2.append(neph_weight[2]*datalist_jux2[-1]*solute_conversion)
        female_delivery_jux3.append(neph_weight[3]*datalist_jux3[-1]*solute_conversion)
        female_delivery_jux4.append(neph_weight[4]*datalist_jux4[-1]*solute_conversion)
        female_delivery_jux5.append(neph_weight[5]*datalist_jux5[-1]*solute_conversion)
for seg in segment_late:
    file_data = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        female_delivery_number.append(number_of_delivery*solute_conversion)
    else:
        number_of_delivery = datalist[0]
    

male_delivery_number = []
male_delivery_sup = []
male_delivery_jux1 = []
male_delivery_jux2 = []
male_delivery_jux3 = []
male_delivery_jux4 = []
male_delivery_jux5 = []
for seg in segment_early:
    file_sup = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    for i in file_jux1:
        line = i.split(' ')
        datalist_jux1.append(float(line[0]))
    for i in file_jux2:
        line = i.split(' ')
        datalist_jux2.append(float(line[0]))
    for i in file_jux3:
        line = i.split(' ')
        datalist_jux3.append(float(line[0]))
    for i in file_jux4:
        line = i.split(' ')
        datalist_jux4.append(float(line[0]))
    for i in file_jux5:
        line = i.split(' ')
        datalist_jux5.append(float(line[0]))
    number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_delivery_number.append(0)
    male_delivery_sup.append(neph_weight[0]*datalist_sup[0]*solute_conversion)
    male_delivery_jux1.append(neph_weight[1]*datalist_jux1[0]*solute_conversion)
    male_delivery_jux2.append(neph_weight[2]*datalist_jux2[0]*solute_conversion)
    male_delivery_jux3.append(neph_weight[3]*datalist_jux3[0]*solute_conversion)
    male_delivery_jux4.append(neph_weight[4]*datalist_jux4[0]*solute_conversion)
    male_delivery_jux5.append(neph_weight[5]*datalist_jux5[0]*solute_conversion)
    if seg == 'cnt':
        male_delivery_number.append(0)
        male_delivery_sup.append(neph_weight[0]*datalist_sup[-1]*solute_conversion)
        male_delivery_jux1.append(neph_weight[1]*datalist_jux1[-1]*solute_conversion)
        male_delivery_jux2.append(neph_weight[2]*datalist_jux2[-1]*solute_conversion)
        male_delivery_jux3.append(neph_weight[3]*datalist_jux3[-1]*solute_conversion)
        male_delivery_jux4.append(neph_weight[4]*datalist_jux4[-1]*solute_conversion)
        male_delivery_jux5.append(neph_weight[5]*datalist_jux5[-1]*solute_conversion)
for seg in segment_late:
    file_data = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        male_delivery_number.append(number_of_delivery*solute_conversion)
    else:
        number_of_delivery = datalist[0]

    #===================================
    # NHE3 50% inhibited
    #===================================
female_delivery_number_nhe50 = []
female_delivery_sup_nhe50 = []
female_delivery_jux1_nhe50 = []
female_delivery_jux2_nhe50 = []
female_delivery_jux3_nhe50 = []
female_delivery_jux4_nhe50 = []
female_delivery_jux5_nhe50 = []
for seg in segment_early:
    file_sup = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    for i in file_jux1:
        line = i.split(' ')
        datalist_jux1.append(float(line[0]))
    for i in file_jux2:
        line = i.split(' ')
        datalist_jux2.append(float(line[0]))
    for i in file_jux3:
        line = i.split(' ')
        datalist_jux3.append(float(line[0]))
    for i in file_jux4:
        line = i.split(' ')
        datalist_jux4.append(float(line[0]))
    for i in file_jux5:
        line = i.split(' ')
        datalist_jux5.append(float(line[0]))
    number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    female_delivery_number_nhe50.append(0)
    female_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[0]*solute_conversion)
    female_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[0]*solute_conversion)
    female_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[0]*solute_conversion)
    female_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[0]*solute_conversion)
    female_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[0]*solute_conversion)
    female_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[0]*solute_conversion)
    if seg == 'cnt':
        female_delivery_number_nhe50.append(0)
        female_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[-1]*solute_conversion)
        female_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[-1]*solute_conversion)
        female_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[-1]*solute_conversion)
        female_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[-1]*solute_conversion)
        female_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[-1]*solute_conversion)
        female_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[-1]*solute_conversion)
for seg in segment_late:
    file_data = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        female_delivery_number_nhe50.append(number_of_delivery*solute_conversion)
    else:
        number_of_delivery = datalist[0]
    

male_delivery_number_nhe50 = []
male_delivery_sup_nhe50 = []
male_delivery_jux1_nhe50 = []
male_delivery_jux2_nhe50 = []
male_delivery_jux3_nhe50 = []
male_delivery_jux4_nhe50 = []
male_delivery_jux5_nhe50 = []
for seg in segment_early:
    file_sup = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    for i in file_jux1:
        line = i.split(' ')
        datalist_jux1.append(float(line[0]))
    for i in file_jux2:
        line = i.split(' ')
        datalist_jux2.append(float(line[0]))
    for i in file_jux3:
        line = i.split(' ')
        datalist_jux3.append(float(line[0]))
    for i in file_jux4:
        line = i.split(' ')
        datalist_jux4.append(float(line[0]))
    for i in file_jux5:
        line = i.split(' ')
        datalist_jux5.append(float(line[0]))
    number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_delivery_number_nhe50.append(0)
    male_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[0]*solute_conversion)
    male_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[0]*solute_conversion)
    male_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[0]*solute_conversion)
    male_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[0]*solute_conversion)
    male_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[0]*solute_conversion)
    male_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[0]*solute_conversion)
    if seg == 'cnt':
        male_delivery_number_nhe50.append(0)
        male_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[-1]*solute_conversion)
        male_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[-1]*solute_conversion)
        male_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[-1]*solute_conversion)
        male_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[-1]*solute_conversion)
        male_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[-1]*solute_conversion)
        male_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[-1]*solute_conversion)
for seg in segment_late:
    file_data = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        male_delivery_number_nhe50.append(number_of_delivery*solute_conversion)
    else:
        number_of_delivery = datalist[0]

segment = ['PT','DL','mTAL','DCT','CNT','CCD','urine']
#bar_width = 0.15

#print(segment[:6],male_delivery_sup)

male_sup=axarr[1,0].bar(np.arange(len(segment[:6])),male_delivery_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')
male_jux=axarr[1,0].bar(np.arange(len(segment[:6])),[male_delivery_jux1[i]+male_delivery_jux2[i]+male_delivery_jux3[i]+male_delivery_jux4[i]+male_delivery_jux5[i] for i in range(len(male_delivery_sup))],bar_width,bottom=male_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later=axarr[1,0].bar(np.arange(len(segment)),male_delivery_number,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

male_sup_nhe50=axarr[1,0].bar(np.arange(len(segment[:6]))+bar_width,male_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')
male_jux_nhe50=axarr[1,0].bar(np.arange(len(segment[:6]))+bar_width,[male_delivery_jux1_nhe50[i]+male_delivery_jux2_nhe50[i]+male_delivery_jux3_nhe50[i]+male_delivery_jux4_nhe50[i]+male_delivery_jux5_nhe50[i] for i in range(len(male_delivery_sup_nhe50))],bar_width,bottom=male_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later_nhe50=axarr[1,0].bar(np.arange(len(segment))+bar_width,male_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

Female_sup=axarr[1,0].bar(np.arange(len(segment[:6]))+2*bar_width,female_delivery_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')
Female_jux=axarr[1,0].bar(np.arange(len(segment[:6]))+2*bar_width,[female_delivery_jux1[i]+female_delivery_jux2[i]+female_delivery_jux3[i]+female_delivery_jux4[i]+female_delivery_jux5[i] for i in range(len(female_delivery_sup))],bar_width,bottom=female_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
Female_later=axarr[1,0].bar(np.arange(len(segment))+2*bar_width,female_delivery_number,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

Female_sup_nhe50=axarr[1,0].bar(np.arange(len(segment[:6]))+3*bar_width,female_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')
Female_jux_nhe50=axarr[1,0].bar(np.arange(len(segment[:6]))+3*bar_width,[female_delivery_jux1_nhe50[i]+female_delivery_jux2_nhe50[i]+female_delivery_jux3_nhe50[i]+female_delivery_jux4_nhe50[i]+female_delivery_jux5_nhe50[i] for i in range(len(female_delivery_sup_nhe50))],bar_width,bottom=female_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
Female_later_nhe50=axarr[1,0].bar(np.arange(len(segment))+3*bar_width,female_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')
axarr[1,0].set_xticks(np.arange(len(segment))+1.5*bar_width)
axarr[1,0].set_xticklabels(segment,fontsize=30)
axarr[1,0].tick_params(axis='both',labelsize=30)
#ax.set_xlabel('Segment',fontsize=20)
axarr[1,0].set_ylabel('Cl$^-$ delivery (mol/Day)',fontsize=30)
#axarr[1,0].legend(fontsize=30,markerscale=30)

bar_width_ins = bar_width
axins = inset_axes(axarr[1,0],width=2.5,height=2.5,loc=7)

male_sup_inset=axins.bar(np.arange(len(segment[:6])),male_delivery_sup,bar_width_ins,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')
male_jux_inset=axins.bar(np.arange(len(segment[:6])),[male_delivery_jux1[i]+male_delivery_jux2[i]+male_delivery_jux3[i]+male_delivery_jux4[i]+male_delivery_jux5[i] for i in range(len(male_delivery_sup))],bar_width_ins,bottom=male_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later_inset=axins.bar(np.arange(len(segment)),male_delivery_number,bar_width_ins,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

male_sup_nhe50_inset=axins.bar(np.arange(len(segment[:6]))+bar_width_ins,male_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')
male_jux_nhe50_inset=axins.bar(np.arange(len(segment[:6]))+bar_width_ins,[male_delivery_jux1_nhe50[i]+male_delivery_jux2_nhe50[i]+male_delivery_jux3_nhe50[i]+male_delivery_jux4_nhe50[i]+male_delivery_jux5_nhe50[i] for i in range(len(male_delivery_sup_nhe50))],bar_width,bottom=male_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later_nhe50_inset=axins.bar(np.arange(len(segment))+bar_width_ins,male_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

Female_sup_inset=axins.bar(np.arange(len(segment[:6]))+2*bar_width_ins,female_delivery_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')
Female_jux_inset=axins.bar(np.arange(len(segment[:6]))+2*bar_width_ins,[female_delivery_jux1[i]+female_delivery_jux2[i]+female_delivery_jux3[i]+female_delivery_jux4[i]+female_delivery_jux5[i] for i in range(len(female_delivery_sup))],bar_width,bottom=female_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
Female_later_inset=axins.bar(np.arange(len(segment))+2*bar_width_ins,female_delivery_number,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

Female_sup_nhe50_inset=axins.bar(np.arange(len(segment[:6]))+3*bar_width,female_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')
Female_jux_nhe50_inset=axins.bar(np.arange(len(segment[:6]))+3*bar_width,[female_delivery_jux1_nhe50[i]+female_delivery_jux2_nhe50[i]+female_delivery_jux3_nhe50[i]+female_delivery_jux4_nhe50[i]+female_delivery_jux5_nhe50[i] for i in range(len(female_delivery_sup_nhe50))],bar_width,bottom=female_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
Female_later_nhe50_inset=axins.bar(np.arange(len(segment))+3*bar_width,female_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')

axins.set_xticks(np.arange(len(segment))+1.5*bar_width_ins)
axins.set_xticklabels(segment,fontsize=30)
axins.set_xlim(5-1.5*bar_width_ins,6+4*bar_width_ins)
axins.set_ylim(0,0.5)
axins.tick_params(axis='both',labelsize=30)

#=================================================================
# Glucose
#=================================================================

#s = 'HCO3'
s = 'glu'
female_delivery_number = []
female_delivery_sup = []
female_delivery_jux1 = []
female_delivery_jux2 = []
female_delivery_jux3 = []
female_delivery_jux4 = []
female_delivery_jux5 = []
for seg in segment_early:
    file_sup = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    for i in file_jux1:
        line = i.split(' ')
        datalist_jux1.append(float(line[0]))
    for i in file_jux2:
        line = i.split(' ')
        datalist_jux2.append(float(line[0]))
    for i in file_jux3:
        line = i.split(' ')
        datalist_jux3.append(float(line[0]))
    for i in file_jux4:
        line = i.split(' ')
        datalist_jux4.append(float(line[0]))
    for i in file_jux5:
        line = i.split(' ')
        datalist_jux5.append(float(line[0]))
    number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    female_delivery_number.append(0)
    female_delivery_sup.append(neph_weight[0]*datalist_sup[0]*solute_conversion)
    female_delivery_jux1.append(neph_weight[1]*datalist_jux1[0]*solute_conversion)
    female_delivery_jux2.append(neph_weight[2]*datalist_jux2[0]*solute_conversion)
    female_delivery_jux3.append(neph_weight[3]*datalist_jux3[0]*solute_conversion)
    female_delivery_jux4.append(neph_weight[4]*datalist_jux4[0]*solute_conversion)
    female_delivery_jux5.append(neph_weight[5]*datalist_jux5[0]*solute_conversion)
    if seg == 'cnt':
        female_delivery_number.append(0)
        female_delivery_sup.append(neph_weight[0]*datalist_sup[-1]*solute_conversion)#+0.1
        female_delivery_jux1.append(neph_weight[1]*datalist_jux1[-1]*solute_conversion)
        female_delivery_jux2.append(neph_weight[2]*datalist_jux2[-1]*solute_conversion)
        female_delivery_jux3.append(neph_weight[3]*datalist_jux3[-1]*solute_conversion)
        female_delivery_jux4.append(neph_weight[4]*datalist_jux4[-1]*solute_conversion)
        female_delivery_jux5.append(neph_weight[5]*datalist_jux5[-1]*solute_conversion)
for seg in segment_late:
    file_data = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        female_delivery_number.append(number_of_delivery*solute_conversion)
    else:
        number_of_delivery = datalist[0]
    

male_delivery_number = []
male_delivery_sup = []
male_delivery_jux1 = []
male_delivery_jux2 = []
male_delivery_jux3 = []
male_delivery_jux4 = []
male_delivery_jux5 = []
for seg in segment_early:
    file_sup = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    for i in file_jux1:
        line = i.split(' ')
        datalist_jux1.append(float(line[0]))
    for i in file_jux2:
        line = i.split(' ')
        datalist_jux2.append(float(line[0]))
    for i in file_jux3:
        line = i.split(' ')
        datalist_jux3.append(float(line[0]))
    for i in file_jux4:
        line = i.split(' ')
        datalist_jux4.append(float(line[0]))
    for i in file_jux5:
        line = i.split(' ')
        datalist_jux5.append(float(line[0]))
    number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_delivery_number.append(0)
    male_delivery_sup.append(neph_weight[0]*datalist_sup[0]*solute_conversion)
    male_delivery_jux1.append(neph_weight[1]*datalist_jux1[0]*solute_conversion)
    male_delivery_jux2.append(neph_weight[2]*datalist_jux2[0]*solute_conversion)
    male_delivery_jux3.append(neph_weight[3]*datalist_jux3[0]*solute_conversion)
    male_delivery_jux4.append(neph_weight[4]*datalist_jux4[0]*solute_conversion)
    male_delivery_jux5.append(neph_weight[5]*datalist_jux5[0]*solute_conversion)
    if seg == 'cnt':
        male_delivery_number.append(0)
        male_delivery_sup.append(neph_weight[0]*datalist_sup[-1]*solute_conversion)
        male_delivery_jux1.append(neph_weight[1]*datalist_jux1[-1]*solute_conversion)
        male_delivery_jux2.append(neph_weight[2]*datalist_jux2[-1]*solute_conversion)
        male_delivery_jux3.append(neph_weight[3]*datalist_jux3[-1]*solute_conversion)
        male_delivery_jux4.append(neph_weight[4]*datalist_jux4[-1]*solute_conversion)
        male_delivery_jux5.append(neph_weight[5]*datalist_jux5[-1]*solute_conversion)
for seg in segment_late:
    file_data = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        male_delivery_number.append(number_of_delivery*solute_conversion)
    else:
        number_of_delivery = datalist[0]

    #===================================
    # NHE3 50% inhibited
    #===================================
female_delivery_number_nhe50 = []
female_delivery_sup_nhe50 = []
female_delivery_jux1_nhe50 = []
female_delivery_jux2_nhe50 = []
female_delivery_jux3_nhe50 = []
female_delivery_jux4_nhe50 = []
female_delivery_jux5_nhe50 = []
for seg in segment_early:
    file_sup = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    for i in file_jux1:
        line = i.split(' ')
        datalist_jux1.append(float(line[0]))
    for i in file_jux2:
        line = i.split(' ')
        datalist_jux2.append(float(line[0]))
    for i in file_jux3:
        line = i.split(' ')
        datalist_jux3.append(float(line[0]))
    for i in file_jux4:
        line = i.split(' ')
        datalist_jux4.append(float(line[0]))
    for i in file_jux5:
        line = i.split(' ')
        datalist_jux5.append(float(line[0]))
    number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    female_delivery_number_nhe50.append(0)
    female_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[0]*solute_conversion)
    female_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[0]*solute_conversion)
    female_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[0]*solute_conversion)
    female_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[0]*solute_conversion)
    female_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[0]*solute_conversion)
    female_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[0]*solute_conversion)
    if seg == 'cnt':
        female_delivery_number_nhe50.append(0)
        female_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[-1]*solute_conversion)
        female_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[-1]*solute_conversion)
        female_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[-1]*solute_conversion)
        female_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[-1]*solute_conversion)
        female_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[-1]*solute_conversion)
        female_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[-1]*solute_conversion)
for seg in segment_late:
    file_data = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        female_delivery_number_nhe50.append(number_of_delivery*solute_conversion)
    else:
        number_of_delivery = datalist[0]
    

male_delivery_number_nhe50 = []
male_delivery_sup_nhe50 = []
male_delivery_jux1_nhe50 = []
male_delivery_jux2_nhe50 = []
male_delivery_jux3_nhe50 = []
male_delivery_jux4_nhe50 = []
male_delivery_jux5_nhe50 = []
for seg in segment_early:
    file_sup = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    for i in file_jux1:
        line = i.split(' ')
        datalist_jux1.append(float(line[0]))
    for i in file_jux2:
        line = i.split(' ')
        datalist_jux2.append(float(line[0]))
    for i in file_jux3:
        line = i.split(' ')
        datalist_jux3.append(float(line[0]))
    for i in file_jux4:
        line = i.split(' ')
        datalist_jux4.append(float(line[0]))
    for i in file_jux5:
        line = i.split(' ')
        datalist_jux5.append(float(line[0]))
    number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_delivery_number_nhe50.append(0)
    male_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[0]*solute_conversion)
    male_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[0]*solute_conversion)
    male_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[0]*solute_conversion)
    male_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[0]*solute_conversion)
    male_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[0]*solute_conversion)
    male_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[0]*solute_conversion)
    if seg == 'cnt':
        male_delivery_number_nhe50.append(0)
        male_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[-1]*solute_conversion)
        male_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[-1]*solute_conversion)
        male_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[-1]*solute_conversion)
        male_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[-1]*solute_conversion)
        male_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[-1]*solute_conversion)
        male_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[-1]*solute_conversion)
for seg in segment_late:
    file_data = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        male_delivery_number_nhe50.append(number_of_delivery*solute_conversion)
    else:
        number_of_delivery = datalist[0]

segment = ['PT','DL','mTAL','DCT','CNT','CCD','urine']

#print(segment[:6],male_delivery_sup)

male_sup=axarr[1,1].bar(np.arange(len(segment[:6])),male_delivery_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')
male_jux=axarr[1,1].bar(np.arange(len(segment[:6])),[male_delivery_jux1[i]+male_delivery_jux2[i]+male_delivery_jux3[i]+male_delivery_jux4[i]+male_delivery_jux5[i] for i in range(len(male_delivery_sup))],bar_width,bottom=male_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later=axarr[1,1].bar(np.arange(len(segment)),male_delivery_number,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

male_sup_nhe50=axarr[1,1].bar(np.arange(len(segment[:6]))+bar_width,male_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')
male_jux_nhe50=axarr[1,1].bar(np.arange(len(segment[:6]))+bar_width,[male_delivery_jux1_nhe50[i]+male_delivery_jux2_nhe50[i]+male_delivery_jux3_nhe50[i]+male_delivery_jux4_nhe50[i]+male_delivery_jux5_nhe50[i] for i in range(len(male_delivery_sup_nhe50))],bar_width,bottom=male_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later_nhe50=axarr[1,1].bar(np.arange(len(segment))+bar_width,male_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

print(male_delivery_sup_nhe50[0])
print(male_delivery_jux1_nhe50[0]+male_delivery_jux2_nhe50[0]+male_delivery_jux3_nhe50[0]+male_delivery_jux4_nhe50[0]+male_delivery_jux5_nhe50[0])

Female_sup=axarr[1,1].bar(np.arange(len(segment[:6]))+2*bar_width,female_delivery_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')
Female_jux=axarr[1,1].bar(np.arange(len(segment[:6]))+2*bar_width,[female_delivery_jux1[i]+female_delivery_jux2[i]+female_delivery_jux3[i]+female_delivery_jux4[i]+female_delivery_jux5[i] for i in range(len(female_delivery_sup))],bar_width,bottom=female_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
Female_later=axarr[1,1].bar(np.arange(len(segment))+2*bar_width,female_delivery_number,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

Female_sup_nhe50=axarr[1,1].bar(np.arange(len(segment[:6]))+3*bar_width,female_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')
Female_jux_nhe50=axarr[1,1].bar(np.arange(len(segment[:6]))+3*bar_width,[female_delivery_jux1_nhe50[i]+female_delivery_jux2_nhe50[i]+female_delivery_jux3_nhe50[i]+female_delivery_jux4_nhe50[i]+female_delivery_jux5_nhe50[i] for i in range(len(female_delivery_sup_nhe50))],bar_width,bottom=female_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
Female_later_nhe50=axarr[1,1].bar(np.arange(len(segment))+3*bar_width,female_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')
axarr[1,1].set_xticks(np.arange(len(segment))+1.5*bar_width)
axarr[1,1].set_xticklabels(segment,fontsize=30)
axarr[1,1].tick_params(axis='both',labelsize=30)
#ax.set_xlabel('Segment',fontsize=20)
axarr[1,1].set_ylabel('Glucose delivery (mol/Day)',fontsize=30) #Glucose
#axarr[1,1].legend(fontsize=30,markerscale=30)
#axarr[1,1].set_ylim(0,1.1)
# bar_width_ins = bar_width

# bar_width_ins = bar_width
# axins = inset_axes(axarr[1,1],width=5,height=5,loc=7)

# male_sup_inset=axins.bar(np.arange(len(segment[:6])),male_delivery_sup,bar_width_ins,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')
# male_jux_inset=axins.bar(np.arange(len(segment[:6])),[male_delivery_jux1[i]+male_delivery_jux2[i]+male_delivery_jux3[i]+male_delivery_jux4[i]+male_delivery_jux5[i] for i in range(len(male_delivery_sup))],bar_width_ins,bottom=male_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# male_later_inset=axins.bar(np.arange(len(segment)),male_delivery_number,bar_width_ins,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

# male_sup_nhe50_inset=axins.bar(np.arange(len(segment[:6]))+bar_width_ins,male_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')
# male_jux_nhe50_inset=axins.bar(np.arange(len(segment[:6]))+bar_width_ins,[male_delivery_jux1_nhe50[i]+male_delivery_jux2_nhe50[i]+male_delivery_jux3_nhe50[i]+male_delivery_jux4_nhe50[i]+male_delivery_jux5_nhe50[i] for i in range(len(male_delivery_sup_nhe50))],bar_width,bottom=male_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# male_later_nhe50_inset=axins.bar(np.arange(len(segment))+bar_width_ins,male_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

# Female_sup_inset=axins.bar(np.arange(len(segment[:6]))+2*bar_width_ins,female_delivery_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')
# Female_jux_inset=axins.bar(np.arange(len(segment[:6]))+2*bar_width_ins,[female_delivery_jux1[i]+female_delivery_jux2[i]+female_delivery_jux3[i]+female_delivery_jux4[i]+female_delivery_jux5[i] for i in range(len(female_delivery_sup))],bar_width,bottom=female_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# Female_later_inset=axins.bar(np.arange(len(segment))+2*bar_width_ins,female_delivery_number,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

# Female_sup_nhe50_inset=axins.bar(np.arange(len(segment[:6]))+3*bar_width,female_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')
# Female_jux_nhe50_inset=axins.bar(np.arange(len(segment[:6]))+3*bar_width,[female_delivery_jux1_nhe50[i]+female_delivery_jux2_nhe50[i]+female_delivery_jux3_nhe50[i]+female_delivery_jux4_nhe50[i]+female_delivery_jux5_nhe50[i] for i in range(len(female_delivery_sup_nhe50))],bar_width,bottom=female_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# Female_later_nhe50_inset=axins.bar(np.arange(len(segment))+3*bar_width,female_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')

# axins.set_xticks(np.arange(len(segment))+1.5*bar_width_ins)
# axins.set_xticklabels(segment,fontsize=30)
# axins.set_xlim(3-1.5*bar_width_ins,6+4*bar_width_ins)
# axins.set_ylim(-0.1,0.1)
# axins.tick_params(axis='both',labelsize=30)


# #=================================================================
# # NH4
# #=================================================================

# s = 'NH4'
# female_delivery_number = []
# female_delivery_sup = []
# female_delivery_jux1 = []
# female_delivery_jux2 = []
# female_delivery_jux3 = []
# female_delivery_jux4 = []
# female_delivery_jux5 = []
# for seg in segment_early:
#     file_sup = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
#     file_jux1 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
#     file_jux2 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
#     file_jux3 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
#     file_jux4 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
#     file_jux5 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
#     datalist_sup = []
#     datalist_jux1 = []
#     datalist_jux2 = []
#     datalist_jux3 = []
#     datalist_jux4 = []
#     datalist_jux5 = []
#     for i in file_sup:
#         line = i.split(' ')
#         datalist_sup.append(float(line[0]))
#     for i in file_jux1:
#         line = i.split(' ')
#         datalist_jux1.append(float(line[0]))
#     for i in file_jux2:
#         line = i.split(' ')
#         datalist_jux2.append(float(line[0]))
#     for i in file_jux3:
#         line = i.split(' ')
#         datalist_jux3.append(float(line[0]))
#     for i in file_jux4:
#         line = i.split(' ')
#         datalist_jux4.append(float(line[0]))
#     for i in file_jux5:
#         line = i.split(' ')
#         datalist_jux5.append(float(line[0]))
#     number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
#     female_delivery_number.append(0)
#     female_delivery_sup.append(neph_weight[0]*datalist_sup[0]*solute_conversion)
#     female_delivery_jux1.append(neph_weight[1]*datalist_jux1[0]*solute_conversion)
#     female_delivery_jux2.append(neph_weight[2]*datalist_jux2[0]*solute_conversion)
#     female_delivery_jux3.append(neph_weight[3]*datalist_jux3[0]*solute_conversion)
#     female_delivery_jux4.append(neph_weight[4]*datalist_jux4[0]*solute_conversion)
#     female_delivery_jux5.append(neph_weight[5]*datalist_jux5[0]*solute_conversion)
#     if seg == 'cnt':
#         female_delivery_number.append(0)
#         female_delivery_sup.append(neph_weight[0]*datalist_sup[-1]*solute_conversion)
#         female_delivery_jux1.append(neph_weight[1]*datalist_jux1[-1]*solute_conversion)
#         female_delivery_jux2.append(neph_weight[2]*datalist_jux2[-1]*solute_conversion)
#         female_delivery_jux3.append(neph_weight[3]*datalist_jux3[-1]*solute_conversion)
#         female_delivery_jux4.append(neph_weight[4]*datalist_jux4[-1]*solute_conversion)
#         female_delivery_jux5.append(neph_weight[5]*datalist_jux5[-1]*solute_conversion)
# for seg in segment_late:
#     file_data = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
#     datalist = []
#     for i in file_data:
#         line = i.split(' ')
#         datalist.append(float(line[0]))
#     if seg == 'imcd':
#         number_of_delivery = datalist[-1]
#         female_delivery_number.append(number_of_delivery*solute_conversion)
#     else:
#         number_of_delivery = datalist[0]
    

# male_delivery_number = []
# male_delivery_sup = []
# male_delivery_jux1 = []
# male_delivery_jux2 = []
# male_delivery_jux3 = []
# male_delivery_jux4 = []
# male_delivery_jux5 = []
# for seg in segment_early:
#     file_sup = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
#     file_jux1 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
#     file_jux2 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
#     file_jux3 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
#     file_jux4 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
#     file_jux5 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
#     datalist_sup = []
#     datalist_jux1 = []
#     datalist_jux2 = []
#     datalist_jux3 = []
#     datalist_jux4 = []
#     datalist_jux5 = []
#     for i in file_sup:
#         line = i.split(' ')
#         datalist_sup.append(float(line[0]))
#     for i in file_jux1:
#         line = i.split(' ')
#         datalist_jux1.append(float(line[0]))
#     for i in file_jux2:
#         line = i.split(' ')
#         datalist_jux2.append(float(line[0]))
#     for i in file_jux3:
#         line = i.split(' ')
#         datalist_jux3.append(float(line[0]))
#     for i in file_jux4:
#         line = i.split(' ')
#         datalist_jux4.append(float(line[0]))
#     for i in file_jux5:
#         line = i.split(' ')
#         datalist_jux5.append(float(line[0]))
#     number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
#     male_delivery_number.append(0)
#     male_delivery_sup.append(neph_weight[0]*datalist_sup[0]*solute_conversion)
#     male_delivery_jux1.append(neph_weight[1]*datalist_jux1[0]*solute_conversion)
#     male_delivery_jux2.append(neph_weight[2]*datalist_jux2[0]*solute_conversion)
#     male_delivery_jux3.append(neph_weight[3]*datalist_jux3[0]*solute_conversion)
#     male_delivery_jux4.append(neph_weight[4]*datalist_jux4[0]*solute_conversion)
#     male_delivery_jux5.append(neph_weight[5]*datalist_jux5[0]*solute_conversion)
#     if seg == 'cnt':
#         male_delivery_number.append(0)
#         male_delivery_sup.append(neph_weight[0]*datalist_sup[-1]*solute_conversion)
#         male_delivery_jux1.append(neph_weight[1]*datalist_jux1[-1]*solute_conversion)
#         male_delivery_jux2.append(neph_weight[2]*datalist_jux2[-1]*solute_conversion)
#         male_delivery_jux3.append(neph_weight[3]*datalist_jux3[-1]*solute_conversion)
#         male_delivery_jux4.append(neph_weight[4]*datalist_jux4[-1]*solute_conversion)
#         male_delivery_jux5.append(neph_weight[5]*datalist_jux5[-1]*solute_conversion)
# for seg in segment_late:
#     file_data = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
#     datalist = []
#     for i in file_data:
#         line = i.split(' ')
#         datalist.append(float(line[0]))
#     if seg == 'imcd':
#         number_of_delivery = datalist[-1]
#         male_delivery_number.append(number_of_delivery*solute_conversion)
#     else:
#         number_of_delivery = datalist[0]

#     #===================================
#     # NHE3 50% inhibited
#     #===================================
# female_delivery_number_nhe50 = []
# female_delivery_sup_nhe50 = []
# female_delivery_jux1_nhe50 = []
# female_delivery_jux2_nhe50 = []
# female_delivery_jux3_nhe50 = []
# female_delivery_jux4_nhe50 = []
# female_delivery_jux5_nhe50 = []
# for seg in segment_early:
#     file_sup = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
#     file_jux1 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
#     file_jux2 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
#     file_jux3 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
#     file_jux4 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
#     file_jux5 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
#     datalist_sup = []
#     datalist_jux1 = []
#     datalist_jux2 = []
#     datalist_jux3 = []
#     datalist_jux4 = []
#     datalist_jux5 = []
#     for i in file_sup:
#         line = i.split(' ')
#         datalist_sup.append(float(line[0]))
#     for i in file_jux1:
#         line = i.split(' ')
#         datalist_jux1.append(float(line[0]))
#     for i in file_jux2:
#         line = i.split(' ')
#         datalist_jux2.append(float(line[0]))
#     for i in file_jux3:
#         line = i.split(' ')
#         datalist_jux3.append(float(line[0]))
#     for i in file_jux4:
#         line = i.split(' ')
#         datalist_jux4.append(float(line[0]))
#     for i in file_jux5:
#         line = i.split(' ')
#         datalist_jux5.append(float(line[0]))
#     number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
#     female_delivery_number_nhe50.append(0)
#     female_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[0]*solute_conversion)
#     female_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[0]*solute_conversion)
#     female_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[0]*solute_conversion)
#     female_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[0]*solute_conversion)
#     female_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[0]*solute_conversion)
#     female_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[0]*solute_conversion)
#     if seg == 'cnt':
#         female_delivery_number_nhe50.append(0)
#         female_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[-1]*solute_conversion)
#         female_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[-1]*solute_conversion)
#         female_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[-1]*solute_conversion)
#         female_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[-1]*solute_conversion)
#         female_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[-1]*solute_conversion)
#         female_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[-1]*solute_conversion)
# for seg in segment_late:
#     file_data = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
#     datalist = []
#     for i in file_data:
#         line = i.split(' ')
#         datalist.append(float(line[0]))
#     if seg == 'imcd':
#         number_of_delivery = datalist[-1]
#         female_delivery_number_nhe50.append(number_of_delivery*solute_conversion)
#     else:
#         number_of_delivery = datalist[0]
    

# male_delivery_number_nhe50 = []
# male_delivery_sup_nhe50 = []
# male_delivery_jux1_nhe50 = []
# male_delivery_jux2_nhe50 = []
# male_delivery_jux3_nhe50 = []
# male_delivery_jux4_nhe50 = []
# male_delivery_jux5_nhe50 = []
# for seg in segment_early:
#     file_sup = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
#     file_jux1 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
#     file_jux2 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
#     file_jux3 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
#     file_jux4 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
#     file_jux5 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
#     datalist_sup = []
#     datalist_jux1 = []
#     datalist_jux2 = []
#     datalist_jux3 = []
#     datalist_jux4 = []
#     datalist_jux5 = []
#     for i in file_sup:
#         line = i.split(' ')
#         datalist_sup.append(float(line[0]))
#     for i in file_jux1:
#         line = i.split(' ')
#         datalist_jux1.append(float(line[0]))
#     for i in file_jux2:
#         line = i.split(' ')
#         datalist_jux2.append(float(line[0]))
#     for i in file_jux3:
#         line = i.split(' ')
#         datalist_jux3.append(float(line[0]))
#     for i in file_jux4:
#         line = i.split(' ')
#         datalist_jux4.append(float(line[0]))
#     for i in file_jux5:
#         line = i.split(' ')
#         datalist_jux5.append(float(line[0]))
#     number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
#     male_delivery_number_nhe50.append(0)
#     male_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[0]*solute_conversion)
#     male_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[0]*solute_conversion)
#     male_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[0]*solute_conversion)
#     male_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[0]*solute_conversion)
#     male_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[0]*solute_conversion)
#     male_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[0]*solute_conversion)
#     if seg == 'cnt':
#         male_delivery_number_nhe50.append(0)
#         male_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[-1]*solute_conversion)
#         male_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[-1]*solute_conversion)
#         male_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[-1]*solute_conversion)
#         male_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[-1]*solute_conversion)
#         male_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[-1]*solute_conversion)
#         male_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[-1]*solute_conversion)
# for seg in segment_late:
#     file_data = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
#     datalist = []
#     for i in file_data:
#         line = i.split(' ')
#         datalist.append(float(line[0]))
#     if seg == 'imcd':
#         number_of_delivery = datalist[-1]
#         male_delivery_number_nhe50.append(number_of_delivery*solute_conversion)
#     else:
#         number_of_delivery = datalist[0]

# segment = ['PT','DL','mTAL','DCT','CNT','CCD','urine']
# bar_width = 0.15

# #print(segment[:6],male_delivery_sup)

# male_sup=axarr[2,0].bar(np.arange(len(segment[:6])),male_delivery_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')
# male_jux=axarr[2,0].bar(np.arange(len(segment[:6])),[male_delivery_jux1[i]+male_delivery_jux2[i]+male_delivery_jux3[i]+male_delivery_jux4[i]+male_delivery_jux5[i] for i in range(len(male_delivery_sup))],bar_width,bottom=male_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# male_later=axarr[2,0].bar(np.arange(len(segment)),male_delivery_number,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

# male_sup_nhe50=axarr[2,0].bar(np.arange(len(segment[:6]))+bar_width,male_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')
# male_jux_nhe50=axarr[2,0].bar(np.arange(len(segment[:6]))+bar_width,[male_delivery_jux1_nhe50[i]+male_delivery_jux2_nhe50[i]+male_delivery_jux3_nhe50[i]+male_delivery_jux4_nhe50[i]+male_delivery_jux5_nhe50[i] for i in range(len(male_delivery_sup_nhe50))],bar_width,bottom=male_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# male_later_nhe50=axarr[2,0].bar(np.arange(len(segment))+bar_width,male_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

# Female_sup=axarr[2,0].bar(np.arange(len(segment[:6]))+2*bar_width,female_delivery_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')
# Female_jux=axarr[2,0].bar(np.arange(len(segment[:6]))+2*bar_width,[female_delivery_jux1[i]+female_delivery_jux2[i]+female_delivery_jux3[i]+female_delivery_jux4[i]+female_delivery_jux5[i] for i in range(len(female_delivery_sup))],bar_width,bottom=female_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# Female_later=axarr[2,0].bar(np.arange(len(segment))+2*bar_width,female_delivery_number,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

# Female_sup_nhe50=axarr[2,0].bar(np.arange(len(segment[:6]))+3*bar_width,female_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')
# Female_jux_nhe50=axarr[2,0].bar(np.arange(len(segment[:6]))+3*bar_width,[female_delivery_jux1_nhe50[i]+female_delivery_jux2_nhe50[i]+female_delivery_jux3_nhe50[i]+female_delivery_jux4_nhe50[i]+female_delivery_jux5_nhe50[i] for i in range(len(female_delivery_sup_nhe50))],bar_width,bottom=female_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# Female_later_nhe50=axarr[2,0].bar(np.arange(len(segment))+3*bar_width,female_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')
# axarr[2,0].set_xticks(np.arange(len(segment))+1.5*bar_width)
# axarr[2,0].set_xticklabels(segment,fontsize=30)
# axarr[2,0].tick_params(axis='both',labelsize=30)
# #ax.set_xlabel('Segment',fontsize=20)
# axarr[2,0].set_ylabel('NH$_4^+$ delivery (mol/Day)',fontsize=30)
# #axarr[2,0].legend(fontsize=30,markerscale=30)
# bar_width_ins = bar_width
# #axins = inset_axes(ax,width=2,height=2,loc=7)
# #Male_inset=axins.bar(np.arange(len(segment)),male_list,bar_width_ins,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='black',label='Male')
# #Female_inset=axins.bar(np.arange(len(segment))+bar_width_ins,female_list,bar_width_ins,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white',label='Female')
# #axins.set_xticks(np.arange(len(segment))+0.5*bar_width_ins)
# #axins.set_xticklabels(segment,fontsize=20)
# #axins.set_xlim(5-1.5*bar_width_ins,6+2*bar_width)
# #axins.set_ylim(0,2)
# #axins.tick_params(axis='both',labelsize=20)
# #autolabel(Male,'left')
# #autolabel(Female,'right')

# #=================================================================
# # Urea
# #=================================================================

# s = 'urea'
# female_delivery_number = []
# female_delivery_sup = []
# female_delivery_jux1 = []
# female_delivery_jux2 = []
# female_delivery_jux3 = []
# female_delivery_jux4 = []
# female_delivery_jux5 = []
# for seg in segment_early:
#     file_sup = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
#     file_jux1 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
#     file_jux2 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
#     file_jux3 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
#     file_jux4 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
#     file_jux5 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
#     datalist_sup = []
#     datalist_jux1 = []
#     datalist_jux2 = []
#     datalist_jux3 = []
#     datalist_jux4 = []
#     datalist_jux5 = []
#     for i in file_sup:
#         line = i.split(' ')
#         datalist_sup.append(float(line[0]))
#     for i in file_jux1:
#         line = i.split(' ')
#         datalist_jux1.append(float(line[0]))
#     for i in file_jux2:
#         line = i.split(' ')
#         datalist_jux2.append(float(line[0]))
#     for i in file_jux3:
#         line = i.split(' ')
#         datalist_jux3.append(float(line[0]))
#     for i in file_jux4:
#         line = i.split(' ')
#         datalist_jux4.append(float(line[0]))
#     for i in file_jux5:
#         line = i.split(' ')
#         datalist_jux5.append(float(line[0]))
#     number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
#     female_delivery_number.append(0)
#     female_delivery_sup.append(neph_weight[0]*datalist_sup[0]*solute_conversion)
#     female_delivery_jux1.append(neph_weight[1]*datalist_jux1[0]*solute_conversion)
#     female_delivery_jux2.append(neph_weight[2]*datalist_jux2[0]*solute_conversion)
#     female_delivery_jux3.append(neph_weight[3]*datalist_jux3[0]*solute_conversion)
#     female_delivery_jux4.append(neph_weight[4]*datalist_jux4[0]*solute_conversion)
#     female_delivery_jux5.append(neph_weight[5]*datalist_jux5[0]*solute_conversion)
#     if seg == 'cnt':
#         female_delivery_number.append(0)
#         female_delivery_sup.append(neph_weight[0]*datalist_sup[-1]*solute_conversion)
#         female_delivery_jux1.append(neph_weight[1]*datalist_jux1[-1]*solute_conversion)
#         female_delivery_jux2.append(neph_weight[2]*datalist_jux2[-1]*solute_conversion)
#         female_delivery_jux3.append(neph_weight[3]*datalist_jux3[-1]*solute_conversion)
#         female_delivery_jux4.append(neph_weight[4]*datalist_jux4[-1]*solute_conversion)
#         female_delivery_jux5.append(neph_weight[5]*datalist_jux5[-1]*solute_conversion)
# for seg in segment_late:
#     file_data = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
#     datalist = []
#     for i in file_data:
#         line = i.split(' ')
#         datalist.append(float(line[0]))
#     if seg == 'imcd':
#         number_of_delivery = datalist[-1]
#         female_delivery_number.append(number_of_delivery*solute_conversion)
#     else:
#         number_of_delivery = datalist[0]
    

# male_delivery_number = []
# male_delivery_sup = []
# male_delivery_jux1 = []
# male_delivery_jux2 = []
# male_delivery_jux3 = []
# male_delivery_jux4 = []
# male_delivery_jux5 = []
# for seg in segment_early:
#     file_sup = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
#     file_jux1 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
#     file_jux2 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
#     file_jux3 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
#     file_jux4 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
#     file_jux5 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
#     datalist_sup = []
#     datalist_jux1 = []
#     datalist_jux2 = []
#     datalist_jux3 = []
#     datalist_jux4 = []
#     datalist_jux5 = []
#     for i in file_sup:
#         line = i.split(' ')
#         datalist_sup.append(float(line[0]))
#     for i in file_jux1:
#         line = i.split(' ')
#         datalist_jux1.append(float(line[0]))
#     for i in file_jux2:
#         line = i.split(' ')
#         datalist_jux2.append(float(line[0]))
#     for i in file_jux3:
#         line = i.split(' ')
#         datalist_jux3.append(float(line[0]))
#     for i in file_jux4:
#         line = i.split(' ')
#         datalist_jux4.append(float(line[0]))
#     for i in file_jux5:
#         line = i.split(' ')
#         datalist_jux5.append(float(line[0]))
#     number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
#     male_delivery_number.append(0)
#     male_delivery_sup.append(neph_weight[0]*datalist_sup[0]*solute_conversion)
#     male_delivery_jux1.append(neph_weight[1]*datalist_jux1[0]*solute_conversion)
#     male_delivery_jux2.append(neph_weight[2]*datalist_jux2[0]*solute_conversion)
#     male_delivery_jux3.append(neph_weight[3]*datalist_jux3[0]*solute_conversion)
#     male_delivery_jux4.append(neph_weight[4]*datalist_jux4[0]*solute_conversion)
#     male_delivery_jux5.append(neph_weight[5]*datalist_jux5[0]*solute_conversion)
#     if seg == 'cnt':
#         male_delivery_number.append(0)
#         male_delivery_sup.append(neph_weight[0]*datalist_sup[-1]*solute_conversion)
#         male_delivery_jux1.append(neph_weight[1]*datalist_jux1[-1]*solute_conversion)
#         male_delivery_jux2.append(neph_weight[2]*datalist_jux2[-1]*solute_conversion)
#         male_delivery_jux3.append(neph_weight[3]*datalist_jux3[-1]*solute_conversion)
#         male_delivery_jux4.append(neph_weight[4]*datalist_jux4[-1]*solute_conversion)
#         male_delivery_jux5.append(neph_weight[5]*datalist_jux5[-1]*solute_conversion)
# for seg in segment_late:
#     file_data = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
#     datalist = []
#     for i in file_data:
#         line = i.split(' ')
#         datalist.append(float(line[0]))
#     if seg == 'imcd':
#         number_of_delivery = datalist[-1]
#         male_delivery_number.append(number_of_delivery*solute_conversion)
#     else:
#         number_of_delivery = datalist[0]

#     #===================================
#     # NHE3 50% inhibited
#     #===================================
# female_delivery_number_nhe50 = []
# female_delivery_sup_nhe50 = []
# female_delivery_jux1_nhe50 = []
# female_delivery_jux2_nhe50 = []
# female_delivery_jux3_nhe50 = []
# female_delivery_jux4_nhe50 = []
# female_delivery_jux5_nhe50 = []
# for seg in segment_early:
#     file_sup = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
#     file_jux1 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
#     file_jux2 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
#     file_jux3 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
#     file_jux4 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
#     file_jux5 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
#     datalist_sup = []
#     datalist_jux1 = []
#     datalist_jux2 = []
#     datalist_jux3 = []
#     datalist_jux4 = []
#     datalist_jux5 = []
#     for i in file_sup:
#         line = i.split(' ')
#         datalist_sup.append(float(line[0]))
#     for i in file_jux1:
#         line = i.split(' ')
#         datalist_jux1.append(float(line[0]))
#     for i in file_jux2:
#         line = i.split(' ')
#         datalist_jux2.append(float(line[0]))
#     for i in file_jux3:
#         line = i.split(' ')
#         datalist_jux3.append(float(line[0]))
#     for i in file_jux4:
#         line = i.split(' ')
#         datalist_jux4.append(float(line[0]))
#     for i in file_jux5:
#         line = i.split(' ')
#         datalist_jux5.append(float(line[0]))
#     number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
#     female_delivery_number_nhe50.append(0)
#     female_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[0]*solute_conversion)
#     female_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[0]*solute_conversion)
#     female_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[0]*solute_conversion)
#     female_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[0]*solute_conversion)
#     female_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[0]*solute_conversion)
#     female_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[0]*solute_conversion)
#     if seg == 'cnt':
#         female_delivery_number_nhe50.append(0)
#         female_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[-1]*solute_conversion)
#         female_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[-1]*solute_conversion)
#         female_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[-1]*solute_conversion)
#         female_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[-1]*solute_conversion)
#         female_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[-1]*solute_conversion)
#         female_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[-1]*solute_conversion)
# for seg in segment_late:
#     file_data = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
#     datalist = []
#     for i in file_data:
#         line = i.split(' ')
#         datalist.append(float(line[0]))
#     if seg == 'imcd':
#         number_of_delivery = datalist[-1]
#         female_delivery_number_nhe50.append(number_of_delivery*solute_conversion)
#     else:
#         number_of_delivery = datalist[0]
    

# male_delivery_number_nhe50 = []
# male_delivery_sup_nhe50 = []
# male_delivery_jux1_nhe50 = []
# male_delivery_jux2_nhe50 = []
# male_delivery_jux3_nhe50 = []
# male_delivery_jux4_nhe50 = []
# male_delivery_jux5_nhe50 = []
# for seg in segment_early:
#     file_sup = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
#     file_jux1 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
#     file_jux2 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
#     file_jux3 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
#     file_jux4 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
#     file_jux5 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
#     datalist_sup = []
#     datalist_jux1 = []
#     datalist_jux2 = []
#     datalist_jux3 = []
#     datalist_jux4 = []
#     datalist_jux5 = []
#     for i in file_sup:
#         line = i.split(' ')
#         datalist_sup.append(float(line[0]))
#     for i in file_jux1:
#         line = i.split(' ')
#         datalist_jux1.append(float(line[0]))
#     for i in file_jux2:
#         line = i.split(' ')
#         datalist_jux2.append(float(line[0]))
#     for i in file_jux3:
#         line = i.split(' ')
#         datalist_jux3.append(float(line[0]))
#     for i in file_jux4:
#         line = i.split(' ')
#         datalist_jux4.append(float(line[0]))
#     for i in file_jux5:
#         line = i.split(' ')
#         datalist_jux5.append(float(line[0]))
#     number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
#     male_delivery_number_nhe50.append(0)
#     male_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[0]*solute_conversion)
#     male_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[0]*solute_conversion)
#     male_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[0]*solute_conversion)
#     male_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[0]*solute_conversion)
#     male_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[0]*solute_conversion)
#     male_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[0]*solute_conversion)
#     if seg == 'cnt':
#         male_delivery_number_nhe50.append(0)
#         male_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[-1]*solute_conversion)
#         male_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[-1]*solute_conversion)
#         male_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[-1]*solute_conversion)
#         male_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[-1]*solute_conversion)
#         male_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[-1]*solute_conversion)
#         male_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[-1]*solute_conversion)
# for seg in segment_late:
#     file_data = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
#     datalist = []
#     for i in file_data:
#         line = i.split(' ')
#         datalist.append(float(line[0]))
#     if seg == 'imcd':
#         number_of_delivery = datalist[-1]
#         male_delivery_number_nhe50.append(number_of_delivery*solute_conversion)
#     else:
#         number_of_delivery = datalist[0]

# segment = ['PT','DL','mTAL','DCT','CNT','CCD','urine']
# bar_width = 0.15

# #print(segment[:6],male_delivery_sup)

# male_sup=axarr[2,1].bar(np.arange(len(segment[:6])),male_delivery_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')
# male_jux=axarr[2,1].bar(np.arange(len(segment[:6])),[male_delivery_jux1[i]+male_delivery_jux2[i]+male_delivery_jux3[i]+male_delivery_jux4[i]+male_delivery_jux5[i] for i in range(len(male_delivery_sup))],bar_width,bottom=male_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# male_later=axarr[2,1].bar(np.arange(len(segment)),male_delivery_number,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

# male_sup_nhe50=axarr[2,1].bar(np.arange(len(segment[:6]))+bar_width,male_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')
# male_jux_nhe50=axarr[2,1].bar(np.arange(len(segment[:6]))+bar_width,[male_delivery_jux1_nhe50[i]+male_delivery_jux2_nhe50[i]+male_delivery_jux3_nhe50[i]+male_delivery_jux4_nhe50[i]+male_delivery_jux5_nhe50[i] for i in range(len(male_delivery_sup_nhe50))],bar_width,bottom=male_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# male_later_nhe50=axarr[2,1].bar(np.arange(len(segment))+bar_width,male_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

# Female_sup=axarr[2,1].bar(np.arange(len(segment[:6]))+2*bar_width,female_delivery_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')
# Female_jux=axarr[2,1].bar(np.arange(len(segment[:6]))+2*bar_width,[female_delivery_jux1[i]+female_delivery_jux2[i]+female_delivery_jux3[i]+female_delivery_jux4[i]+female_delivery_jux5[i] for i in range(len(female_delivery_sup))],bar_width,bottom=female_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# Female_later=axarr[2,1].bar(np.arange(len(segment))+2*bar_width,female_delivery_number,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

# Female_sup_nhe50=axarr[2,1].bar(np.arange(len(segment[:6]))+3*bar_width,female_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')
# Female_jux_nhe50=axarr[2,1].bar(np.arange(len(segment[:6]))+3*bar_width,[female_delivery_jux1_nhe50[i]+female_delivery_jux2_nhe50[i]+female_delivery_jux3_nhe50[i]+female_delivery_jux4_nhe50[i]+female_delivery_jux5_nhe50[i] for i in range(len(female_delivery_sup_nhe50))],bar_width,bottom=female_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# Female_later_nhe50=axarr[2,1].bar(np.arange(len(segment))+3*bar_width,female_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')
# axarr[2,1].set_xticks(np.arange(len(segment))+1.5*bar_width)
# axarr[2,1].set_xticklabels(segment,fontsize=30)
# axarr[2,1].tick_params(axis='both',labelsize=30)
# #ax.set_xlabel('Segment',fontsize=20)
# axarr[2,1].set_ylabel('Urea delivery (mol/Day)',fontsize=30)
# #axarr[2,1].legend(fontsize=30,markerscale=30)
# bar_width_ins = bar_width
# #axins = inset_axes(ax,width=2,height=2,loc=7)
# #Male_inset=axins.bar(np.arange(len(segment)),male_list,bar_width_ins,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='black',label='Male')
# #Female_inset=axins.bar(np.arange(len(segment))+bar_width_ins,female_list,bar_width_ins,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white',label='Female')
# #axins.set_xticks(np.arange(len(segment))+0.5*bar_width_ins)
# #axins.set_xticklabels(segment,fontsize=20)
# #axins.set_xlim(5-1.5*bar_width_ins,6+2*bar_width)
# #axins.set_ylim(0,2)
# #axins.tick_params(axis='both',labelsize=20)
# #autolabel(Male,'left')
# #autolabel(Female,'right')

#=================================================================
# TA
#=================================================================

female_delivery_number = []
female_delivery_sup = []
female_delivery_jux1 = []
female_delivery_jux2 = []
female_delivery_jux3 = []
female_delivery_jux4 = []
female_delivery_jux5 = []
for seg in segment_early:
    file_sup = open(female_normal_file+'/female_hum_'+seg+'_flow_of_H2PO4_in_Lumen_sup.txt','r')
    file_jux1 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    file_sup_2 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_HPO4_in_Lumen_sup.txt','r')
    file_jux1_2 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux1.txt','r')
    file_jux2_2 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux2.txt','r')
    file_jux3_2 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux3.txt','r')
    file_jux4_2 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux4.txt','r')
    file_jux5_2 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux5.txt','r')
    datalist_sup_2 = []
    datalist_jux1_2 = []
    datalist_jux2_2 = []
    datalist_jux3_2 = []
    datalist_jux4_2 = []
    datalist_jux5_2 = []
    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    for i in file_jux1:
        line = i.split(' ')
        datalist_jux1.append(float(line[0]))
    for i in file_jux2:
        line = i.split(' ')
        datalist_jux2.append(float(line[0]))
    for i in file_jux3:
        line = i.split(' ')
        datalist_jux3.append(float(line[0]))
    for i in file_jux4:
        line = i.split(' ')
        datalist_jux4.append(float(line[0]))
    for i in file_jux5:
        line = i.split(' ')
        datalist_jux5.append(float(line[0]))
    for i in file_sup_2:
        line = i.split(' ')
        datalist_sup_2.append(float(line[0]))
    for i in file_jux1_2:
        line = i.split(' ')
        datalist_jux1_2.append(float(line[0]))
    for i in file_jux2_2:
        line = i.split(' ')
        datalist_jux2_2.append(float(line[0]))
    for i in file_jux3_2:
        line = i.split(' ')
        datalist_jux3_2.append(float(line[0]))
    for i in file_jux4_2:
        line = i.split(' ')
        datalist_jux4_2.append(float(line[0]))
    for i in file_jux5_2:
        line = i.split(' ')
        datalist_jux5_2.append(float(line[0]))
    female_delivery_number.append(0)
    female_delivery_sup.append(neph_weight[0]*(10**(7.4-6.8)*datalist_sup[0]-datalist_sup_2[0])/(1+10**(7.4-6.8))*solute_conversion)
    female_delivery_jux1.append(neph_weight[1]*(10**(7.4-6.8)*datalist_jux1[0]-datalist_jux1_2[0])/(1+10**(7.4-6.8))*solute_conversion)
    female_delivery_jux2.append(neph_weight[2]*(10**(7.4-6.8)*datalist_jux2[0]-datalist_jux2_2[0])/(1+10**(7.4-6.8))*solute_conversion)
    female_delivery_jux3.append(neph_weight[3]*(10**(7.4-6.8)*datalist_jux3[0]-datalist_jux3_2[0])/(1+10**(7.4-6.8))*solute_conversion)
    female_delivery_jux4.append(neph_weight[4]*(10**(7.4-6.8)*datalist_jux4[0]-datalist_jux4_2[0])/(1+10**(7.4-6.8))*solute_conversion)
    female_delivery_jux5.append(neph_weight[5]*(10**(7.4-6.8)*datalist_jux5[0]-datalist_jux5_2[0])/(1+10**(7.4-6.8))*solute_conversion)
    if seg == 'cnt':
        female_delivery_number.append(0)
        female_delivery_sup.append(neph_weight[0]*(10**(7.4-6.8)*datalist_sup[-1]-datalist_sup_2[-1])/(1+10**(7.4-6.8))*solute_conversion)
        female_delivery_jux1.append(neph_weight[1]*(10**(7.4-6.8)*datalist_jux1[-1]-datalist_jux1_2[-1])/(1+10**(7.4-6.8))*solute_conversion)
        female_delivery_jux2.append(neph_weight[2]*(10**(7.4-6.8)*datalist_jux2[-1]-datalist_jux2_2[-1])/(1+10**(7.4-6.8))*solute_conversion)
        female_delivery_jux3.append(neph_weight[3]*(10**(7.4-6.8)*datalist_jux3[-1]-datalist_jux3_2[-1])/(1+10**(7.4-6.8))*solute_conversion)
        female_delivery_jux4.append(neph_weight[4]*(10**(7.4-6.8)*datalist_jux4[-1]-datalist_jux4_2[-1])/(1+10**(7.4-6.8))*solute_conversion)
        female_delivery_jux5.append(neph_weight[5]*(10**(7.4-6.8)*datalist_jux5[-1]-datalist_jux5_2[-1])/(1+10**(7.4-6.8))*solute_conversion)
for seg in segment_late:
    file_data = open(female_normal_file+'/female_hum_'+seg+'_flow_of_H2PO4_in_Lumen.txt','r')
    file_data_2 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_HPO4_in_Lumen.txt','r')
    datalist = []
    datalist_2 = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    for i in file_data_2:
        line = i.split(' ')
        datalist_2.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = (10**(7.4-6.8)*datalist[-1]-datalist_2[-1])/(1+10**(7.4-6.8))
        female_delivery_number.append(number_of_delivery*solute_conversion)
    else:
        number_of_delivery = datalist[0]
    

male_delivery_number = []
male_delivery_sup = []
male_delivery_jux1 = []
male_delivery_jux2 = []
male_delivery_jux3 = []
male_delivery_jux4 = []
male_delivery_jux5 = []
for seg in segment_early:
    file_sup = open(male_normal_file+'/male_hum_'+seg+'_flow_of_H2PO4_in_Lumen_sup.txt','r')
    file_jux1 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    file_sup_2 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_HPO4_in_Lumen_sup.txt','r')
    file_jux1_2 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux1.txt','r')
    file_jux2_2 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux2.txt','r')
    file_jux3_2 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux3.txt','r')
    file_jux4_2 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux4.txt','r')
    file_jux5_2 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux5.txt','r')
    datalist_sup_2 = []
    datalist_jux1_2 = []
    datalist_jux2_2 = []
    datalist_jux3_2 = []
    datalist_jux4_2 = []
    datalist_jux5_2 = []
    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    for i in file_jux1:
        line = i.split(' ')
        datalist_jux1.append(float(line[0]))
    for i in file_jux2:
        line = i.split(' ')
        datalist_jux2.append(float(line[0]))
    for i in file_jux3:
        line = i.split(' ')
        datalist_jux3.append(float(line[0]))
    for i in file_jux4:
        line = i.split(' ')
        datalist_jux4.append(float(line[0]))
    for i in file_jux5:
        line = i.split(' ')
        datalist_jux5.append(float(line[0]))
    for i in file_sup_2:
        line = i.split(' ')
        datalist_sup_2.append(float(line[0]))
    for i in file_jux1_2:
        line = i.split(' ')
        datalist_jux1_2.append(float(line[0]))
    for i in file_jux2_2:
        line = i.split(' ')
        datalist_jux2_2.append(float(line[0]))
    for i in file_jux3_2:
        line = i.split(' ')
        datalist_jux3_2.append(float(line[0]))
    for i in file_jux4_2:
        line = i.split(' ')
        datalist_jux4_2.append(float(line[0]))
    for i in file_jux5_2:
        line = i.split(' ')
        datalist_jux5_2.append(float(line[0]))
    male_delivery_number.append(0)
    male_delivery_sup.append(neph_weight[0]*(10**(7.4-6.8)*datalist_sup[0]-datalist_sup_2[0])/(1+10**(7.4-6.8))*solute_conversion)
    male_delivery_jux1.append(neph_weight[1]*(10**(7.4-6.8)*datalist_jux1[0]-datalist_jux1_2[0])/(1+10**(7.4-6.8))*solute_conversion)
    male_delivery_jux2.append(neph_weight[2]*(10**(7.4-6.8)*datalist_jux2[0]-datalist_jux2_2[0])/(1+10**(7.4-6.8))*solute_conversion)
    male_delivery_jux3.append(neph_weight[3]*(10**(7.4-6.8)*datalist_jux3[0]-datalist_jux3_2[0])/(1+10**(7.4-6.8))*solute_conversion)
    male_delivery_jux4.append(neph_weight[4]*(10**(7.4-6.8)*datalist_jux4[0]-datalist_jux4_2[0])/(1+10**(7.4-6.8))*solute_conversion)
    male_delivery_jux5.append(neph_weight[5]*(10**(7.4-6.8)*datalist_jux5[0]-datalist_jux5_2[0])/(1+10**(7.4-6.8))*solute_conversion)
    if seg == 'cnt':
        male_delivery_number.append(0)
        male_delivery_sup.append(neph_weight[0]*(10**(7.4-6.8)*datalist_sup[-1]-datalist_sup_2[-1])/(1+10**(7.4-6.8))*solute_conversion)
        male_delivery_jux1.append(neph_weight[1]*(10**(7.4-6.8)*datalist_jux1[-1]-datalist_jux1_2[-1])/(1+10**(7.4-6.8))*solute_conversion)
        male_delivery_jux2.append(neph_weight[2]*(10**(7.4-6.8)*datalist_jux2[-1]-datalist_jux2_2[-1])/(1+10**(7.4-6.8))*solute_conversion)
        male_delivery_jux3.append(neph_weight[3]*(10**(7.4-6.8)*datalist_jux3[-1]-datalist_jux3_2[-1])/(1+10**(7.4-6.8))*solute_conversion)
        male_delivery_jux4.append(neph_weight[4]*(10**(7.4-6.8)*datalist_jux4[-1]-datalist_jux4_2[-1])/(1+10**(7.4-6.8))*solute_conversion)
        male_delivery_jux5.append(neph_weight[5]*(10**(7.4-6.8)*datalist_jux5[-1]-datalist_jux5_2[-1])/(1+10**(7.4-6.8))*solute_conversion)
for seg in segment_late:
    file_data = open(male_normal_file+'/male_hum_'+seg+'_flow_of_H2PO4_in_Lumen.txt','r')
    file_data_2 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_HPO4_in_Lumen.txt','r')
    datalist = []
    datalist_2 = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    for i in file_data_2:
        line = i.split(' ')
        datalist_2.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = (10**(7.4-6.8)*datalist[-1]-datalist_2[-1])/(1+10**(7.4-6.8))
        male_delivery_number.append(number_of_delivery*solute_conversion)
    else:
        number_of_delivery = datalist[0]

    #=======================================
    # NHE3 50% inhibited
    #=======================================
female_delivery_number_nhe50 = []
female_delivery_sup_nhe50 = []
female_delivery_jux1_nhe50 = []
female_delivery_jux2_nhe50 = []
female_delivery_jux3_nhe50 = []
female_delivery_jux4_nhe50 = []
female_delivery_jux5_nhe50 = []
for seg in segment_early:
    file_sup = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_H2PO4_in_Lumen_sup.txt','r')
    file_jux1 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    file_sup_2 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_HPO4_in_Lumen_sup.txt','r')
    file_jux1_2 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux1.txt','r')
    file_jux2_2 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux2.txt','r')
    file_jux3_2 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux3.txt','r')
    file_jux4_2 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux4.txt','r')
    file_jux5_2 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux5.txt','r')
    datalist_sup_2 = []
    datalist_jux1_2 = []
    datalist_jux2_2 = []
    datalist_jux3_2 = []
    datalist_jux4_2 = []
    datalist_jux5_2 = []
    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    for i in file_jux1:
        line = i.split(' ')
        datalist_jux1.append(float(line[0]))
    for i in file_jux2:
        line = i.split(' ')
        datalist_jux2.append(float(line[0]))
    for i in file_jux3:
        line = i.split(' ')
        datalist_jux3.append(float(line[0]))
    for i in file_jux4:
        line = i.split(' ')
        datalist_jux4.append(float(line[0]))
    for i in file_jux5:
        line = i.split(' ')
        datalist_jux5.append(float(line[0]))
    for i in file_sup_2:
        line = i.split(' ')
        datalist_sup_2.append(float(line[0]))
    for i in file_jux1_2:
        line = i.split(' ')
        datalist_jux1_2.append(float(line[0]))
    for i in file_jux2_2:
        line = i.split(' ')
        datalist_jux2_2.append(float(line[0]))
    for i in file_jux3_2:
        line = i.split(' ')
        datalist_jux3_2.append(float(line[0]))
    for i in file_jux4_2:
        line = i.split(' ')
        datalist_jux4_2.append(float(line[0]))
    for i in file_jux5_2:
        line = i.split(' ')
        datalist_jux5_2.append(float(line[0]))
    female_delivery_number_nhe50.append(0)
    female_delivery_sup_nhe50.append(neph_weight[0]*(10**(7.4-6.8)*datalist_sup[0]-datalist_sup_2[0])/(1+10**(7.4-6.8))*solute_conversion)
    female_delivery_jux1_nhe50.append(neph_weight[1]*(10**(7.4-6.8)*datalist_jux1[0]-datalist_jux1_2[0])/(1+10**(7.4-6.8))*solute_conversion)
    female_delivery_jux2_nhe50.append(neph_weight[2]*(10**(7.4-6.8)*datalist_jux2[0]-datalist_jux2_2[0])/(1+10**(7.4-6.8))*solute_conversion)
    female_delivery_jux3_nhe50.append(neph_weight[3]*(10**(7.4-6.8)*datalist_jux3[0]-datalist_jux3_2[0])/(1+10**(7.4-6.8))*solute_conversion)
    female_delivery_jux4_nhe50.append(neph_weight[4]*(10**(7.4-6.8)*datalist_jux4[0]-datalist_jux4_2[0])/(1+10**(7.4-6.8))*solute_conversion)
    female_delivery_jux5_nhe50.append(neph_weight[5]*(10**(7.4-6.8)*datalist_jux5[0]-datalist_jux5_2[0])/(1+10**(7.4-6.8))*solute_conversion)
    if seg == 'cnt':
        female_delivery_number_nhe50.append(0)
        female_delivery_sup_nhe50.append(neph_weight[0]*(10**(7.4-6.8)*datalist_sup[-1]-datalist_sup_2[-1])/(1+10**(7.4-6.8))*solute_conversion)
        female_delivery_jux1_nhe50.append(neph_weight[1]*(10**(7.4-6.8)*datalist_jux1[-1]-datalist_jux1_2[-1])/(1+10**(7.4-6.8))*solute_conversion)
        female_delivery_jux2_nhe50.append(neph_weight[2]*(10**(7.4-6.8)*datalist_jux2[-1]-datalist_jux2_2[-1])/(1+10**(7.4-6.8))*solute_conversion)
        female_delivery_jux3_nhe50.append(neph_weight[3]*(10**(7.4-6.8)*datalist_jux3[-1]-datalist_jux3_2[-1])/(1+10**(7.4-6.8))*solute_conversion)
        female_delivery_jux4_nhe50.append(neph_weight[4]*(10**(7.4-6.8)*datalist_jux4[-1]-datalist_jux4_2[-1])/(1+10**(7.4-6.8))*solute_conversion)
        female_delivery_jux5_nhe50.append(neph_weight[5]*(10**(7.4-6.8)*datalist_jux5[-1]-datalist_jux5_2[-1])/(1+10**(7.4-6.8))*solute_conversion)
for seg in segment_late:
    file_data = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_H2PO4_in_Lumen.txt','r')
    file_data_2 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_HPO4_in_Lumen.txt','r')
    datalist = []
    datalist_2 = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    for i in file_data_2:
        line = i.split(' ')
        datalist_2.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = (10**(7.4-6.8)*datalist[-1]-datalist_2[-1])/(1+10**(7.4-6.8))
        female_delivery_number_nhe50.append(number_of_delivery*solute_conversion)
    else:
        number_of_delivery = datalist[0]
    

male_delivery_number_nhe50 = []
male_delivery_sup_nhe50 = []
male_delivery_jux1_nhe50 = []
male_delivery_jux2_nhe50 = []
male_delivery_jux3_nhe50 = []
male_delivery_jux4_nhe50 = []
male_delivery_jux5_nhe50 = []
for seg in segment_early:
    file_sup = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_H2PO4_in_Lumen_sup.txt','r')
    file_jux1 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    file_sup_2 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_HPO4_in_Lumen_sup.txt','r')
    file_jux1_2 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux1.txt','r')
    file_jux2_2 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux2.txt','r')
    file_jux3_2 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux3.txt','r')
    file_jux4_2 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux4.txt','r')
    file_jux5_2 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux5.txt','r')
    datalist_sup_2 = []
    datalist_jux1_2 = []
    datalist_jux2_2 = []
    datalist_jux3_2 = []
    datalist_jux4_2 = []
    datalist_jux5_2 = []
    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    for i in file_jux1:
        line = i.split(' ')
        datalist_jux1.append(float(line[0]))
    for i in file_jux2:
        line = i.split(' ')
        datalist_jux2.append(float(line[0]))
    for i in file_jux3:
        line = i.split(' ')
        datalist_jux3.append(float(line[0]))
    for i in file_jux4:
        line = i.split(' ')
        datalist_jux4.append(float(line[0]))
    for i in file_jux5:
        line = i.split(' ')
        datalist_jux5.append(float(line[0]))
    for i in file_sup_2:
        line = i.split(' ')
        datalist_sup_2.append(float(line[0]))
    for i in file_jux1_2:
        line = i.split(' ')
        datalist_jux1_2.append(float(line[0]))
    for i in file_jux2_2:
        line = i.split(' ')
        datalist_jux2_2.append(float(line[0]))
    for i in file_jux3_2:
        line = i.split(' ')
        datalist_jux3_2.append(float(line[0]))
    for i in file_jux4_2:
        line = i.split(' ')
        datalist_jux4_2.append(float(line[0]))
    for i in file_jux5_2:
        line = i.split(' ')
        datalist_jux5_2.append(float(line[0]))
    male_delivery_number_nhe50.append(0)
    male_delivery_sup_nhe50.append(neph_weight[0]*(10**(7.4-6.8)*datalist_sup[0]-datalist_sup_2[0])/(1+10**(7.4-6.8))*solute_conversion)
    male_delivery_jux1_nhe50.append(neph_weight[1]*(10**(7.4-6.8)*datalist_jux1[0]-datalist_jux1_2[0])/(1+10**(7.4-6.8))*solute_conversion)
    male_delivery_jux2_nhe50.append(neph_weight[2]*(10**(7.4-6.8)*datalist_jux2[0]-datalist_jux2_2[0])/(1+10**(7.4-6.8))*solute_conversion)
    male_delivery_jux3_nhe50.append(neph_weight[3]*(10**(7.4-6.8)*datalist_jux3[0]-datalist_jux3_2[0])/(1+10**(7.4-6.8))*solute_conversion)
    male_delivery_jux4_nhe50.append(neph_weight[4]*(10**(7.4-6.8)*datalist_jux4[0]-datalist_jux4_2[0])/(1+10**(7.4-6.8))*solute_conversion)
    male_delivery_jux5_nhe50.append(neph_weight[5]*(10**(7.4-6.8)*datalist_jux5[0]-datalist_jux5_2[0])/(1+10**(7.4-6.8))*solute_conversion)
    if seg == 'cnt':
        male_delivery_number_nhe50.append(0)
        male_delivery_sup_nhe50.append(neph_weight[0]*(10**(7.4-6.8)*datalist_sup[-1]-datalist_sup_2[-1])/(1+10**(7.4-6.8))*solute_conversion)
        male_delivery_jux1_nhe50.append(neph_weight[1]*(10**(7.4-6.8)*datalist_jux1[-1]-datalist_jux1_2[-1])/(1+10**(7.4-6.8))*solute_conversion)
        male_delivery_jux2_nhe50.append(neph_weight[2]*(10**(7.4-6.8)*datalist_jux2[-1]-datalist_jux2_2[-1])/(1+10**(7.4-6.8))*solute_conversion)
        male_delivery_jux3_nhe50.append(neph_weight[3]*(10**(7.4-6.8)*datalist_jux3[-1]-datalist_jux3_2[-1])/(1+10**(7.4-6.8))*solute_conversion)
        male_delivery_jux4_nhe50.append(neph_weight[4]*(10**(7.4-6.8)*datalist_jux4[-1]-datalist_jux4_2[-1])/(1+10**(7.4-6.8))*solute_conversion)
        male_delivery_jux5_nhe50.append(neph_weight[5]*(10**(7.4-6.8)*datalist_jux5[-1]-datalist_jux5_2[-1])/(1+10**(7.4-6.8))*solute_conversion)
for seg in segment_late:
    file_data = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_H2PO4_in_Lumen.txt','r')
    file_data_2 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_HPO4_in_Lumen.txt','r')
    datalist = []
    datalist_2 = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    for i in file_data_2:
        line = i.split(' ')
        datalist_2.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = (10**(7.4-6.8)*datalist[-1]-datalist_2[-1])/(1+10**(7.4-6.8))
        male_delivery_number_nhe50.append(number_of_delivery*solute_conversion)
    else:
        number_of_delivery = datalist[0]

male_sup=axarr[2,0].bar(np.arange(len(segment[:6])),male_delivery_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Male')
male_jux=axarr[2,0].bar(np.arange(len(segment[:6])),[male_delivery_jux1[i]+male_delivery_jux2[i]+male_delivery_jux3[i]+male_delivery_jux4[i]+male_delivery_jux5[i] for i in range(len(male_delivery_sup))],bar_width,bottom=male_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later=axarr[2,0].bar(np.arange(len(segment)),male_delivery_number,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

male_sup_nhe50=axarr[2,0].bar(np.arange(len(segment[:6]))+bar_width,male_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue',label='Male')
male_jux_nhe50=axarr[2,0].bar(np.arange(len(segment[:6]))+bar_width,[male_delivery_jux1_nhe50[i]+male_delivery_jux2_nhe50[i]+male_delivery_jux3_nhe50[i]+male_delivery_jux4_nhe50[i]+male_delivery_jux5_nhe50[i] for i in range(len(male_delivery_sup_nhe50))],bar_width,bottom=male_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later_nhe50=axarr[2,0].bar(np.arange(len(segment))+bar_width,male_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

Female_sup=axarr[2,0].bar(np.arange(len(segment[:6]))+2*bar_width,female_delivery_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta',label='Female')
Female_jux=axarr[2,0].bar(np.arange(len(segment[:6]))+2*bar_width,[female_delivery_jux1[i]+female_delivery_jux2[i]+female_delivery_jux3[i]+female_delivery_jux4[i]+female_delivery_jux5[i] for i in range(len(female_delivery_sup))],bar_width,bottom=female_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white',label='Juxtamedullary')
Female_later=axarr[2,0].bar(np.arange(len(segment))+2*bar_width,female_delivery_number,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

Female_sup_nhe50=axarr[2,0].bar(np.arange(len(segment[:6]))+3*bar_width,female_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink',label='Female')
Female_jux_nhe50=axarr[2,0].bar(np.arange(len(segment[:6]))+3*bar_width,[female_delivery_jux1_nhe50[i]+female_delivery_jux2_nhe50[i]+female_delivery_jux3_nhe50[i]+female_delivery_jux4_nhe50[i]+female_delivery_jux5_nhe50[i] for i in range(len(female_delivery_sup_nhe50))],bar_width,bottom=female_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white',label='Juxtamedullary')
Female_later_nhe50=axarr[2,0].bar(np.arange(len(segment))+3*bar_width,female_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')

axarr[2,0].set_xticks(np.arange(len(segment))+1.5*bar_width)
axarr[2,0].set_xticklabels(segment,fontsize=30)
axarr[2,0].tick_params(axis='both',labelsize=30)
#ax.set_xlabel('Segment',fontsize=20)
axarr[2,0].set_ylabel('TA delivery (mol/Day)',fontsize=30)
#axarr[3,0].legend(fontsize=30,markerscale=30)
# bar_width_ins = bar_width
# #axins = inset_axes(ax,width=2,height=2,loc=7)
# #Male_inset=axins.bar(np.arange(len(segment)),male_list,bar_width_ins,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='black',label='Male')
# #Female_inset=axins.bar(np.arange(len(segment))+bar_width_ins,female_list,bar_width_ins,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white',label='Female')
# #axins.set_xticks(np.arange(len(segment))+0.5*bar_width_ins)
# #axins.set_xticklabels(segment,fontsize=20)
# #axins.set_xlim(5-1.5*bar_width_ins,6+2*bar_width)
# #axins.set_ylim(0,2)
# #axins.tick_params(axis='both',labelsize=20)
# #autolabel(Male,'left')
# #autolabel(Female,'right')

#====================================================
# Water volume
#====================================================
female_delivery_number = []
female_delivery_sup = []
female_delivery_jux1 = []
female_delivery_jux2 = []
female_delivery_jux3 = []
female_delivery_jux4 = []
female_delivery_jux5 = []
for seg in segment_early:
    file_sup = open(female_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen_sup.txt','r')
    file_jux1 = open(female_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    for i in file_jux1:
        line = i.split(' ')
        datalist_jux1.append(float(line[0]))
    for i in file_jux2:
        line = i.split(' ')
        datalist_jux2.append(float(line[0]))
    for i in file_jux3:
        line = i.split(' ')
        datalist_jux3.append(float(line[0]))
    for i in file_jux4:
        line = i.split(' ')
        datalist_jux4.append(float(line[0]))
    for i in file_jux5:
        line = i.split(' ')
        datalist_jux5.append(float(line[0]))
    number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    female_delivery_number.append(0)
    female_delivery_sup.append(neph_weight[0]*datalist_sup[0]*volume_conversion)
    female_delivery_jux1.append(neph_weight[1]*datalist_jux1[0]*volume_conversion)
    female_delivery_jux2.append(neph_weight[2]*datalist_jux2[0]*volume_conversion)
    female_delivery_jux3.append(neph_weight[3]*datalist_jux3[0]*volume_conversion)
    female_delivery_jux4.append(neph_weight[4]*datalist_jux4[0]*volume_conversion)
    female_delivery_jux5.append(neph_weight[5]*datalist_jux5[0]*volume_conversion)
    if seg == 'cnt':
        female_delivery_number.append(0)
        female_delivery_sup.append(neph_weight[0]*datalist_sup[-1]*volume_conversion)
        female_delivery_jux1.append(neph_weight[1]*datalist_jux1[-1]*volume_conversion)
        female_delivery_jux2.append(neph_weight[2]*datalist_jux2[-1]*volume_conversion)
        female_delivery_jux3.append(neph_weight[3]*datalist_jux3[-1]*volume_conversion)
        female_delivery_jux4.append(neph_weight[4]*datalist_jux4[-1]*volume_conversion)
        female_delivery_jux5.append(neph_weight[5]*datalist_jux5[-1]*volume_conversion)
for seg in segment_late:
    file_data = open(female_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        female_delivery_number.append(number_of_delivery*volume_conversion)
    else:
        number_of_delivery = datalist[0]
        #female_delivery_number.append(number_of_delivery)

#=====================================================
#  Male
#=====================================================

male_delivery_number = []
male_delivery_sup = []
male_delivery_jux1 = []
male_delivery_jux2 = []
male_delivery_jux3 = []
male_delivery_jux4 = []
male_delivery_jux5 = []
for seg in segment_early:
    file_sup = open(male_normal_file+'/male_hum_'+seg+'_water_volume_in_Lumen_sup.txt','r')
    file_jux1 = open(male_normal_file+'/male_hum_'+seg+'_water_volume_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_normal_file+'/male_hum_'+seg+'_water_volume_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_normal_file+'/male_hum_'+seg+'_water_volume_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_normal_file+'/male_hum_'+seg+'_water_volume_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_normal_file+'/male_hum_'+seg+'_water_volume_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    for i in file_jux1:
        line = i.split(' ')
        datalist_jux1.append(float(line[0]))
    for i in file_jux2:
        line = i.split(' ')
        datalist_jux2.append(float(line[0]))
    for i in file_jux3:
        line = i.split(' ')
        datalist_jux3.append(float(line[0]))
    for i in file_jux4:
        line = i.split(' ')
        datalist_jux4.append(float(line[0]))
    for i in file_jux5:
        line = i.split(' ')
        datalist_jux5.append(float(line[0]))
    number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_delivery_number.append(0)
    male_delivery_sup.append(neph_weight[0]*datalist_sup[0]*volume_conversion)
    male_delivery_jux1.append(neph_weight[1]*datalist_jux1[0]*volume_conversion)
    male_delivery_jux2.append(neph_weight[2]*datalist_jux2[0]*volume_conversion)
    male_delivery_jux3.append(neph_weight[3]*datalist_jux3[0]*volume_conversion)
    male_delivery_jux4.append(neph_weight[4]*datalist_jux4[0]*volume_conversion)
    male_delivery_jux5.append(neph_weight[5]*datalist_jux5[0]*volume_conversion)
    if seg == 'cnt':
        male_delivery_number.append(0)
        male_delivery_sup.append(neph_weight[0]*datalist_sup[-1]*volume_conversion)
        male_delivery_jux1.append(neph_weight[1]*datalist_jux1[-1]*volume_conversion)
        male_delivery_jux2.append(neph_weight[2]*datalist_jux2[-1]*volume_conversion)
        male_delivery_jux3.append(neph_weight[3]*datalist_jux3[-1]*volume_conversion)
        male_delivery_jux4.append(neph_weight[4]*datalist_jux4[-1]*volume_conversion)
        male_delivery_jux5.append(neph_weight[5]*datalist_jux5[-1]*volume_conversion)
for seg in segment_late:
    file_data = open(male_normal_file+'/male_hum_'+seg+'_water_volume_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        male_delivery_number.append(number_of_delivery*volume_conversion)
    else:
        number_of_delivery = datalist[0]

    #===================================
    # NHE3 50% inhibited
    #===================================
female_delivery_number_nhe50 = []
female_delivery_sup_nhe50 = []
female_delivery_jux1_nhe50 = []
female_delivery_jux2_nhe50 = []
female_delivery_jux3_nhe50 = []
female_delivery_jux4_nhe50 = []
female_delivery_jux5_nhe50 = []
for seg in segment_early:
    file_sup = open(female_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen_sup.txt','r')
    file_jux1 = open(female_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    for i in file_jux1:
        line = i.split(' ')
        datalist_jux1.append(float(line[0]))
    for i in file_jux2:
        line = i.split(' ')
        datalist_jux2.append(float(line[0]))
    for i in file_jux3:
        line = i.split(' ')
        datalist_jux3.append(float(line[0]))
    for i in file_jux4:
        line = i.split(' ')
        datalist_jux4.append(float(line[0]))
    for i in file_jux5:
        line = i.split(' ')
        datalist_jux5.append(float(line[0]))
    number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    female_delivery_number_nhe50.append(0)
    female_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[0]*volume_conversion)
    female_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[0]*volume_conversion)
    female_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[0]*volume_conversion)
    female_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[0]*volume_conversion)
    female_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[0]*volume_conversion)
    female_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[0]*volume_conversion)
    if seg == 'cnt':
        female_delivery_number_nhe50.append(0)
        female_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[-1]*volume_conversion)
        female_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[-1]*volume_conversion)
        female_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[-1]*volume_conversion)
        female_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[-1]*volume_conversion)
        female_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[-1]*volume_conversion)
        female_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[-1]*volume_conversion)
for seg in segment_late:
    file_data = open(female_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        female_delivery_number_nhe50.append(number_of_delivery*volume_conversion)
    else:
        number_of_delivery = datalist[0]
    

male_delivery_number_nhe50 = []
male_delivery_sup_nhe50 = []
male_delivery_jux1_nhe50 = []
male_delivery_jux2_nhe50 = []
male_delivery_jux3_nhe50 = []
male_delivery_jux4_nhe50 = []
male_delivery_jux5_nhe50 = []
for seg in segment_early:
    file_sup = open(male_nhe50_file+'/male_hum_'+seg+'_water_volume_in_Lumen_sup.txt','r')
    file_jux1 = open(male_nhe50_file+'/male_hum_'+seg+'_water_volume_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe50_file+'/male_hum_'+seg+'_water_volume_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe50_file+'/male_hum_'+seg+'_water_volume_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe50_file+'/male_hum_'+seg+'_water_volume_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe50_file+'/male_hum_'+seg+'_water_volume_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    for i in file_sup:
        line = i.split(' ')
        datalist_sup.append(float(line[0]))
    for i in file_jux1:
        line = i.split(' ')
        datalist_jux1.append(float(line[0]))
    for i in file_jux2:
        line = i.split(' ')
        datalist_jux2.append(float(line[0]))
    for i in file_jux3:
        line = i.split(' ')
        datalist_jux3.append(float(line[0]))
    for i in file_jux4:
        line = i.split(' ')
        datalist_jux4.append(float(line[0]))
    for i in file_jux5:
        line = i.split(' ')
        datalist_jux5.append(float(line[0]))
    number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_delivery_number_nhe50.append(0)
    male_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[0]*volume_conversion)
    male_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[0]*volume_conversion)
    male_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[0]*volume_conversion)
    male_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[0]*volume_conversion)
    male_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[0]*volume_conversion)
    male_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[0]*volume_conversion)
    if seg == 'cnt':
        male_delivery_number_nhe50.append(0)
        male_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[-1]*volume_conversion)
        male_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[-1]*volume_conversion)
        male_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[-1]*volume_conversion)
        male_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[-1]*volume_conversion)
        male_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[-1]*volume_conversion)
        male_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[-1]*volume_conversion)
for seg in segment_late:
    file_data = open(male_nhe50_file+'/male_hum_'+seg+'_water_volume_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        male_delivery_number_nhe50.append(number_of_delivery*volume_conversion)
    else:
        number_of_delivery = datalist[0]


male_sup=axarr[2,1].bar(np.arange(len(segment[:6])),male_delivery_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Male')
male_jux=axarr[2,1].bar(np.arange(len(segment[:6])),[male_delivery_jux1[i]+male_delivery_jux2[i]+male_delivery_jux3[i]+male_delivery_jux4[i]+male_delivery_jux5[i] for i in range(len(male_delivery_sup))],bar_width,bottom=male_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later=axarr[2,1].bar(np.arange(len(segment)),male_delivery_number,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

male_sup_nhe50=axarr[2,1].bar(np.arange(len(segment[:6]))+bar_width,male_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue',label='Male')
male_jux_nhe50=axarr[2,1].bar(np.arange(len(segment[:6]))+bar_width,[male_delivery_jux1_nhe50[i]+male_delivery_jux2_nhe50[i]+male_delivery_jux3_nhe50[i]+male_delivery_jux4_nhe50[i]+male_delivery_jux5_nhe50[i] for i in range(len(male_delivery_sup_nhe50))],bar_width,bottom=male_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later_nhe50=axarr[2,1].bar(np.arange(len(segment))+bar_width,male_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

Female_sup=axarr[2,1].bar(np.arange(len(segment[:6]))+2*bar_width,female_delivery_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta',label='Female')
Female_jux=axarr[2,1].bar(np.arange(len(segment[:6]))+2*bar_width,[female_delivery_jux1[i]+female_delivery_jux2[i]+female_delivery_jux3[i]+female_delivery_jux4[i]+female_delivery_jux5[i] for i in range(len(female_delivery_sup))],bar_width,bottom=female_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white',label='Juxtamedullary')
Female_later=axarr[2,1].bar(np.arange(len(segment))+2*bar_width,female_delivery_number,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

Female_sup_nhe50=axarr[2,1].bar(np.arange(len(segment[:6]))+3*bar_width,female_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink',label='Female')
Female_jux_nhe50=axarr[2,1].bar(np.arange(len(segment[:6]))+3*bar_width,[female_delivery_jux1_nhe50[i]+female_delivery_jux2_nhe50[i]+female_delivery_jux3_nhe50[i]+female_delivery_jux4_nhe50[i]+female_delivery_jux5_nhe50[i] for i in range(len(female_delivery_sup_nhe50))],bar_width,bottom=female_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white',label='Juxtamedullary')
Female_later_nhe50=axarr[2,1].bar(np.arange(len(segment))+3*bar_width,female_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')

axarr[2,1].set_xticks(np.arange(len(segment))+1.5*bar_width)
axarr[2,1].set_xticklabels(segment,fontsize=30)
axarr[2,1].tick_params(axis='both',labelsize=30)
#ax.set_xlabel('Segment',fontsize=20)
axarr[2,1].set_ylabel('Volume delivery (L/Day)',fontsize=30)
#axarr[3,1].legend(fontsize=30,markerscale=30)

bar_width_ins = bar_width
axins = inset_axes(axarr[2,1],width=2.5,height=2.5,loc=7)

male_sup_inset=axins.bar(np.arange(len(segment[:6])),male_delivery_sup,bar_width_ins,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Male')
male_jux_inset=axins.bar(np.arange(len(segment[:6])),[male_delivery_jux1[i]+male_delivery_jux2[i]+male_delivery_jux3[i]+male_delivery_jux4[i]+male_delivery_jux5[i] for i in range(len(male_delivery_sup))],bar_width_ins,bottom=male_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later_inset=axins.bar(np.arange(len(segment)),male_delivery_number,bar_width_ins,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

male_sup_nhe50_inset=axins.bar(np.arange(len(segment[:6]))+bar_width_ins,male_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue',label='50% NHE3 inhib')
male_jux_nhe50_inset=axins.bar(np.arange(len(segment[:6]))+bar_width_ins,[male_delivery_jux1_nhe50[i]+male_delivery_jux2_nhe50[i]+male_delivery_jux3_nhe50[i]+male_delivery_jux4_nhe50[i]+male_delivery_jux5_nhe50[i] for i in range(len(male_delivery_sup_nhe50))],bar_width,bottom=male_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later_nhe50_inset=axins.bar(np.arange(len(segment))+bar_width_ins,male_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

Female_sup_inset=axins.bar(np.arange(len(segment[:6]))+2*bar_width_ins,female_delivery_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta',label='Baseline')
Female_jux_inset=axins.bar(np.arange(len(segment[:6]))+2*bar_width_ins,[female_delivery_jux1[i]+female_delivery_jux2[i]+female_delivery_jux3[i]+female_delivery_jux4[i]+female_delivery_jux5[i] for i in range(len(female_delivery_sup))],bar_width,bottom=female_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
Female_later_inset=axins.bar(np.arange(len(segment))+2*bar_width_ins,female_delivery_number,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

Female_sup_nhe50_inset=axins.bar(np.arange(len(segment[:6]))+3*bar_width,female_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink',label='50% NHE3 inhib')
Female_jux_nhe50_inset=axins.bar(np.arange(len(segment[:6]))+3*bar_width,[female_delivery_jux1_nhe50[i]+female_delivery_jux2_nhe50[i]+female_delivery_jux3_nhe50[i]+female_delivery_jux4_nhe50[i]+female_delivery_jux5_nhe50[i] for i in range(len(female_delivery_sup_nhe50))],bar_width,bottom=female_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
Female_later_nhe50_inset=axins.bar(np.arange(len(segment))+3*bar_width,female_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')


axins.set_xticks(np.arange(len(segment))+1.5*bar_width_ins)
axins.set_xticklabels(segment,fontsize=30)
axins.set_xlim(6-1.5*bar_width_ins,6+4*bar_width_ins)
axins.set_ylim(0,5)
axins.tick_params(axis='both',labelsize=30)



#fig.delaxes(axarr[2,2])
axarr[0,0].text(-1,axarr[0,0].get_ylim()[1],'A',size=40,weight='bold')
axarr[0,1].text(-1,axarr[0,1].get_ylim()[1],'B',size=40,weight='bold')
axarr[1,0].text(-1,axarr[1,0].get_ylim()[1],'C',size=40,weight='bold')
axarr[1,1].text(-1,axarr[1,1].get_ylim()[1],'D',size=40,weight='bold')
axarr[2,0].text(-1,axarr[2,0].get_ylim()[1],'E',size=40,weight='bold')
axarr[2,1].text(-1,axarr[2,1].get_ylim()[1],'F',size=40,weight='bold')
# axarr[3,0].text(-1,axarr[3,0].get_ylim()[1],'G',size=40,weight='bold')
# axarr[3,1].text(-1,axarr[3,1].get_ylim()[1],'H',size=40,weight='bold')

plt.subplots_adjust(wspace=0.21)
#plt.show()
plt.savefig('delivery_diabetic_men_women',bbox_inches='tight')