import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np
import os
import argparse

segment = ['PT','DL','TAL','DCT','CNT','CCD','urine']

female_normal_file = './female_normal_check'
female_nhe50_file = './female_enac70_check'
female_nhe80_file = './female_enac100_check'

male_normal_file = './male_normal_check'
male_nhe50_file = './male_enac70_check'
male_nhe80_file = './male_enac100_check'

neph_weight = [2/3,(1/3)*0.4,(1/3)*0.3,(1/3)*0.15,(1/3)*0.1,(1/3)*0.05]

solute = ['Na','K','Cl','HCO3','H2CO3','CO2','HPO4','H2PO4','urea','NH3','NH4','H','HCO2','H2CO2','glu']
segment_early = ['pt','sdl','mtal','dct','cnt']
segment_late = ['ccd','imcd']

bar_width = 0.1
fig,axarr = plt.subplots(4,)
fig.set_figheight(60)
fig.set_figwidth(30)
fig.subplots_adjust(hspace = 0.06)
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
    file_sup = open(female_normal_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(female_normal_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_normal_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_normal_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_normal_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_normal_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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
    female_delivery_sup.append(neph_weight[0]*datalist_sup[0]*36000*10e-7)
    female_delivery_jux1.append(neph_weight[1]*datalist_jux1[0]*36000*10e-7)
    female_delivery_jux2.append(neph_weight[2]*datalist_jux2[0]*36000*10e-7)
    female_delivery_jux3.append(neph_weight[3]*datalist_jux3[0]*36000*10e-7)
    female_delivery_jux4.append(neph_weight[4]*datalist_jux4[0]*36000*10e-7)
    female_delivery_jux5.append(neph_weight[5]*datalist_jux5[0]*36000*10e-7)
    if seg == 'cnt':
        female_delivery_number.append(0)
        female_delivery_sup.append(neph_weight[0]*datalist_sup[-1]*36000*10e-7)
        female_delivery_jux1.append(neph_weight[1]*datalist_jux1[-1]*36000*10e-7)
        female_delivery_jux2.append(neph_weight[2]*datalist_jux2[-1]*36000*10e-7)
        female_delivery_jux3.append(neph_weight[3]*datalist_jux3[-1]*36000*10e-7)
        female_delivery_jux4.append(neph_weight[4]*datalist_jux4[-1]*36000*10e-7)
        female_delivery_jux5.append(neph_weight[5]*datalist_jux5[-1]*36000*10e-7)
for seg in segment_late:
    file_data = open(female_normal_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        female_delivery_number.append(number_of_delivery*36000*10e-7)
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
    file_sup = open(male_normal_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(male_normal_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_normal_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_normal_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_normal_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_normal_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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
    male_delivery_sup.append(neph_weight[0]*datalist_sup[0]*36000*10e-7)
    male_delivery_jux1.append(neph_weight[1]*datalist_jux1[0]*36000*10e-7)
    male_delivery_jux2.append(neph_weight[2]*datalist_jux2[0]*36000*10e-7)
    male_delivery_jux3.append(neph_weight[3]*datalist_jux3[0]*36000*10e-7)
    male_delivery_jux4.append(neph_weight[4]*datalist_jux4[0]*36000*10e-7)
    male_delivery_jux5.append(neph_weight[5]*datalist_jux5[0]*36000*10e-7)
    if seg == 'cnt':
        male_delivery_number.append(0)
        male_delivery_sup.append(neph_weight[0]*datalist_sup[-1]*36000*10e-7)
        male_delivery_jux1.append(neph_weight[1]*datalist_jux1[-1]*36000*10e-7)
        male_delivery_jux2.append(neph_weight[2]*datalist_jux2[-1]*36000*10e-7)
        male_delivery_jux3.append(neph_weight[3]*datalist_jux3[-1]*36000*10e-7)
        male_delivery_jux4.append(neph_weight[4]*datalist_jux4[-1]*36000*10e-7)
        male_delivery_jux5.append(neph_weight[5]*datalist_jux5[-1]*36000*10e-7)
for seg in segment_late:
    file_data = open(male_normal_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        male_delivery_number.append(number_of_delivery*36000*10e-7)
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
    file_sup = open(female_nhe50_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(female_nhe50_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_nhe50_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_nhe50_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_nhe50_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_nhe50_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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
    female_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[0]*36000*10e-7)
    female_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[0]*36000*10e-7)
    female_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[0]*36000*10e-7)
    female_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[0]*36000*10e-7)
    female_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[0]*36000*10e-7)
    female_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[0]*36000*10e-7)
    if seg == 'cnt':
        female_delivery_number_nhe50.append(0)
        female_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[-1]*36000*10e-7)
        female_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[-1]*36000*10e-7)
        female_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[-1]*36000*10e-7)
        female_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[-1]*36000*10e-7)
        female_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[-1]*36000*10e-7)
        female_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[-1]*36000*10e-7)
for seg in segment_late:
    file_data = open(female_nhe50_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        female_delivery_number_nhe50.append(number_of_delivery*36000*10e-7)
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
    file_sup = open(male_nhe50_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(male_nhe50_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe50_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe50_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe50_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe50_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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
    male_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[0]*36000*10e-7)
    male_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[0]*36000*10e-7)
    male_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[0]*36000*10e-7)
    male_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[0]*36000*10e-7)
    male_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[0]*36000*10e-7)
    male_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[0]*36000*10e-7)
    if seg == 'cnt':
        male_delivery_number_nhe50.append(0)
        male_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[-1]*36000*10e-7)
        male_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[-1]*36000*10e-7)
        male_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[-1]*36000*10e-7)
        male_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[-1]*36000*10e-7)
        male_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[-1]*36000*10e-7)
        male_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[-1]*36000*10e-7)
