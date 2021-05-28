import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np
import os
import argparse

segment = ['PT','DL','mTAL','DCT','CNT','CCD','urine']

female_normal_file = './Female_hum_Severe_diab_N_unx'
female_nhe50_file = './SGLT2_Female_hum_Severe_diab_N_unx'
#female_nhe80_file = './female_nhe80_check'

male_normal_file = './Female_hum_Non_diab'
male_nhe50_file = './Female_hum_Moderate_diab_N_unx'
#male_nhe80_file = './male_nhe80_check'

neph_weight = [0.85,(0.15)*0.4,(0.15)*0.3,(0.15)*0.15,(0.15)*0.1,(0.15)*0.05]

solute = ['Na','K','Cl','HCO3','H2CO3','CO2','HPO4','H2PO4','urea','NH3','NH4','H','HCO2','H2CO2','glu']
segment_early = ['pt','s3','sdl','mtal','ctal','dct','cnt']
segment_jux = ['sdl','ldl','lal']
segment_late = ['ccd','omcd','imcd']
segment_transport = ['PT','DL','LAL','TAL','DCT','CNT','CD']

bar_width = 0.15
fig,axarr = plt.subplots(4,3,gridspec_kw={'width_ratios': [1,1,2]})
fig.set_figheight(50)
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
    file_sup = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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
    file_data = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
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
    file_sup = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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
    file_data = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
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
bar_width = 0.15

#print(segment[:6],male_delivery_sup)

male_sup=axarr[0,0].bar(np.arange(3),[0,male_delivery_sup[0]+male_delivery_jux1[0]+male_delivery_jux2[0]+male_delivery_jux3[0]+male_delivery_jux4[0]+male_delivery_jux5[0],0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Non-diabetic')
#male_jux=axarr[0,0].bar(np.arange(1),male_delivery_jux1[0]+male_delivery_jux2[0]+male_delivery_jux3[0]+male_delivery_jux4[0]+male_delivery_jux5[0],bar_width,bottom=male_delivery_sup[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')

male_sup_nhe50=axarr[0,0].bar(np.arange(3)+bar_width,[0,male_delivery_sup_nhe50[0]+male_delivery_jux1_nhe50[0]+male_delivery_jux2_nhe50[0]+male_delivery_jux3_nhe50[0]+male_delivery_jux4_nhe50[0]+male_delivery_jux5_nhe50[0],0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue',label='Diabetic,[Glu]=8.6mM')
# male_jux_nhe50=axarr[0,0].bar(np.arange(1)+bar_width,male_delivery_jux1_nhe50[0]+male_delivery_jux2_nhe50[0]+male_delivery_jux3_nhe50[0]+male_delivery_jux4_nhe50[0]+male_delivery_jux5_nhe50[0],bar_width,bottom=male_delivery_sup_nhe50[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# male_later_nhe50=axarr[0,0].bar(np.arange(2)+bar_width,[male_delivery_number_nhe50[0],male_delivery_number_nhe50[-1]],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

Female_sup=axarr[0,0].bar(np.arange(3)+2*bar_width,[0,female_delivery_sup[0]+female_delivery_jux1[0]+female_delivery_jux2[0]+female_delivery_jux3[0]+female_delivery_jux4[0]+female_delivery_jux5[0],0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta',label='Diabetic,[Glu]=20mM')
#Female_jux=axarr[0,0].bar(np.arange(1)+1*bar_width,female_delivery_jux1[0]+female_delivery_jux2[0]+female_delivery_jux3[0]+female_delivery_jux4[0]+female_delivery_jux5[0],bar_width,bottom=female_delivery_sup[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')

# Female_sup_nhe50=axarr[0,0].bar(np.arange(1)+3*bar_width,female_delivery_sup_nhe50[0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')
# Female_jux_nhe50=axarr[0,0].bar(np.arange(1)+3*bar_width,female_delivery_jux1_nhe50[0]+female_delivery_jux2_nhe50[0]+female_delivery_jux3_nhe50[0]+female_delivery_jux4_nhe50[0]+female_delivery_jux5_nhe50[0],bar_width,bottom=female_delivery_sup_nhe50[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# Female_later_nhe50=axarr[0,0].bar(np.arange(2)+3*bar_width,[female_delivery_number_nhe50[0],female_delivery_number_nhe50[-1]],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')
axarr[0,0].set_xticks(np.arange(3)+0.5*bar_width)
axarr[0,0].set_xticklabels(['','Filtered',''],fontsize=30)
axarr[0,0].tick_params(axis='both',labelsize=30)
#ax.set_xlabel('Segment',fontsize=20)
axarr[0,0].set_ylabel('Filtered Na$^+$ (mol/Day)',fontsize=30)
axarr[0,0].get_xaxis().set_visible(False)
#axarr[0,0].legend(fontsize=30,markerscale=30)

male_later=axarr[0,1].bar(np.arange(3),[male_delivery_number[0],male_delivery_number[-1],0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')
male_later_nhe50=axarr[0,1].bar(np.arange(3)+bar_width,[male_delivery_number_nhe50[0],male_delivery_number_nhe50[-1],0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')
Female_later=axarr[0,1].bar(np.arange(3)+2*bar_width,[female_delivery_number[0],female_delivery_number[-1],0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

axarr[0,1].set_xticks(np.arange(3)+0.5*bar_width)
axarr[0,1].set_xticklabels(['','Excretion',''],fontsize=30)
axarr[0,1].tick_params(axis='both',labelsize=30)
#ax.set_xlabel('Segment',fontsize=20)
axarr[0,1].set_ylabel('Na$^+$ excretion (mol/Day)',fontsize=30)
axarr[0,1].get_xaxis().set_visible(False)
axarr[0,1].set_ylim(0,0.15)
#axarr[0,1].legend(fontsize=30,markerscale=30)
# bar_width_ins = bar_width
# axins = inset_axes(axarr[0,0],width=2.5,height=2.5,loc=7)

# male_sup_inset=axins.bar(np.arange(1),male_delivery_sup[0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Baseline')
# male_jux_inset=axins.bar(np.arange(1),male_delivery_jux1[0]+male_delivery_jux2[0]+male_delivery_jux3[0]+male_delivery_jux4[0]+male_delivery_jux5[0],bar_width,bottom=male_delivery_sup[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# male_later_inset=axins.bar(np.arange(2),[male_delivery_number[0],male_delivery_number[-1]],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

# # male_sup_nhe50=axarr[0,0].bar(np.arange(1)+bar_width,male_delivery_sup_nhe50[0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue',label='Healthy, SGLT2i')
# # male_jux_nhe50=axarr[0,0].bar(np.arange(1)+bar_width,male_delivery_jux1_nhe50[0]+male_delivery_jux2_nhe50[0]+male_delivery_jux3_nhe50[0]+male_delivery_jux4_nhe50[0]+male_delivery_jux5_nhe50[0],bar_width,bottom=male_delivery_sup_nhe50[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# # male_later_nhe50=axarr[0,0].bar(np.arange(2)+bar_width,[male_delivery_number_nhe50[0],male_delivery_number_nhe50[-1]],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

# Female_sup_inset=axins.bar(np.arange(1)+1*bar_width,female_delivery_sup[0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')
# Female_jux_inset=axins.bar(np.arange(1)+1*bar_width,female_delivery_jux1[0]+female_delivery_jux2[0]+female_delivery_jux3[0]+female_delivery_jux4[0]+female_delivery_jux5[0],bar_width,bottom=female_delivery_sup[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# Female_later_inset=axins.bar(np.arange(2)+1*bar_width,[female_delivery_number[0],female_delivery_number[-1]],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

# # Female_sup_nhe50=axarr[0,0].bar(np.arange(1)+3*bar_width,female_delivery_sup_nhe50[0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')
# # Female_jux_nhe50=axarr[0,0].bar(np.arange(1)+3*bar_width,female_delivery_jux1_nhe50[0]+female_delivery_jux2_nhe50[0]+female_delivery_jux3_nhe50[0]+female_delivery_jux4_nhe50[0]+female_delivery_jux5_nhe50[0],bar_width,bottom=female_delivery_sup_nhe50[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# # Female_later_nhe50=axarr[0,0].bar(np.arange(2)+3*bar_width,[female_delivery_number_nhe50[0],female_delivery_number_nhe50[-1]],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')

# axins.set_xticks(np.arange(2)+0.5*bar_width_ins)
# axins.set_xticklabels(['Filtered','Excretion'],fontsize=30)
# axins.set_xlim(1-1*bar_width_ins,1+2*bar_width_ins)
# axins.set_ylim(0,0.2)
# axins.tick_params(axis='both',labelsize=30)

#==================================================================
# Na transport
#==================================================================

female_transport_number = []
female_transport_sup = []
female_transport_jux1 = []
female_transport_jux2 = []
female_transport_jux3 = []
female_transport_jux4 = []
female_transport_jux5 = []
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
    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    female_transport_number.append(0)
    female_transport_sup.append(solute_conversion*neph_weight[0]*(datalist_sup[0]-datalist_sup[-1]))
    female_transport_jux1.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    female_transport_jux2.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    female_transport_jux3.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    female_transport_jux4.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    female_transport_jux5.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))
for seg in segment_late:
    file_data = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
        number_of_transport = datalist[0]-datalist[-1]
    female_transport_number.append(solute_conversion*number_of_transport)

female_transport_number_reformed_sup = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux1 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux2 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux3 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux4 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux5 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed = [0 for _ in segment_transport]

female_transport_number_reformed[6] = female_transport_number[7]+female_transport_number[8]+female_transport_number[9]

female_transport_long_jux1 = []
female_transport_long_jux2 = []
female_transport_long_jux3 = []
female_transport_long_jux4 = []
female_transport_long_jux5 = []
for seg in segment_jux:
    file_jux1 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
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
    female_transport_long_jux1.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    female_transport_long_jux2.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    female_transport_long_jux3.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    female_transport_long_jux4.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    female_transport_long_jux5.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))

female_transport_number_reformed_sup[0] = female_transport_sup[0]+female_transport_sup[1]
female_transport_number_reformed_sup[1] = female_transport_sup[2]
female_transport_number_reformed_sup[3] = female_transport_sup[3]+female_transport_sup[4]
female_transport_number_reformed_sup[4] = female_transport_sup[5]
female_transport_number_reformed_sup[5] = female_transport_sup[6]

female_transport_number_reformed_jux1[0] = female_transport_jux1[0]+female_transport_jux1[1]
female_transport_number_reformed_jux1[1] = female_transport_long_jux1[0]+female_transport_long_jux1[1]
female_transport_number_reformed_jux1[2] = female_transport_long_jux1[2]
female_transport_number_reformed_jux1[3] = female_transport_jux1[3]+female_transport_jux1[4]
female_transport_number_reformed_jux1[4] = female_transport_jux1[5]
female_transport_number_reformed_jux1[5] = female_transport_jux1[6]

female_transport_number_reformed_jux2[0] = female_transport_jux2[0]+female_transport_jux2[1]
female_transport_number_reformed_jux2[1] = female_transport_long_jux2[0]+female_transport_long_jux2[1]
female_transport_number_reformed_jux2[2] = female_transport_long_jux2[2]
female_transport_number_reformed_jux2[3] = female_transport_jux2[3]+female_transport_jux2[4]
female_transport_number_reformed_jux2[4] = female_transport_jux2[5]
female_transport_number_reformed_jux2[5] = female_transport_jux2[6]

female_transport_number_reformed_jux3[0] = female_transport_jux3[0]+female_transport_jux3[1]
female_transport_number_reformed_jux3[1] = female_transport_long_jux3[0]+female_transport_long_jux3[1]
female_transport_number_reformed_jux3[2] = female_transport_long_jux3[2]
female_transport_number_reformed_jux3[3] = female_transport_jux3[3]+female_transport_jux3[4]
female_transport_number_reformed_jux3[4] = female_transport_jux3[5]
female_transport_number_reformed_jux3[5] = female_transport_jux3[6]

female_transport_number_reformed_jux4[0] = female_transport_jux4[0]+female_transport_jux4[1]
female_transport_number_reformed_jux4[1] = female_transport_long_jux4[0]+female_transport_long_jux4[1]
female_transport_number_reformed_jux4[2] = female_transport_long_jux4[2]
female_transport_number_reformed_jux4[3] = female_transport_jux4[3]+female_transport_jux4[4]
female_transport_number_reformed_jux4[4] = female_transport_jux4[5]
female_transport_number_reformed_jux4[5] = female_transport_jux4[6]

female_transport_number_reformed_jux5[0] = female_transport_jux5[0]+female_transport_jux5[1]
female_transport_number_reformed_jux5[1] = female_transport_long_jux5[0]+female_transport_long_jux5[1]
female_transport_number_reformed_jux5[2] = female_transport_long_jux5[2]
female_transport_number_reformed_jux5[3] = female_transport_jux5[3]+female_transport_jux5[4]
female_transport_number_reformed_jux5[4] = female_transport_jux5[5]
female_transport_number_reformed_jux5[5] = female_transport_jux5[6]

#==================================================================
# Male transport
#==================================================================

male_transport_number = []
male_transport_sup = []
male_transport_jux1 = []
male_transport_jux2 = []
male_transport_jux3 = []
male_transport_jux4 = []
male_transport_jux5 = []
for seg in segment_early:
    file_sup = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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
    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_transport_number.append(0)
    male_transport_sup.append(solute_conversion*neph_weight[0]*(datalist_sup[0]-datalist_sup[-1]))
    male_transport_jux1.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    male_transport_jux2.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    male_transport_jux3.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    male_transport_jux4.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    male_transport_jux5.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))
for seg in segment_late:
    file_data = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
        number_of_transport = datalist[0]-datalist[-1]
    male_transport_number.append(solute_conversion*number_of_transport)

male_transport_number_reformed_sup = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux1 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux2 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux3 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux4 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux5 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed = [0 for _ in segment_transport]

male_transport_number_reformed[6] = male_transport_number[7]+male_transport_number[8]+male_transport_number[9]

male_transport_long_jux1 = []
male_transport_long_jux2 = []
male_transport_long_jux3 = []
male_transport_long_jux4 = []
male_transport_long_jux5 = []
for seg in segment_jux:
    file_jux1 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
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
    male_transport_long_jux1.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    male_transport_long_jux2.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    male_transport_long_jux3.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    male_transport_long_jux4.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    male_transport_long_jux5.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))

male_transport_number_reformed_sup[0] = male_transport_sup[0]+male_transport_sup[1]
male_transport_number_reformed_sup[1] = male_transport_sup[2]
male_transport_number_reformed_sup[3] = male_transport_sup[3]+male_transport_sup[4]
male_transport_number_reformed_sup[4] = male_transport_sup[5]
male_transport_number_reformed_sup[5] = male_transport_sup[6]

male_transport_number_reformed_jux1[0] = male_transport_jux1[0]+male_transport_jux1[1]
male_transport_number_reformed_jux1[1] = male_transport_long_jux1[0]+male_transport_long_jux1[1]
male_transport_number_reformed_jux1[2] = male_transport_long_jux1[2]
male_transport_number_reformed_jux1[3] = male_transport_jux1[3]+male_transport_jux1[4]
male_transport_number_reformed_jux1[4] = male_transport_jux1[5]
male_transport_number_reformed_jux1[5] = male_transport_jux1[6]

male_transport_number_reformed_jux2[0] = male_transport_jux2[0]+male_transport_jux2[1]
male_transport_number_reformed_jux2[1] = male_transport_long_jux2[0]+male_transport_long_jux2[1]
male_transport_number_reformed_jux2[2] = male_transport_long_jux2[2]
male_transport_number_reformed_jux2[3] = male_transport_jux2[3]+male_transport_jux2[4]
male_transport_number_reformed_jux2[4] = male_transport_jux2[5]
male_transport_number_reformed_jux2[5] = male_transport_jux2[6]

male_transport_number_reformed_jux3[0] = male_transport_jux3[0]+male_transport_jux3[1]
male_transport_number_reformed_jux3[1] = male_transport_long_jux3[0]+male_transport_long_jux3[1]
male_transport_number_reformed_jux3[2] = male_transport_long_jux3[2]
male_transport_number_reformed_jux3[3] = male_transport_jux3[3]+male_transport_jux3[4]
male_transport_number_reformed_jux3[4] = male_transport_jux3[5]
male_transport_number_reformed_jux3[5] = male_transport_jux3[6]

male_transport_number_reformed_jux4[0] = male_transport_jux4[0]+male_transport_jux4[1]
male_transport_number_reformed_jux4[1] = male_transport_long_jux4[0]+male_transport_long_jux4[1]
male_transport_number_reformed_jux4[2] = male_transport_long_jux4[2]
male_transport_number_reformed_jux4[3] = male_transport_jux4[3]+male_transport_jux4[4]
male_transport_number_reformed_jux4[4] = male_transport_jux4[5]
male_transport_number_reformed_jux4[5] = male_transport_jux4[6]

male_transport_number_reformed_jux5[0] = male_transport_jux5[0]+male_transport_jux5[1]
male_transport_number_reformed_jux5[1] = male_transport_long_jux5[0]+male_transport_long_jux5[1]
male_transport_number_reformed_jux5[2] = male_transport_long_jux5[2]
male_transport_number_reformed_jux5[3] = male_transport_jux5[3]+male_transport_jux5[4]
male_transport_number_reformed_jux5[4] = male_transport_jux5[5]
male_transport_number_reformed_jux5[5] = male_transport_jux5[6]

male_transport_number_nhe50 = []
male_transport_sup_nhe50 = []
male_transport_jux1_nhe50 = []
male_transport_jux2_nhe50 = []
male_transport_jux3_nhe50 = []
male_transport_jux4_nhe50 = []
male_transport_jux5_nhe50 = []
for seg in segment_early:
    file_sup = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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
    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_transport_number_nhe50.append(0)
    male_transport_sup_nhe50.append(solute_conversion*neph_weight[0]*(datalist_sup[0]-datalist_sup[-1]))
    male_transport_jux1_nhe50.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    male_transport_jux2_nhe50.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    male_transport_jux3_nhe50.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    male_transport_jux4_nhe50.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    male_transport_jux5_nhe50.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))
for seg in segment_late:
    file_data = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
        number_of_transport = datalist[0]-datalist[-1]
    male_transport_number_nhe50.append(solute_conversion*number_of_transport)

male_transport_number_reformed_sup_nhe50 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux1_nhe50 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux2_nhe50 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux3_nhe50 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux4_nhe50 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux5_nhe50 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_nhe50 = [0 for _ in segment_transport]

male_transport_number_reformed_nhe50[6] = male_transport_number_nhe50[7]+male_transport_number_nhe50[8]+male_transport_number_nhe50[9]

male_transport_long_jux1_nhe50 = []
male_transport_long_jux2_nhe50 = []
male_transport_long_jux3_nhe50 = []
male_transport_long_jux4_nhe50 = []
male_transport_long_jux5_nhe50 = []
for seg in segment_jux:
    file_jux1 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
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
    male_transport_long_jux1_nhe50.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    male_transport_long_jux2_nhe50.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    male_transport_long_jux3_nhe50.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    male_transport_long_jux4_nhe50.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    male_transport_long_jux5_nhe50.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))

male_transport_number_reformed_sup_nhe50[0] = male_transport_sup_nhe50[0]+male_transport_sup_nhe50[1]
male_transport_number_reformed_sup_nhe50[1] = male_transport_sup_nhe50[2]
male_transport_number_reformed_sup_nhe50[3] = male_transport_sup_nhe50[3]+male_transport_sup_nhe50[4]
male_transport_number_reformed_sup_nhe50[4] = male_transport_sup_nhe50[5]
male_transport_number_reformed_sup_nhe50[5] = male_transport_sup_nhe50[6]

male_transport_number_reformed_jux1_nhe50[0] = male_transport_jux1_nhe50[0]+male_transport_jux1_nhe50[1]
male_transport_number_reformed_jux1_nhe50[1] = male_transport_long_jux1_nhe50[0]+male_transport_long_jux1_nhe50[1]
male_transport_number_reformed_jux1_nhe50[2] = male_transport_long_jux1_nhe50[2]
male_transport_number_reformed_jux1_nhe50[3] = male_transport_jux1_nhe50[3]+male_transport_jux1_nhe50[4]
male_transport_number_reformed_jux1_nhe50[4] = male_transport_jux1_nhe50[5]
male_transport_number_reformed_jux1_nhe50[5] = male_transport_jux1_nhe50[6]

male_transport_number_reformed_jux2_nhe50[0] = male_transport_jux2_nhe50[0]+male_transport_jux2_nhe50[1]
male_transport_number_reformed_jux2_nhe50[1] = male_transport_long_jux2_nhe50[0]+male_transport_long_jux2_nhe50[1]
male_transport_number_reformed_jux2_nhe50[2] = male_transport_long_jux2_nhe50[2]
male_transport_number_reformed_jux2_nhe50[3] = male_transport_jux2_nhe50[3]+male_transport_jux2_nhe50[4]
male_transport_number_reformed_jux2_nhe50[4] = male_transport_jux2_nhe50[5]
male_transport_number_reformed_jux2_nhe50[5] = male_transport_jux2_nhe50[6]

male_transport_number_reformed_jux3_nhe50[0] = male_transport_jux3_nhe50[0]+male_transport_jux3_nhe50[1]
male_transport_number_reformed_jux3_nhe50[1] = male_transport_long_jux3_nhe50[0]+male_transport_long_jux3_nhe50[1]
male_transport_number_reformed_jux3_nhe50[2] = male_transport_long_jux3_nhe50[2]
male_transport_number_reformed_jux3_nhe50[3] = male_transport_jux3_nhe50[3]+male_transport_jux3_nhe50[4]
male_transport_number_reformed_jux3_nhe50[4] = male_transport_jux3_nhe50[5]
male_transport_number_reformed_jux3_nhe50[5] = male_transport_jux3_nhe50[6]

male_transport_number_reformed_jux4_nhe50[0] = male_transport_jux4_nhe50[0]+male_transport_jux4_nhe50[1]
male_transport_number_reformed_jux4_nhe50[1] = male_transport_long_jux4_nhe50[0]+male_transport_long_jux4_nhe50[1]
male_transport_number_reformed_jux4_nhe50[2] = male_transport_long_jux4_nhe50[2]
male_transport_number_reformed_jux4_nhe50[3] = male_transport_jux4_nhe50[3]+male_transport_jux4_nhe50[4]
male_transport_number_reformed_jux4_nhe50[4] = male_transport_jux4_nhe50[5]
male_transport_number_reformed_jux4_nhe50[5] = male_transport_jux4_nhe50[6]

male_transport_number_reformed_jux5_nhe50[0] = male_transport_jux5_nhe50[0]+male_transport_jux5_nhe50[1]
male_transport_number_reformed_jux5_nhe50[1] = male_transport_long_jux5_nhe50[0]+male_transport_long_jux5_nhe50[1]
male_transport_number_reformed_jux5_nhe50[2] = male_transport_long_jux5_nhe50[2]
male_transport_number_reformed_jux5_nhe50[3] = male_transport_jux5_nhe50[3]+male_transport_jux5_nhe50[4]
male_transport_number_reformed_jux5_nhe50[4] = male_transport_jux5_nhe50[5]
male_transport_number_reformed_jux5_nhe50[5] = male_transport_jux5_nhe50[6]