for seg in segment_late:
    file_data = open(male_nhe50_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        male_delivery_number_nhe50.append(number_of_delivery*36000*10e-7)
    else:
        number_of_delivery = datalist[0]
    #===================================
    # NHE3 80% inhibited
    #===================================
female_delivery_number_nhe80 = []
female_delivery_sup_nhe80 = []
female_delivery_jux1_nhe80 = []
female_delivery_jux2_nhe80 = []
female_delivery_jux3_nhe80 = []
female_delivery_jux4_nhe80 = []
female_delivery_jux5_nhe80 = []
for seg in segment_early:
    file_sup = open(female_nhe80_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(female_nhe80_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_nhe80_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_nhe80_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_nhe80_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_nhe80_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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
    female_delivery_number_nhe80.append(0)
    female_delivery_sup_nhe80.append(neph_weight[0]*datalist_sup[0]*36000*10e-7)
    female_delivery_jux1_nhe80.append(neph_weight[1]*datalist_jux1[0]*36000*10e-7)
    female_delivery_jux2_nhe80.append(neph_weight[2]*datalist_jux2[0]*36000*10e-7)
    female_delivery_jux3_nhe80.append(neph_weight[3]*datalist_jux3[0]*36000*10e-7)
    female_delivery_jux4_nhe80.append(neph_weight[4]*datalist_jux4[0]*36000*10e-7)
    female_delivery_jux5_nhe80.append(neph_weight[5]*datalist_jux5[0]*36000*10e-7)
    if seg == 'cnt':
        female_delivery_number_nhe80.append(0)
        female_delivery_sup_nhe80.append(neph_weight[0]*datalist_sup[-1]*36000*10e-7)
        female_delivery_jux1_nhe80.append(neph_weight[1]*datalist_jux1[-1]*36000*10e-7)
        female_delivery_jux2_nhe80.append(neph_weight[2]*datalist_jux2[-1]*36000*10e-7)
        female_delivery_jux3_nhe80.append(neph_weight[3]*datalist_jux3[-1]*36000*10e-7)
        female_delivery_jux4_nhe80.append(neph_weight[4]*datalist_jux4[-1]*36000*10e-7)
        female_delivery_jux5_nhe80.append(neph_weight[5]*datalist_jux5[-1]*36000*10e-7)
for seg in segment_late:
    file_data = open(female_nhe80_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        female_delivery_number_nhe80.append(number_of_delivery*36000*10e-7)
    else:
        number_of_delivery = datalist[0]
    

male_delivery_number_nhe80 = []
male_delivery_sup_nhe80 = []
male_delivery_jux1_nhe80 = []
male_delivery_jux2_nhe80 = []
male_delivery_jux3_nhe80 = []
male_delivery_jux4_nhe80 = []
male_delivery_jux5_nhe80 = []
for seg in segment_early:
    file_sup = open(male_nhe80_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(male_nhe80_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe80_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe80_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe80_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe80_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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
    male_delivery_number_nhe80.append(0)
    male_delivery_sup_nhe80.append(neph_weight[0]*datalist_sup[0]*36000*10e-7)
    male_delivery_jux1_nhe80.append(neph_weight[1]*datalist_jux1[0]*36000*10e-7)
    male_delivery_jux2_nhe80.append(neph_weight[2]*datalist_jux2[0]*36000*10e-7)
    male_delivery_jux3_nhe80.append(neph_weight[3]*datalist_jux3[0]*36000*10e-7)
    male_delivery_jux4_nhe80.append(neph_weight[4]*datalist_jux4[0]*36000*10e-7)
    male_delivery_jux5_nhe80.append(neph_weight[5]*datalist_jux5[0]*36000*10e-7)
    if seg == 'cnt':
        male_delivery_number_nhe80.append(0)
        male_delivery_sup_nhe80.append(neph_weight[0]*datalist_sup[-1]*36000*10e-7)
        male_delivery_jux1_nhe80.append(neph_weight[1]*datalist_jux1[-1]*36000*10e-7)
        male_delivery_jux2_nhe80.append(neph_weight[2]*datalist_jux2[-1]*36000*10e-7)
        male_delivery_jux3_nhe80.append(neph_weight[3]*datalist_jux3[-1]*36000*10e-7)
        male_delivery_jux4_nhe80.append(neph_weight[4]*datalist_jux4[-1]*36000*10e-7)
        male_delivery_jux5_nhe80.append(neph_weight[5]*datalist_jux5[-1]*36000*10e-7)
for seg in segment_late:
    file_data = open(male_nhe80_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        male_delivery_number_nhe80.append(number_of_delivery*36000*10e-7)
    else:
        number_of_delivery = datalist[0]

male_delivery_sup = male_delivery_sup[4:]
male_delivery_jux1 = male_delivery_jux1[4:]
male_delivery_jux2 = male_delivery_jux2[4:]
male_delivery_jux3 = male_delivery_jux3[4:]
male_delivery_jux4 = male_delivery_jux4[4:]
male_delivery_jux5 = male_delivery_jux5[4:]
male_delivery_sup_nhe50 = male_delivery_sup_nhe50[4:]
male_delivery_jux1_nhe50 = male_delivery_jux1_nhe50[4:]
male_delivery_jux2_nhe50 = male_delivery_jux2_nhe50[4:]
male_delivery_jux3_nhe50 = male_delivery_jux3_nhe50[4:]
male_delivery_jux4_nhe50 = male_delivery_jux4_nhe50[4:]
male_delivery_jux5_nhe50 = male_delivery_jux5_nhe50[4:]
male_delivery_sup_nhe80 = male_delivery_sup_nhe80[4:]
male_delivery_jux1_nhe80 = male_delivery_jux1_nhe80[4:]
male_delivery_jux2_nhe80 = male_delivery_jux2_nhe80[4:]
male_delivery_jux3_nhe80 = male_delivery_jux3_nhe80[4:]
male_delivery_jux4_nhe80 = male_delivery_jux4_nhe80[4:]
male_delivery_jux5_nhe80 = male_delivery_jux5_nhe80[4:]
male_delivery_number = male_delivery_number[4:]
male_delivery_number_nhe50 = male_delivery_number_nhe50[4:]
male_delivery_number_nhe80 = male_delivery_number_nhe80[4:]

female_delivery_sup = female_delivery_sup[4:]
female_delivery_jux1 = female_delivery_jux1[4:]
female_delivery_jux2 = female_delivery_jux2[4:]
female_delivery_jux3 = female_delivery_jux3[4:]
female_delivery_jux4 = female_delivery_jux4[4:]
female_delivery_jux5 = female_delivery_jux5[4:]
female_delivery_sup_nhe50 = female_delivery_sup_nhe50[4:]
female_delivery_jux1_nhe50 = female_delivery_jux1_nhe50[4:]
female_delivery_jux2_nhe50 = female_delivery_jux2_nhe50[4:]
female_delivery_jux3_nhe50 = female_delivery_jux3_nhe50[4:]
female_delivery_jux4_nhe50 = female_delivery_jux4_nhe50[4:]
female_delivery_jux5_nhe50 = female_delivery_jux5_nhe50[4:]
female_delivery_sup_nhe80 = female_delivery_sup_nhe80[4:]
female_delivery_jux1_nhe80 = female_delivery_jux1_nhe80[4:]
female_delivery_jux2_nhe80 = female_delivery_jux2_nhe80[4:]
female_delivery_jux3_nhe80 = female_delivery_jux3_nhe80[4:]
female_delivery_jux4_nhe80 = female_delivery_jux4_nhe80[4:]
female_delivery_jux5_nhe80 = female_delivery_jux5_nhe80[4:]
female_delivery_number = female_delivery_number[4:]
female_delivery_number_nhe50 = female_delivery_number_nhe50[4:]
female_delivery_number_nhe80 = female_delivery_number_nhe80[4:]

male_sup=axarr[0].bar(np.arange(len(segment[4:6])),male_delivery_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Male Baseline')
male_jux=axarr[0].bar(np.arange(len(segment[4:6])),[male_delivery_jux1[i]+male_delivery_jux2[i]+male_delivery_jux3[i]+male_delivery_jux4[i]+male_delivery_jux5[i] for i in range(len(male_delivery_sup))],bar_width,bottom=male_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later=axarr[0].bar(np.arange(len(segment[4:])),male_delivery_number,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

male_sup_nhe50=axarr[0].bar(np.arange(len(segment[4:6]))+bar_width,male_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue',label='Male 70% ENaC inhib')
male_jux_nhe50=axarr[0].bar(np.arange(len(segment[4:6]))+bar_width,[male_delivery_jux1_nhe50[i]+male_delivery_jux2_nhe50[i]+male_delivery_jux3_nhe50[i]+male_delivery_jux4_nhe50[i]+male_delivery_jux5_nhe50[i] for i in range(len(male_delivery_sup_nhe50))],bar_width,bottom=male_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later_nhe50=axarr[0].bar(np.arange(len(segment[4:]))+bar_width,male_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

male_sup_nhe80=axarr[0].bar(np.arange(len(segment[4:6]))+2*bar_width,male_delivery_sup_nhe80,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='paleturquoise',label='Male 100% ENaC inhib')
male_jux_nhe80=axarr[0].bar(np.arange(len(segment[4:6]))+2*bar_width,[male_delivery_jux1_nhe80[i]+male_delivery_jux2_nhe80[i]+male_delivery_jux3_nhe80[i]+male_delivery_jux4_nhe80[i]+male_delivery_jux5_nhe80[i] for i in range(len(male_delivery_sup_nhe80))],bar_width,bottom=male_delivery_sup_nhe80,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later_nhe80=axarr[0].bar(np.arange(len(segment[4:]))+2*bar_width,male_delivery_number_nhe80,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='paleturquoise')

Female_sup=axarr[0].bar(np.arange(len(segment[4:6]))+3*bar_width,female_delivery_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')
Female_jux=axarr[0].bar(np.arange(len(segment[4:6]))+3*bar_width,[female_delivery_jux1[i]+female_delivery_jux2[i]+female_delivery_jux3[i]+female_delivery_jux4[i]+female_delivery_jux5[i] for i in range(len(female_delivery_sup))],bar_width,bottom=female_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
Female_later=axarr[0].bar(np.arange(len(segment[4:]))+3*bar_width,female_delivery_number,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

Female_sup_nhe50=axarr[0].bar(np.arange(len(segment[4:6]))+4*bar_width,female_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')
Female_jux_nhe50=axarr[0].bar(np.arange(len(segment[4:6]))+4*bar_width,[female_delivery_jux1_nhe50[i]+female_delivery_jux2_nhe50[i]+female_delivery_jux3_nhe50[i]+female_delivery_jux4_nhe50[i]+female_delivery_jux5_nhe50[i] for i in range(len(female_delivery_sup_nhe50))],bar_width,bottom=female_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
Female_later_nhe50=axarr[0].bar(np.arange(len(segment[4:]))+4*bar_width,female_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')

Female_sup_nhe80=axarr[0].bar(np.arange(len(segment[4:6]))+5*bar_width,female_delivery_sup_nhe80,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='pink')
Female_jux_nhe80=axarr[0].bar(np.arange(len(segment[4:6]))+5*bar_width,[female_delivery_jux1_nhe80[i]+female_delivery_jux2_nhe80[i]+female_delivery_jux3_nhe80[i]+female_delivery_jux4_nhe80[i]+female_delivery_jux5_nhe80[i] for i in range(len(female_delivery_sup_nhe80))],bar_width,bottom=female_delivery_sup_nhe80,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
Female_later_nhe80=axarr[0].bar(np.arange(len(segment[4:]))+5*bar_width,female_delivery_number_nhe80,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='pink')

axarr[0].set_xticks(np.arange(len(segment[4:]))+2.5*bar_width)
axarr[0].set_xticklabels(segment[4:],fontsize=40)
axarr[0].tick_params(axis='both',labelsize=40)
#axarr[0].set_title('ENaC inhibitions',fontsize = 50)
#ax.set_xlabel('Segment',fontsize=20)
axarr[0].set_ylabel('Na$^+$ delivery ($\mu$mol/min)',fontsize=40)
axarr[0].legend(fontsize=40,markerscale=40)

# bar_width_ins = bar_width
# axins = inset_axes(axarr[0,0],width=3.5,height=3.5,loc=7)

# male_sup_inset=axins.bar(np.arange(len(segment[:6])),male_delivery_sup,bar_width_ins,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Male')
# male_jux_inset=axins.bar(np.arange(len(segment[:6])),[male_delivery_jux1[i]+male_delivery_jux2[i]+male_delivery_jux3[i]+male_delivery_jux4[i]+male_delivery_jux5[i] for i in range(len(male_delivery_sup))],bar_width_ins,bottom=male_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# male_later_inset=axins.bar(np.arange(len(segment)),male_delivery_number,bar_width_ins,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

# male_sup_nhe50_inset=axins.bar(np.arange(len(segment[:6]))+bar_width,male_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue',label='70% ENaC inhib')
# male_jux_nhe50_inset=axins.bar(np.arange(len(segment[:6]))+bar_width,[male_delivery_jux1_nhe50[i]+male_delivery_jux2_nhe50[i]+male_delivery_jux3_nhe50[i]+male_delivery_jux4_nhe50[i]+male_delivery_jux5_nhe50[i] for i in range(len(male_delivery_sup_nhe50))],bar_width,bottom=male_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# male_later_nhe50_inset=axins.bar(np.arange(len(segment))+bar_width,male_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

# male_sup_nhe80_inset=axins.bar(np.arange(len(segment[:6]))+2*bar_width,male_delivery_sup_nhe80,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='paleturquoise',label='100% ENaC inhib')
# male_jux_nhe80_inset=axins.bar(np.arange(len(segment[:6]))+2*bar_width,[male_delivery_jux1_nhe80[i]+male_delivery_jux2_nhe80[i]+male_delivery_jux3_nhe80[i]+male_delivery_jux4_nhe80[i]+male_delivery_jux5_nhe80[i] for i in range(len(male_delivery_sup_nhe80))],bar_width,bottom=male_delivery_sup_nhe80,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# male_later_nhe80_inset=axins.bar(np.arange(len(segment))+2*bar_width,male_delivery_number_nhe80,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='paleturquoise')

# axins.set_xticks(np.arange(len(segment))+1*bar_width_ins)
# axins.set_xticklabels(segment,fontsize=40)
# axins.set_xlim(5-1.5*bar_width_ins,6+3*bar_width_ins)
# axins.set_ylim(0,15)
# axins.tick_params(axis='both',labelsize=40)

# bar_width_ins = bar_width
# axins = inset_axes(axarr[0,1],width=3.5,height=3.5,loc=7)

# Female_sup_inset=axins.bar(np.arange(len(segment[:6])),female_delivery_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta',label='Baseline')
# Female_jux_inset=axins.bar(np.arange(len(segment[:6])),[female_delivery_jux1[i]+female_delivery_jux2[i]+female_delivery_jux3[i]+female_delivery_jux4[i]+female_delivery_jux5[i] for i in range(len(female_delivery_sup))],bar_width,bottom=female_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# Female_later_inset=axins.bar(np.arange(len(segment)),female_delivery_number,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

# Female_sup_nhe50_inset=axins.bar(np.arange(len(segment[:6]))+1*bar_width,female_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink',label='70% ENaC inhib')
# Female_jux_nhe50_inset=axins.bar(np.arange(len(segment[:6]))+1*bar_width,[female_delivery_jux1_nhe50[i]+female_delivery_jux2_nhe50[i]+female_delivery_jux3_nhe50[i]+female_delivery_jux4_nhe50[i]+female_delivery_jux5_nhe50[i] for i in range(len(female_delivery_sup_nhe50))],bar_width,bottom=female_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# Female_later_nhe50_inset=axins.bar(np.arange(len(segment))+1*bar_width,female_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')

# Female_sup_nhe80_inset=axins.bar(np.arange(len(segment[:6]))+2*bar_width,female_delivery_sup_nhe80,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='pink',label='100% ENaC inhib')
# Female_jux_nhe80_inset=axins.bar(np.arange(len(segment[:6]))+2*bar_width,[female_delivery_jux1_nhe80[i]+female_delivery_jux2_nhe80[i]+female_delivery_jux3_nhe80[i]+female_delivery_jux4_nhe80[i]+female_delivery_jux5_nhe80[i] for i in range(len(female_delivery_sup_nhe80))],bar_width,bottom=female_delivery_sup_nhe80,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
# Female_later_nhe80_inset=axins.bar(np.arange(len(segment))+2*bar_width,female_delivery_number_nhe80,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='pink')

# axins.set_xticks(np.arange(len(segment))+1*bar_width_ins)
# axins.set_xticklabels(segment,fontsize=40)
# axins.set_xlim(5-1.5*bar_width_ins,6+3*bar_width_ins)
# axins.set_ylim(0,15)
# axins.tick_params(axis='both',labelsize=40)



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
    file_sup = open(female_normal_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(female_normal_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_normal_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_normal_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_normal_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_normal_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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
    female_delivery_sup.append(neph_weight[0]*datalist_sup[0]*36000*10e-7)
    female_delivery_jux1.append(neph_weight[1]*datalist_jux1[0]*36000*10e-7)
    female_delivery_jux2.append(neph_weight[2]*datalist_jux2[0]*36000*10e-7)
    female_delivery_jux3.append(neph_weight[3]*datalist_jux3[0]*36000*10e-7)
    female_delivery_jux4.append(neph_weight[4]*datalist_jux4[0]*36000*10e-7)
    female_delivery_jux5.append(neph_weight[5]*datalist_jux5[0]*36000*10e-7)
    if seg == 'cnt':
        female_delivery_number.append(0)
        female_delivery_sup.append(neph_weight[0]*datalist_sup[-1]*36000*10e-7)
        female_delivery_jux1.append(neph_weight[1]*datalist_jux1[-1]*36000*10e-7)
        female_delivery_jux2.append(neph_weight[2]*datalist_jux2[-1]*36000*10e-7)
        female_delivery_jux3.append(neph_weight[3]*datalist_jux3[-1]*36000*10e-7)
        female_delivery_jux4.append(neph_weight[4]*datalist_jux4[-1]*36000*10e-7)
        female_delivery_jux5.append(neph_weight[5]*datalist_jux5[-1]*36000*10e-7)
for seg in segment_late:
    file_data = open(female_normal_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        female_delivery_number.append(number_of_delivery*36000*10e-7)
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
    file_sup = open(male_normal_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(male_normal_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_normal_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_normal_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_normal_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_normal_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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
    male_delivery_sup.append(neph_weight[0]*datalist_sup[0]*36000*10e-7)
    male_delivery_jux1.append(neph_weight[1]*datalist_jux1[0]*36000*10e-7)
    male_delivery_jux2.append(neph_weight[2]*datalist_jux2[0]*36000*10e-7)
    male_delivery_jux3.append(neph_weight[3]*datalist_jux3[0]*36000*10e-7)
    male_delivery_jux4.append(neph_weight[4]*datalist_jux4[0]*36000*10e-7)
    male_delivery_jux5.append(neph_weight[5]*datalist_jux5[0]*36000*10e-7)
    if seg == 'cnt':
        male_delivery_number.append(0)
        male_delivery_sup.append(neph_weight[0]*datalist_sup[-1]*36000*10e-7)
        male_delivery_jux1.append(neph_weight[1]*datalist_jux1[-1]*36000*10e-7)
        male_delivery_jux2.append(neph_weight[2]*datalist_jux2[-1]*36000*10e-7)
        male_delivery_jux3.append(neph_weight[3]*datalist_jux3[-1]*36000*10e-7)
        male_delivery_jux4.append(neph_weight[4]*datalist_jux4[-1]*36000*10e-7)
        male_delivery_jux5.append(neph_weight[5]*datalist_jux5[-1]*36000*10e-7)
for seg in segment_late:
    file_data = open(male_normal_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        male_delivery_number.append(number_of_delivery*36000*10e-7)
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
    file_sup = open(female_nhe50_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(female_nhe50_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_nhe50_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_nhe50_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_nhe50_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_nhe50_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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
    female_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[0]*36000*10e-7)
    female_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[0]*36000*10e-7)
    female_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[0]*36000*10e-7)
    female_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[0]*36000*10e-7)
    female_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[0]*36000*10e-7)
    female_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[0]*36000*10e-7)
    if seg == 'cnt':
        female_delivery_number_nhe50.append(0)
        female_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[-1]*36000*10e-7)
        female_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[-1]*36000*10e-7)
        female_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[-1]*36000*10e-7)
        female_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[-1]*36000*10e-7)
        female_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[-1]*36000*10e-7)
        female_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[-1]*36000*10e-7)
for seg in segment_late:
    file_data = open(female_nhe50_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        female_delivery_number_nhe50.append(number_of_delivery*36000*10e-7)
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
    file_sup = open(male_nhe50_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(male_nhe50_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe50_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe50_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe50_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe50_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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
    male_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[0]*36000*10e-7)
    male_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[0]*36000*10e-7)
    male_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[0]*36000*10e-7)
    male_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[0]*36000*10e-7)
    male_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[0]*36000*10e-7)
    male_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[0]*36000*10e-7)
    if seg == 'cnt':
        male_delivery_number_nhe50.append(0)
        male_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[-1]*36000*10e-7)
        male_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[-1]*36000*10e-7)
        male_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[-1]*36000*10e-7)
        male_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[-1]*36000*10e-7)
        male_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[-1]*36000*10e-7)
        male_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[-1]*36000*10e-7)
for seg in segment_late:
    file_data = open(male_nhe50_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        male_delivery_number_nhe50.append(number_of_delivery*36000*10e-7)
    else:
        number_of_delivery = datalist[0]
    #===================================
    # NHE3 80% inhibited
    #===================================
female_delivery_number_nhe80 = []
female_delivery_sup_nhe80 = []
female_delivery_jux1_nhe80 = []
female_delivery_jux2_nhe80 = []
female_delivery_jux3_nhe80 = []
female_delivery_jux4_nhe80 = []
female_delivery_jux5_nhe80 = []
for seg in segment_early:
    file_sup = open(female_nhe80_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(female_nhe80_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_nhe80_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_nhe80_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_nhe80_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_nhe80_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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
    female_delivery_number_nhe80.append(0)
    female_delivery_sup_nhe80.append(neph_weight[0]*datalist_sup[0]*36000*10e-7)
    female_delivery_jux1_nhe80.append(neph_weight[1]*datalist_jux1[0]*36000*10e-7)
    female_delivery_jux2_nhe80.append(neph_weight[2]*datalist_jux2[0]*36000*10e-7)
    female_delivery_jux3_nhe80.append(neph_weight[3]*datalist_jux3[0]*36000*10e-7)
    female_delivery_jux4_nhe80.append(neph_weight[4]*datalist_jux4[0]*36000*10e-7)
    female_delivery_jux5_nhe80.append(neph_weight[5]*datalist_jux5[0]*36000*10e-7)
    if seg == 'cnt':
        female_delivery_number_nhe80.append(0)
        female_delivery_sup_nhe80.append(neph_weight[0]*datalist_sup[-1]*36000*10e-7)
        female_delivery_jux1_nhe80.append(neph_weight[1]*datalist_jux1[-1]*36000*10e-7)
        female_delivery_jux2_nhe80.append(neph_weight[2]*datalist_jux2[-1]*36000*10e-7)
        female_delivery_jux3_nhe80.append(neph_weight[3]*datalist_jux3[-1]*36000*10e-7)
        female_delivery_jux4_nhe80.append(neph_weight[4]*datalist_jux4[-1]*36000*10e-7)
        female_delivery_jux5_nhe80.append(neph_weight[5]*datalist_jux5[-1]*36000*10e-7)
for seg in segment_late:
    file_data = open(female_nhe80_file+'/female'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        female_delivery_number_nhe80.append(number_of_delivery*36000*10e-7)
    else:
        number_of_delivery = datalist[0]
    

male_delivery_number_nhe80 = []
male_delivery_sup_nhe80 = []
male_delivery_jux1_nhe80 = []
male_delivery_jux2_nhe80 = []
male_delivery_jux3_nhe80 = []
male_delivery_jux4_nhe80 = []
male_delivery_jux5_nhe80 = []
for seg in segment_early:
    file_sup = open(male_nhe80_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_sup.txt','r')
    file_jux1 = open(male_nhe80_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe80_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe80_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe80_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe80_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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
    male_delivery_number_nhe80.append(0)
    male_delivery_sup_nhe80.append(neph_weight[0]*datalist_sup[0]*36000*10e-7)
    male_delivery_jux1_nhe80.append(neph_weight[1]*datalist_jux1[0]*36000*10e-7)
    male_delivery_jux2_nhe80.append(neph_weight[2]*datalist_jux2[0]*36000*10e-7)
    male_delivery_jux3_nhe80.append(neph_weight[3]*datalist_jux3[0]*36000*10e-7)
    male_delivery_jux4_nhe80.append(neph_weight[4]*datalist_jux4[0]*36000*10e-7)
    male_delivery_jux5_nhe80.append(neph_weight[5]*datalist_jux5[0]*36000*10e-7)
    if seg == 'cnt':
        male_delivery_number_nhe80.append(0)
        male_delivery_sup_nhe80.append(neph_weight[0]*datalist_sup[-1]*36000*10e-7)
        male_delivery_jux1_nhe80.append(neph_weight[1]*datalist_jux1[-1]*36000*10e-7)
        male_delivery_jux2_nhe80.append(neph_weight[2]*datalist_jux2[-1]*36000*10e-7)
        male_delivery_jux3_nhe80.append(neph_weight[3]*datalist_jux3[-1]*36000*10e-7)
        male_delivery_jux4_nhe80.append(neph_weight[4]*datalist_jux4[-1]*36000*10e-7)
        male_delivery_jux5_nhe80.append(neph_weight[5]*datalist_jux5[-1]*36000*10e-7)
for seg in segment_late:
    file_data = open(male_nhe80_file+'/male'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        male_delivery_number_nhe80.append(number_of_delivery*36000*10e-7)
    else:
        number_of_delivery = datalist[0]

male_delivery_sup = male_delivery_sup[4:]
male_delivery_jux1 = male_delivery_jux1[4:]
male_delivery_jux2 = male_delivery_jux2[4:]
male_delivery_jux3 = male_delivery_jux3[4:]
male_delivery_jux4 = male_delivery_jux4[4:]
male_delivery_jux5 = male_delivery_jux5[4:]
male_delivery_sup_nhe50 = male_delivery_sup_nhe50[4:]
male_delivery_jux1_nhe50 = male_delivery_jux1_nhe50[4:]
male_delivery_jux2_nhe50 = male_delivery_jux2_nhe50[4:]
male_delivery_jux3_nhe50 = male_delivery_jux3_nhe50[4:]
male_delivery_jux4_nhe50 = male_delivery_jux4_nhe50[4:]
male_delivery_jux5_nhe50 = male_delivery_jux5_nhe50[4:]
male_delivery_sup_nhe80 = male_delivery_sup_nhe80[4:]
male_delivery_jux1_nhe80 = male_delivery_jux1_nhe80[4:]
male_delivery_jux2_nhe80 = male_delivery_jux2_nhe80[4:]
male_delivery_jux3_nhe80 = male_delivery_jux3_nhe80[4:]
male_delivery_jux4_nhe80 = male_delivery_jux4_nhe80[4:]
male_delivery_jux5_nhe80 = male_delivery_jux5_nhe80[4:]
male_delivery_number = male_delivery_number[4:]
male_delivery_number_nhe50 = male_delivery_number_nhe50[4:]
male_delivery_number_nhe80 = male_delivery_number_nhe80[4:]

female_delivery_sup = female_delivery_sup[4:]
female_delivery_jux1 = female_delivery_jux1[4:]
female_delivery_jux2 = female_delivery_jux2[4:]
female_delivery_jux3 = female_delivery_jux3[4:]
female_delivery_jux4 = female_delivery_jux4[4:]
female_delivery_jux5 = female_delivery_jux5[4:]
female_delivery_sup_nhe50 = female_delivery_sup_nhe50[4:]
female_delivery_jux1_nhe50 = female_delivery_jux1_nhe50[4:]
female_delivery_jux2_nhe50 = female_delivery_jux2_nhe50[4:]
female_delivery_jux3_nhe50 = female_delivery_jux3_nhe50[4:]
female_delivery_jux4_nhe50 = female_delivery_jux4_nhe50[4:]
female_delivery_jux5_nhe50 = female_delivery_jux5_nhe50[4:]
female_delivery_sup_nhe80 = female_delivery_sup_nhe80[4:]
female_delivery_jux1_nhe80 = female_delivery_jux1_nhe80[4:]
female_delivery_jux2_nhe80 = female_delivery_jux2_nhe80[4:]
female_delivery_jux3_nhe80 = female_delivery_jux3_nhe80[4:]
female_delivery_jux4_nhe80 = female_delivery_jux4_nhe80[4:]
female_delivery_jux5_nhe80 = female_delivery_jux5_nhe80[4:]
female_delivery_number = female_delivery_number[4:]
female_delivery_number_nhe50 = female_delivery_number_nhe50[4:]
female_delivery_number_nhe80 = female_delivery_number_nhe80[4:]

male_sup=axarr[1].bar(np.arange(len(segment[4:6])),male_delivery_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')
male_jux=axarr[1].bar(np.arange(len(segment[4:6])),[male_delivery_jux1[i]+male_delivery_jux2[i]+male_delivery_jux3[i]+male_delivery_jux4[i]+male_delivery_jux5[i] for i in range(len(male_delivery_sup))],bar_width,bottom=male_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later=axarr[1].bar(np.arange(len(segment[4:])),male_delivery_number,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

male_sup_nhe50=axarr[1].bar(np.arange(len(segment[4:6]))+bar_width,male_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')
male_jux_nhe50=axarr[1].bar(np.arange(len(segment[4:6]))+bar_width,[male_delivery_jux1_nhe50[i]+male_delivery_jux2_nhe50[i]+male_delivery_jux3_nhe50[i]+male_delivery_jux4_nhe50[i]+male_delivery_jux5_nhe50[i] for i in range(len(male_delivery_sup_nhe50))],bar_width,bottom=male_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later_nhe50=axarr[1].bar(np.arange(len(segment[4:]))+bar_width,male_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

male_sup_nhe80=axarr[1].bar(np.arange(len(segment[4:6]))+2*bar_width,male_delivery_sup_nhe80,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='paleturquoise')
male_jux_nhe80=axarr[1].bar(np.arange(len(segment[4:6]))+2*bar_width,[male_delivery_jux1_nhe80[i]+male_delivery_jux2_nhe80[i]+male_delivery_jux3_nhe80[i]+male_delivery_jux4_nhe80[i]+male_delivery_jux5_nhe80[i] for i in range(len(male_delivery_sup_nhe80))],bar_width,bottom=male_delivery_sup_nhe80,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later_nhe80=axarr[1].bar(np.arange(len(segment[4:]))+2*bar_width,male_delivery_number_nhe80,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='paleturquoise')

Female_sup=axarr[1].bar(np.arange(len(segment[4:6]))+3*bar_width,female_delivery_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta',label='Female Baseline')
Female_jux=axarr[1].bar(np.arange(len(segment[4:6]))+3*bar_width,[female_delivery_jux1[i]+female_delivery_jux2[i]+female_delivery_jux3[i]+female_delivery_jux4[i]+female_delivery_jux5[i] for i in range(len(female_delivery_sup))],bar_width,bottom=female_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
Female_later=axarr[1].bar(np.arange(len(segment[4:]))+3*bar_width,female_delivery_number,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

Female_sup_nhe50=axarr[1].bar(np.arange(len(segment[4:6]))+4*bar_width,female_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink',label='Female 70% ENaC inhib')
Female_jux_nhe50=axarr[1].bar(np.arange(len(segment[4:6]))+4*bar_width,[female_delivery_jux1_nhe50[i]+female_delivery_jux2_nhe50[i]+female_delivery_jux3_nhe50[i]+female_delivery_jux4_nhe50[i]+female_delivery_jux5_nhe50[i] for i in range(len(female_delivery_sup_nhe50))],bar_width,bottom=female_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
Female_later_nhe50=axarr[1].bar(np.arange(len(segment[4:]))+4*bar_width,female_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')

Female_sup_nhe80=axarr[1].bar(np.arange(len(segment[4:6]))+5*bar_width,female_delivery_sup_nhe80,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='pink',label='Female 100% ENaC inhib')
Female_jux_nhe80=axarr[1].bar(np.arange(len(segment[4:6]))+5*bar_width,[female_delivery_jux1_nhe80[i]+female_delivery_jux2_nhe80[i]+female_delivery_jux3_nhe80[i]+female_delivery_jux4_nhe80[i]+female_delivery_jux5_nhe80[i] for i in range(len(female_delivery_sup_nhe80))],bar_width,bottom=female_delivery_sup_nhe80,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
Female_later_nhe80=axarr[1].bar(np.arange(len(segment[4:]))+5*bar_width,female_delivery_number_nhe80,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='pink')

axarr[1].set_xticks(np.arange(len(segment[4:]))+2.5*bar_width)
axarr[1].set_xticklabels(segment[4:],fontsize=40)
axarr[1].tick_params(axis='both',labelsize=40)
#axarr[1].set_ylim(0,17)
#axarr[0].set_title('Male',fontsize = 50)
#ax.set_xlabel('Segment',fontsize=20)
axarr[1].set_ylabel('K$^+$ delivery ($\mu$mol/min)',fontsize=40)
axarr[1].legend(fontsize=40,markerscale=40)

#===================================================
#  TA
#===================================================

female_delivery_number = []
female_delivery_sup = []
female_delivery_jux1 = []
female_delivery_jux2 = []
female_delivery_jux3 = []
female_delivery_jux4 = []
female_delivery_jux5 = []
for seg in segment_early:
    file_sup = open(female_normal_file+'/female'+seg+'_flow_of_H2PO4_in_Lumen_sup.txt','r')
    file_jux1 = open(female_normal_file+'/female'+seg+'_flow_of_H2PO4_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_normal_file+'/female'+seg+'_flow_of_H2PO4_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_normal_file+'/female'+seg+'_flow_of_H2PO4_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_normal_file+'/female'+seg+'_flow_of_H2PO4_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_normal_file+'/female'+seg+'_flow_of_H2PO4_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    file_sup_2 = open(female_normal_file+'/female'+seg+'_flow_of_HPO4_in_Lumen_sup.txt','r')
    file_jux1_2 = open(female_normal_file+'/female'+seg+'_flow_of_HPO4_in_Lumen_jux1.txt','r')
    file_jux2_2 = open(female_normal_file+'/female'+seg+'_flow_of_HPO4_in_Lumen_jux2.txt','r')
    file_jux3_2 = open(female_normal_file+'/female'+seg+'_flow_of_HPO4_in_Lumen_jux3.txt','r')
    file_jux4_2 = open(female_normal_file+'/female'+seg+'_flow_of_HPO4_in_Lumen_jux4.txt','r')
    file_jux5_2 = open(female_normal_file+'/female'+seg+'_flow_of_HPO4_in_Lumen_jux5.txt','r')
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
    female_delivery_sup.append(neph_weight[0]*(10**(7.4-6.8)*datalist_sup[0]-datalist_sup_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    female_delivery_jux1.append(neph_weight[1]*(10**(7.4-6.8)*datalist_jux1[0]-datalist_jux1_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    female_delivery_jux2.append(neph_weight[2]*(10**(7.4-6.8)*datalist_jux2[0]-datalist_jux2_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    female_delivery_jux3.append(neph_weight[3]*(10**(7.4-6.8)*datalist_jux3[0]-datalist_jux3_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    female_delivery_jux4.append(neph_weight[4]*(10**(7.4-6.8)*datalist_jux4[0]-datalist_jux4_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    female_delivery_jux5.append(neph_weight[5]*(10**(7.4-6.8)*datalist_jux5[0]-datalist_jux5_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    if seg == 'cnt':
        female_delivery_number.append(0)
        female_delivery_sup.append(neph_weight[0]*(10**(7.4-6.8)*datalist_sup[0]-datalist_sup_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        female_delivery_jux1.append(neph_weight[1]*(10**(7.4-6.8)*datalist_jux1[0]-datalist_jux1_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        female_delivery_jux2.append(neph_weight[2]*(10**(7.4-6.8)*datalist_jux2[0]-datalist_jux2_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        female_delivery_jux3.append(neph_weight[3]*(10**(7.4-6.8)*datalist_jux3[0]-datalist_jux3_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        female_delivery_jux4.append(neph_weight[4]*(10**(7.4-6.8)*datalist_jux4[0]-datalist_jux4_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        female_delivery_jux5.append(neph_weight[5]*(10**(7.4-6.8)*datalist_jux5[0]-datalist_jux5_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
for seg in segment_late:
    file_data = open(female_normal_file+'/female'+seg+'_flow_of_H2PO4_in_Lumen.txt','r')
    file_data_2 = open(female_normal_file+'/female'+seg+'_flow_of_HPO4_in_Lumen.txt','r')
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
        female_delivery_number.append(number_of_delivery*36000*10e-7)
        print(number_of_delivery*36000*10e-7)
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
    file_sup = open(male_normal_file+'/male'+seg+'_flow_of_H2PO4_in_Lumen_sup.txt','r')
    file_jux1 = open(male_normal_file+'/male'+seg+'_flow_of_H2PO4_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_normal_file+'/male'+seg+'_flow_of_H2PO4_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_normal_file+'/male'+seg+'_flow_of_H2PO4_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_normal_file+'/male'+seg+'_flow_of_H2PO4_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_normal_file+'/male'+seg+'_flow_of_H2PO4_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    file_sup_2 = open(male_normal_file+'/male'+seg+'_flow_of_HPO4_in_Lumen_sup.txt','r')
    file_jux1_2 = open(male_normal_file+'/male'+seg+'_flow_of_HPO4_in_Lumen_jux1.txt','r')
    file_jux2_2 = open(male_normal_file+'/male'+seg+'_flow_of_HPO4_in_Lumen_jux2.txt','r')
    file_jux3_2 = open(male_normal_file+'/male'+seg+'_flow_of_HPO4_in_Lumen_jux3.txt','r')
    file_jux4_2 = open(male_normal_file+'/male'+seg+'_flow_of_HPO4_in_Lumen_jux4.txt','r')
    file_jux5_2 = open(male_normal_file+'/male'+seg+'_flow_of_HPO4_in_Lumen_jux5.txt','r')
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
    male_delivery_sup.append(neph_weight[0]*(10**(7.4-6.8)*datalist_sup[0]-datalist_sup_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    male_delivery_jux1.append(neph_weight[1]*(10**(7.4-6.8)*datalist_jux1[0]-datalist_jux1_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    male_delivery_jux2.append(neph_weight[2]*(10**(7.4-6.8)*datalist_jux2[0]-datalist_jux2_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    male_delivery_jux3.append(neph_weight[3]*(10**(7.4-6.8)*datalist_jux3[0]-datalist_jux3_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    male_delivery_jux4.append(neph_weight[4]*(10**(7.4-6.8)*datalist_jux4[0]-datalist_jux4_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    male_delivery_jux5.append(neph_weight[5]*(10**(7.4-6.8)*datalist_jux5[0]-datalist_jux5_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    if seg == 'cnt':
        male_delivery_number.append(0)
        male_delivery_sup.append(neph_weight[0]*(10**(7.4-6.8)*datalist_sup[0]-datalist_sup_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        male_delivery_jux1.append(neph_weight[1]*(10**(7.4-6.8)*datalist_jux1[0]-datalist_jux1_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        male_delivery_jux2.append(neph_weight[2]*(10**(7.4-6.8)*datalist_jux2[0]-datalist_jux2_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        male_delivery_jux3.append(neph_weight[3]*(10**(7.4-6.8)*datalist_jux3[0]-datalist_jux3_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        male_delivery_jux4.append(neph_weight[4]*(10**(7.4-6.8)*datalist_jux4[0]-datalist_jux4_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        male_delivery_jux5.append(neph_weight[5]*(10**(7.4-6.8)*datalist_jux5[0]-datalist_jux5_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
for seg in segment_late:
    file_data = open(male_normal_file+'/male'+seg+'_flow_of_H2PO4_in_Lumen.txt','r')
    file_data_2 = open(male_normal_file+'/male'+seg+'_flow_of_HPO4_in_Lumen.txt','r')
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
        male_delivery_number.append(number_of_delivery*36000*10e-7)
        print(number_of_delivery*36000*10e-7)
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
    file_sup = open(female_nhe50_file+'/female'+seg+'_flow_of_H2PO4_in_Lumen_sup.txt','r')
    file_jux1 = open(female_nhe50_file+'/female'+seg+'_flow_of_H2PO4_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_nhe50_file+'/female'+seg+'_flow_of_H2PO4_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_nhe50_file+'/female'+seg+'_flow_of_H2PO4_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_nhe50_file+'/female'+seg+'_flow_of_H2PO4_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_nhe50_file+'/female'+seg+'_flow_of_H2PO4_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    file_sup_2 = open(female_nhe50_file+'/female'+seg+'_flow_of_HPO4_in_Lumen_sup.txt','r')
    file_jux1_2 = open(female_nhe50_file+'/female'+seg+'_flow_of_HPO4_in_Lumen_jux1.txt','r')
    file_jux2_2 = open(female_nhe50_file+'/female'+seg+'_flow_of_HPO4_in_Lumen_jux2.txt','r')
    file_jux3_2 = open(female_nhe50_file+'/female'+seg+'_flow_of_HPO4_in_Lumen_jux3.txt','r')
    file_jux4_2 = open(female_nhe50_file+'/female'+seg+'_flow_of_HPO4_in_Lumen_jux4.txt','r')
    file_jux5_2 = open(female_nhe50_file+'/female'+seg+'_flow_of_HPO4_in_Lumen_jux5.txt','r')
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
    female_delivery_sup_nhe50.append(neph_weight[0]*(10**(7.4-6.8)*datalist_sup[0]-datalist_sup_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    female_delivery_jux1_nhe50.append(neph_weight[1]*(10**(7.4-6.8)*datalist_jux1[0]-datalist_jux1_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    female_delivery_jux2_nhe50.append(neph_weight[2]*(10**(7.4-6.8)*datalist_jux2[0]-datalist_jux2_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    female_delivery_jux3_nhe50.append(neph_weight[3]*(10**(7.4-6.8)*datalist_jux3[0]-datalist_jux3_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    female_delivery_jux4_nhe50.append(neph_weight[4]*(10**(7.4-6.8)*datalist_jux4[0]-datalist_jux4_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    female_delivery_jux5_nhe50.append(neph_weight[5]*(10**(7.4-6.8)*datalist_jux5[0]-datalist_jux5_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    if seg == 'cnt':
        female_delivery_number_nhe50.append(0)
        female_delivery_sup_nhe50.append(neph_weight[0]*(10**(7.4-6.8)*datalist_sup[0]-datalist_sup_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        female_delivery_jux1_nhe50.append(neph_weight[1]*(10**(7.4-6.8)*datalist_jux1[0]-datalist_jux1_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        female_delivery_jux2_nhe50.append(neph_weight[2]*(10**(7.4-6.8)*datalist_jux2[0]-datalist_jux2_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        female_delivery_jux3_nhe50.append(neph_weight[3]*(10**(7.4-6.8)*datalist_jux3[0]-datalist_jux3_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        female_delivery_jux4_nhe50.append(neph_weight[4]*(10**(7.4-6.8)*datalist_jux4[0]-datalist_jux4_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        female_delivery_jux5_nhe50.append(neph_weight[5]*(10**(7.4-6.8)*datalist_jux5[0]-datalist_jux5_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
for seg in segment_late:
    file_data = open(female_nhe50_file+'/female'+seg+'_flow_of_H2PO4_in_Lumen.txt','r')
    file_data_2 = open(female_nhe50_file+'/female'+seg+'_flow_of_HPO4_in_Lumen.txt','r')
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
        female_delivery_number_nhe50.append(number_of_delivery*36000*10e-7)
        print(number_of_delivery*36000*10e-7)
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
    file_sup = open(male_nhe50_file+'/male'+seg+'_flow_of_H2PO4_in_Lumen_sup.txt','r')
    file_jux1 = open(male_nhe50_file+'/male'+seg+'_flow_of_H2PO4_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe50_file+'/male'+seg+'_flow_of_H2PO4_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe50_file+'/male'+seg+'_flow_of_H2PO4_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe50_file+'/male'+seg+'_flow_of_H2PO4_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe50_file+'/male'+seg+'_flow_of_H2PO4_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    file_sup_2 = open(male_nhe50_file+'/male'+seg+'_flow_of_HPO4_in_Lumen_sup.txt','r')
    file_jux1_2 = open(male_nhe50_file+'/male'+seg+'_flow_of_HPO4_in_Lumen_jux1.txt','r')
    file_jux2_2 = open(male_nhe50_file+'/male'+seg+'_flow_of_HPO4_in_Lumen_jux2.txt','r')
    file_jux3_2 = open(male_nhe50_file+'/male'+seg+'_flow_of_HPO4_in_Lumen_jux3.txt','r')
    file_jux4_2 = open(male_nhe50_file+'/male'+seg+'_flow_of_HPO4_in_Lumen_jux4.txt','r')
    file_jux5_2 = open(male_nhe50_file+'/male'+seg+'_flow_of_HPO4_in_Lumen_jux5.txt','r')
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
    male_delivery_sup_nhe50.append(neph_weight[0]*(10**(7.4-6.8)*datalist_sup[0]-datalist_sup_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    male_delivery_jux1_nhe50.append(neph_weight[1]*(10**(7.4-6.8)*datalist_jux1[0]-datalist_jux1_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    male_delivery_jux2_nhe50.append(neph_weight[2]*(10**(7.4-6.8)*datalist_jux2[0]-datalist_jux2_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    male_delivery_jux3_nhe50.append(neph_weight[3]*(10**(7.4-6.8)*datalist_jux3[0]-datalist_jux3_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    male_delivery_jux4_nhe50.append(neph_weight[4]*(10**(7.4-6.8)*datalist_jux4[0]-datalist_jux4_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    male_delivery_jux5_nhe50.append(neph_weight[5]*(10**(7.4-6.8)*datalist_jux5[0]-datalist_jux5_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    if seg == 'cnt':
        male_delivery_number_nhe50.append(0)
        male_delivery_sup_nhe50.append(neph_weight[0]*(10**(7.4-6.8)*datalist_sup[0]-datalist_sup_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        male_delivery_jux1_nhe50.append(neph_weight[1]*(10**(7.4-6.8)*datalist_jux1[0]-datalist_jux1_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        male_delivery_jux2_nhe50.append(neph_weight[2]*(10**(7.4-6.8)*datalist_jux2[0]-datalist_jux2_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        male_delivery_jux3_nhe50.append(neph_weight[3]*(10**(7.4-6.8)*datalist_jux3[0]-datalist_jux3_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        male_delivery_jux4_nhe50.append(neph_weight[4]*(10**(7.4-6.8)*datalist_jux4[0]-datalist_jux4_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        male_delivery_jux5_nhe50.append(neph_weight[5]*(10**(7.4-6.8)*datalist_jux5[0]-datalist_jux5_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
for seg in segment_late:
    file_data = open(male_nhe50_file+'/male'+seg+'_flow_of_H2PO4_in_Lumen.txt','r')
    file_data_2 = open(male_nhe50_file+'/male'+seg+'_flow_of_HPO4_in_Lumen.txt','r')
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
        male_delivery_number_nhe50.append(number_of_delivery*36000*10e-7)
        print(number_of_delivery*36000*10e-7)
    else:
        number_of_delivery = datalist[0]
    #=======================================
    # NHE3 80% inhibited
    #=======================================
female_delivery_number_nhe80 = []
female_delivery_sup_nhe80 = []
female_delivery_jux1_nhe80 = []
female_delivery_jux2_nhe80 = []
female_delivery_jux3_nhe80 = []
female_delivery_jux4_nhe80 = []
female_delivery_jux5_nhe80 = []
for seg in segment_early:
    file_sup = open(female_nhe80_file+'/female'+seg+'_flow_of_H2PO4_in_Lumen_sup.txt','r')
    file_jux1 = open(female_nhe80_file+'/female'+seg+'_flow_of_H2PO4_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_nhe80_file+'/female'+seg+'_flow_of_H2PO4_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_nhe80_file+'/female'+seg+'_flow_of_H2PO4_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_nhe80_file+'/female'+seg+'_flow_of_H2PO4_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_nhe80_file+'/female'+seg+'_flow_of_H2PO4_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    file_sup_2 = open(female_nhe80_file+'/female'+seg+'_flow_of_HPO4_in_Lumen_sup.txt','r')
    file_jux1_2 = open(female_nhe80_file+'/female'+seg+'_flow_of_HPO4_in_Lumen_jux1.txt','r')
    file_jux2_2 = open(female_nhe80_file+'/female'+seg+'_flow_of_HPO4_in_Lumen_jux2.txt','r')
    file_jux3_2 = open(female_nhe80_file+'/female'+seg+'_flow_of_HPO4_in_Lumen_jux3.txt','r')
    file_jux4_2 = open(female_nhe80_file+'/female'+seg+'_flow_of_HPO4_in_Lumen_jux4.txt','r')
    file_jux5_2 = open(female_nhe80_file+'/female'+seg+'_flow_of_HPO4_in_Lumen_jux5.txt','r')
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
    female_delivery_number_nhe80.append(0)
    female_delivery_sup_nhe80.append(neph_weight[0]*(10**(7.4-6.8)*datalist_sup[0]-datalist_sup_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    female_delivery_jux1_nhe80.append(neph_weight[1]*(10**(7.4-6.8)*datalist_jux1[0]-datalist_jux1_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    female_delivery_jux2_nhe80.append(neph_weight[2]*(10**(7.4-6.8)*datalist_jux2[0]-datalist_jux2_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    female_delivery_jux3_nhe80.append(neph_weight[3]*(10**(7.4-6.8)*datalist_jux3[0]-datalist_jux3_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    female_delivery_jux4_nhe80.append(neph_weight[4]*(10**(7.4-6.8)*datalist_jux4[0]-datalist_jux4_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    female_delivery_jux5_nhe80.append(neph_weight[5]*(10**(7.4-6.8)*datalist_jux5[0]-datalist_jux5_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    if seg == 'cnt':
        female_delivery_number_nhe80.append(0)
        female_delivery_sup_nhe80.append(neph_weight[0]*(10**(7.4-6.8)*datalist_sup[0]-datalist_sup_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        female_delivery_jux1_nhe80.append(neph_weight[1]*(10**(7.4-6.8)*datalist_jux1[0]-datalist_jux1_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        female_delivery_jux2_nhe80.append(neph_weight[2]*(10**(7.4-6.8)*datalist_jux2[0]-datalist_jux2_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        female_delivery_jux3_nhe80.append(neph_weight[3]*(10**(7.4-6.8)*datalist_jux3[0]-datalist_jux3_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        female_delivery_jux4_nhe80.append(neph_weight[4]*(10**(7.4-6.8)*datalist_jux4[0]-datalist_jux4_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        female_delivery_jux5_nhe80.append(neph_weight[5]*(10**(7.4-6.8)*datalist_jux5[0]-datalist_jux5_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
for seg in segment_late:
    file_data = open(female_nhe80_file+'/female'+seg+'_flow_of_H2PO4_in_Lumen.txt','r')
    file_data_2 = open(female_nhe80_file+'/female'+seg+'_flow_of_HPO4_in_Lumen.txt','r')
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
        female_delivery_number_nhe80.append(number_of_delivery*36000*10e-7)
        print(number_of_delivery*36000*10e-7)
    else:
        number_of_delivery = datalist[0]
    

male_delivery_number_nhe80 = []
male_delivery_sup_nhe80 = []
male_delivery_jux1_nhe80 = []
male_delivery_jux2_nhe80 = []
male_delivery_jux3_nhe80 = []
male_delivery_jux4_nhe80 = []
male_delivery_jux5_nhe80 = []
for seg in segment_early:
    file_sup = open(male_nhe80_file+'/male'+seg+'_flow_of_H2PO4_in_Lumen_sup.txt','r')
    file_jux1 = open(male_nhe80_file+'/male'+seg+'_flow_of_H2PO4_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe80_file+'/male'+seg+'_flow_of_H2PO4_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe80_file+'/male'+seg+'_flow_of_H2PO4_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe80_file+'/male'+seg+'_flow_of_H2PO4_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe80_file+'/male'+seg+'_flow_of_H2PO4_in_Lumen_jux5.txt','r')
    datalist_sup = []
    datalist_jux1 = []
    datalist_jux2 = []
    datalist_jux3 = []
    datalist_jux4 = []
    datalist_jux5 = []
    file_sup_2 = open(male_nhe80_file+'/male'+seg+'_flow_of_HPO4_in_Lumen_sup.txt','r')
    file_jux1_2 = open(male_nhe80_file+'/male'+seg+'_flow_of_HPO4_in_Lumen_jux1.txt','r')
    file_jux2_2 = open(male_nhe80_file+'/male'+seg+'_flow_of_HPO4_in_Lumen_jux2.txt','r')
    file_jux3_2 = open(male_nhe80_file+'/male'+seg+'_flow_of_HPO4_in_Lumen_jux3.txt','r')
    file_jux4_2 = open(male_nhe80_file+'/male'+seg+'_flow_of_HPO4_in_Lumen_jux4.txt','r')
    file_jux5_2 = open(male_nhe80_file+'/male'+seg+'_flow_of_HPO4_in_Lumen_jux5.txt','r')
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
    male_delivery_number_nhe80.append(0)
    male_delivery_sup_nhe80.append(neph_weight[0]*(10**(7.4-6.8)*datalist_sup[0]-datalist_sup_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    male_delivery_jux1_nhe80.append(neph_weight[1]*(10**(7.4-6.8)*datalist_jux1[0]-datalist_jux1_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    male_delivery_jux2_nhe80.append(neph_weight[2]*(10**(7.4-6.8)*datalist_jux2[0]-datalist_jux2_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    male_delivery_jux3_nhe80.append(neph_weight[3]*(10**(7.4-6.8)*datalist_jux3[0]-datalist_jux3_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    male_delivery_jux4_nhe80.append(neph_weight[4]*(10**(7.4-6.8)*datalist_jux4[0]-datalist_jux4_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    male_delivery_jux5_nhe80.append(neph_weight[5]*(10**(7.4-6.8)*datalist_jux5[0]-datalist_jux5_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
    if seg == 'cnt':
        male_delivery_number_nhe80.append(0)
        male_delivery_sup_nhe80.append(neph_weight[0]*(10**(7.4-6.8)*datalist_sup[0]-datalist_sup_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        male_delivery_jux1_nhe80.append(neph_weight[1]*(10**(7.4-6.8)*datalist_jux1[0]-datalist_jux1_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        male_delivery_jux2_nhe80.append(neph_weight[2]*(10**(7.4-6.8)*datalist_jux2[0]-datalist_jux2_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        male_delivery_jux3_nhe80.append(neph_weight[3]*(10**(7.4-6.8)*datalist_jux3[0]-datalist_jux3_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        male_delivery_jux4_nhe80.append(neph_weight[4]*(10**(7.4-6.8)*datalist_jux4[0]-datalist_jux4_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
        male_delivery_jux5_nhe80.append(neph_weight[5]*(10**(7.4-6.8)*datalist_jux5[0]-datalist_jux5_2[0])/(1+10**(7.4-6.8))*36000*10e-7)
for seg in segment_late:
    file_data = open(male_nhe80_file+'/male'+seg+'_flow_of_H2PO4_in_Lumen.txt','r')
    file_data_2 = open(male_nhe80_file+'/male'+seg+'_flow_of_HPO4_in_Lumen.txt','r')
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
        male_delivery_number_nhe80.append(number_of_delivery*36000*10e-7)
        print(number_of_delivery*36000*10e-7)
    else:
        number_of_delivery = datalist[0]

male_delivery_sup = male_delivery_sup[4:]
male_delivery_jux1 = male_delivery_jux1[4:]
male_delivery_jux2 = male_delivery_jux2[4:]
male_delivery_jux3 = male_delivery_jux3[4:]
male_delivery_jux4 = male_delivery_jux4[4:]
male_delivery_jux5 = male_delivery_jux5[4:]
male_delivery_sup_nhe50 = male_delivery_sup_nhe50[4:]
male_delivery_jux1_nhe50 = male_delivery_jux1_nhe50[4:]
male_delivery_jux2_nhe50 = male_delivery_jux2_nhe50[4:]
male_delivery_jux3_nhe50 = male_delivery_jux3_nhe50[4:]
male_delivery_jux4_nhe50 = male_delivery_jux4_nhe50[4:]
male_delivery_jux5_nhe50 = male_delivery_jux5_nhe50[4:]
male_delivery_sup_nhe80 = male_delivery_sup_nhe80[4:]
male_delivery_jux1_nhe80 = male_delivery_jux1_nhe80[4:]
male_delivery_jux2_nhe80 = male_delivery_jux2_nhe80[4:]
male_delivery_jux3_nhe80 = male_delivery_jux3_nhe80[4:]
male_delivery_jux4_nhe80 = male_delivery_jux4_nhe80[4:]
male_delivery_jux5_nhe80 = male_delivery_jux5_nhe80[4:]
male_delivery_number = male_delivery_number[4:]
male_delivery_number_nhe50 = male_delivery_number_nhe50[4:]
male_delivery_number_nhe80 = male_delivery_number_nhe80[4:]

female_delivery_sup = female_delivery_sup[4:]
female_delivery_jux1 = female_delivery_jux1[4:]
female_delivery_jux2 = female_delivery_jux2[4:]
female_delivery_jux3 = female_delivery_jux3[4:]
female_delivery_jux4 = female_delivery_jux4[4:]
female_delivery_jux5 = female_delivery_jux5[4:]
female_delivery_sup_nhe50 = female_delivery_sup_nhe50[4:]
female_delivery_jux1_nhe50 = female_delivery_jux1_nhe50[4:]
female_delivery_jux2_nhe50 = female_delivery_jux2_nhe50[4:]
female_delivery_jux3_nhe50 = female_delivery_jux3_nhe50[4:]
female_delivery_jux4_nhe50 = female_delivery_jux4_nhe50[4:]
female_delivery_jux5_nhe50 = female_delivery_jux5_nhe50[4:]
female_delivery_sup_nhe80 = female_delivery_sup_nhe80[4:]
female_delivery_jux1_nhe80 = female_delivery_jux1_nhe80[4:]
female_delivery_jux2_nhe80 = female_delivery_jux2_nhe80[4:]
female_delivery_jux3_nhe80 = female_delivery_jux3_nhe80[4:]
female_delivery_jux4_nhe80 = female_delivery_jux4_nhe80[4:]
female_delivery_jux5_nhe80 = female_delivery_jux5_nhe80[4:]
female_delivery_number = female_delivery_number[4:]
female_delivery_number_nhe50 = female_delivery_number_nhe50[4:]
female_delivery_number_nhe80 = female_delivery_number_nhe80[4:]

male_sup=axarr[2].bar(np.arange(len(segment[4:6])),male_delivery_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Male')
male_jux=axarr[2].bar(np.arange(len(segment[4:6])),[male_delivery_jux1[i]+male_delivery_jux2[i]+male_delivery_jux3[i]+male_delivery_jux4[i]+male_delivery_jux5[i] for i in range(len(male_delivery_sup))],bar_width,bottom=male_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later=axarr[2].bar(np.arange(len(segment[4:])),male_delivery_number,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

male_sup_nhe50=axarr[2].bar(np.arange(len(segment[4:6]))+bar_width,male_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue',label='Male')
male_jux_nhe50=axarr[2].bar(np.arange(len(segment[4:6]))+bar_width,[male_delivery_jux1_nhe50[i]+male_delivery_jux2_nhe50[i]+male_delivery_jux3_nhe50[i]+male_delivery_jux4_nhe50[i]+male_delivery_jux5_nhe50[i] for i in range(len(male_delivery_sup_nhe50))],bar_width,bottom=male_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later_nhe50=axarr[2].bar(np.arange(len(segment[4:]))+bar_width,male_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

male_sup_nhe80=axarr[2].bar(np.arange(len(segment[4:6]))+2*bar_width,male_delivery_sup_nhe80,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='paleturquoise',label='Male')
male_jux_nhe80=axarr[2].bar(np.arange(len(segment[4:6]))+2*bar_width,[male_delivery_jux1_nhe80[i]+male_delivery_jux2_nhe80[i]+male_delivery_jux3_nhe80[i]+male_delivery_jux4_nhe80[i]+male_delivery_jux5_nhe80[i] for i in range(len(male_delivery_sup_nhe80))],bar_width,bottom=male_delivery_sup_nhe80,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later_nhe80=axarr[2].bar(np.arange(len(segment[4:]))+2*bar_width,male_delivery_number_nhe80,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='paleturquoise')

Female_sup=axarr[2].bar(np.arange(len(segment[4:6]))+3*bar_width,female_delivery_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta',label='Female')
Female_jux=axarr[2].bar(np.arange(len(segment[4:6]))+3*bar_width,[female_delivery_jux1[i]+female_delivery_jux2[i]+female_delivery_jux3[i]+female_delivery_jux4[i]+female_delivery_jux5[i] for i in range(len(female_delivery_sup))],bar_width,bottom=female_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white',label='Juxtamedullary')
Female_later=axarr[2].bar(np.arange(len(segment[4:]))+3*bar_width,female_delivery_number,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

Female_sup_nhe50=axarr[2].bar(np.arange(len(segment[4:6]))+4*bar_width,female_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink',label='Female')
Female_jux_nhe50=axarr[2].bar(np.arange(len(segment[4:6]))+4*bar_width,[female_delivery_jux1_nhe50[i]+female_delivery_jux2_nhe50[i]+female_delivery_jux3_nhe50[i]+female_delivery_jux4_nhe50[i]+female_delivery_jux5_nhe50[i] for i in range(len(female_delivery_sup_nhe50))],bar_width,bottom=female_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
Female_later_nhe50=axarr[2].bar(np.arange(len(segment[4:]))+4*bar_width,female_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')

Female_sup_nhe80=axarr[2].bar(np.arange(len(segment[4:6]))+5*bar_width,female_delivery_sup_nhe80,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='pink',label='Female')
Female_jux_nhe80=axarr[2].bar(np.arange(len(segment[4:6]))+5*bar_width,[female_delivery_jux1_nhe80[i]+female_delivery_jux2_nhe80[i]+female_delivery_jux3_nhe80[i]+female_delivery_jux4_nhe80[i]+female_delivery_jux5_nhe80[i] for i in range(len(female_delivery_sup_nhe80))],bar_width,bottom=female_delivery_sup_nhe80,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
Female_later_nhe80=axarr[2].bar(np.arange(len(segment[4:]))+5*bar_width,female_delivery_number_nhe80,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='pink')

axarr[2].set_xticks(np.arange(len(segment[4:]))+2.5*bar_width)
axarr[2].set_xticklabels(segment[4:],fontsize=40)
axarr[2].tick_params(axis='both',labelsize=40)
#axarr[2].set_ylim(0,17)
#axarr[0].set_title('Male',fontsize = 50)
#ax.set_xlabel('Segment',fontsize=20)
axarr[2].set_ylabel('TA delivery ($\mu$mol/min)',fontsize=40)
#axarr[2].legend(fontsize=30,markerscale=30)

#=================================================================
# Water volume
#=================================================================

female_delivery_number = []
female_delivery_sup = []
female_delivery_jux1 = []
female_delivery_jux2 = []
female_delivery_jux3 = []
female_delivery_jux4 = []
female_delivery_jux5 = []
for seg in segment_early:
    file_sup = open(female_normal_file+'/female'+seg+'_water_volume_in_Lumen_sup.txt','r')
    file_jux1 = open(female_normal_file+'/female'+seg+'_water_volume_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_normal_file+'/female'+seg+'_water_volume_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_normal_file+'/female'+seg+'_water_volume_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_normal_file+'/female'+seg+'_water_volume_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_normal_file+'/female'+seg+'_water_volume_in_Lumen_jux5.txt','r')
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
    female_delivery_sup.append(neph_weight[0]*datalist_sup[0]*36000*10e-7)
    female_delivery_jux1.append(neph_weight[1]*datalist_jux1[0]*36000*10e-7)
    female_delivery_jux2.append(neph_weight[2]*datalist_jux2[0]*36000*10e-7)
    female_delivery_jux3.append(neph_weight[3]*datalist_jux3[0]*36000*10e-7)
    female_delivery_jux4.append(neph_weight[4]*datalist_jux4[0]*36000*10e-7)
    female_delivery_jux5.append(neph_weight[5]*datalist_jux5[0]*36000*10e-7)
    if seg == 'cnt':
        female_delivery_number.append(0)
        female_delivery_sup.append(neph_weight[0]*datalist_sup[-1]*36000*10e-7)
        female_delivery_jux1.append(neph_weight[1]*datalist_jux1[-1]*36000*10e-7)
        female_delivery_jux2.append(neph_weight[2]*datalist_jux2[-1]*36000*10e-7)
        female_delivery_jux3.append(neph_weight[3]*datalist_jux3[-1]*36000*10e-7)
        female_delivery_jux4.append(neph_weight[4]*datalist_jux4[-1]*36000*10e-7)
        female_delivery_jux5.append(neph_weight[5]*datalist_jux5[-1]*36000*10e-7)
for seg in segment_late:
    file_data = open(female_normal_file+'/female'+seg+'_water_volume_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        female_delivery_number.append(number_of_delivery*36000*10e-7)
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
    file_sup = open(male_normal_file+'/male'+seg+'_water_volume_in_Lumen_sup.txt','r')
    file_jux1 = open(male_normal_file+'/male'+seg+'_water_volume_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_normal_file+'/male'+seg+'_water_volume_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_normal_file+'/male'+seg+'_water_volume_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_normal_file+'/male'+seg+'_water_volume_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_normal_file+'/male'+seg+'_water_volume_in_Lumen_jux5.txt','r')
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
    male_delivery_sup.append(neph_weight[0]*datalist_sup[0]*36000*10e-7)
    male_delivery_jux1.append(neph_weight[1]*datalist_jux1[0]*36000*10e-7)
    male_delivery_jux2.append(neph_weight[2]*datalist_jux2[0]*36000*10e-7)
    male_delivery_jux3.append(neph_weight[3]*datalist_jux3[0]*36000*10e-7)
    male_delivery_jux4.append(neph_weight[4]*datalist_jux4[0]*36000*10e-7)
    male_delivery_jux5.append(neph_weight[5]*datalist_jux5[0]*36000*10e-7)
    if seg == 'cnt':
        male_delivery_number.append(0)
        male_delivery_sup.append(neph_weight[0]*datalist_sup[-1]*36000*10e-7)
        male_delivery_jux1.append(neph_weight[1]*datalist_jux1[-1]*36000*10e-7)
        male_delivery_jux2.append(neph_weight[2]*datalist_jux2[-1]*36000*10e-7)
        male_delivery_jux3.append(neph_weight[3]*datalist_jux3[-1]*36000*10e-7)
        male_delivery_jux4.append(neph_weight[4]*datalist_jux4[-1]*36000*10e-7)
        male_delivery_jux5.append(neph_weight[5]*datalist_jux5[-1]*36000*10e-7)
for seg in segment_late:
    file_data = open(male_normal_file+'/male'+seg+'_water_volume_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        male_delivery_number.append(number_of_delivery*36000*10e-7)
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
    file_sup = open(female_nhe50_file+'/female'+seg+'_water_volume_in_Lumen_sup.txt','r')
    file_jux1 = open(female_nhe50_file+'/female'+seg+'_water_volume_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_nhe50_file+'/female'+seg+'_water_volume_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_nhe50_file+'/female'+seg+'_water_volume_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_nhe50_file+'/female'+seg+'_water_volume_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_nhe50_file+'/female'+seg+'_water_volume_in_Lumen_jux5.txt','r')
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
    female_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[0]*36000*10e-7)
    female_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[0]*36000*10e-7)
    female_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[0]*36000*10e-7)
    female_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[0]*36000*10e-7)
    female_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[0]*36000*10e-7)
    female_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[0]*36000*10e-7)
    if seg == 'cnt':
        female_delivery_number_nhe50.append(0)
        female_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[-1]*36000*10e-7)
        female_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[-1]*36000*10e-7)
        female_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[-1]*36000*10e-7)
        female_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[-1]*36000*10e-7)
        female_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[-1]*36000*10e-7)
        female_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[-1]*36000*10e-7)
for seg in segment_late:
    file_data = open(female_nhe50_file+'/female'+seg+'_water_volume_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        female_delivery_number_nhe50.append(number_of_delivery*36000*10e-7)
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
    file_sup = open(male_nhe50_file+'/male'+seg+'_water_volume_in_Lumen_sup.txt','r')
    file_jux1 = open(male_nhe50_file+'/male'+seg+'_water_volume_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe50_file+'/male'+seg+'_water_volume_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe50_file+'/male'+seg+'_water_volume_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe50_file+'/male'+seg+'_water_volume_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe50_file+'/male'+seg+'_water_volume_in_Lumen_jux5.txt','r')
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
    male_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[0]*36000*10e-7)
    male_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[0]*36000*10e-7)
    male_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[0]*36000*10e-7)
    male_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[0]*36000*10e-7)
    male_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[0]*36000*10e-7)
    male_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[0]*36000*10e-7)
    if seg == 'cnt':
        male_delivery_number_nhe50.append(0)
        male_delivery_sup_nhe50.append(neph_weight[0]*datalist_sup[-1]*36000*10e-7)
        male_delivery_jux1_nhe50.append(neph_weight[1]*datalist_jux1[-1]*36000*10e-7)
        male_delivery_jux2_nhe50.append(neph_weight[2]*datalist_jux2[-1]*36000*10e-7)
        male_delivery_jux3_nhe50.append(neph_weight[3]*datalist_jux3[-1]*36000*10e-7)
        male_delivery_jux4_nhe50.append(neph_weight[4]*datalist_jux4[-1]*36000*10e-7)
        male_delivery_jux5_nhe50.append(neph_weight[5]*datalist_jux5[-1]*36000*10e-7)
for seg in segment_late:
    file_data = open(male_nhe50_file+'/male'+seg+'_water_volume_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        male_delivery_number_nhe50.append(number_of_delivery*36000*10e-7)
    else:
        number_of_delivery = datalist[0]
    #===================================
    # NHE3 80% inhibited
    #===================================
female_delivery_number_nhe80 = []
female_delivery_sup_nhe80 = []
female_delivery_jux1_nhe80 = []
female_delivery_jux2_nhe80 = []
female_delivery_jux3_nhe80 = []
female_delivery_jux4_nhe80 = []
female_delivery_jux5_nhe80 = []
for seg in segment_early:
    file_sup = open(female_nhe80_file+'/female'+seg+'_water_volume_in_Lumen_sup.txt','r')
    file_jux1 = open(female_nhe80_file+'/female'+seg+'_water_volume_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_nhe80_file+'/female'+seg+'_water_volume_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_nhe80_file+'/female'+seg+'_water_volume_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_nhe80_file+'/female'+seg+'_water_volume_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_nhe80_file+'/female'+seg+'_water_volume_in_Lumen_jux5.txt','r')
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
    female_delivery_number_nhe80.append(0)
    female_delivery_sup_nhe80.append(neph_weight[0]*datalist_sup[0]*36000*10e-7)
    female_delivery_jux1_nhe80.append(neph_weight[1]*datalist_jux1[0]*36000*10e-7)
    female_delivery_jux2_nhe80.append(neph_weight[2]*datalist_jux2[0]*36000*10e-7)
    female_delivery_jux3_nhe80.append(neph_weight[3]*datalist_jux3[0]*36000*10e-7)
    female_delivery_jux4_nhe80.append(neph_weight[4]*datalist_jux4[0]*36000*10e-7)
    female_delivery_jux5_nhe80.append(neph_weight[5]*datalist_jux5[0]*36000*10e-7)
    if seg == 'cnt':
        female_delivery_number_nhe80.append(0)
        female_delivery_sup_nhe80.append(neph_weight[0]*datalist_sup[-1]*36000*10e-7)
        female_delivery_jux1_nhe80.append(neph_weight[1]*datalist_jux1[-1]*36000*10e-7)
        female_delivery_jux2_nhe80.append(neph_weight[2]*datalist_jux2[-1]*36000*10e-7)
        female_delivery_jux3_nhe80.append(neph_weight[3]*datalist_jux3[-1]*36000*10e-7)
        female_delivery_jux4_nhe80.append(neph_weight[4]*datalist_jux4[-1]*36000*10e-7)
        female_delivery_jux5_nhe80.append(neph_weight[5]*datalist_jux5[-1]*36000*10e-7)
for seg in segment_late:
    file_data = open(female_nhe80_file+'/female'+seg+'_water_volume_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        female_delivery_number_nhe80.append(number_of_delivery*36000*10e-7)
    else:
        number_of_delivery = datalist[0]
    

male_delivery_number_nhe80 = []
male_delivery_sup_nhe80 = []
male_delivery_jux1_nhe80 = []
male_delivery_jux2_nhe80 = []
male_delivery_jux3_nhe80 = []
male_delivery_jux4_nhe80 = []
male_delivery_jux5_nhe80 = []
for seg in segment_early:
    file_sup = open(male_nhe80_file+'/male'+seg+'_water_volume_in_Lumen_sup.txt','r')
    file_jux1 = open(male_nhe80_file+'/male'+seg+'_water_volume_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe80_file+'/male'+seg+'_water_volume_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe80_file+'/male'+seg+'_water_volume_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe80_file+'/male'+seg+'_water_volume_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe80_file+'/male'+seg+'_water_volume_in_Lumen_jux5.txt','r')
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
    male_delivery_number_nhe80.append(0)
    male_delivery_sup_nhe80.append(neph_weight[0]*datalist_sup[0]*36000*10e-7)
    male_delivery_jux1_nhe80.append(neph_weight[1]*datalist_jux1[0]*36000*10e-7)
    male_delivery_jux2_nhe80.append(neph_weight[2]*datalist_jux2[0]*36000*10e-7)
    male_delivery_jux3_nhe80.append(neph_weight[3]*datalist_jux3[0]*36000*10e-7)
    male_delivery_jux4_nhe80.append(neph_weight[4]*datalist_jux4[0]*36000*10e-7)
    male_delivery_jux5_nhe80.append(neph_weight[5]*datalist_jux5[0]*36000*10e-7)
    if seg == 'cnt':
        male_delivery_number_nhe80.append(0)
        male_delivery_sup_nhe80.append(neph_weight[0]*datalist_sup[-1]*36000*10e-7)
        male_delivery_jux1_nhe80.append(neph_weight[1]*datalist_jux1[-1]*36000*10e-7)
        male_delivery_jux2_nhe80.append(neph_weight[2]*datalist_jux2[-1]*36000*10e-7)
        male_delivery_jux3_nhe80.append(neph_weight[3]*datalist_jux3[-1]*36000*10e-7)
        male_delivery_jux4_nhe80.append(neph_weight[4]*datalist_jux4[-1]*36000*10e-7)
        male_delivery_jux5_nhe80.append(neph_weight[5]*datalist_jux5[-1]*36000*10e-7)
for seg in segment_late:
    file_data = open(male_nhe80_file+'/male'+seg+'_water_volume_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
    if seg == 'imcd':
        number_of_delivery = datalist[-1]
        male_delivery_number_nhe80.append(number_of_delivery*36000*10e-7)
    else:
        number_of_delivery = datalist[0]

male_delivery_sup = male_delivery_sup[4:]
male_delivery_jux1 = male_delivery_jux1[4:]
male_delivery_jux2 = male_delivery_jux2[4:]
male_delivery_jux3 = male_delivery_jux3[4:]
male_delivery_jux4 = male_delivery_jux4[4:]
male_delivery_jux5 = male_delivery_jux5[4:]
male_delivery_sup_nhe50 = male_delivery_sup_nhe50[4:]
male_delivery_jux1_nhe50 = male_delivery_jux1_nhe50[4:]
male_delivery_jux2_nhe50 = male_delivery_jux2_nhe50[4:]
male_delivery_jux3_nhe50 = male_delivery_jux3_nhe50[4:]
male_delivery_jux4_nhe50 = male_delivery_jux4_nhe50[4:]
male_delivery_jux5_nhe50 = male_delivery_jux5_nhe50[4:]
male_delivery_sup_nhe80 = male_delivery_sup_nhe80[4:]
male_delivery_jux1_nhe80 = male_delivery_jux1_nhe80[4:]
male_delivery_jux2_nhe80 = male_delivery_jux2_nhe80[4:]
male_delivery_jux3_nhe80 = male_delivery_jux3_nhe80[4:]
male_delivery_jux4_nhe80 = male_delivery_jux4_nhe80[4:]
male_delivery_jux5_nhe80 = male_delivery_jux5_nhe80[4:]
male_delivery_number = male_delivery_number[4:]
male_delivery_number_nhe50 = male_delivery_number_nhe50[4:]
male_delivery_number_nhe80 = male_delivery_number_nhe80[4:]

female_delivery_sup = female_delivery_sup[4:]
female_delivery_jux1 = female_delivery_jux1[4:]
female_delivery_jux2 = female_delivery_jux2[4:]
female_delivery_jux3 = female_delivery_jux3[4:]
female_delivery_jux4 = female_delivery_jux4[4:]
female_delivery_jux5 = female_delivery_jux5[4:]
female_delivery_sup_nhe50 = female_delivery_sup_nhe50[4:]
female_delivery_jux1_nhe50 = female_delivery_jux1_nhe50[4:]
female_delivery_jux2_nhe50 = female_delivery_jux2_nhe50[4:]
female_delivery_jux3_nhe50 = female_delivery_jux3_nhe50[4:]
female_delivery_jux4_nhe50 = female_delivery_jux4_nhe50[4:]
female_delivery_jux5_nhe50 = female_delivery_jux5_nhe50[4:]
female_delivery_sup_nhe80 = female_delivery_sup_nhe80[4:]
female_delivery_jux1_nhe80 = female_delivery_jux1_nhe80[4:]
female_delivery_jux2_nhe80 = female_delivery_jux2_nhe80[4:]
female_delivery_jux3_nhe80 = female_delivery_jux3_nhe80[4:]
female_delivery_jux4_nhe80 = female_delivery_jux4_nhe80[4:]
female_delivery_jux5_nhe80 = female_delivery_jux5_nhe80[4:]
female_delivery_number = female_delivery_number[4:]
female_delivery_number_nhe50 = female_delivery_number_nhe50[4:]
female_delivery_number_nhe80 = female_delivery_number_nhe80[4:]

male_sup=axarr[3].bar(np.arange(len(segment[4:6])),male_delivery_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Male')
male_jux=axarr[3].bar(np.arange(len(segment[4:6])),[male_delivery_jux1[i]+male_delivery_jux2[i]+male_delivery_jux3[i]+male_delivery_jux4[i]+male_delivery_jux5[i] for i in range(len(male_delivery_sup))],bar_width,bottom=male_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later=axarr[3].bar(np.arange(len(segment[4:])),male_delivery_number,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

male_sup_nhe50=axarr[3].bar(np.arange(len(segment[4:6]))+bar_width,male_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue',label='Male')
male_jux_nhe50=axarr[3].bar(np.arange(len(segment[4:6]))+bar_width,[male_delivery_jux1_nhe50[i]+male_delivery_jux2_nhe50[i]+male_delivery_jux3_nhe50[i]+male_delivery_jux4_nhe50[i]+male_delivery_jux5_nhe50[i] for i in range(len(male_delivery_sup_nhe50))],bar_width,bottom=male_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later_nhe50=axarr[3].bar(np.arange(len(segment[4:]))+bar_width,male_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

male_sup_nhe80=axarr[3].bar(np.arange(len(segment[4:6]))+2*bar_width,male_delivery_sup_nhe80,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='paleturquoise',label='Male')
male_jux_nhe80=axarr[3].bar(np.arange(len(segment[4:6]))+2*bar_width,[male_delivery_jux1_nhe80[i]+male_delivery_jux2_nhe80[i]+male_delivery_jux3_nhe80[i]+male_delivery_jux4_nhe80[i]+male_delivery_jux5_nhe80[i] for i in range(len(male_delivery_sup_nhe80))],bar_width,bottom=male_delivery_sup_nhe80,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
male_later_nhe80=axarr[3].bar(np.arange(len(segment[4:]))+2*bar_width,male_delivery_number_nhe80,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='paleturquoise')

Female_sup=axarr[3].bar(np.arange(len(segment[4:6]))+3*bar_width,female_delivery_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta',label='Female')
Female_jux=axarr[3].bar(np.arange(len(segment[4:6]))+3*bar_width,[female_delivery_jux1[i]+female_delivery_jux2[i]+female_delivery_jux3[i]+female_delivery_jux4[i]+female_delivery_jux5[i] for i in range(len(female_delivery_sup))],bar_width,bottom=female_delivery_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white',label='Juxtamedullary')
Female_later=axarr[3].bar(np.arange(len(segment[4:]))+3*bar_width,female_delivery_number,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

Female_sup_nhe50=axarr[3].bar(np.arange(len(segment[4:6]))+4*bar_width,female_delivery_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink',label='Female')
Female_jux_nhe50=axarr[3].bar(np.arange(len(segment[4:6]))+4*bar_width,[female_delivery_jux1_nhe50[i]+female_delivery_jux2_nhe50[i]+female_delivery_jux3_nhe50[i]+female_delivery_jux4_nhe50[i]+female_delivery_jux5_nhe50[i] for i in range(len(female_delivery_sup_nhe50))],bar_width,bottom=female_delivery_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
Female_later_nhe50=axarr[3].bar(np.arange(len(segment[4:]))+4*bar_width,female_delivery_number_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')

Female_sup_nhe80=axarr[3].bar(np.arange(len(segment[4:6]))+5*bar_width,female_delivery_sup_nhe80,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='pink',label='Female')
Female_jux_nhe80=axarr[3].bar(np.arange(len(segment[4:6]))+5*bar_width,[female_delivery_jux1_nhe80[i]+female_delivery_jux2_nhe80[i]+female_delivery_jux3_nhe80[i]+female_delivery_jux4_nhe80[i]+female_delivery_jux5_nhe80[i] for i in range(len(female_delivery_sup_nhe80))],bar_width,bottom=female_delivery_sup_nhe80,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='white')
Female_later_nhe80=axarr[3].bar(np.arange(len(segment[4:]))+5*bar_width,female_delivery_number_nhe80,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='pink')

axarr[3].set_xticks(np.arange(len(segment[4:]))+2.5*bar_width)
axarr[3].set_xticklabels(segment[4:],fontsize=40)
axarr[3].tick_params(axis='both',labelsize=40)
#axarr[3].set_ylim(0,17)
#axarr[0].set_title('Male',fontsize = 50)
#ax.set_xlabel('Segment',fontsize=20)
axarr[3].set_ylabel('Volume delivery (ml/min)',fontsize=40)
#axarr[3].legend(fontsize=30,markerscale=30)

axarr[0].text(-0.3,axarr[0].get_ylim()[1],'A',size=40,weight='bold')
axarr[1].text(-0.3,axarr[1].get_ylim()[1],'B',size=40,weight='bold')
axarr[2].text(-0.3,axarr[2].get_ylim()[1],'C',size=40,weight='bold')
axarr[3].text(-0.3,axarr[3].get_ylim()[1],'D',size=40,weight='bold')

plt.savefig('delivery_comp_panel_enac_female_male',bbox_inches='tight')