#print(segment_transport,male_transport_number)
bar_width = 0.25
male_sup=axarr[0,2].bar(np.arange(len(segment_transport[:6])),[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i]+male_transport_number_reformed_jux5[i] for i in range(len(male_transport_number_reformed_sup))],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Non-diabetic women')
#male_jux=axarr[0,1].bar(np.arange(len(segment_transport[:6])),[male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i]+male_transport_number_reformed_jux5[i] for i in range(len(male_transport_number_reformed_sup))],bar_width,bottom=male_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
#male_jux2=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux2,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='cyan',label='Male juxtamedullary type 2')
#male_jux3=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux3,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='darkturquoise',label='Male juxtamedullary type 3')
#male_jux4=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux4,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='powderblue',label='Male juxtamedullary type 4')
#male_jux5=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux5,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='deepskyblue',label='Male juxtamedullary type 5')
male_later=axarr[0,2].bar(np.arange(len(segment_transport)),male_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

male_sup_nhe50=axarr[0,2].bar(np.arange(len(segment_transport[:6]))+bar_width,[male_transport_number_reformed_sup_nhe50[i]+male_transport_number_reformed_jux1_nhe50[i]+male_transport_number_reformed_jux2_nhe50[i]+male_transport_number_reformed_jux3_nhe50[i]+male_transport_number_reformed_jux4_nhe50[i]+male_transport_number_reformed_jux5_nhe50[i] for i in range(len(male_transport_number_reformed_sup_nhe50))],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue',label='Moderate diabetes women')
#male_jux=axarr[0,1].bar(np.arange(len(segment_transport[:6])),[male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i]+male_transport_number_reformed_jux5[i] for i in range(len(male_transport_number_reformed_sup))],bar_width,bottom=male_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
#male_jux2=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux2,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='cyan',label='Male juxtamedullary type 2')
#male_jux3=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux3,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='darkturquoise',label='Male juxtamedullary type 3')
#male_jux4=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux4,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='powderblue',label='Male juxtamedullary type 4')
#male_jux5=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux5,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='deepskyblue',label='Male juxtamedullary type 5')
male_later_nhe50=axarr[0,2].bar(np.arange(len(segment_transport))+bar_width,male_transport_number_reformed_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')


Female_sup=axarr[0,2].bar(np.arange(len(segment_transport[:6]))+2*bar_width,[female_transport_number_reformed_sup[i]+female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i]+female_transport_number_reformed_jux3[i]+female_transport_number_reformed_jux4[i]+female_transport_number_reformed_jux5[i] for i in range(len(female_transport_number_reformed_sup))],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta',label='Severe diabetes women')
#Female_jux=axarr[0,1].bar(np.arange(len(segment_transport[:6]))+bar_width,[female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i]+female_transport_number_reformed_jux3[i]+female_transport_number_reformed_jux4[i]+female_transport_number_reformed_jux5[i] for i in range(len(female_transport_number_reformed_sup))],bar_width,bottom=female_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
#Female_jux2=ax.bar(np.arange(len(segment_transport[:4]))+bar_width,female_transport_number_reformed_jux2,bar_width,bottom=[female_transport_number_reformed_sup[i]+female_transport_number_reformed_jux1[i] for i in range(len(female_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='violet',label='Female juxtamedullary type 2')
#Female_jux3=ax.bar(np.arange(len(segment_transport[:4]))+bar_width,female_transport_number_reformed_jux3,bar_width,bottom=[female_transport_number_reformed_sup[i]+female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i] for i in range(len(female_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='crimson',label='Female juxtamedullary type 3')
#Female_jux4=ax.bar(np.arange(len(segment_transport[:4]))+bar_width,female_transport_number_reformed_jux4,bar_width,bottom=[female_transport_number_reformed_sup[i]+female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i]+female_transport_number_reformed_jux3[i] for i in range(len(female_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='lavenderblush',label='Female juxtamedullary type 4')
#Female_jux5=ax.bar(np.arange(len(segment_transport[:4]))+bar_width,female_transport_number_reformed_jux5,bar_width,bottom=[female_transport_number_reformed_sup[i]+female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i]+female_transport_number_reformed_jux3[i]+female_transport_number_reformed_jux4[i] for i in range(len(female_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='deeppink',label='Female juxtamedullary type 5')
Female_later=axarr[0,2].bar(np.arange(len(segment_transport))+2*bar_width,female_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

axarr[0,2].set_xticks(np.arange(len(segment_transport))+1*bar_width)
axarr[0,2].set_xticklabels(segment_transport,fontsize=30)
axarr[0,2].tick_params(axis='both',labelsize=30)
#ax.set_xlabel('Segment',fontsize=20)
axarr[0,2].set_ylabel('Segmental Na$^+$ transport (mol/Day)',fontsize=30)
axarr[0,2].legend(fontsize=30,markerscale=30)

bar_width_ins = bar_width
axins = inset_axes(axarr[0,2],width=2.5,height=2.5,loc=7)

male_sup_inset=axins.bar(np.arange(len(segment_transport[:6])),[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i]+male_transport_number_reformed_jux5[i] for i in range(len(male_transport_number_reformed_sup))],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Male')
#male_jux_inset=axins.bar(np.arange(len(segment_transport[:6])),[male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i]+male_transport_number_reformed_jux5[i] for i in range(len(male_transport_number_reformed_sup))],bar_width,bottom=male_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
male_later_inset=axins.bar(np.arange(len(segment_transport)),male_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

male_sup_nhe50_inset=axins.bar(np.arange(len(segment_transport[:6]))+bar_width,[male_transport_number_reformed_sup_nhe50[i]+male_transport_number_reformed_jux1_nhe50[i]+male_transport_number_reformed_jux2_nhe50[i]+male_transport_number_reformed_jux3_nhe50[i]+male_transport_number_reformed_jux4_nhe50[i]+male_transport_number_reformed_jux5_nhe50[i] for i in range(len(male_transport_number_reformed_sup))],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue',label='Male')
#male_jux_inset=axins.bar(np.arange(len(segment_transport[:6])),[male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i]+male_transport_number_reformed_jux5[i] for i in range(len(male_transport_number_reformed_sup))],bar_width,bottom=male_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
male_later_nhe50_inset=axins.bar(np.arange(len(segment_transport))+bar_width,male_transport_number_reformed_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

Female_sup_inset=axins.bar(np.arange(len(segment_transport[:6]))+2*bar_width,[female_transport_number_reformed_sup[i]+female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i]+female_transport_number_reformed_jux3[i]+female_transport_number_reformed_jux4[i]+female_transport_number_reformed_jux5[i] for i in range(len(female_transport_number_reformed_sup))],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta',label='Female')
#Female_jux_inset=axins.bar(np.arange(len(segment_transport[:6]))+bar_width,[female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i]+female_transport_number_reformed_jux3[i]+female_transport_number_reformed_jux4[i]+female_transport_number_reformed_jux5[i] for i in range(len(female_transport_number_reformed_sup))],bar_width,bottom=female_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
Female_later_inset=axins.bar(np.arange(len(segment_transport))+2*bar_width,female_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

axins.set_xticks(np.arange(len(segment_transport))+1*bar_width_ins)
axins.set_xticklabels(segment_transport,fontsize=30)
axins.set_xlim(5-1.5*bar_width_ins,6+3*bar_width_ins)
axins.set_ylim(0,0.3)
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
    file_sup = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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
    file_data = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
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
    file_sup = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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
    file_data = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
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
bar_width = 0.15

#print(segment[:6],male_delivery_sup)

male_sup=axarr[1,0].bar(np.arange(3),[0,male_delivery_sup[0]+male_delivery_jux1[0]+male_delivery_jux2[0]+male_delivery_jux3[0]+male_delivery_jux4[0]+male_delivery_jux5[0],0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Non-diabetic')
#male_jux=axarr[0,0].bar(np.arange(1),male_delivery_jux1[0]+male_delivery_jux2[0]+male_delivery_jux3[0]+male_delivery_jux4[0]+male_delivery_jux5[0],bar_width,bottom=male_delivery_sup[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')

male_sup_nhe50=axarr[1,0].bar(np.arange(3)+bar_width,[0,male_delivery_sup_nhe50[0]+male_delivery_jux1_nhe50[0]+male_delivery_jux2_nhe50[0]+male_delivery_jux3_nhe50[0]+male_delivery_jux4_nhe50[0]+male_delivery_jux5_nhe50[0],0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue',label='Diabetic,[Glu]=8.6mM')
# male_jux_nhe50=axarr[0,0].bar(np.arange(1)+bar_width,male_delivery_jux1_nhe50[0]+male_delivery_jux2_nhe50[0]+male_delivery_jux3_nhe50[0]+male_delivery_jux4_nhe50[0]+male_delivery_jux5_nhe50[0],bar_width,bottom=male_delivery_sup_nhe50[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# male_later_nhe50=axarr[0,0].bar(np.arange(2)+bar_width,[male_delivery_number_nhe50[0],male_delivery_number_nhe50[-1]],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

Female_sup=axarr[1,0].bar(np.arange(3)+2*bar_width,[0,female_delivery_sup[0]+female_delivery_jux1[0]+female_delivery_jux2[0]+female_delivery_jux3[0]+female_delivery_jux4[0]+female_delivery_jux5[0],0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta',label='Diabetic')
#Female_jux=axarr[0,0].bar(np.arange(1)+1*bar_width,female_delivery_jux1[0]+female_delivery_jux2[0]+female_delivery_jux3[0]+female_delivery_jux4[0]+female_delivery_jux5[0],bar_width,bottom=female_delivery_sup[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')

# Female_sup_nhe50=axarr[0,0].bar(np.arange(1)+3*bar_width,female_delivery_sup_nhe50[0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')
# Female_jux_nhe50=axarr[0,0].bar(np.arange(1)+3*bar_width,female_delivery_jux1_nhe50[0]+female_delivery_jux2_nhe50[0]+female_delivery_jux3_nhe50[0]+female_delivery_jux4_nhe50[0]+female_delivery_jux5_nhe50[0],bar_width,bottom=female_delivery_sup_nhe50[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# Female_later_nhe50=axarr[0,0].bar(np.arange(2)+3*bar_width,[female_delivery_number_nhe50[0],female_delivery_number_nhe50[-1]],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')
axarr[1,0].set_xticks(np.arange(3)+0.5*bar_width)
axarr[1,0].set_xticklabels(['','Filtered',''],fontsize=30)
axarr[1,0].tick_params(axis='both',labelsize=30)
#ax.set_xlabel('Segment',fontsize=20)
axarr[1,0].set_ylabel('Filtered K$^+$ (mol/Day)',fontsize=30)
axarr[1,0].get_xaxis().set_visible(False)
#axarr[0,0].legend(fontsize=30,markerscale=30)

male_later=axarr[1,1].bar(np.arange(3),[male_delivery_number[0],male_delivery_number[-1],0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')
male_later_nhe50=axarr[1,1].bar(np.arange(3)+bar_width,[male_delivery_number_nhe50[0],male_delivery_number_nhe50[-1],0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')
Female_later=axarr[1,1].bar(np.arange(3)+2*bar_width,[female_delivery_number[0],female_delivery_number[-1],0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

axarr[1,1].set_xticks(np.arange(3)+0.5*bar_width)
axarr[1,1].set_xticklabels(['','Excretion',''],fontsize=30)
axarr[1,1].tick_params(axis='both',labelsize=30)
#ax.set_xlabel('Segment',fontsize=20)
axarr[1,1].set_ylabel('K$^+$ excretion (mol/Day)',fontsize=30)
axarr[1,1].get_xaxis().set_visible(False)

# bar_width_ins = bar_width
# axins = inset_axes(axarr[1,0],width=2.5,height=2.5,loc=7)

# male_sup_inset=axins.bar(np.arange(1),male_delivery_sup[0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Baseline')
# male_jux_inset=axins.bar(np.arange(1),male_delivery_jux1[0]+male_delivery_jux2[0]+male_delivery_jux3[0]+male_delivery_jux4[0]+male_delivery_jux5[0],bar_width,bottom=male_delivery_sup[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# male_later_inset=axins.bar(np.arange(2),[male_delivery_number[0],male_delivery_number[-1]],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

# # male_sup_nhe50=axarr[0,0].bar(np.arange(1)+bar_width,male_delivery_sup_nhe50[0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue',label='Healthy, SGLT2i')
# # male_jux_nhe50=axarr[0,0].bar(np.arange(1)+bar_width,male_delivery_jux1_nhe50[0]+male_delivery_jux2_nhe50[0]+male_delivery_jux3_nhe50[0]+male_delivery_jux4_nhe50[0]+male_delivery_jux5_nhe50[0],bar_width,bottom=male_delivery_sup_nhe50[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# # male_later_nhe50=axarr[0,0].bar(np.arange(2)+bar_width,[male_delivery_number_nhe50[0],male_delivery_number_nhe50[-1]],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

# Female_sup_inset=axins.bar(np.arange(1)+1*bar_width,female_delivery_sup[0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')
# Female_jux_inset=axins.bar(np.arange(1)+1*bar_width,female_delivery_jux1[0]+female_delivery_jux2[0]+female_delivery_jux3[0]+female_delivery_jux4[0]+female_delivery_jux5[0],bar_width,bottom=female_delivery_sup[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# Female_later_inset=axins.bar(np.arange(2)+1*bar_width,[female_delivery_number[0],female_delivery_number[-1]],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

# # Female_sup_nhe50=axarr[0,0].bar(np.arange(1)+3*bar_width,female_delivery_sup_nhe50[0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')
# # Female_jux_nhe50=axarr[0,0].bar(np.arange(1)+3*bar_width,female_delivery_jux1_nhe50[0]+female_delivery_jux2_nhe50[0]+female_delivery_jux3_nhe50[0]+female_delivery_jux4_nhe50[0]+female_delivery_jux5_nhe50[0],bar_width,bottom=female_delivery_sup_nhe50[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# # Female_later_nhe50=axarr[0,0].bar(np.arange(2)+3*bar_width,[female_delivery_number_nhe50[0],female_delivery_number_nhe50[-1]],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')

# axins.set_xticks(np.arange(2)+0.5*bar_width_ins)
# axins.set_xticklabels(['Filtered','Excretion'],fontsize=30)
# axins.set_xlim(1-1*bar_width_ins,1+2*bar_width_ins)
# axins.set_ylim(0,0.2)
# axins.tick_params(axis='both',labelsize=30)

#==================================================================
# K transport
#==================================================================

female_transport_number = []
female_transport_sup = []
female_transport_jux1 = []
female_transport_jux2 = []
female_transport_jux3 = []
female_transport_jux4 = []
female_transport_jux5 = []
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
    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    female_transport_number.append(0)
    female_transport_sup.append(solute_conversion*neph_weight[0]*(datalist_sup[0]-datalist_sup[-1]))
    female_transport_jux1.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    female_transport_jux2.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    female_transport_jux3.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    female_transport_jux4.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    female_transport_jux5.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))
for seg in segment_late:
    file_data = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
        number_of_transport = datalist[0]-datalist[-1]
    female_transport_number.append(solute_conversion*number_of_transport)

female_transport_number_reformed_sup = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux1 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux2 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux3 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux4 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux5 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed = [0 for _ in segment_transport]

female_transport_number_reformed[6] = female_transport_number[7]+female_transport_number[8]+female_transport_number[9]

female_transport_long_jux1 = []
female_transport_long_jux2 = []
female_transport_long_jux3 = []
female_transport_long_jux4 = []
female_transport_long_jux5 = []
for seg in segment_jux:
    file_jux1 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
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
    female_transport_long_jux1.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    female_transport_long_jux2.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    female_transport_long_jux3.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    female_transport_long_jux4.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    female_transport_long_jux5.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))

female_transport_number_reformed_sup[0] = female_transport_sup[0]+female_transport_sup[1]
female_transport_number_reformed_sup[1] = female_transport_sup[2]
female_transport_number_reformed_sup[3] = female_transport_sup[3]+female_transport_sup[4]
female_transport_number_reformed_sup[4] = female_transport_sup[5]
female_transport_number_reformed_sup[5] = female_transport_sup[6]

female_transport_number_reformed_jux1[0] = female_transport_jux1[0]+female_transport_jux1[1]
female_transport_number_reformed_jux1[1] = female_transport_long_jux1[0]+female_transport_long_jux1[1]
female_transport_number_reformed_jux1[2] = female_transport_long_jux1[2]
female_transport_number_reformed_jux1[3] = female_transport_jux1[3]+female_transport_jux1[4]
female_transport_number_reformed_jux1[4] = female_transport_jux1[5]
female_transport_number_reformed_jux1[5] = female_transport_jux1[6]

female_transport_number_reformed_jux2[0] = female_transport_jux2[0]+female_transport_jux2[1]
female_transport_number_reformed_jux2[1] = female_transport_long_jux2[0]+female_transport_long_jux2[1]
female_transport_number_reformed_jux2[2] = female_transport_long_jux2[2]
female_transport_number_reformed_jux2[3] = female_transport_jux2[3]+female_transport_jux2[4]
female_transport_number_reformed_jux2[4] = female_transport_jux2[5]
female_transport_number_reformed_jux2[5] = female_transport_jux2[6]

female_transport_number_reformed_jux3[0] = female_transport_jux3[0]+female_transport_jux3[1]
female_transport_number_reformed_jux3[1] = female_transport_long_jux3[0]+female_transport_long_jux3[1]
female_transport_number_reformed_jux3[2] = female_transport_long_jux3[2]
female_transport_number_reformed_jux3[3] = female_transport_jux3[3]+female_transport_jux3[4]
female_transport_number_reformed_jux3[4] = female_transport_jux3[5]
female_transport_number_reformed_jux3[5] = female_transport_jux3[6]

female_transport_number_reformed_jux4[0] = female_transport_jux4[0]+female_transport_jux4[1]
female_transport_number_reformed_jux4[1] = female_transport_long_jux4[0]+female_transport_long_jux4[1]
female_transport_number_reformed_jux4[2] = female_transport_long_jux4[2]
female_transport_number_reformed_jux4[3] = female_transport_jux4[3]+female_transport_jux4[4]
female_transport_number_reformed_jux4[4] = female_transport_jux4[5]
female_transport_number_reformed_jux4[5] = female_transport_jux4[6]

female_transport_number_reformed_jux5[0] = female_transport_jux5[0]+female_transport_jux5[1]
female_transport_number_reformed_jux5[1] = female_transport_long_jux5[0]+female_transport_long_jux5[1]
female_transport_number_reformed_jux5[2] = female_transport_long_jux5[2]
female_transport_number_reformed_jux5[3] = female_transport_jux5[3]+female_transport_jux5[4]
female_transport_number_reformed_jux5[4] = female_transport_jux5[5]
female_transport_number_reformed_jux5[5] = female_transport_jux5[6]

#==================================================================
# Male transport
#==================================================================

male_transport_number = []
male_transport_sup = []
male_transport_jux1 = []
male_transport_jux2 = []
male_transport_jux3 = []
male_transport_jux4 = []
male_transport_jux5 = []
for seg in segment_early:
    file_sup = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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
    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_transport_number.append(0)
    male_transport_sup.append(solute_conversion*neph_weight[0]*(datalist_sup[0]-datalist_sup[-1]))
    male_transport_jux1.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    male_transport_jux2.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    male_transport_jux3.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    male_transport_jux4.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    male_transport_jux5.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))
for seg in segment_late:
    file_data = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
        number_of_transport = datalist[0]-datalist[-1]
    male_transport_number.append(solute_conversion*number_of_transport)

male_transport_number_reformed_sup = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux1 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux2 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux3 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux4 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux5 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed = [0 for _ in segment_transport]

male_transport_number_reformed[6] = male_transport_number[7]+male_transport_number[8]+male_transport_number[9]

male_transport_long_jux1 = []
male_transport_long_jux2 = []
male_transport_long_jux3 = []
male_transport_long_jux4 = []
male_transport_long_jux5 = []
for seg in segment_jux:
    file_jux1 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
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
    male_transport_long_jux1.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    male_transport_long_jux2.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    male_transport_long_jux3.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    male_transport_long_jux4.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    male_transport_long_jux5.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))

male_transport_number_reformed_sup[0] = male_transport_sup[0]+male_transport_sup[1]
male_transport_number_reformed_sup[1] = male_transport_sup[2]
male_transport_number_reformed_sup[3] = male_transport_sup[3]+male_transport_sup[4]
male_transport_number_reformed_sup[4] = male_transport_sup[5]
male_transport_number_reformed_sup[5] = male_transport_sup[6]

male_transport_number_reformed_jux1[0] = male_transport_jux1[0]+male_transport_jux1[1]
male_transport_number_reformed_jux1[1] = male_transport_long_jux1[0]+male_transport_long_jux1[1]
male_transport_number_reformed_jux1[2] = male_transport_long_jux1[2]
male_transport_number_reformed_jux1[3] = male_transport_jux1[3]+male_transport_jux1[4]
male_transport_number_reformed_jux1[4] = male_transport_jux1[5]
male_transport_number_reformed_jux1[5] = male_transport_jux1[6]

male_transport_number_reformed_jux2[0] = male_transport_jux2[0]+male_transport_jux2[1]
male_transport_number_reformed_jux2[1] = male_transport_long_jux2[0]+male_transport_long_jux2[1]
male_transport_number_reformed_jux2[2] = male_transport_long_jux2[2]
male_transport_number_reformed_jux2[3] = male_transport_jux2[3]+male_transport_jux2[4]
male_transport_number_reformed_jux2[4] = male_transport_jux2[5]
male_transport_number_reformed_jux2[5] = male_transport_jux2[6]

male_transport_number_reformed_jux3[0] = male_transport_jux3[0]+male_transport_jux3[1]
male_transport_number_reformed_jux3[1] = male_transport_long_jux3[0]+male_transport_long_jux3[1]
male_transport_number_reformed_jux3[2] = male_transport_long_jux3[2]
male_transport_number_reformed_jux3[3] = male_transport_jux3[3]+male_transport_jux3[4]
male_transport_number_reformed_jux3[4] = male_transport_jux3[5]
male_transport_number_reformed_jux3[5] = male_transport_jux3[6]

male_transport_number_reformed_jux4[0] = male_transport_jux4[0]+male_transport_jux4[1]
male_transport_number_reformed_jux4[1] = male_transport_long_jux4[0]+male_transport_long_jux4[1]
male_transport_number_reformed_jux4[2] = male_transport_long_jux4[2]
male_transport_number_reformed_jux4[3] = male_transport_jux4[3]+male_transport_jux4[4]
male_transport_number_reformed_jux4[4] = male_transport_jux4[5]
male_transport_number_reformed_jux4[5] = male_transport_jux4[6]

male_transport_number_reformed_jux5[0] = male_transport_jux5[0]+male_transport_jux5[1]
male_transport_number_reformed_jux5[1] = male_transport_long_jux5[0]+male_transport_long_jux5[1]
male_transport_number_reformed_jux5[2] = male_transport_long_jux5[2]
male_transport_number_reformed_jux5[3] = male_transport_jux5[3]+male_transport_jux5[4]
male_transport_number_reformed_jux5[4] = male_transport_jux5[5]
male_transport_number_reformed_jux5[5] = male_transport_jux5[6]

male_transport_number_nhe50 = []
male_transport_sup_nhe50 = []
male_transport_jux1_nhe50 = []
male_transport_jux2_nhe50 = []
male_transport_jux3_nhe50 = []
male_transport_jux4_nhe50 = []
male_transport_jux5_nhe50 = []
for seg in segment_early:
    file_sup = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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
    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_transport_number_nhe50.append(0)
    male_transport_sup_nhe50.append(solute_conversion*neph_weight[0]*(datalist_sup[0]-datalist_sup[-1]))
    male_transport_jux1_nhe50.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    male_transport_jux2_nhe50.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    male_transport_jux3_nhe50.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    male_transport_jux4_nhe50.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    male_transport_jux5_nhe50.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))
for seg in segment_late:
    file_data = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
        number_of_transport = datalist[0]-datalist[-1]
    male_transport_number_nhe50.append(solute_conversion*number_of_transport)

male_transport_number_reformed_sup_nhe50 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux1_nhe50 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux2_nhe50 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux3_nhe50 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux4_nhe50 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux5_nhe50 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_nhe50 = [0 for _ in segment_transport]

male_transport_number_reformed_nhe50[6] = male_transport_number_nhe50[7]+male_transport_number_nhe50[8]+male_transport_number_nhe50[9]

male_transport_long_jux1_nhe50 = []
male_transport_long_jux2_nhe50 = []
male_transport_long_jux3_nhe50 = []
male_transport_long_jux4_nhe50 = []
male_transport_long_jux5_nhe50 = []
for seg in segment_jux:
    file_jux1 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
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
    male_transport_long_jux1_nhe50.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    male_transport_long_jux2_nhe50.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    male_transport_long_jux3_nhe50.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    male_transport_long_jux4_nhe50.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    male_transport_long_jux5_nhe50.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))

male_transport_number_reformed_sup_nhe50[0] = male_transport_sup_nhe50[0]+male_transport_sup_nhe50[1]
male_transport_number_reformed_sup_nhe50[1] = male_transport_sup_nhe50[2]
male_transport_number_reformed_sup_nhe50[3] = male_transport_sup_nhe50[3]+male_transport_sup_nhe50[4]
male_transport_number_reformed_sup_nhe50[4] = male_transport_sup_nhe50[5]
male_transport_number_reformed_sup_nhe50[5] = male_transport_sup_nhe50[6]

male_transport_number_reformed_jux1_nhe50[0] = male_transport_jux1_nhe50[0]+male_transport_jux1_nhe50[1]
male_transport_number_reformed_jux1_nhe50[1] = male_transport_long_jux1_nhe50[0]+male_transport_long_jux1_nhe50[1]
male_transport_number_reformed_jux1_nhe50[2] = male_transport_long_jux1_nhe50[2]
male_transport_number_reformed_jux1_nhe50[3] = male_transport_jux1_nhe50[3]+male_transport_jux1_nhe50[4]
male_transport_number_reformed_jux1_nhe50[4] = male_transport_jux1_nhe50[5]
male_transport_number_reformed_jux1_nhe50[5] = male_transport_jux1_nhe50[6]

male_transport_number_reformed_jux2_nhe50[0] = male_transport_jux2_nhe50[0]+male_transport_jux2_nhe50[1]
male_transport_number_reformed_jux2_nhe50[1] = male_transport_long_jux2_nhe50[0]+male_transport_long_jux2_nhe50[1]
male_transport_number_reformed_jux2_nhe50[2] = male_transport_long_jux2_nhe50[2]
male_transport_number_reformed_jux2_nhe50[3] = male_transport_jux2_nhe50[3]+male_transport_jux2_nhe50[4]
male_transport_number_reformed_jux2_nhe50[4] = male_transport_jux2_nhe50[5]
male_transport_number_reformed_jux2_nhe50[5] = male_transport_jux2_nhe50[6]

male_transport_number_reformed_jux3_nhe50[0] = male_transport_jux3_nhe50[0]+male_transport_jux3_nhe50[1]
male_transport_number_reformed_jux3_nhe50[1] = male_transport_long_jux3_nhe50[0]+male_transport_long_jux3_nhe50[1]
male_transport_number_reformed_jux3_nhe50[2] = male_transport_long_jux3_nhe50[2]
male_transport_number_reformed_jux3_nhe50[3] = male_transport_jux3_nhe50[3]+male_transport_jux3_nhe50[4]
male_transport_number_reformed_jux3_nhe50[4] = male_transport_jux3_nhe50[5]
male_transport_number_reformed_jux3_nhe50[5] = male_transport_jux3_nhe50[6]

male_transport_number_reformed_jux4_nhe50[0] = male_transport_jux4_nhe50[0]+male_transport_jux4_nhe50[1]
male_transport_number_reformed_jux4_nhe50[1] = male_transport_long_jux4_nhe50[0]+male_transport_long_jux4_nhe50[1]
male_transport_number_reformed_jux4_nhe50[2] = male_transport_long_jux4_nhe50[2]
male_transport_number_reformed_jux4_nhe50[3] = male_transport_jux4_nhe50[3]+male_transport_jux4_nhe50[4]
male_transport_number_reformed_jux4_nhe50[4] = male_transport_jux4_nhe50[5]
male_transport_number_reformed_jux4_nhe50[5] = male_transport_jux4_nhe50[6]

male_transport_number_reformed_jux5_nhe50[0] = male_transport_jux5_nhe50[0]+male_transport_jux5_nhe50[1]
male_transport_number_reformed_jux5_nhe50[1] = male_transport_long_jux5_nhe50[0]+male_transport_long_jux5_nhe50[1]
male_transport_number_reformed_jux5_nhe50[2] = male_transport_long_jux5_nhe50[2]
male_transport_number_reformed_jux5_nhe50[3] = male_transport_jux5_nhe50[3]+male_transport_jux5_nhe50[4]
male_transport_number_reformed_jux5_nhe50[4] = male_transport_jux5_nhe50[5]
male_transport_number_reformed_jux5_nhe50[5] = male_transport_jux5_nhe50[6]

#print(segment_transport,male_transport_number)
bar_width = 0.25
male_sup=axarr[1,2].bar(np.arange(len(segment_transport[:6])),[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i]+male_transport_number_reformed_jux5[i] for i in range(len(male_transport_number_reformed_sup))],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Non-diabetic')
#male_jux=axarr[0,1].bar(np.arange(len(segment_transport[:6])),[male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i]+male_transport_number_reformed_jux5[i] for i in range(len(male_transport_number_reformed_sup))],bar_width,bottom=male_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
#male_jux2=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux2,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='cyan',label='Male juxtamedullary type 2')
#male_jux3=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux3,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='darkturquoise',label='Male juxtamedullary type 3')
#male_jux4=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux4,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='powderblue',label='Male juxtamedullary type 4')
#male_jux5=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux5,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='deepskyblue',label='Male juxtamedullary type 5')
male_later=axarr[1,2].bar(np.arange(len(segment_transport)),male_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

male_sup_nhe50=axarr[1,2].bar(np.arange(len(segment_transport[:6]))+bar_width,[male_transport_number_reformed_sup_nhe50[i]+male_transport_number_reformed_jux1_nhe50[i]+male_transport_number_reformed_jux2_nhe50[i]+male_transport_number_reformed_jux3_nhe50[i]+male_transport_number_reformed_jux4_nhe50[i]+male_transport_number_reformed_jux5_nhe50[i] for i in range(len(male_transport_number_reformed_sup_nhe50))],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue',label='Diabetic,[Glu]=8.6mM')
#male_jux=axarr[0,1].bar(np.arange(len(segment_transport[:6])),[male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i]+male_transport_number_reformed_jux5[i] for i in range(len(male_transport_number_reformed_sup))],bar_width,bottom=male_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
#male_jux2=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux2,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='cyan',label='Male juxtamedullary type 2')
#male_jux3=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux3,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='darkturquoise',label='Male juxtamedullary type 3')
#male_jux4=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux4,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='powderblue',label='Male juxtamedullary type 4')
#male_jux5=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux5,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='deepskyblue',label='Male juxtamedullary type 5')
male_later_nhe50=axarr[1,2].bar(np.arange(len(segment_transport))+bar_width,male_transport_number_reformed_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')


Female_sup=axarr[1,2].bar(np.arange(len(segment_transport[:6]))+2*bar_width,[female_transport_number_reformed_sup[i]+female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i]+female_transport_number_reformed_jux3[i]+female_transport_number_reformed_jux4[i]+female_transport_number_reformed_jux5[i] for i in range(len(female_transport_number_reformed_sup))],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta',label='Diabetic,[Glu]=20mM')
#Female_jux=axarr[0,1].bar(np.arange(len(segment_transport[:6]))+bar_width,[female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i]+female_transport_number_reformed_jux3[i]+female_transport_number_reformed_jux4[i]+female_transport_number_reformed_jux5[i] for i in range(len(female_transport_number_reformed_sup))],bar_width,bottom=female_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
#Female_jux2=ax.bar(np.arange(len(segment_transport[:4]))+bar_width,female_transport_number_reformed_jux2,bar_width,bottom=[female_transport_number_reformed_sup[i]+female_transport_number_reformed_jux1[i] for i in range(len(female_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='violet',label='Female juxtamedullary type 2')
#Female_jux3=ax.bar(np.arange(len(segment_transport[:4]))+bar_width,female_transport_number_reformed_jux3,bar_width,bottom=[female_transport_number_reformed_sup[i]+female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i] for i in range(len(female_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='crimson',label='Female juxtamedullary type 3')
#Female_jux4=ax.bar(np.arange(len(segment_transport[:4]))+bar_width,female_transport_number_reformed_jux4,bar_width,bottom=[female_transport_number_reformed_sup[i]+female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i]+female_transport_number_reformed_jux3[i] for i in range(len(female_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='lavenderblush',label='Female juxtamedullary type 4')
#Female_jux5=ax.bar(np.arange(len(segment_transport[:4]))+bar_width,female_transport_number_reformed_jux5,bar_width,bottom=[female_transport_number_reformed_sup[i]+female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i]+female_transport_number_reformed_jux3[i]+female_transport_number_reformed_jux4[i] for i in range(len(female_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='deeppink',label='Female juxtamedullary type 5')
Female_later=axarr[1,2].bar(np.arange(len(segment_transport))+2*bar_width,female_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

axarr[1,2].set_xticks(np.arange(len(segment_transport))+1*bar_width)
axarr[1,2].set_xticklabels(segment_transport,fontsize=30)
axarr[1,2].tick_params(axis='both',labelsize=30)
#ax.set_xlabel('Segment',fontsize=20)
axarr[1,2].set_ylim(-0.1,0.55)
axarr[1,2].set_ylabel('Segmental K$^+$ transport (mol/Day)',fontsize=30)

# bar_width_ins = bar_width
# axins = inset_axes(axarr[1,1],width=2.5,height=2.5,loc=7)

# male_sup_inset=axins.bar(np.arange(len(segment_transport[:6])),male_transport_number_reformed_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Male')
# male_jux_inset=axins.bar(np.arange(len(segment_transport[:6])),[male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i]+male_transport_number_reformed_jux5[i] for i in range(len(male_transport_number_reformed_sup))],bar_width,bottom=male_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
# male_later_inset=axins.bar(np.arange(len(segment_transport)),male_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

# Female_sup_inset=axins.bar(np.arange(len(segment_transport[:6]))+bar_width,female_transport_number_reformed_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta',label='Female')
# Female_jux_inset=axins.bar(np.arange(len(segment_transport[:6]))+bar_width,[female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i]+female_transport_number_reformed_jux3[i]+female_transport_number_reformed_jux4[i]+female_transport_number_reformed_jux5[i] for i in range(len(female_transport_number_reformed_sup))],bar_width,bottom=female_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
# Female_later_inset=axins.bar(np.arange(len(segment_transport))+bar_width,female_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

# axins.set_xticks(np.arange(len(segment_transport))+0.5*bar_width_ins)
# axins.set_xticklabels(segment_transport,fontsize=30)
# axins.set_xlim(5-1.5*bar_width_ins,6+2*bar_width_ins)
# axins.set_ylim(0,0.3)
# axins.tick_params(axis='both',labelsize=30)
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
    file_sup = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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
    file_data = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
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
    file_sup = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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
    file_data = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
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
bar_width = 0.15

#print(segment[:6],male_delivery_sup)

male_sup=axarr[2,0].bar(np.arange(3),[0,male_delivery_sup[0]+male_delivery_jux1[0]+male_delivery_jux2[0]+male_delivery_jux3[0]+male_delivery_jux4[0]+male_delivery_jux5[0],0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Non-diabetic')
#male_jux=axarr[0,0].bar(np.arange(1),male_delivery_jux1[0]+male_delivery_jux2[0]+male_delivery_jux3[0]+male_delivery_jux4[0]+male_delivery_jux5[0],bar_width,bottom=male_delivery_sup[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')

male_sup_nhe50=axarr[2,0].bar(np.arange(3)+bar_width,[0,male_delivery_sup_nhe50[0]+male_delivery_jux1_nhe50[0]+male_delivery_jux2_nhe50[0]+male_delivery_jux3_nhe50[0]+male_delivery_jux4_nhe50[0]+male_delivery_jux5_nhe50[0],0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue',label='Diabetic,[Glu]=8.6mM')
# male_jux_nhe50=axarr[0,0].bar(np.arange(1)+bar_width,male_delivery_jux1_nhe50[0]+male_delivery_jux2_nhe50[0]+male_delivery_jux3_nhe50[0]+male_delivery_jux4_nhe50[0]+male_delivery_jux5_nhe50[0],bar_width,bottom=male_delivery_sup_nhe50[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# male_later_nhe50=axarr[0,0].bar(np.arange(2)+bar_width,[male_delivery_number_nhe50[0],male_delivery_number_nhe50[-1]],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

Female_sup=axarr[2,0].bar(np.arange(3)+2*bar_width,[0,female_delivery_sup[0]+female_delivery_jux1[0]+female_delivery_jux2[0]+female_delivery_jux3[0]+female_delivery_jux4[0]+female_delivery_jux5[0],0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta',label='Diabetic,[Glu]=20mM')
#Female_jux=axarr[0,0].bar(np.arange(1)+1*bar_width,female_delivery_jux1[0]+female_delivery_jux2[0]+female_delivery_jux3[0]+female_delivery_jux4[0]+female_delivery_jux5[0],bar_width,bottom=female_delivery_sup[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')

# Female_sup_nhe50=axarr[0,0].bar(np.arange(1)+3*bar_width,female_delivery_sup_nhe50[0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')
# Female_jux_nhe50=axarr[0,0].bar(np.arange(1)+3*bar_width,female_delivery_jux1_nhe50[0]+female_delivery_jux2_nhe50[0]+female_delivery_jux3_nhe50[0]+female_delivery_jux4_nhe50[0]+female_delivery_jux5_nhe50[0],bar_width,bottom=female_delivery_sup_nhe50[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# Female_later_nhe50=axarr[0,0].bar(np.arange(2)+3*bar_width,[female_delivery_number_nhe50[0],female_delivery_number_nhe50[-1]],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')
axarr[2,0].set_xticks(np.arange(3)+0.5*bar_width)
axarr[2,0].set_xticklabels(['','Filtered',''],fontsize=30)
axarr[2,0].tick_params(axis='both',labelsize=30)
#ax.set_xlabel('Segment',fontsize=20)
axarr[2,0].set_ylabel('Filtered Cl$^-$ (mol/Day)',fontsize=30)
axarr[2,0].get_xaxis().set_visible(False)
#axarr[0,0].legend(fontsize=30,markerscale=30)

male_later=axarr[2,1].bar(np.arange(3),[male_delivery_number[0],male_delivery_number[-1],0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')
male_later_nhe50=axarr[2,1].bar(np.arange(3)+bar_width,[male_delivery_number_nhe50[0],male_delivery_number_nhe50[-1],0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')
Female_later=axarr[2,1].bar(np.arange(3)+2*bar_width,[female_delivery_number[0],female_delivery_number[-1],0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

axarr[2,1].set_xticks(np.arange(3)+0.5*bar_width)
axarr[2,1].set_xticklabels(['','Excretion',''],fontsize=30)
axarr[2,1].tick_params(axis='both',labelsize=30)
#ax.set_xlabel('Segment',fontsize=20)
axarr[2,1].set_ylabel('Cl$^-$ excretion (mol/Day)',fontsize=30)
axarr[2,1].get_xaxis().set_visible(False)
axarr[2,1].set_ylim(0,0.29)
#axarr[0,1].legend(fontsize=30,markerscale=30)
# bar_width_ins = bar_width
# axins = inset_axes(axarr[0,0],width=2.5,height=2.5,loc=7)

# male_sup_inset=axins.bar(np.arange(1),male_delivery_sup[0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Baseline')
# male_jux_inset=axins.bar(np.arange(1),male_delivery_jux1[0]+male_delivery_jux2[0]+male_delivery_jux3[0]+male_delivery_jux4[0]+male_delivery_jux5[0],bar_width,bottom=male_delivery_sup[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# male_later_inset=axins.bar(np.arange(2),[male_delivery_number[0],male_delivery_number[-1]],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

# # male_sup_nhe50=axarr[0,0].bar(np.arange(1)+bar_width,male_delivery_sup_nhe50[0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue',label='Healthy, SGLT2i')
# # male_jux_nhe50=axarr[0,0].bar(np.arange(1)+bar_width,male_delivery_jux1_nhe50[0]+male_delivery_jux2_nhe50[0]+male_delivery_jux3_nhe50[0]+male_delivery_jux4_nhe50[0]+male_delivery_jux5_nhe50[0],bar_width,bottom=male_delivery_sup_nhe50[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# # male_later_nhe50=axarr[0,0].bar(np.arange(2)+bar_width,[male_delivery_number_nhe50[0],male_delivery_number_nhe50[-1]],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

# Female_sup_inset=axins.bar(np.arange(1)+1*bar_width,female_delivery_sup[0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')
# Female_jux_inset=axins.bar(np.arange(1)+1*bar_width,female_delivery_jux1[0]+female_delivery_jux2[0]+female_delivery_jux3[0]+female_delivery_jux4[0]+female_delivery_jux5[0],bar_width,bottom=female_delivery_sup[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# Female_later_inset=axins.bar(np.arange(2)+1*bar_width,[female_delivery_number[0],female_delivery_number[-1]],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

# # Female_sup_nhe50=axarr[0,0].bar(np.arange(1)+3*bar_width,female_delivery_sup_nhe50[0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')
# # Female_jux_nhe50=axarr[0,0].bar(np.arange(1)+3*bar_width,female_delivery_jux1_nhe50[0]+female_delivery_jux2_nhe50[0]+female_delivery_jux3_nhe50[0]+female_delivery_jux4_nhe50[0]+female_delivery_jux5_nhe50[0],bar_width,bottom=female_delivery_sup_nhe50[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# # Female_later_nhe50=axarr[0,0].bar(np.arange(2)+3*bar_width,[female_delivery_number_nhe50[0],female_delivery_number_nhe50[-1]],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')

# axins.set_xticks(np.arange(2)+0.5*bar_width_ins)
# axins.set_xticklabels(['Filtered','Excretion'],fontsize=30)
# axins.set_xlim(1-1*bar_width_ins,1+2*bar_width_ins)
# axins.set_ylim(0,0.2)
# axins.tick_params(axis='both',labelsize=30)

#==================================================================
# Cl transport
#==================================================================

female_transport_number = []
female_transport_sup = []
female_transport_jux1 = []
female_transport_jux2 = []
female_transport_jux3 = []
female_transport_jux4 = []
female_transport_jux5 = []
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
    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    female_transport_number.append(0)
    female_transport_sup.append(solute_conversion*neph_weight[0]*(datalist_sup[0]-datalist_sup[-1]))
    female_transport_jux1.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    female_transport_jux2.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    female_transport_jux3.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    female_transport_jux4.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    female_transport_jux5.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))
for seg in segment_late:
    file_data = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
        number_of_transport = datalist[0]-datalist[-1]
    female_transport_number.append(solute_conversion*number_of_transport)

female_transport_number_reformed_sup = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux1 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux2 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux3 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux4 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux5 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed = [0 for _ in segment_transport]

female_transport_number_reformed[6] = female_transport_number[7]+female_transport_number[8]+female_transport_number[9]

female_transport_long_jux1 = []
female_transport_long_jux2 = []
female_transport_long_jux3 = []
female_transport_long_jux4 = []
female_transport_long_jux5 = []
for seg in segment_jux:
    file_jux1 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
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
    female_transport_long_jux1.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    female_transport_long_jux2.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    female_transport_long_jux3.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    female_transport_long_jux4.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    female_transport_long_jux5.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))

female_transport_number_reformed_sup[0] = female_transport_sup[0]+female_transport_sup[1]
female_transport_number_reformed_sup[1] = female_transport_sup[2]
female_transport_number_reformed_sup[3] = female_transport_sup[3]+female_transport_sup[4]
female_transport_number_reformed_sup[4] = female_transport_sup[5]
female_transport_number_reformed_sup[5] = female_transport_sup[6]

female_transport_number_reformed_jux1[0] = female_transport_jux1[0]+female_transport_jux1[1]
female_transport_number_reformed_jux1[1] = female_transport_long_jux1[0]+female_transport_long_jux1[1]
female_transport_number_reformed_jux1[2] = female_transport_long_jux1[2]
female_transport_number_reformed_jux1[3] = female_transport_jux1[3]+female_transport_jux1[4]
female_transport_number_reformed_jux1[4] = female_transport_jux1[5]
female_transport_number_reformed_jux1[5] = female_transport_jux1[6]

female_transport_number_reformed_jux2[0] = female_transport_jux2[0]+female_transport_jux2[1]
female_transport_number_reformed_jux2[1] = female_transport_long_jux2[0]+female_transport_long_jux2[1]
female_transport_number_reformed_jux2[2] = female_transport_long_jux2[2]
female_transport_number_reformed_jux2[3] = female_transport_jux2[3]+female_transport_jux2[4]
female_transport_number_reformed_jux2[4] = female_transport_jux2[5]
female_transport_number_reformed_jux2[5] = female_transport_jux2[6]

female_transport_number_reformed_jux3[0] = female_transport_jux3[0]+female_transport_jux3[1]
female_transport_number_reformed_jux3[1] = female_transport_long_jux3[0]+female_transport_long_jux3[1]
female_transport_number_reformed_jux3[2] = female_transport_long_jux3[2]
female_transport_number_reformed_jux3[3] = female_transport_jux3[3]+female_transport_jux3[4]
female_transport_number_reformed_jux3[4] = female_transport_jux3[5]
female_transport_number_reformed_jux3[5] = female_transport_jux3[6]

female_transport_number_reformed_jux4[0] = female_transport_jux4[0]+female_transport_jux4[1]
female_transport_number_reformed_jux4[1] = female_transport_long_jux4[0]+female_transport_long_jux4[1]
female_transport_number_reformed_jux4[2] = female_transport_long_jux4[2]
female_transport_number_reformed_jux4[3] = female_transport_jux4[3]+female_transport_jux4[4]
female_transport_number_reformed_jux4[4] = female_transport_jux4[5]
female_transport_number_reformed_jux4[5] = female_transport_jux4[6]

female_transport_number_reformed_jux5[0] = female_transport_jux5[0]+female_transport_jux5[1]
female_transport_number_reformed_jux5[1] = female_transport_long_jux5[0]+female_transport_long_jux5[1]
female_transport_number_reformed_jux5[2] = female_transport_long_jux5[2]
female_transport_number_reformed_jux5[3] = female_transport_jux5[3]+female_transport_jux5[4]
female_transport_number_reformed_jux5[4] = female_transport_jux5[5]
female_transport_number_reformed_jux5[5] = female_transport_jux5[6]

#==================================================================
# Male transport
#==================================================================

male_transport_number = []
male_transport_sup = []
male_transport_jux1 = []
male_transport_jux2 = []
male_transport_jux3 = []
male_transport_jux4 = []
male_transport_jux5 = []
for seg in segment_early:
    file_sup = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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
    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_transport_number.append(0)
    male_transport_sup.append(solute_conversion*neph_weight[0]*(datalist_sup[0]-datalist_sup[-1]))
    male_transport_jux1.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    male_transport_jux2.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    male_transport_jux3.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    male_transport_jux4.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    male_transport_jux5.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))
for seg in segment_late:
    file_data = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
        number_of_transport = datalist[0]-datalist[-1]
    male_transport_number.append(solute_conversion*number_of_transport)

male_transport_number_reformed_sup = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux1 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux2 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux3 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux4 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux5 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed = [0 for _ in segment_transport]

male_transport_number_reformed[6] = male_transport_number[7]+male_transport_number[8]+male_transport_number[9]

male_transport_long_jux1 = []
male_transport_long_jux2 = []
male_transport_long_jux3 = []
male_transport_long_jux4 = []
male_transport_long_jux5 = []
for seg in segment_jux:
    file_jux1 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_normal_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
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
    male_transport_long_jux1.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    male_transport_long_jux2.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    male_transport_long_jux3.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    male_transport_long_jux4.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    male_transport_long_jux5.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))

male_transport_number_reformed_sup[0] = male_transport_sup[0]+male_transport_sup[1]
male_transport_number_reformed_sup[1] = male_transport_sup[2]
male_transport_number_reformed_sup[3] = male_transport_sup[3]+male_transport_sup[4]
male_transport_number_reformed_sup[4] = male_transport_sup[5]
male_transport_number_reformed_sup[5] = male_transport_sup[6]

male_transport_number_reformed_jux1[0] = male_transport_jux1[0]+male_transport_jux1[1]
male_transport_number_reformed_jux1[1] = male_transport_long_jux1[0]+male_transport_long_jux1[1]
male_transport_number_reformed_jux1[2] = male_transport_long_jux1[2]
male_transport_number_reformed_jux1[3] = male_transport_jux1[3]+male_transport_jux1[4]
male_transport_number_reformed_jux1[4] = male_transport_jux1[5]
male_transport_number_reformed_jux1[5] = male_transport_jux1[6]

male_transport_number_reformed_jux2[0] = male_transport_jux2[0]+male_transport_jux2[1]
male_transport_number_reformed_jux2[1] = male_transport_long_jux2[0]+male_transport_long_jux2[1]
male_transport_number_reformed_jux2[2] = male_transport_long_jux2[2]
male_transport_number_reformed_jux2[3] = male_transport_jux2[3]+male_transport_jux2[4]
male_transport_number_reformed_jux2[4] = male_transport_jux2[5]
male_transport_number_reformed_jux2[5] = male_transport_jux2[6]

male_transport_number_reformed_jux3[0] = male_transport_jux3[0]+male_transport_jux3[1]
male_transport_number_reformed_jux3[1] = male_transport_long_jux3[0]+male_transport_long_jux3[1]
male_transport_number_reformed_jux3[2] = male_transport_long_jux3[2]
male_transport_number_reformed_jux3[3] = male_transport_jux3[3]+male_transport_jux3[4]
male_transport_number_reformed_jux3[4] = male_transport_jux3[5]
male_transport_number_reformed_jux3[5] = male_transport_jux3[6]

male_transport_number_reformed_jux4[0] = male_transport_jux4[0]+male_transport_jux4[1]
male_transport_number_reformed_jux4[1] = male_transport_long_jux4[0]+male_transport_long_jux4[1]
male_transport_number_reformed_jux4[2] = male_transport_long_jux4[2]
male_transport_number_reformed_jux4[3] = male_transport_jux4[3]+male_transport_jux4[4]
male_transport_number_reformed_jux4[4] = male_transport_jux4[5]
male_transport_number_reformed_jux4[5] = male_transport_jux4[6]

male_transport_number_reformed_jux5[0] = male_transport_jux5[0]+male_transport_jux5[1]
male_transport_number_reformed_jux5[1] = male_transport_long_jux5[0]+male_transport_long_jux5[1]
male_transport_number_reformed_jux5[2] = male_transport_long_jux5[2]
male_transport_number_reformed_jux5[3] = male_transport_jux5[3]+male_transport_jux5[4]
male_transport_number_reformed_jux5[4] = male_transport_jux5[5]
male_transport_number_reformed_jux5[5] = male_transport_jux5[6]

male_transport_number_nhe50 = []
male_transport_sup_nhe50 = []
male_transport_jux1_nhe50 = []
male_transport_jux2_nhe50 = []
male_transport_jux3_nhe50 = []
male_transport_jux4_nhe50 = []
male_transport_jux5_nhe50 = []
for seg in segment_early:
    file_sup = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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
    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_transport_number_nhe50.append(0)
    male_transport_sup_nhe50.append(solute_conversion*neph_weight[0]*(datalist_sup[0]-datalist_sup[-1]))
    male_transport_jux1_nhe50.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    male_transport_jux2_nhe50.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    male_transport_jux3_nhe50.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    male_transport_jux4_nhe50.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    male_transport_jux5_nhe50.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))
for seg in segment_late:
    file_data = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
        number_of_transport = datalist[0]-datalist[-1]
    male_transport_number_nhe50.append(solute_conversion*number_of_transport)

male_transport_number_reformed_sup_nhe50 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux1_nhe50 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux2_nhe50 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux3_nhe50 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux4_nhe50 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux5_nhe50 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_nhe50 = [0 for _ in segment_transport]

male_transport_number_reformed_nhe50[6] = male_transport_number_nhe50[7]+male_transport_number_nhe50[8]+male_transport_number_nhe50[9]

male_transport_long_jux1_nhe50 = []
male_transport_long_jux2_nhe50 = []
male_transport_long_jux3_nhe50 = []
male_transport_long_jux4_nhe50 = []
male_transport_long_jux5_nhe50 = []
for seg in segment_jux:
    file_jux1 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
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
    male_transport_long_jux1_nhe50.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    male_transport_long_jux2_nhe50.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    male_transport_long_jux3_nhe50.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    male_transport_long_jux4_nhe50.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    male_transport_long_jux5_nhe50.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))

male_transport_number_reformed_sup_nhe50[0] = male_transport_sup_nhe50[0]+male_transport_sup_nhe50[1]
male_transport_number_reformed_sup_nhe50[1] = male_transport_sup_nhe50[2]
male_transport_number_reformed_sup_nhe50[3] = male_transport_sup_nhe50[3]+male_transport_sup_nhe50[4]
male_transport_number_reformed_sup_nhe50[4] = male_transport_sup_nhe50[5]
male_transport_number_reformed_sup_nhe50[5] = male_transport_sup_nhe50[6]

male_transport_number_reformed_jux1_nhe50[0] = male_transport_jux1_nhe50[0]+male_transport_jux1_nhe50[1]
male_transport_number_reformed_jux1_nhe50[1] = male_transport_long_jux1_nhe50[0]+male_transport_long_jux1_nhe50[1]
male_transport_number_reformed_jux1_nhe50[2] = male_transport_long_jux1_nhe50[2]
male_transport_number_reformed_jux1_nhe50[3] = male_transport_jux1_nhe50[3]+male_transport_jux1_nhe50[4]
male_transport_number_reformed_jux1_nhe50[4] = male_transport_jux1_nhe50[5]
male_transport_number_reformed_jux1_nhe50[5] = male_transport_jux1_nhe50[6]

male_transport_number_reformed_jux2_nhe50[0] = male_transport_jux2_nhe50[0]+male_transport_jux2_nhe50[1]
male_transport_number_reformed_jux2_nhe50[1] = male_transport_long_jux2_nhe50[0]+male_transport_long_jux2_nhe50[1]
male_transport_number_reformed_jux2_nhe50[2] = male_transport_long_jux2_nhe50[2]
male_transport_number_reformed_jux2_nhe50[3] = male_transport_jux2_nhe50[3]+male_transport_jux2_nhe50[4]
male_transport_number_reformed_jux2_nhe50[4] = male_transport_jux2_nhe50[5]
male_transport_number_reformed_jux2_nhe50[5] = male_transport_jux2_nhe50[6]

male_transport_number_reformed_jux3_nhe50[0] = male_transport_jux3_nhe50[0]+male_transport_jux3_nhe50[1]
male_transport_number_reformed_jux3_nhe50[1] = male_transport_long_jux3_nhe50[0]+male_transport_long_jux3_nhe50[1]
male_transport_number_reformed_jux3_nhe50[2] = male_transport_long_jux3_nhe50[2]
male_transport_number_reformed_jux3_nhe50[3] = male_transport_jux3_nhe50[3]+male_transport_jux3_nhe50[4]
male_transport_number_reformed_jux3_nhe50[4] = male_transport_jux3_nhe50[5]
male_transport_number_reformed_jux3_nhe50[5] = male_transport_jux3_nhe50[6]

male_transport_number_reformed_jux4_nhe50[0] = male_transport_jux4_nhe50[0]+male_transport_jux4_nhe50[1]
male_transport_number_reformed_jux4_nhe50[1] = male_transport_long_jux4_nhe50[0]+male_transport_long_jux4_nhe50[1]
male_transport_number_reformed_jux4_nhe50[2] = male_transport_long_jux4_nhe50[2]
male_transport_number_reformed_jux4_nhe50[3] = male_transport_jux4_nhe50[3]+male_transport_jux4_nhe50[4]
male_transport_number_reformed_jux4_nhe50[4] = male_transport_jux4_nhe50[5]
male_transport_number_reformed_jux4_nhe50[5] = male_transport_jux4_nhe50[6]

male_transport_number_reformed_jux5_nhe50[0] = male_transport_jux5_nhe50[0]+male_transport_jux5_nhe50[1]
male_transport_number_reformed_jux5_nhe50[1] = male_transport_long_jux5_nhe50[0]+male_transport_long_jux5_nhe50[1]
male_transport_number_reformed_jux5_nhe50[2] = male_transport_long_jux5_nhe50[2]
male_transport_number_reformed_jux5_nhe50[3] = male_transport_jux5_nhe50[3]+male_transport_jux5_nhe50[4]
male_transport_number_reformed_jux5_nhe50[4] = male_transport_jux5_nhe50[5]
male_transport_number_reformed_jux5_nhe50[5] = male_transport_jux5_nhe50[6]

#print(segment_transport,male_transport_number)
bar_width = 0.25
male_sup=axarr[2,2].bar(np.arange(len(segment_transport[:6])),[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i]+male_transport_number_reformed_jux5[i] for i in range(len(male_transport_number_reformed_sup))],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Non-diabetic')
#male_jux=axarr[0,1].bar(np.arange(len(segment_transport[:6])),[male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i]+male_transport_number_reformed_jux5[i] for i in range(len(male_transport_number_reformed_sup))],bar_width,bottom=male_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
#male_jux2=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux2,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='cyan',label='Male juxtamedullary type 2')
#male_jux3=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux3,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='darkturquoise',label='Male juxtamedullary type 3')
#male_jux4=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux4,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='powderblue',label='Male juxtamedullary type 4')
#male_jux5=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux5,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='deepskyblue',label='Male juxtamedullary type 5')
male_later=axarr[2,2].bar(np.arange(len(segment_transport)),male_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

male_sup_nhe50=axarr[2,2].bar(np.arange(len(segment_transport[:6]))+bar_width,[male_transport_number_reformed_sup_nhe50[i]+male_transport_number_reformed_jux1_nhe50[i]+male_transport_number_reformed_jux2_nhe50[i]+male_transport_number_reformed_jux3_nhe50[i]+male_transport_number_reformed_jux4_nhe50[i]+male_transport_number_reformed_jux5_nhe50[i] for i in range(len(male_transport_number_reformed_sup_nhe50))],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue',label='Diabetic,[Glu]=8.6mM')
#male_jux=axarr[0,1].bar(np.arange(len(segment_transport[:6])),[male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i]+male_transport_number_reformed_jux5[i] for i in range(len(male_transport_number_reformed_sup))],bar_width,bottom=male_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
#male_jux2=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux2,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='cyan',label='Male juxtamedullary type 2')
#male_jux3=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux3,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='darkturquoise',label='Male juxtamedullary type 3')
#male_jux4=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux4,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='powderblue',label='Male juxtamedullary type 4')
#male_jux5=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux5,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='deepskyblue',label='Male juxtamedullary type 5')
male_later_nhe50=axarr[2,2].bar(np.arange(len(segment_transport))+bar_width,male_transport_number_reformed_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')


Female_sup=axarr[2,2].bar(np.arange(len(segment_transport[:6]))+2*bar_width,[female_transport_number_reformed_sup[i]+female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i]+female_transport_number_reformed_jux3[i]+female_transport_number_reformed_jux4[i]+female_transport_number_reformed_jux5[i] for i in range(len(female_transport_number_reformed_sup))],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta',label='Diabetic,[Glu]=20mM')
#Female_jux=axarr[0,1].bar(np.arange(len(segment_transport[:6]))+bar_width,[female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i]+female_transport_number_reformed_jux3[i]+female_transport_number_reformed_jux4[i]+female_transport_number_reformed_jux5[i] for i in range(len(female_transport_number_reformed_sup))],bar_width,bottom=female_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
#Female_jux2=ax.bar(np.arange(len(segment_transport[:4]))+bar_width,female_transport_number_reformed_jux2,bar_width,bottom=[female_transport_number_reformed_sup[i]+female_transport_number_reformed_jux1[i] for i in range(len(female_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='violet',label='Female juxtamedullary type 2')
#Female_jux3=ax.bar(np.arange(len(segment_transport[:4]))+bar_width,female_transport_number_reformed_jux3,bar_width,bottom=[female_transport_number_reformed_sup[i]+female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i] for i in range(len(female_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='crimson',label='Female juxtamedullary type 3')
#Female_jux4=ax.bar(np.arange(len(segment_transport[:4]))+bar_width,female_transport_number_reformed_jux4,bar_width,bottom=[female_transport_number_reformed_sup[i]+female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i]+female_transport_number_reformed_jux3[i] for i in range(len(female_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='lavenderblush',label='Female juxtamedullary type 4')
#Female_jux5=ax.bar(np.arange(len(segment_transport[:4]))+bar_width,female_transport_number_reformed_jux5,bar_width,bottom=[female_transport_number_reformed_sup[i]+female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i]+female_transport_number_reformed_jux3[i]+female_transport_number_reformed_jux4[i] for i in range(len(female_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='deeppink',label='Female juxtamedullary type 5')
Female_later=axarr[2,2].bar(np.arange(len(segment_transport))+2*bar_width,female_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

axarr[2,2].set_xticks(np.arange(len(segment_transport))+1*bar_width)
axarr[2,2].set_xticklabels(segment_transport,fontsize=30)
axarr[2,2].tick_params(axis='both',labelsize=30)
#ax.set_xlabel('Segment',fontsize=20)
axarr[2,2].set_ylabel('Segmental Cl$^-$ transport (mol/Day)',fontsize=30)
#axarr[2,2].legend(fontsize=30,markerscale=30)

bar_width_ins = bar_width
axins = inset_axes(axarr[2,2],width=2.5,height=2.5,loc=7)

male_sup_inset=axins.bar(np.arange(len(segment_transport[:6])),[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i]+male_transport_number_reformed_jux5[i] for i in range(len(male_transport_number_reformed_sup))],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Male')
#male_jux_inset=axins.bar(np.arange(len(segment_transport[:6])),[male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i]+male_transport_number_reformed_jux5[i] for i in range(len(male_transport_number_reformed_sup))],bar_width,bottom=male_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
male_later_inset=axins.bar(np.arange(len(segment_transport)),male_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

male_sup_nhe50_inset=axins.bar(np.arange(len(segment_transport[:6]))+bar_width,[male_transport_number_reformed_sup_nhe50[i]+male_transport_number_reformed_jux1_nhe50[i]+male_transport_number_reformed_jux2_nhe50[i]+male_transport_number_reformed_jux3_nhe50[i]+male_transport_number_reformed_jux4_nhe50[i]+male_transport_number_reformed_jux5_nhe50[i] for i in range(len(male_transport_number_reformed_sup))],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue',label='Male')
#male_jux_inset=axins.bar(np.arange(len(segment_transport[:6])),[male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i]+male_transport_number_reformed_jux5[i] for i in range(len(male_transport_number_reformed_sup))],bar_width,bottom=male_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
male_later_nhe50_inset=axins.bar(np.arange(len(segment_transport))+bar_width,male_transport_number_reformed_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

Female_sup_inset=axins.bar(np.arange(len(segment_transport[:6]))+2*bar_width,[female_transport_number_reformed_sup[i]+female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i]+female_transport_number_reformed_jux3[i]+female_transport_number_reformed_jux4[i]+female_transport_number_reformed_jux5[i] for i in range(len(female_transport_number_reformed_sup))],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta',label='Female')
#Female_jux_inset=axins.bar(np.arange(len(segment_transport[:6]))+bar_width,[female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i]+female_transport_number_reformed_jux3[i]+female_transport_number_reformed_jux4[i]+female_transport_number_reformed_jux5[i] for i in range(len(female_transport_number_reformed_sup))],bar_width,bottom=female_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
Female_later_inset=axins.bar(np.arange(len(segment_transport))+2*bar_width,female_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

axins.set_xticks(np.arange(len(segment_transport))+1*bar_width_ins)
axins.set_xticklabels(segment_transport,fontsize=30)
axins.set_xlim(5-1.5*bar_width_ins,6+3*bar_width_ins)
axins.set_ylim(0,0.3)
axins.tick_params(axis='both',labelsize=30)
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
    file_sup = open(male_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen_sup.txt','r')
    file_jux1 = open(male_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux5.txt','r')
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
    file_data = open(male_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen.txt','r')
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
    file_sup = open(male_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen_sup.txt','r')
    file_jux1 = open(male_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux5.txt','r')
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
    file_data = open(male_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        male_delivery_number_nhe50.append(number_of_delivery*volume_conversion)
    else:
        number_of_delivery = datalist[0]

segment = ['PT','DL','mTAL','DCT','CNT','CCD','urine']
bar_width = 0.15

#print(segment[:6],male_delivery_sup)

male_sup=axarr[3,0].bar(np.arange(3),[0,male_delivery_sup[0]+male_delivery_jux1[0]+male_delivery_jux2[0]+male_delivery_jux3[0]+male_delivery_jux4[0]+male_delivery_jux5[0],0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Non-diabetic')
#male_jux=axarr[0,0].bar(np.arange(1),male_delivery_jux1[0]+male_delivery_jux2[0]+male_delivery_jux3[0]+male_delivery_jux4[0]+male_delivery_jux5[0],bar_width,bottom=male_delivery_sup[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')

male_sup_nhe50=axarr[3,0].bar(np.arange(3)+bar_width,[0,male_delivery_sup_nhe50[0]+male_delivery_jux1_nhe50[0]+male_delivery_jux2_nhe50[0]+male_delivery_jux3_nhe50[0]+male_delivery_jux4_nhe50[0]+male_delivery_jux5_nhe50[0],0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue',label='Diabetic,[Glu]=8.6mM')
# male_jux_nhe50=axarr[0,0].bar(np.arange(1)+bar_width,male_delivery_jux1_nhe50[0]+male_delivery_jux2_nhe50[0]+male_delivery_jux3_nhe50[0]+male_delivery_jux4_nhe50[0]+male_delivery_jux5_nhe50[0],bar_width,bottom=male_delivery_sup_nhe50[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# male_later_nhe50=axarr[0,0].bar(np.arange(2)+bar_width,[male_delivery_number_nhe50[0],male_delivery_number_nhe50[-1]],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

Female_sup=axarr[3,0].bar(np.arange(3)+2*bar_width,[0,female_delivery_sup[0]+female_delivery_jux1[0]+female_delivery_jux2[0]+female_delivery_jux3[0]+female_delivery_jux4[0]+female_delivery_jux5[0],0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta',label='Diabetic')
#Female_jux=axarr[0,0].bar(np.arange(1)+1*bar_width,female_delivery_jux1[0]+female_delivery_jux2[0]+female_delivery_jux3[0]+female_delivery_jux4[0]+female_delivery_jux5[0],bar_width,bottom=female_delivery_sup[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')

# Female_sup_nhe50=axarr[0,0].bar(np.arange(1)+3*bar_width,female_delivery_sup_nhe50[0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')
# Female_jux_nhe50=axarr[0,0].bar(np.arange(1)+3*bar_width,female_delivery_jux1_nhe50[0]+female_delivery_jux2_nhe50[0]+female_delivery_jux3_nhe50[0]+female_delivery_jux4_nhe50[0]+female_delivery_jux5_nhe50[0],bar_width,bottom=female_delivery_sup_nhe50[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# Female_later_nhe50=axarr[0,0].bar(np.arange(2)+3*bar_width,[female_delivery_number_nhe50[0],female_delivery_number_nhe50[-1]],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')
axarr[3,0].set_xticks(np.arange(3)+1*bar_width)
axarr[3,0].set_xticklabels(['','Filtered',''],fontsize=30)
axarr[3,0].tick_params(axis='both',labelsize=30)
#ax.set_xlabel('Segment',fontsize=20)
axarr[3,0].set_ylabel('Filtered volume (L/Day)',fontsize=30)
axarr[3,0].get_xaxis().set_visible(False)
#axarr[0,0].legend(fontsize=30,markerscale=30)

male_later=axarr[3,1].bar(np.arange(3),[male_delivery_number[0],male_delivery_number[-1],0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')
male_later_nhe50=axarr[3,1].bar(np.arange(3)+bar_width,[male_delivery_number_nhe50[0],male_delivery_number_nhe50[-1],0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')
Female_later=axarr[3,1].bar(np.arange(3)+2*bar_width,[female_delivery_number[0],female_delivery_number[-1],0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

axarr[3,1].set_xticks(np.arange(3)+1*bar_width)
axarr[3,1].set_xticklabels(['','Excretion',''],fontsize=30)
axarr[3,1].tick_params(axis='both',labelsize=30)
#ax.set_xlabel('Segment',fontsize=20)
axarr[3,1].set_ylabel('Volume excretion (L/Day)',fontsize=30)
axarr[3,1].get_xaxis().set_visible(False)

# bar_width_ins = bar_width
# axins = inset_axes(axarr[2,0],width=2.5,height=2.5,loc=7)

# male_sup_inset=axins.bar(np.arange(1),male_delivery_sup[0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Baseline')
# male_jux_inset=axins.bar(np.arange(1),male_delivery_jux1[0]+male_delivery_jux2[0]+male_delivery_jux3[0]+male_delivery_jux4[0]+male_delivery_jux5[0],bar_width,bottom=male_delivery_sup[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# male_later_inset=axins.bar(np.arange(2),[male_delivery_number[0],male_delivery_number[-1]],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

# # male_sup_nhe50=axarr[0,0].bar(np.arange(1)+bar_width,male_delivery_sup_nhe50[0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue',label='Healthy, SGLT2i')
# # male_jux_nhe50=axarr[0,0].bar(np.arange(1)+bar_width,male_delivery_jux1_nhe50[0]+male_delivery_jux2_nhe50[0]+male_delivery_jux3_nhe50[0]+male_delivery_jux4_nhe50[0]+male_delivery_jux5_nhe50[0],bar_width,bottom=male_delivery_sup_nhe50[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# # male_later_nhe50=axarr[0,0].bar(np.arange(2)+bar_width,[male_delivery_number_nhe50[0],male_delivery_number_nhe50[-1]],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

# Female_sup_inset=axins.bar(np.arange(1)+1*bar_width,female_delivery_sup[0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')
# Female_jux_inset=axins.bar(np.arange(1)+1*bar_width,female_delivery_jux1[0]+female_delivery_jux2[0]+female_delivery_jux3[0]+female_delivery_jux4[0]+female_delivery_jux5[0],bar_width,bottom=female_delivery_sup[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# Female_later_inset=axins.bar(np.arange(2)+1*bar_width,[female_delivery_number[0],female_delivery_number[-1]],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

# # Female_sup_nhe50=axarr[0,0].bar(np.arange(1)+3*bar_width,female_delivery_sup_nhe50[0],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')
# # Female_jux_nhe50=axarr[0,0].bar(np.arange(1)+3*bar_width,female_delivery_jux1_nhe50[0]+female_delivery_jux2_nhe50[0]+female_delivery_jux3_nhe50[0]+female_delivery_jux4_nhe50[0]+female_delivery_jux5_nhe50[0],bar_width,bottom=female_delivery_sup_nhe50[0],align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# # Female_later_nhe50=axarr[0,0].bar(np.arange(2)+3*bar_width,[female_delivery_number_nhe50[0],female_delivery_number_nhe50[-1]],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')

# axins.set_xticks(np.arange(2)+0.5*bar_width_ins)
# axins.set_xticklabels(['Filtered','Excretion'],fontsize=30)
# axins.set_xlim(1-1*bar_width_ins,1+2*bar_width_ins)
# axins.set_ylim(0,5)
# axins.tick_params(axis='both',labelsize=30)

#====================================================
# Water reabsorption
#====================================================

female_transport_number = []
female_transport_sup = []
female_transport_jux1 = []
female_transport_jux2 = []
female_transport_jux3 = []
female_transport_jux4 = []
female_transport_jux5 = []
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
    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    female_transport_number.append(0)
    female_transport_sup.append(volume_conversion*neph_weight[0]*(datalist_sup[0]-datalist_sup[-1]))
    female_transport_jux1.append(volume_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    female_transport_jux2.append(volume_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    female_transport_jux3.append(volume_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    female_transport_jux4.append(volume_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    female_transport_jux5.append(volume_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))
for seg in segment_late:
    file_data = open(female_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
        number_of_transport = datalist[0]-datalist[-1]
    female_transport_number.append(volume_conversion*number_of_transport)

female_transport_number_reformed_sup = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux1 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux2 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux3 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux4 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux5 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed = [0 for _ in segment_transport]

female_transport_number_reformed[6] = female_transport_number[7]+female_transport_number[8]+female_transport_number[9]

female_transport_long_jux1 = []
female_transport_long_jux2 = []
female_transport_long_jux3 = []
female_transport_long_jux4 = []
female_transport_long_jux5 = []
for seg in segment_jux:
    file_jux1 = open(female_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux5.txt','r')
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
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
    female_transport_long_jux1.append(volume_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    female_transport_long_jux2.append(volume_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    female_transport_long_jux3.append(volume_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    female_transport_long_jux4.append(volume_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    female_transport_long_jux5.append(volume_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))

female_transport_number_reformed_sup[0] = female_transport_sup[0]+female_transport_sup[1]
female_transport_number_reformed_sup[1] = female_transport_sup[2]
female_transport_number_reformed_sup[3] = female_transport_sup[3]+female_transport_sup[4]
female_transport_number_reformed_sup[4] = female_transport_sup[5]
female_transport_number_reformed_sup[5] = female_transport_sup[6]

female_transport_number_reformed_jux1[0] = female_transport_jux1[0]+female_transport_jux1[1]
female_transport_number_reformed_jux1[1] = female_transport_long_jux1[0]+female_transport_long_jux1[1]
female_transport_number_reformed_jux1[2] = female_transport_long_jux1[2]
female_transport_number_reformed_jux1[3] = female_transport_jux1[3]+female_transport_jux1[4]
female_transport_number_reformed_jux1[4] = female_transport_jux1[5]
female_transport_number_reformed_jux1[5] = female_transport_jux1[6]

female_transport_number_reformed_jux2[0] = female_transport_jux2[0]+female_transport_jux2[1]
female_transport_number_reformed_jux2[1] = female_transport_long_jux2[0]+female_transport_long_jux2[1]
female_transport_number_reformed_jux2[2] = female_transport_long_jux2[2]
female_transport_number_reformed_jux2[3] = female_transport_jux2[3]+female_transport_jux2[4]
female_transport_number_reformed_jux2[4] = female_transport_jux2[5]
female_transport_number_reformed_jux2[5] = female_transport_jux2[6]

female_transport_number_reformed_jux3[0] = female_transport_jux3[0]+female_transport_jux3[1]
female_transport_number_reformed_jux3[1] = female_transport_long_jux3[0]+female_transport_long_jux3[1]
female_transport_number_reformed_jux3[2] = female_transport_long_jux3[2]
female_transport_number_reformed_jux3[3] = female_transport_jux3[3]+female_transport_jux3[4]
female_transport_number_reformed_jux3[4] = female_transport_jux3[5]
female_transport_number_reformed_jux3[5] = female_transport_jux3[6]

female_transport_number_reformed_jux4[0] = female_transport_jux4[0]+female_transport_jux4[1]
female_transport_number_reformed_jux4[1] = female_transport_long_jux4[0]+female_transport_long_jux4[1]
female_transport_number_reformed_jux4[2] = female_transport_long_jux4[2]
female_transport_number_reformed_jux4[3] = female_transport_jux4[3]+female_transport_jux4[4]
female_transport_number_reformed_jux4[4] = female_transport_jux4[5]
female_transport_number_reformed_jux4[5] = female_transport_jux4[6]

female_transport_number_reformed_jux5[0] = female_transport_jux5[0]+female_transport_jux5[1]
female_transport_number_reformed_jux5[1] = female_transport_long_jux5[0]+female_transport_long_jux5[1]
female_transport_number_reformed_jux5[2] = female_transport_long_jux5[2]
female_transport_number_reformed_jux5[3] = female_transport_jux5[3]+female_transport_jux5[4]
female_transport_number_reformed_jux5[4] = female_transport_jux5[5]
female_transport_number_reformed_jux5[5] = female_transport_jux5[6]

#==================================================================
# Male transport
#==================================================================

male_transport_number = []
male_transport_sup = []
male_transport_jux1 = []
male_transport_jux2 = []
male_transport_jux3 = []
male_transport_jux4 = []
male_transport_jux5 = []
for seg in segment_early:
    file_sup = open(male_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen_sup.txt','r')
    file_jux1 = open(male_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux5.txt','r')
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
    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_transport_number.append(0)
    male_transport_sup.append(volume_conversion*neph_weight[0]*(datalist_sup[0]-datalist_sup[-1]))
    male_transport_jux1.append(volume_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    male_transport_jux2.append(volume_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    male_transport_jux3.append(volume_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    male_transport_jux4.append(volume_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    male_transport_jux5.append(volume_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))
for seg in segment_late:
    file_data = open(male_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
        number_of_transport = datalist[0]-datalist[-1]
    male_transport_number.append(volume_conversion*number_of_transport)

male_transport_number_reformed_sup = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux1 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux2 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux3 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux4 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux5 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed = [0 for _ in segment_transport]

male_transport_number_reformed[6] = male_transport_number[7]+male_transport_number[8]+male_transport_number[9]

male_transport_long_jux1 = []
male_transport_long_jux2 = []
male_transport_long_jux3 = []
male_transport_long_jux4 = []
male_transport_long_jux5 = []
for seg in segment_jux:
    file_jux1 = open(male_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_normal_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux5.txt','r')
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
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
    male_transport_long_jux1.append(volume_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    male_transport_long_jux2.append(volume_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    male_transport_long_jux3.append(volume_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    male_transport_long_jux4.append(volume_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    male_transport_long_jux5.append(volume_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))

male_transport_number_reformed_sup[0] = male_transport_sup[0]+male_transport_sup[1]
male_transport_number_reformed_sup[1] = male_transport_sup[2]
male_transport_number_reformed_sup[3] = male_transport_sup[3]+male_transport_sup[4]
male_transport_number_reformed_sup[4] = male_transport_sup[5]
male_transport_number_reformed_sup[5] = male_transport_sup[6]

male_transport_number_reformed_jux1[0] = male_transport_jux1[0]+male_transport_jux1[1]
male_transport_number_reformed_jux1[1] = male_transport_long_jux1[0]+male_transport_long_jux1[1]
male_transport_number_reformed_jux1[2] = male_transport_long_jux1[2]
male_transport_number_reformed_jux1[3] = male_transport_jux1[3]+male_transport_jux1[4]
male_transport_number_reformed_jux1[4] = male_transport_jux1[5]
male_transport_number_reformed_jux1[5] = male_transport_jux1[6]

male_transport_number_reformed_jux2[0] = male_transport_jux2[0]+male_transport_jux2[1]
male_transport_number_reformed_jux2[1] = male_transport_long_jux2[0]+male_transport_long_jux2[1]
male_transport_number_reformed_jux2[2] = male_transport_long_jux2[2]
male_transport_number_reformed_jux2[3] = male_transport_jux2[3]+male_transport_jux2[4]
male_transport_number_reformed_jux2[4] = male_transport_jux2[5]
male_transport_number_reformed_jux2[5] = male_transport_jux2[6]

male_transport_number_reformed_jux3[0] = male_transport_jux3[0]+male_transport_jux3[1]
male_transport_number_reformed_jux3[1] = male_transport_long_jux3[0]+male_transport_long_jux3[1]
male_transport_number_reformed_jux3[2] = male_transport_long_jux3[2]
male_transport_number_reformed_jux3[3] = male_transport_jux3[3]+male_transport_jux3[4]
male_transport_number_reformed_jux3[4] = male_transport_jux3[5]
male_transport_number_reformed_jux3[5] = male_transport_jux3[6]

male_transport_number_reformed_jux4[0] = male_transport_jux4[0]+male_transport_jux4[1]
male_transport_number_reformed_jux4[1] = male_transport_long_jux4[0]+male_transport_long_jux4[1]
male_transport_number_reformed_jux4[2] = male_transport_long_jux4[2]
male_transport_number_reformed_jux4[3] = male_transport_jux4[3]+male_transport_jux4[4]
male_transport_number_reformed_jux4[4] = male_transport_jux4[5]
male_transport_number_reformed_jux4[5] = male_transport_jux4[6]

male_transport_number_reformed_jux5[0] = male_transport_jux5[0]+male_transport_jux5[1]
male_transport_number_reformed_jux5[1] = male_transport_long_jux5[0]+male_transport_long_jux5[1]
male_transport_number_reformed_jux5[2] = male_transport_long_jux5[2]
male_transport_number_reformed_jux5[3] = male_transport_jux5[3]+male_transport_jux5[4]
male_transport_number_reformed_jux5[4] = male_transport_jux5[5]
male_transport_number_reformed_jux5[5] = male_transport_jux5[6]

male_transport_number_nhe50 = []
male_transport_sup_nhe50 = []
male_transport_jux1_nhe50 = []
male_transport_jux2_nhe50 = []
male_transport_jux3_nhe50 = []
male_transport_jux4_nhe50 = []
male_transport_jux5_nhe50 = []
for seg in segment_early:
    file_sup = open(male_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen_sup.txt','r')
    file_jux1 = open(male_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux5.txt','r')
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
    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_transport_number_nhe50.append(0)
    male_transport_sup_nhe50.append(volume_conversion*neph_weight[0]*(datalist_sup[0]-datalist_sup[-1]))
    male_transport_jux1_nhe50.append(volume_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    male_transport_jux2_nhe50.append(volume_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    male_transport_jux3_nhe50.append(volume_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    male_transport_jux4_nhe50.append(volume_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    male_transport_jux5_nhe50.append(volume_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))
for seg in segment_late:
    file_data = open(male_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
        number_of_transport = datalist[0]-datalist[-1]
    male_transport_number_nhe50.append(volume_conversion*number_of_transport)

male_transport_number_reformed_sup_nhe50 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux1_nhe50 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux2_nhe50 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux3_nhe50 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux4_nhe50 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux5_nhe50 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_nhe50 = [0 for _ in segment_transport]

male_transport_number_reformed_nhe50[6] = male_transport_number_nhe50[7]+male_transport_number_nhe50[8]+male_transport_number_nhe50[9]

male_transport_long_jux1_nhe50 = []
male_transport_long_jux2_nhe50 = []
male_transport_long_jux3_nhe50 = []
male_transport_long_jux4_nhe50 = []
male_transport_long_jux5_nhe50 = []
for seg in segment_jux:
    file_jux1 = open(male_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux5.txt','r')
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
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
    male_transport_long_jux1_nhe50.append(volume_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    male_transport_long_jux2_nhe50.append(volume_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    male_transport_long_jux3_nhe50.append(volume_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    male_transport_long_jux4_nhe50.append(volume_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    male_transport_long_jux5_nhe50.append(volume_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))

male_transport_number_reformed_sup_nhe50[0] = male_transport_sup_nhe50[0]+male_transport_sup_nhe50[1]
male_transport_number_reformed_sup_nhe50[1] = male_transport_sup_nhe50[2]
male_transport_number_reformed_sup_nhe50[3] = male_transport_sup_nhe50[3]+male_transport_sup_nhe50[4]
male_transport_number_reformed_sup_nhe50[4] = male_transport_sup_nhe50[5]
male_transport_number_reformed_sup_nhe50[5] = male_transport_sup_nhe50[6]

male_transport_number_reformed_jux1_nhe50[0] = male_transport_jux1_nhe50[0]+male_transport_jux1_nhe50[1]
male_transport_number_reformed_jux1_nhe50[1] = male_transport_long_jux1_nhe50[0]+male_transport_long_jux1_nhe50[1]
male_transport_number_reformed_jux1_nhe50[2] = male_transport_long_jux1_nhe50[2]
male_transport_number_reformed_jux1_nhe50[3] = male_transport_jux1_nhe50[3]+male_transport_jux1_nhe50[4]
male_transport_number_reformed_jux1_nhe50[4] = male_transport_jux1_nhe50[5]
male_transport_number_reformed_jux1_nhe50[5] = male_transport_jux1_nhe50[6]

male_transport_number_reformed_jux2_nhe50[0] = male_transport_jux2_nhe50[0]+male_transport_jux2_nhe50[1]
male_transport_number_reformed_jux2_nhe50[1] = male_transport_long_jux2_nhe50[0]+male_transport_long_jux2_nhe50[1]
male_transport_number_reformed_jux2_nhe50[2] = male_transport_long_jux2_nhe50[2]
male_transport_number_reformed_jux2_nhe50[3] = male_transport_jux2_nhe50[3]+male_transport_jux2_nhe50[4]
male_transport_number_reformed_jux2_nhe50[4] = male_transport_jux2_nhe50[5]
male_transport_number_reformed_jux2_nhe50[5] = male_transport_jux2_nhe50[6]

male_transport_number_reformed_jux3_nhe50[0] = male_transport_jux3_nhe50[0]+male_transport_jux3_nhe50[1]
male_transport_number_reformed_jux3_nhe50[1] = male_transport_long_jux3_nhe50[0]+male_transport_long_jux3_nhe50[1]
male_transport_number_reformed_jux3_nhe50[2] = male_transport_long_jux3_nhe50[2]
male_transport_number_reformed_jux3_nhe50[3] = male_transport_jux3_nhe50[3]+male_transport_jux3_nhe50[4]
male_transport_number_reformed_jux3_nhe50[4] = male_transport_jux3_nhe50[5]
male_transport_number_reformed_jux3_nhe50[5] = male_transport_jux3_nhe50[6]

male_transport_number_reformed_jux4_nhe50[0] = male_transport_jux4_nhe50[0]+male_transport_jux4_nhe50[1]
male_transport_number_reformed_jux4_nhe50[1] = male_transport_long_jux4_nhe50[0]+male_transport_long_jux4_nhe50[1]
male_transport_number_reformed_jux4_nhe50[2] = male_transport_long_jux4_nhe50[2]
male_transport_number_reformed_jux4_nhe50[3] = male_transport_jux4_nhe50[3]+male_transport_jux4_nhe50[4]
male_transport_number_reformed_jux4_nhe50[4] = male_transport_jux4_nhe50[5]
male_transport_number_reformed_jux4_nhe50[5] = male_transport_jux4_nhe50[6]

male_transport_number_reformed_jux5_nhe50[0] = male_transport_jux5_nhe50[0]+male_transport_jux5_nhe50[1]
male_transport_number_reformed_jux5_nhe50[1] = male_transport_long_jux5_nhe50[0]+male_transport_long_jux5_nhe50[1]
male_transport_number_reformed_jux5_nhe50[2] = male_transport_long_jux5_nhe50[2]
male_transport_number_reformed_jux5_nhe50[3] = male_transport_jux5_nhe50[3]+male_transport_jux5_nhe50[4]
male_transport_number_reformed_jux5_nhe50[4] = male_transport_jux5_nhe50[5]
male_transport_number_reformed_jux5_nhe50[5] = male_transport_jux5_nhe50[6]

#print(segment_transport,male_transport_number)
bar_width = 0.25
male_sup=axarr[3,2].bar(np.arange(len(segment_transport[:6])),[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i]+male_transport_number_reformed_jux5[i] for i in range(len(male_transport_number_reformed_sup))],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Non-diabetic')
#male_jux=axarr[0,1].bar(np.arange(len(segment_transport[:6])),[male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i]+male_transport_number_reformed_jux5[i] for i in range(len(male_transport_number_reformed_sup))],bar_width,bottom=male_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
#male_jux2=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux2,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='cyan',label='Male juxtamedullary type 2')
#male_jux3=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux3,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='darkturquoise',label='Male juxtamedullary type 3')
#male_jux4=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux4,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='powderblue',label='Male juxtamedullary type 4')
#male_jux5=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux5,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='deepskyblue',label='Male juxtamedullary type 5')
male_later=axarr[3,2].bar(np.arange(len(segment_transport)),male_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

male_sup_nhe50=axarr[3,2].bar(np.arange(len(segment_transport[:6]))+bar_width,[male_transport_number_reformed_sup_nhe50[i]+male_transport_number_reformed_jux1_nhe50[i]+male_transport_number_reformed_jux2_nhe50[i]+male_transport_number_reformed_jux3_nhe50[i]+male_transport_number_reformed_jux4_nhe50[i]+male_transport_number_reformed_jux5_nhe50[i] for i in range(len(male_transport_number_reformed_sup_nhe50))],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue',label='Moderate diabetic')
#male_jux=axarr[0,1].bar(np.arange(len(segment_transport[:6])),[male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i]+male_transport_number_reformed_jux5[i] for i in range(len(male_transport_number_reformed_sup))],bar_width,bottom=male_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
#male_jux2=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux2,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='cyan',label='Male juxtamedullary type 2')
#male_jux3=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux3,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='darkturquoise',label='Male juxtamedullary type 3')
#male_jux4=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux4,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='powderblue',label='Male juxtamedullary type 4')
#male_jux5=ax.bar(np.arange(len(segment_transport[:4])),male_transport_number_reformed_jux5,bar_width,bottom=[male_transport_number_reformed_sup[i]+male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i] for i in range(len(male_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='deepskyblue',label='Male juxtamedullary type 5')
male_later_nhe50=axarr[3,2].bar(np.arange(len(segment_transport))+bar_width,male_transport_number_reformed_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')


Female_sup=axarr[3,2].bar(np.arange(len(segment_transport[:6]))+2*bar_width,[female_transport_number_reformed_sup[i]+female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i]+female_transport_number_reformed_jux3[i]+female_transport_number_reformed_jux4[i]+female_transport_number_reformed_jux5[i] for i in range(len(female_transport_number_reformed_sup))],bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta',label='Severe diabetic')
#Female_jux=axarr[0,1].bar(np.arange(len(segment_transport[:6]))+bar_width,[female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i]+female_transport_number_reformed_jux3[i]+female_transport_number_reformed_jux4[i]+female_transport_number_reformed_jux5[i] for i in range(len(female_transport_number_reformed_sup))],bar_width,bottom=female_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
#Female_jux2=ax.bar(np.arange(len(segment_transport[:4]))+bar_width,female_transport_number_reformed_jux2,bar_width,bottom=[female_transport_number_reformed_sup[i]+female_transport_number_reformed_jux1[i] for i in range(len(female_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='violet',label='Female juxtamedullary type 2')
#Female_jux3=ax.bar(np.arange(len(segment_transport[:4]))+bar_width,female_transport_number_reformed_jux3,bar_width,bottom=[female_transport_number_reformed_sup[i]+female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i] for i in range(len(female_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='crimson',label='Female juxtamedullary type 3')
#Female_jux4=ax.bar(np.arange(len(segment_transport[:4]))+bar_width,female_transport_number_reformed_jux4,bar_width,bottom=[female_transport_number_reformed_sup[i]+female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i]+female_transport_number_reformed_jux3[i] for i in range(len(female_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='lavenderblush',label='Female juxtamedullary type 4')
#Female_jux5=ax.bar(np.arange(len(segment_transport[:4]))+bar_width,female_transport_number_reformed_jux5,bar_width,bottom=[female_transport_number_reformed_sup[i]+female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i]+female_transport_number_reformed_jux3[i]+female_transport_number_reformed_jux4[i] for i in range(len(female_transport_number_reformed_sup))],align='center',alpha=0.8,linewidth=2,color='deeppink',label='Female juxtamedullary type 5')
Female_later=axarr[3,2].bar(np.arange(len(segment_transport))+2*bar_width,female_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

axarr[3,2].set_xticks(np.arange(len(segment_transport))+0.5*bar_width)
axarr[3,2].set_xticklabels(segment_transport,fontsize=30)
axarr[3,2].tick_params(axis='both',labelsize=30)
#ax.set_xlabel('Segment',fontsize=20)
axarr[3,2].set_ylabel('Segmental volume transport (L/Day)',fontsize=30)

axarr[0,0].text(-0.6,axarr[0,0].get_ylim()[1],'A1',size=40,weight='bold')
axarr[0,1].text(-0.6,axarr[0,1].get_ylim()[1],'A2',size=40,weight='bold')
axarr[0,2].text(-1,axarr[0,2].get_ylim()[1],'A3',size=40,weight='bold')
axarr[1,0].text(-0.6,axarr[1,0].get_ylim()[1],'B1',size=40,weight='bold')
axarr[1,1].text(-0.6,axarr[1,1].get_ylim()[1],'B2',size=40,weight='bold')
axarr[1,2].text(-1,axarr[1,2].get_ylim()[1],'B3',size=40,weight='bold')
axarr[2,0].text(-0.6,axarr[2,0].get_ylim()[1],'C1',size=40,weight='bold')
axarr[2,1].text(-0.6,axarr[2,1].get_ylim()[1],'C2',size=40,weight='bold')
axarr[2,2].text(-1,axarr[2,2].get_ylim()[1],'C3',size=40,weight='bold')
axarr[3,0].text(-0.6,axarr[3,0].get_ylim()[1],'D1',size=40,weight='bold')
axarr[3,1].text(-0.6,axarr[3,1].get_ylim()[1],'D2',size=40,weight='bold')
axarr[3,2].text(-1,axarr[3,2].get_ylim()[1],'D3',size=40,weight='bold')

plt.savefig('Figure2',bbox_inches='tight')