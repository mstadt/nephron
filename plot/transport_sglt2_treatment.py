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

male_normal_file = './Male_hum_N_diab'
male_nhe50_file = './Male_hum_Y_diab'

neph_weight = [0.85,(0.15)*0.4,(0.15)*0.3,(0.15)*0.15,(0.15)*0.1,(0.15)*0.05]

solute = ['Na','K','Cl','HCO3','H2CO3','CO2','HPO4','H2PO4','urea','NH3','NH4','H','HCO2','H2CO2','glu']
segment_early = ['pt','s3','sdl','mtal','ctal','dct','cnt']
segment_jux = ['sdl','ldl','lal']
segment_late = ['ccd','omcd','imcd']
segment_transport = ['PT','DL','LAL','TAL','DCT','CNT','CD']

bar_width = 0.2
fig,axarr = plt.subplots(3,2)
fig.set_figheight(45)
fig.set_figwidth(40)
fig.subplots_adjust(hspace = 0.06)

volume_conversion = 1.44
solute_conversion = 1.44*10e-4

#==================================================================
# Na transport
#==================================================================

s = 'Na'
#==========================
#   Baseline
#==========================

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

male_transport_number = []
male_transport_sup = []
male_transport_jux1 = []
male_transport_jux2 = []
male_transport_jux3 = []
male_transport_jux4 = []
male_transport_jux5 = []
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
    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_transport_number.append(0)
    male_transport_sup.append(solute_conversion*neph_weight[0]*(datalist_sup[0]-datalist_sup[-1]))
    male_transport_jux1.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    male_transport_jux2.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    male_transport_jux3.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    male_transport_jux4.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    male_transport_jux5.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))
for seg in segment_late:
    file_data = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
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
    file_jux1 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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

#============================
#   SGLT2i
#============================

female_transport_number_nhe50 = []
female_transport_sup_nhe50 = []
female_transport_jux1_nhe50 = []
female_transport_jux2_nhe50 = []
female_transport_jux3_nhe50 = []
female_transport_jux4_nhe50 = []
female_transport_jux5_nhe50 = []
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
    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    female_transport_number_nhe50.append(0)
    female_transport_sup_nhe50.append(solute_conversion*neph_weight[0]*(datalist_sup[0]-datalist_sup[-1]))
    female_transport_jux1_nhe50.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    female_transport_jux2_nhe50.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    female_transport_jux3_nhe50.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    female_transport_jux4_nhe50.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    female_transport_jux5_nhe50.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))
for seg in segment_late:
    file_data = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
        number_of_transport = datalist[0]-datalist[-1]
    female_transport_number_nhe50.append(solute_conversion*number_of_transport)

female_transport_number_reformed_sup_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux1_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux2_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux3_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux4_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux5_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_nhe50 = [0 for _ in segment_transport]

female_transport_number_reformed_nhe50[6] = female_transport_number_nhe50[7]+female_transport_number_nhe50[8]+female_transport_number_nhe50[9]

female_transport_long_jux1_nhe50 = []
female_transport_long_jux2_nhe50 = []
female_transport_long_jux3_nhe50 = []
female_transport_long_jux4_nhe50 = []
female_transport_long_jux5_nhe50 = []
for seg in segment_jux:
    file_jux1 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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
    female_transport_long_jux1_nhe50.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    female_transport_long_jux2_nhe50.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    female_transport_long_jux3_nhe50.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    female_transport_long_jux4_nhe50.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    female_transport_long_jux5_nhe50.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))

female_transport_number_reformed_sup_nhe50[0] = female_transport_sup_nhe50[0]+female_transport_sup_nhe50[1]
female_transport_number_reformed_sup_nhe50[1] = female_transport_sup_nhe50[2]
female_transport_number_reformed_sup_nhe50[3] = female_transport_sup_nhe50[3]+female_transport_sup_nhe50[4]
female_transport_number_reformed_sup_nhe50[4] = female_transport_sup_nhe50[5]
female_transport_number_reformed_sup_nhe50[5] = female_transport_sup_nhe50[6]

female_transport_number_reformed_jux1_nhe50[0] = female_transport_jux1_nhe50[0]+female_transport_jux1_nhe50[1]
female_transport_number_reformed_jux1_nhe50[1] = female_transport_long_jux1_nhe50[0]+female_transport_long_jux1_nhe50[1]
female_transport_number_reformed_jux1_nhe50[2] = female_transport_long_jux1_nhe50[2]
female_transport_number_reformed_jux1_nhe50[3] = female_transport_jux1_nhe50[3]+female_transport_jux1_nhe50[4]
female_transport_number_reformed_jux1_nhe50[4] = female_transport_jux1_nhe50[5]
female_transport_number_reformed_jux1_nhe50[5] = female_transport_jux1_nhe50[6]

female_transport_number_reformed_jux2_nhe50[0] = female_transport_jux2_nhe50[0]+female_transport_jux2_nhe50[1]
female_transport_number_reformed_jux2_nhe50[1] = female_transport_long_jux2_nhe50[0]+female_transport_long_jux2_nhe50[1]
female_transport_number_reformed_jux2_nhe50[2] = female_transport_long_jux2_nhe50[2]
female_transport_number_reformed_jux2_nhe50[3] = female_transport_jux2_nhe50[3]+female_transport_jux2_nhe50[4]
female_transport_number_reformed_jux2_nhe50[4] = female_transport_jux2_nhe50[5]
female_transport_number_reformed_jux2_nhe50[5] = female_transport_jux2_nhe50[6]

female_transport_number_reformed_jux3_nhe50[0] = female_transport_jux3_nhe50[0]+female_transport_jux3_nhe50[1]
female_transport_number_reformed_jux3_nhe50[1] = female_transport_long_jux3_nhe50[0]+female_transport_long_jux3_nhe50[1]
female_transport_number_reformed_jux3_nhe50[2] = female_transport_long_jux3_nhe50[2]
female_transport_number_reformed_jux3_nhe50[3] = female_transport_jux3_nhe50[3]+female_transport_jux3_nhe50[4]
female_transport_number_reformed_jux3_nhe50[4] = female_transport_jux3_nhe50[5]
female_transport_number_reformed_jux3_nhe50[5] = female_transport_jux3_nhe50[6]

female_transport_number_reformed_jux4_nhe50[0] = female_transport_jux4_nhe50[0]+female_transport_jux4_nhe50[1]
female_transport_number_reformed_jux4_nhe50[1] = female_transport_long_jux4_nhe50[0]+female_transport_long_jux4_nhe50[1]
female_transport_number_reformed_jux4_nhe50[2] = female_transport_long_jux4_nhe50[2]
female_transport_number_reformed_jux4_nhe50[3] = female_transport_jux4_nhe50[3]+female_transport_jux4_nhe50[4]
female_transport_number_reformed_jux4_nhe50[4] = female_transport_jux4_nhe50[5]
female_transport_number_reformed_jux4_nhe50[5] = female_transport_jux4_nhe50[6]

female_transport_number_reformed_jux5_nhe50[0] = female_transport_jux5_nhe50[0]+female_transport_jux5_nhe50[1]
female_transport_number_reformed_jux5_nhe50[1] = female_transport_long_jux5_nhe50[0]+female_transport_long_jux5_nhe50[1]
female_transport_number_reformed_jux5_nhe50[2] = female_transport_long_jux5_nhe50[2]
female_transport_number_reformed_jux5_nhe50[3] = female_transport_jux5_nhe50[3]+female_transport_jux5_nhe50[4]
female_transport_number_reformed_jux5_nhe50[4] = female_transport_jux5_nhe50[5]
female_transport_number_reformed_jux5_nhe50[5] = female_transport_jux5_nhe50[6]

male_transport_number_nhe50 = []
male_transport_sup_nhe50 = []
male_transport_jux1_nhe50 = []
male_transport_jux2_nhe50 = []
male_transport_jux3_nhe50 = []
male_transport_jux4_nhe50 = []
male_transport_jux5_nhe50 = []
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
    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_transport_number_nhe50.append(0)
    male_transport_sup_nhe50.append(solute_conversion*neph_weight[0]*(datalist_sup[0]-datalist_sup[-1]))
    male_transport_jux1_nhe50.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    male_transport_jux2_nhe50.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    male_transport_jux3_nhe50.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    male_transport_jux4_nhe50.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    male_transport_jux5_nhe50.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))
for seg in segment_late:
    file_data = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
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
    file_jux1 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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

male_sup=axarr[0,0].bar(np.arange(len(segment_transport[:6])),male_transport_number_reformed_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Men, Healthy')
male_jux=axarr[0,0].bar(np.arange(len(segment_transport[:6])),[male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i]+male_transport_number_reformed_jux5[i] for i in range(len(male_transport_number_reformed_sup))],bar_width,bottom=male_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
male_later=axarr[0,0].bar(np.arange(len(segment_transport)),male_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

male_sup_nhe50=axarr[0,0].bar(np.arange(len(segment_transport[:6]))+bar_width,male_transport_number_reformed_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue',label='Men, Diabetic')
male_jux_nhe50=axarr[0,0].bar(np.arange(len(segment_transport[:6]))+bar_width,[male_transport_number_reformed_jux1_nhe50[i]+male_transport_number_reformed_jux2_nhe50[i]+male_transport_number_reformed_jux3_nhe50[i]+male_transport_number_reformed_jux4_nhe50[i]+male_transport_number_reformed_jux5_nhe50[i] for i in range(len(male_transport_number_reformed_sup_nhe50))],bar_width,bottom=male_transport_number_reformed_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
male_later_nhe50=axarr[0,0].bar(np.arange(len(segment_transport))+bar_width,male_transport_number_reformed_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

female_sup=axarr[0,0].bar(np.arange(len(segment_transport[:6]))+2*bar_width,female_transport_number_reformed_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')
female_jux=axarr[0,0].bar(np.arange(len(segment_transport[:6]))+2*bar_width,[female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i]+female_transport_number_reformed_jux3[i]+female_transport_number_reformed_jux4[i]+female_transport_number_reformed_jux5[i] for i in range(len(female_transport_number_reformed_sup))],bar_width,bottom=female_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
female_later=axarr[0,0].bar(np.arange(len(segment_transport))+2*bar_width,female_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

female_sup_nhe50=axarr[0,0].bar(np.arange(len(segment_transport[:6]))+3*bar_width,female_transport_number_reformed_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')
female_jux_nhe50=axarr[0,0].bar(np.arange(len(segment_transport[:6]))+3*bar_width,[female_transport_number_reformed_jux1_nhe50[i]+female_transport_number_reformed_jux2_nhe50[i]+female_transport_number_reformed_jux3_nhe50[i]+female_transport_number_reformed_jux4_nhe50[i]+female_transport_number_reformed_jux5_nhe50[i] for i in range(len(female_transport_number_reformed_sup_nhe50))],bar_width,bottom=female_transport_number_reformed_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
female_later_nhe50=axarr[0,0].bar(np.arange(len(segment_transport))+3*bar_width,female_transport_number_reformed_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')

axarr[0,0].set_xticks(np.arange(len(segment_transport))+1.5*bar_width)
axarr[0,0].set_xticklabels(segment_transport,fontsize=30)
axarr[0,0].tick_params(axis='both',labelsize=40)
#axarr[0,0].set_title('Men',fontsize=50)
#axarr[0,0].set_ylim(-1,16)
axarr[0,0].set_ylabel('Na$^+$ transport (mol/Day)',fontsize=30)
axarr[0,0].legend(fontsize=30,markerscale=30)

bar_width_ins = bar_width
axins = inset_axes(axarr[0,0],width=3.5,height=3.5,loc=7)

male_sup=axins.bar(np.arange(len(segment_transport[:6])),male_transport_number_reformed_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Male full ACEi')
male_jux=axins.bar(np.arange(len(segment_transport[:6])),[male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i]+male_transport_number_reformed_jux5[i] for i in range(len(male_transport_number_reformed_sup))],bar_width,bottom=male_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
male_later=axins.bar(np.arange(len(segment_transport)),male_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

male_sup_nhe50=axins.bar(np.arange(len(segment_transport[:6]))+bar_width,male_transport_number_reformed_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue',label='Male proximal ACEi')
male_jux_nhe50=axins.bar(np.arange(len(segment_transport[:6]))+bar_width,[male_transport_number_reformed_jux1_nhe50[i]+male_transport_number_reformed_jux2_nhe50[i]+male_transport_number_reformed_jux3_nhe50[i]+male_transport_number_reformed_jux4_nhe50[i]+male_transport_number_reformed_jux5_nhe50[i] for i in range(len(male_transport_number_reformed_sup_nhe50))],bar_width,bottom=male_transport_number_reformed_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
male_later_nhe50=axins.bar(np.arange(len(segment_transport))+bar_width,male_transport_number_reformed_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

female_sup=axins.bar(np.arange(len(segment_transport[:6]))+2*bar_width,female_transport_number_reformed_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta',label='Female full ACEi')
female_jux=axins.bar(np.arange(len(segment_transport[:6]))+2*bar_width,[female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i]+female_transport_number_reformed_jux3[i]+female_transport_number_reformed_jux4[i]+female_transport_number_reformed_jux5[i] for i in range(len(female_transport_number_reformed_sup))],bar_width,bottom=female_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
female_later=axins.bar(np.arange(len(segment_transport))+2*bar_width,female_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

female_sup_nhe50=axins.bar(np.arange(len(segment_transport[:6]))+3*bar_width,female_transport_number_reformed_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink',label='Female proximal ACEi')
female_jux_nhe50=axins.bar(np.arange(len(segment_transport[:6]))+3*bar_width,[female_transport_number_reformed_jux1_nhe50[i]+female_transport_number_reformed_jux2_nhe50[i]+female_transport_number_reformed_jux3_nhe50[i]+female_transport_number_reformed_jux4_nhe50[i]+female_transport_number_reformed_jux5_nhe50[i] for i in range(len(female_transport_number_reformed_sup_nhe50))],bar_width,bottom=female_transport_number_reformed_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
female_later_nhe50=axins.bar(np.arange(len(segment_transport))+3*bar_width,female_transport_number_reformed_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')

axins.set_xticks(np.arange(len(segment_transport))+1.5*bar_width_ins)
axins.set_xticklabels(segment_transport,fontsize=40)
axins.set_xlim(5-1.5*bar_width_ins,6+4*bar_width_ins)
axins.set_ylim(0,1.0)
axins.tick_params(axis='both',labelsize=40)

#==================================================================
# K transport
#==================================================================

s = 'K'

#==========================
#   Baseline
#==========================

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

male_transport_number = []
male_transport_sup = []
male_transport_jux1 = []
male_transport_jux2 = []
male_transport_jux3 = []
male_transport_jux4 = []
male_transport_jux5 = []
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
    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_transport_number.append(0)
    male_transport_sup.append(solute_conversion*neph_weight[0]*(datalist_sup[0]-datalist_sup[-1]))
    male_transport_jux1.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    male_transport_jux2.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    male_transport_jux3.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    male_transport_jux4.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    male_transport_jux5.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))
for seg in segment_late:
    file_data = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
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
    file_jux1 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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

#============================
#   SGLT2i
#============================

female_transport_number_nhe50 = []
female_transport_sup_nhe50 = []
female_transport_jux1_nhe50 = []
female_transport_jux2_nhe50 = []
female_transport_jux3_nhe50 = []
female_transport_jux4_nhe50 = []
female_transport_jux5_nhe50 = []
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
    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    female_transport_number_nhe50.append(0)
    female_transport_sup_nhe50.append(solute_conversion*neph_weight[0]*(datalist_sup[0]-datalist_sup[-1]))
    female_transport_jux1_nhe50.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    female_transport_jux2_nhe50.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    female_transport_jux3_nhe50.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    female_transport_jux4_nhe50.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    female_transport_jux5_nhe50.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))
for seg in segment_late:
    file_data = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
        number_of_transport = datalist[0]-datalist[-1]
    female_transport_number_nhe50.append(solute_conversion*number_of_transport)

female_transport_number_reformed_sup_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux1_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux2_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux3_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux4_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux5_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_nhe50 = [0 for _ in segment_transport]

female_transport_number_reformed_nhe50[6] = female_transport_number_nhe50[7]+female_transport_number_nhe50[8]+female_transport_number_nhe50[9]

female_transport_long_jux1_nhe50 = []
female_transport_long_jux2_nhe50 = []
female_transport_long_jux3_nhe50 = []
female_transport_long_jux4_nhe50 = []
female_transport_long_jux5_nhe50 = []
for seg in segment_jux:
    file_jux1 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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
    female_transport_long_jux1_nhe50.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    female_transport_long_jux2_nhe50.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    female_transport_long_jux3_nhe50.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    female_transport_long_jux4_nhe50.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    female_transport_long_jux5_nhe50.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))

female_transport_number_reformed_sup_nhe50[0] = female_transport_sup_nhe50[0]+female_transport_sup_nhe50[1]
female_transport_number_reformed_sup_nhe50[1] = female_transport_sup_nhe50[2]
female_transport_number_reformed_sup_nhe50[3] = female_transport_sup_nhe50[3]+female_transport_sup_nhe50[4]
female_transport_number_reformed_sup_nhe50[4] = female_transport_sup_nhe50[5]
female_transport_number_reformed_sup_nhe50[5] = female_transport_sup_nhe50[6]

female_transport_number_reformed_jux1_nhe50[0] = female_transport_jux1_nhe50[0]+female_transport_jux1_nhe50[1]
female_transport_number_reformed_jux1_nhe50[1] = female_transport_long_jux1_nhe50[0]+female_transport_long_jux1_nhe50[1]
female_transport_number_reformed_jux1_nhe50[2] = female_transport_long_jux1_nhe50[2]
female_transport_number_reformed_jux1_nhe50[3] = female_transport_jux1_nhe50[3]+female_transport_jux1_nhe50[4]
female_transport_number_reformed_jux1_nhe50[4] = female_transport_jux1_nhe50[5]
female_transport_number_reformed_jux1_nhe50[5] = female_transport_jux1_nhe50[6]

female_transport_number_reformed_jux2_nhe50[0] = female_transport_jux2_nhe50[0]+female_transport_jux2_nhe50[1]
female_transport_number_reformed_jux2_nhe50[1] = female_transport_long_jux2_nhe50[0]+female_transport_long_jux2_nhe50[1]
female_transport_number_reformed_jux2_nhe50[2] = female_transport_long_jux2_nhe50[2]
female_transport_number_reformed_jux2_nhe50[3] = female_transport_jux2_nhe50[3]+female_transport_jux2_nhe50[4]
female_transport_number_reformed_jux2_nhe50[4] = female_transport_jux2_nhe50[5]
female_transport_number_reformed_jux2_nhe50[5] = female_transport_jux2_nhe50[6]

female_transport_number_reformed_jux3_nhe50[0] = female_transport_jux3_nhe50[0]+female_transport_jux3_nhe50[1]
female_transport_number_reformed_jux3_nhe50[1] = female_transport_long_jux3_nhe50[0]+female_transport_long_jux3_nhe50[1]
female_transport_number_reformed_jux3_nhe50[2] = female_transport_long_jux3_nhe50[2]
female_transport_number_reformed_jux3_nhe50[3] = female_transport_jux3_nhe50[3]+female_transport_jux3_nhe50[4]
female_transport_number_reformed_jux3_nhe50[4] = female_transport_jux3_nhe50[5]
female_transport_number_reformed_jux3_nhe50[5] = female_transport_jux3_nhe50[6]

female_transport_number_reformed_jux4_nhe50[0] = female_transport_jux4_nhe50[0]+female_transport_jux4_nhe50[1]
female_transport_number_reformed_jux4_nhe50[1] = female_transport_long_jux4_nhe50[0]+female_transport_long_jux4_nhe50[1]
female_transport_number_reformed_jux4_nhe50[2] = female_transport_long_jux4_nhe50[2]
female_transport_number_reformed_jux4_nhe50[3] = female_transport_jux4_nhe50[3]+female_transport_jux4_nhe50[4]
female_transport_number_reformed_jux4_nhe50[4] = female_transport_jux4_nhe50[5]
female_transport_number_reformed_jux4_nhe50[5] = female_transport_jux4_nhe50[6]

female_transport_number_reformed_jux5_nhe50[0] = female_transport_jux5_nhe50[0]+female_transport_jux5_nhe50[1]
female_transport_number_reformed_jux5_nhe50[1] = female_transport_long_jux5_nhe50[0]+female_transport_long_jux5_nhe50[1]
female_transport_number_reformed_jux5_nhe50[2] = female_transport_long_jux5_nhe50[2]
female_transport_number_reformed_jux5_nhe50[3] = female_transport_jux5_nhe50[3]+female_transport_jux5_nhe50[4]
female_transport_number_reformed_jux5_nhe50[4] = female_transport_jux5_nhe50[5]
female_transport_number_reformed_jux5_nhe50[5] = female_transport_jux5_nhe50[6]

male_transport_number_nhe50 = []
male_transport_sup_nhe50 = []
male_transport_jux1_nhe50 = []
male_transport_jux2_nhe50 = []
male_transport_jux3_nhe50 = []
male_transport_jux4_nhe50 = []
male_transport_jux5_nhe50 = []
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
    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_transport_number_nhe50.append(0)
    male_transport_sup_nhe50.append(solute_conversion*neph_weight[0]*(datalist_sup[0]-datalist_sup[-1]))
    male_transport_jux1_nhe50.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    male_transport_jux2_nhe50.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    male_transport_jux3_nhe50.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    male_transport_jux4_nhe50.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    male_transport_jux5_nhe50.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))
for seg in segment_late:
    file_data = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
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
    file_jux1 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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


male_sup=axarr[0,1].bar(np.arange(len(segment_transport[:6])),male_transport_number_reformed_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')
male_jux=axarr[0,1].bar(np.arange(len(segment_transport[:6])),[male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i]+male_transport_number_reformed_jux5[i] for i in range(len(male_transport_number_reformed_sup))],bar_width,bottom=male_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
male_later=axarr[0,1].bar(np.arange(len(segment_transport)),male_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

male_sup_nhe50=axarr[0,1].bar(np.arange(len(segment_transport[:6]))+bar_width,male_transport_number_reformed_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')
male_jux_nhe50=axarr[0,1].bar(np.arange(len(segment_transport[:6]))+bar_width,[male_transport_number_reformed_jux1_nhe50[i]+male_transport_number_reformed_jux2_nhe50[i]+male_transport_number_reformed_jux3_nhe50[i]+male_transport_number_reformed_jux4_nhe50[i]+male_transport_number_reformed_jux5_nhe50[i] for i in range(len(male_transport_number_reformed_sup_nhe50))],bar_width,bottom=male_transport_number_reformed_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
male_later_nhe50=axarr[0,1].bar(np.arange(len(segment_transport))+bar_width,male_transport_number_reformed_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

female_sup=axarr[0,1].bar(np.arange(len(segment_transport[:6]))+2*bar_width,female_transport_number_reformed_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta',label='Women, Healthy')
female_jux=axarr[0,1].bar(np.arange(len(segment_transport[:6]))+2*bar_width,[female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i]+female_transport_number_reformed_jux3[i]+female_transport_number_reformed_jux4[i]+female_transport_number_reformed_jux5[i] for i in range(len(female_transport_number_reformed_sup))],bar_width,bottom=female_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
female_later=axarr[0,1].bar(np.arange(len(segment_transport))+2*bar_width,female_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

female_sup_nhe50=axarr[0,1].bar(np.arange(len(segment_transport[:6]))+3*bar_width,female_transport_number_reformed_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink',label='Women, Diabetic')
female_jux_nhe50=axarr[0,1].bar(np.arange(len(segment_transport[:6]))+3*bar_width,[female_transport_number_reformed_jux1_nhe50[i]+female_transport_number_reformed_jux2_nhe50[i]+female_transport_number_reformed_jux3_nhe50[i]+female_transport_number_reformed_jux4_nhe50[i]+female_transport_number_reformed_jux5_nhe50[i] for i in range(len(female_transport_number_reformed_sup_nhe50))],bar_width,bottom=female_transport_number_reformed_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
female_later_nhe50=axarr[0,1].bar(np.arange(len(segment_transport))+3*bar_width,female_transport_number_reformed_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')

axarr[0,1].set_xticks(np.arange(len(segment_transport))+1.5*bar_width)
axarr[0,1].set_xticklabels(segment_transport,fontsize=30)
axarr[0,1].tick_params(axis='both',labelsize=40)
#axarr[0,1].set_ylim(-0.2,0.5)
axarr[0,1].set_ylabel('K$^+$ transport (mol/Day)',fontsize=30)
axarr[0,1].legend(fontsize=30,markerscale=30)

#==================================================================
# Cl transport
#==================================================================

s = 'Cl'

#==========================
#   Baseline
#==========================

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

male_transport_number = []
male_transport_sup = []
male_transport_jux1 = []
male_transport_jux2 = []
male_transport_jux3 = []
male_transport_jux4 = []
male_transport_jux5 = []
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
    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_transport_number.append(0)
    male_transport_sup.append(solute_conversion*neph_weight[0]*(datalist_sup[0]-datalist_sup[-1]))
    male_transport_jux1.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    male_transport_jux2.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    male_transport_jux3.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    male_transport_jux4.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    male_transport_jux5.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))
for seg in segment_late:
    file_data = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
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
    file_jux1 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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

#============================
#   SGLT2i
#============================

female_transport_number_nhe50 = []
female_transport_sup_nhe50 = []
female_transport_jux1_nhe50 = []
female_transport_jux2_nhe50 = []
female_transport_jux3_nhe50 = []
female_transport_jux4_nhe50 = []
female_transport_jux5_nhe50 = []
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
    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    female_transport_number_nhe50.append(0)
    female_transport_sup_nhe50.append(solute_conversion*neph_weight[0]*(datalist_sup[0]-datalist_sup[-1]))
    female_transport_jux1_nhe50.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    female_transport_jux2_nhe50.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    female_transport_jux3_nhe50.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    female_transport_jux4_nhe50.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    female_transport_jux5_nhe50.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))
for seg in segment_late:
    file_data = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
        number_of_transport = datalist[0]-datalist[-1]
    female_transport_number_nhe50.append(solute_conversion*number_of_transport)

female_transport_number_reformed_sup_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux1_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux2_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux3_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux4_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux5_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_nhe50 = [0 for _ in segment_transport]

female_transport_number_reformed_nhe50[6] = female_transport_number_nhe50[7]+female_transport_number_nhe50[8]+female_transport_number_nhe50[9]

female_transport_long_jux1_nhe50 = []
female_transport_long_jux2_nhe50 = []
female_transport_long_jux3_nhe50 = []
female_transport_long_jux4_nhe50 = []
female_transport_long_jux5_nhe50 = []
for seg in segment_jux:
    file_jux1 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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
    female_transport_long_jux1_nhe50.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    female_transport_long_jux2_nhe50.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    female_transport_long_jux3_nhe50.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    female_transport_long_jux4_nhe50.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    female_transport_long_jux5_nhe50.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))

female_transport_number_reformed_sup_nhe50[0] = female_transport_sup_nhe50[0]+female_transport_sup_nhe50[1]
female_transport_number_reformed_sup_nhe50[1] = female_transport_sup_nhe50[2]
female_transport_number_reformed_sup_nhe50[3] = female_transport_sup_nhe50[3]+female_transport_sup_nhe50[4]
female_transport_number_reformed_sup_nhe50[4] = female_transport_sup_nhe50[5]
female_transport_number_reformed_sup_nhe50[5] = female_transport_sup_nhe50[6]

female_transport_number_reformed_jux1_nhe50[0] = female_transport_jux1_nhe50[0]+female_transport_jux1_nhe50[1]
female_transport_number_reformed_jux1_nhe50[1] = female_transport_long_jux1_nhe50[0]+female_transport_long_jux1_nhe50[1]
female_transport_number_reformed_jux1_nhe50[2] = female_transport_long_jux1_nhe50[2]
female_transport_number_reformed_jux1_nhe50[3] = female_transport_jux1_nhe50[3]+female_transport_jux1_nhe50[4]
female_transport_number_reformed_jux1_nhe50[4] = female_transport_jux1_nhe50[5]
female_transport_number_reformed_jux1_nhe50[5] = female_transport_jux1_nhe50[6]

female_transport_number_reformed_jux2_nhe50[0] = female_transport_jux2_nhe50[0]+female_transport_jux2_nhe50[1]
female_transport_number_reformed_jux2_nhe50[1] = female_transport_long_jux2_nhe50[0]+female_transport_long_jux2_nhe50[1]
female_transport_number_reformed_jux2_nhe50[2] = female_transport_long_jux2_nhe50[2]
female_transport_number_reformed_jux2_nhe50[3] = female_transport_jux2_nhe50[3]+female_transport_jux2_nhe50[4]
female_transport_number_reformed_jux2_nhe50[4] = female_transport_jux2_nhe50[5]
female_transport_number_reformed_jux2_nhe50[5] = female_transport_jux2_nhe50[6]

female_transport_number_reformed_jux3_nhe50[0] = female_transport_jux3_nhe50[0]+female_transport_jux3_nhe50[1]
female_transport_number_reformed_jux3_nhe50[1] = female_transport_long_jux3_nhe50[0]+female_transport_long_jux3_nhe50[1]
female_transport_number_reformed_jux3_nhe50[2] = female_transport_long_jux3_nhe50[2]
female_transport_number_reformed_jux3_nhe50[3] = female_transport_jux3_nhe50[3]+female_transport_jux3_nhe50[4]
female_transport_number_reformed_jux3_nhe50[4] = female_transport_jux3_nhe50[5]
female_transport_number_reformed_jux3_nhe50[5] = female_transport_jux3_nhe50[6]

female_transport_number_reformed_jux4_nhe50[0] = female_transport_jux4_nhe50[0]+female_transport_jux4_nhe50[1]
female_transport_number_reformed_jux4_nhe50[1] = female_transport_long_jux4_nhe50[0]+female_transport_long_jux4_nhe50[1]
female_transport_number_reformed_jux4_nhe50[2] = female_transport_long_jux4_nhe50[2]
female_transport_number_reformed_jux4_nhe50[3] = female_transport_jux4_nhe50[3]+female_transport_jux4_nhe50[4]
female_transport_number_reformed_jux4_nhe50[4] = female_transport_jux4_nhe50[5]
female_transport_number_reformed_jux4_nhe50[5] = female_transport_jux4_nhe50[6]

female_transport_number_reformed_jux5_nhe50[0] = female_transport_jux5_nhe50[0]+female_transport_jux5_nhe50[1]
female_transport_number_reformed_jux5_nhe50[1] = female_transport_long_jux5_nhe50[0]+female_transport_long_jux5_nhe50[1]
female_transport_number_reformed_jux5_nhe50[2] = female_transport_long_jux5_nhe50[2]
female_transport_number_reformed_jux5_nhe50[3] = female_transport_jux5_nhe50[3]+female_transport_jux5_nhe50[4]
female_transport_number_reformed_jux5_nhe50[4] = female_transport_jux5_nhe50[5]
female_transport_number_reformed_jux5_nhe50[5] = female_transport_jux5_nhe50[6]

male_transport_number_nhe50 = []
male_transport_sup_nhe50 = []
male_transport_jux1_nhe50 = []
male_transport_jux2_nhe50 = []
male_transport_jux3_nhe50 = []
male_transport_jux4_nhe50 = []
male_transport_jux5_nhe50 = []
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
    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_transport_number_nhe50.append(0)
    male_transport_sup_nhe50.append(solute_conversion*neph_weight[0]*(datalist_sup[0]-datalist_sup[-1]))
    male_transport_jux1_nhe50.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    male_transport_jux2_nhe50.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    male_transport_jux3_nhe50.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    male_transport_jux4_nhe50.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    male_transport_jux5_nhe50.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))
for seg in segment_late:
    file_data = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
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
    file_jux1 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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

male_sup=axarr[1,0].bar(np.arange(len(segment_transport[:6])),male_transport_number_reformed_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Male full ACEi')
male_jux=axarr[1,0].bar(np.arange(len(segment_transport[:6])),[male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i]+male_transport_number_reformed_jux5[i] for i in range(len(male_transport_number_reformed_sup))],bar_width,bottom=male_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
male_later=axarr[1,0].bar(np.arange(len(segment_transport)),male_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

male_sup_nhe50=axarr[1,0].bar(np.arange(len(segment_transport[:6]))+bar_width,male_transport_number_reformed_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue',label='Male proximal ACEi')
male_jux_nhe50=axarr[1,0].bar(np.arange(len(segment_transport[:6]))+bar_width,[male_transport_number_reformed_jux1_nhe50[i]+male_transport_number_reformed_jux2_nhe50[i]+male_transport_number_reformed_jux3_nhe50[i]+male_transport_number_reformed_jux4_nhe50[i]+male_transport_number_reformed_jux5_nhe50[i] for i in range(len(male_transport_number_reformed_sup_nhe50))],bar_width,bottom=male_transport_number_reformed_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
male_later_nhe50=axarr[1,0].bar(np.arange(len(segment_transport))+bar_width,male_transport_number_reformed_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

female_sup=axarr[1,0].bar(np.arange(len(segment_transport[:6]))+2*bar_width,female_transport_number_reformed_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta',label='Female full ACEi')
female_jux=axarr[1,0].bar(np.arange(len(segment_transport[:6]))+2*bar_width,[female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i]+female_transport_number_reformed_jux3[i]+female_transport_number_reformed_jux4[i]+female_transport_number_reformed_jux5[i] for i in range(len(female_transport_number_reformed_sup))],bar_width,bottom=female_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
female_later=axarr[1,0].bar(np.arange(len(segment_transport))+2*bar_width,female_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

female_sup_nhe50=axarr[1,0].bar(np.arange(len(segment_transport[:6]))+3*bar_width,female_transport_number_reformed_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink',label='Female proximal ACEi')
female_jux_nhe50=axarr[1,0].bar(np.arange(len(segment_transport[:6]))+3*bar_width,[female_transport_number_reformed_jux1_nhe50[i]+female_transport_number_reformed_jux2_nhe50[i]+female_transport_number_reformed_jux3_nhe50[i]+female_transport_number_reformed_jux4_nhe50[i]+female_transport_number_reformed_jux5_nhe50[i] for i in range(len(female_transport_number_reformed_sup_nhe50))],bar_width,bottom=female_transport_number_reformed_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
female_later_nhe50=axarr[1,0].bar(np.arange(len(segment_transport))+3*bar_width,female_transport_number_reformed_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')

axarr[1,0].set_xticks(np.arange(len(segment_transport))+1.5*bar_width)
axarr[1,0].set_xticklabels(segment_transport,fontsize=30)
axarr[1,0].tick_params(axis='both',labelsize=40)
#axarr[1,0].set_ylim(-1,12)
axarr[1,0].set_ylabel('Cl$^-$ transport (mol/Day)',fontsize=30)
#axarr[2,0].legend(fontsize=30,markerscale=30)

bar_width_ins = bar_width
axins = inset_axes(axarr[1,0],width=3.5,height=3.5,loc=7)

male_sup=axins.bar(np.arange(len(segment_transport[:6])),male_transport_number_reformed_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Male full ACEi')
male_jux=axins.bar(np.arange(len(segment_transport[:6])),[male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i]+male_transport_number_reformed_jux5[i] for i in range(len(male_transport_number_reformed_sup))],bar_width,bottom=male_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
male_later=axins.bar(np.arange(len(segment_transport)),male_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

male_sup_nhe50=axins.bar(np.arange(len(segment_transport[:6]))+bar_width,male_transport_number_reformed_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue',label='Male proximal ACEi')
male_jux_nhe50=axins.bar(np.arange(len(segment_transport[:6]))+bar_width,[male_transport_number_reformed_jux1_nhe50[i]+male_transport_number_reformed_jux2_nhe50[i]+male_transport_number_reformed_jux3_nhe50[i]+male_transport_number_reformed_jux4_nhe50[i]+male_transport_number_reformed_jux5_nhe50[i] for i in range(len(male_transport_number_reformed_sup_nhe50))],bar_width,bottom=male_transport_number_reformed_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
male_later_nhe50=axins.bar(np.arange(len(segment_transport))+bar_width,male_transport_number_reformed_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

female_sup=axins.bar(np.arange(len(segment_transport[:6]))+2*bar_width,female_transport_number_reformed_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta',label='Female full ACEi')
female_jux=axins.bar(np.arange(len(segment_transport[:6]))+2*bar_width,[female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i]+female_transport_number_reformed_jux3[i]+female_transport_number_reformed_jux4[i]+female_transport_number_reformed_jux5[i] for i in range(len(female_transport_number_reformed_sup))],bar_width,bottom=female_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
female_later=axins.bar(np.arange(len(segment_transport))+2*bar_width,female_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

female_sup_nhe50=axins.bar(np.arange(len(segment_transport[:6]))+3*bar_width,female_transport_number_reformed_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink',label='Female proximal ACEi')
female_jux_nhe50=axins.bar(np.arange(len(segment_transport[:6]))+3*bar_width,[female_transport_number_reformed_jux1_nhe50[i]+female_transport_number_reformed_jux2_nhe50[i]+female_transport_number_reformed_jux3_nhe50[i]+female_transport_number_reformed_jux4_nhe50[i]+female_transport_number_reformed_jux5_nhe50[i] for i in range(len(female_transport_number_reformed_sup_nhe50))],bar_width,bottom=female_transport_number_reformed_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
female_later_nhe50=axins.bar(np.arange(len(segment_transport))+3*bar_width,female_transport_number_reformed_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')

axins.set_xticks(np.arange(len(segment_transport))+1.5*bar_width_ins)
axins.set_xticklabels(segment_transport,fontsize=40)
axins.set_xlim(5-1.5*bar_width_ins,6+4*bar_width_ins)
axins.set_ylim(-0.1,0.5)
axins.tick_params(axis='both',labelsize=40)

#==================================================================
# Glucose transport
#==================================================================

s = 'glu'

#==========================
#   Baseline
#==========================

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

male_transport_number = []
male_transport_sup = []
male_transport_jux1 = []
male_transport_jux2 = []
male_transport_jux3 = []
male_transport_jux4 = []
male_transport_jux5 = []
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
    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_transport_number.append(0)
    male_transport_sup.append(solute_conversion*neph_weight[0]*(datalist_sup[0]-datalist_sup[-1]))
    male_transport_jux1.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    male_transport_jux2.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    male_transport_jux3.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    male_transport_jux4.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    male_transport_jux5.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))
for seg in segment_late:
    file_data = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
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
    file_jux1 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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

#============================
#   SGLT2i
#============================

female_transport_number_nhe50 = []
female_transport_sup_nhe50 = []
female_transport_jux1_nhe50 = []
female_transport_jux2_nhe50 = []
female_transport_jux3_nhe50 = []
female_transport_jux4_nhe50 = []
female_transport_jux5_nhe50 = []
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
    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    female_transport_number_nhe50.append(0)
    female_transport_sup_nhe50.append(solute_conversion*neph_weight[0]*(datalist_sup[0]-datalist_sup[-1]))
    female_transport_jux1_nhe50.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    female_transport_jux2_nhe50.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    female_transport_jux3_nhe50.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    female_transport_jux4_nhe50.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    female_transport_jux5_nhe50.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))
for seg in segment_late:
    file_data = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
        number_of_transport = datalist[0]-datalist[-1]
    female_transport_number_nhe50.append(solute_conversion*number_of_transport)

female_transport_number_reformed_sup_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux1_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux2_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux3_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux4_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux5_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_nhe50 = [0 for _ in segment_transport]

female_transport_number_reformed_nhe50[6] = female_transport_number_nhe50[7]+female_transport_number_nhe50[8]+female_transport_number_nhe50[9]

female_transport_long_jux1_nhe50 = []
female_transport_long_jux2_nhe50 = []
female_transport_long_jux3_nhe50 = []
female_transport_long_jux4_nhe50 = []
female_transport_long_jux5_nhe50 = []
for seg in segment_jux:
    file_jux1 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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
    female_transport_long_jux1_nhe50.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    female_transport_long_jux2_nhe50.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    female_transport_long_jux3_nhe50.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    female_transport_long_jux4_nhe50.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    female_transport_long_jux5_nhe50.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))

female_transport_number_reformed_sup_nhe50[0] = female_transport_sup_nhe50[0]+female_transport_sup_nhe50[1]
female_transport_number_reformed_sup_nhe50[1] = female_transport_sup_nhe50[2]
female_transport_number_reformed_sup_nhe50[3] = female_transport_sup_nhe50[3]+female_transport_sup_nhe50[4]
female_transport_number_reformed_sup_nhe50[4] = female_transport_sup_nhe50[5]
female_transport_number_reformed_sup_nhe50[5] = female_transport_sup_nhe50[6]

female_transport_number_reformed_jux1_nhe50[0] = female_transport_jux1_nhe50[0]+female_transport_jux1_nhe50[1]
female_transport_number_reformed_jux1_nhe50[1] = female_transport_long_jux1_nhe50[0]+female_transport_long_jux1_nhe50[1]
female_transport_number_reformed_jux1_nhe50[2] = female_transport_long_jux1_nhe50[2]
female_transport_number_reformed_jux1_nhe50[3] = female_transport_jux1_nhe50[3]+female_transport_jux1_nhe50[4]
female_transport_number_reformed_jux1_nhe50[4] = female_transport_jux1_nhe50[5]
female_transport_number_reformed_jux1_nhe50[5] = female_transport_jux1_nhe50[6]

female_transport_number_reformed_jux2_nhe50[0] = female_transport_jux2_nhe50[0]+female_transport_jux2_nhe50[1]
female_transport_number_reformed_jux2_nhe50[1] = female_transport_long_jux2_nhe50[0]+female_transport_long_jux2_nhe50[1]
female_transport_number_reformed_jux2_nhe50[2] = female_transport_long_jux2_nhe50[2]
female_transport_number_reformed_jux2_nhe50[3] = female_transport_jux2_nhe50[3]+female_transport_jux2_nhe50[4]
female_transport_number_reformed_jux2_nhe50[4] = female_transport_jux2_nhe50[5]
female_transport_number_reformed_jux2_nhe50[5] = female_transport_jux2_nhe50[6]

female_transport_number_reformed_jux3_nhe50[0] = female_transport_jux3_nhe50[0]+female_transport_jux3_nhe50[1]
female_transport_number_reformed_jux3_nhe50[1] = female_transport_long_jux3_nhe50[0]+female_transport_long_jux3_nhe50[1]
female_transport_number_reformed_jux3_nhe50[2] = female_transport_long_jux3_nhe50[2]
female_transport_number_reformed_jux3_nhe50[3] = female_transport_jux3_nhe50[3]+female_transport_jux3_nhe50[4]
female_transport_number_reformed_jux3_nhe50[4] = female_transport_jux3_nhe50[5]
female_transport_number_reformed_jux3_nhe50[5] = female_transport_jux3_nhe50[6]

female_transport_number_reformed_jux4_nhe50[0] = female_transport_jux4_nhe50[0]+female_transport_jux4_nhe50[1]
female_transport_number_reformed_jux4_nhe50[1] = female_transport_long_jux4_nhe50[0]+female_transport_long_jux4_nhe50[1]
female_transport_number_reformed_jux4_nhe50[2] = female_transport_long_jux4_nhe50[2]
female_transport_number_reformed_jux4_nhe50[3] = female_transport_jux4_nhe50[3]+female_transport_jux4_nhe50[4]
female_transport_number_reformed_jux4_nhe50[4] = female_transport_jux4_nhe50[5]
female_transport_number_reformed_jux4_nhe50[5] = female_transport_jux4_nhe50[6]

female_transport_number_reformed_jux5_nhe50[0] = female_transport_jux5_nhe50[0]+female_transport_jux5_nhe50[1]
female_transport_number_reformed_jux5_nhe50[1] = female_transport_long_jux5_nhe50[0]+female_transport_long_jux5_nhe50[1]
female_transport_number_reformed_jux5_nhe50[2] = female_transport_long_jux5_nhe50[2]
female_transport_number_reformed_jux5_nhe50[3] = female_transport_jux5_nhe50[3]+female_transport_jux5_nhe50[4]
female_transport_number_reformed_jux5_nhe50[4] = female_transport_jux5_nhe50[5]
female_transport_number_reformed_jux5_nhe50[5] = female_transport_jux5_nhe50[6]

male_transport_number_nhe50 = []
male_transport_sup_nhe50 = []
male_transport_jux1_nhe50 = []
male_transport_jux2_nhe50 = []
male_transport_jux3_nhe50 = []
male_transport_jux4_nhe50 = []
male_transport_jux5_nhe50 = []
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
    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_transport_number_nhe50.append(0)
    male_transport_sup_nhe50.append(solute_conversion*neph_weight[0]*(datalist_sup[0]-datalist_sup[-1]))
    male_transport_jux1_nhe50.append(solute_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    male_transport_jux2_nhe50.append(solute_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    male_transport_jux3_nhe50.append(solute_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    male_transport_jux4_nhe50.append(solute_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    male_transport_jux5_nhe50.append(solute_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))
for seg in segment_late:
    file_data = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen.txt','r')
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
    file_jux1 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_'+s+'_in_Lumen_jux5.txt','r')
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


male_sup=axarr[1,1].bar(np.arange(len(segment_transport[:6])),male_transport_number_reformed_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Male full ACEi')
male_jux=axarr[1,1].bar(np.arange(len(segment_transport[:6])),[male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i]+male_transport_number_reformed_jux5[i] for i in range(len(male_transport_number_reformed_sup))],bar_width,bottom=male_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
male_later=axarr[1,1].bar(np.arange(len(segment_transport)),male_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

male_sup_nhe50=axarr[1,1].bar(np.arange(len(segment_transport[:6]))+bar_width,male_transport_number_reformed_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue',label='Male proximal ACEi')
male_jux_nhe50=axarr[1,1].bar(np.arange(len(segment_transport[:6]))+bar_width,[male_transport_number_reformed_jux1_nhe50[i]+male_transport_number_reformed_jux2_nhe50[i]+male_transport_number_reformed_jux3_nhe50[i]+male_transport_number_reformed_jux4_nhe50[i]+male_transport_number_reformed_jux5_nhe50[i] for i in range(len(male_transport_number_reformed_sup_nhe50))],bar_width,bottom=male_transport_number_reformed_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
male_later_nhe50=axarr[1,1].bar(np.arange(len(segment_transport))+bar_width,male_transport_number_reformed_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

female_sup=axarr[1,1].bar(np.arange(len(segment_transport[:6]))+2*bar_width,female_transport_number_reformed_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta',label='Female full ACEi')
female_jux=axarr[1,1].bar(np.arange(len(segment_transport[:6]))+2*bar_width,[female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i]+female_transport_number_reformed_jux3[i]+female_transport_number_reformed_jux4[i]+female_transport_number_reformed_jux5[i] for i in range(len(female_transport_number_reformed_sup))],bar_width,bottom=female_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
female_later=axarr[1,1].bar(np.arange(len(segment_transport))+2*bar_width,female_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

female_sup_nhe50=axarr[1,1].bar(np.arange(len(segment_transport[:6]))+3*bar_width,female_transport_number_reformed_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink',label='Female proximal ACEi')
female_jux_nhe50=axarr[1,1].bar(np.arange(len(segment_transport[:6]))+3*bar_width,[female_transport_number_reformed_jux1_nhe50[i]+female_transport_number_reformed_jux2_nhe50[i]+female_transport_number_reformed_jux3_nhe50[i]+female_transport_number_reformed_jux4_nhe50[i]+female_transport_number_reformed_jux5_nhe50[i] for i in range(len(female_transport_number_reformed_sup_nhe50))],bar_width,bottom=female_transport_number_reformed_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
female_later_nhe50=axarr[1,1].bar(np.arange(len(segment_transport))+3*bar_width,female_transport_number_reformed_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')

axarr[1,1].set_xticks(np.arange(len(segment_transport))+1.5*bar_width)
axarr[1,1].set_xticklabels(segment_transport,fontsize=30)
axarr[1,1].tick_params(axis='both',labelsize=40)
#axarr[0,1].set_ylim(-0.2,0.5)
axarr[1,1].set_ylabel('Glucose transport (mol/Day)',fontsize=30)

#==================================================================
# TA transport
#==================================================================

#=================
# Baseline
#=================

female_transport_number = []
female_transport_sup = []
female_transport_jux1 = []
female_transport_jux2 = []
female_transport_jux3 = []
female_transport_jux4 = []
female_transport_jux5 = []
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

    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    female_transport_number.append(0)

    female_transport_sup.append(solute_conversion*neph_weight[0]*(10**(7.4-6.8)*(datalist_sup[0]-datalist_sup[-1])-(datalist_sup_2[0]-datalist_sup_2[-1]))/(1+10**(7.4-6.8)))
    female_transport_jux1.append(solute_conversion*neph_weight[1]*(10**(7.4-6.8)*(datalist_jux1[0]-datalist_jux1[-1])-(datalist_jux1_2[0]-datalist_jux1_2[-1]))/(1+10**(7.4-6.8)))
    female_transport_jux2.append(solute_conversion*neph_weight[2]*(10**(7.4-6.8)*(datalist_jux2[0]-datalist_jux2[-1])-(datalist_jux2_2[0]-datalist_jux2_2[-1]))/(1+10**(7.4-6.8)))
    female_transport_jux3.append(solute_conversion*neph_weight[3]*(10**(7.4-6.8)*(datalist_jux3[0]-datalist_jux3[-1])-(datalist_jux3_2[0]-datalist_jux3_2[-1]))/(1+10**(7.4-6.8)))
    female_transport_jux4.append(solute_conversion*neph_weight[4]*(10**(7.4-6.8)*(datalist_jux4[0]-datalist_jux4[-1])-(datalist_jux4_2[0]-datalist_jux4_2[-1]))/(1+10**(7.4-6.8)))
    female_transport_jux5.append(solute_conversion*neph_weight[5]*(10**(7.4-6.8)*(datalist_jux5[0]-datalist_jux5[-1])-(datalist_jux5_2[0]-datalist_jux5_2[-1]))/(1+10**(7.4-6.8)))
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
    number_of_transport = datalist[0]-datalist[-1]
    number_of_transport_2 = datalist_2[0]-datalist_2[-1]
    female_transport_number.append(solute_conversion*(10**(7.4-6.8)*number_of_transport-number_of_transport_2)/(1+10**(7.4-6.8)))

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
    file_jux1 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux5.txt','r')
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
    file_jux1_2 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux1.txt','r')
    file_jux2_2 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux2.txt','r')
    file_jux3_2 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux3.txt','r')
    file_jux4_2 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux4.txt','r')
    file_jux5_2 = open(female_normal_file+'/female_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux5.txt','r')
    datalist_jux1_2 = []
    datalist_jux2_2 = []
    datalist_jux3_2 = []
    datalist_jux4_2 = []
    datalist_jux5_2 = []
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
    female_transport_long_jux1.append(solute_conversion*neph_weight[1]*(10**(7.4-6.8)*(datalist_jux1[0]-datalist_jux1[-1])-(datalist_jux1_2[0]-datalist_jux1_2[-1]))/(1+10**(7.4-6.8)))
    female_transport_long_jux2.append(solute_conversion*neph_weight[2]*(10**(7.4-6.8)*(datalist_jux2[0]-datalist_jux2[-1])-(datalist_jux2_2[0]-datalist_jux2_2[-1]))/(1+10**(7.4-6.8)))
    female_transport_long_jux3.append(solute_conversion*neph_weight[3]*(10**(7.4-6.8)*(datalist_jux3[0]-datalist_jux3[-1])-(datalist_jux3_2[0]-datalist_jux3_2[-1]))/(1+10**(7.4-6.8)))
    female_transport_long_jux4.append(solute_conversion*neph_weight[4]*(10**(7.4-6.8)*(datalist_jux4[0]-datalist_jux4[-1])-(datalist_jux4_2[0]-datalist_jux4_2[-1]))/(1+10**(7.4-6.8)))
    female_transport_long_jux5.append(solute_conversion*neph_weight[5]*(10**(7.4-6.8)*(datalist_jux5[0]-datalist_jux5[-1])-(datalist_jux5_2[0]-datalist_jux5_2[-1]))/(1+10**(7.4-6.8)))


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

male_transport_number = []
male_transport_sup = []
male_transport_jux1 = []
male_transport_jux2 = []
male_transport_jux3 = []
male_transport_jux4 = []
male_transport_jux5 = []
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

    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_transport_number.append(0)

    male_transport_sup.append(solute_conversion*neph_weight[0]*(10**(7.4-6.8)*(datalist_sup[0]-datalist_sup[-1])-(datalist_sup_2[0]-datalist_sup_2[-1]))/(1+10**(7.4-6.8)))
    male_transport_jux1.append(solute_conversion*neph_weight[1]*(10**(7.4-6.8)*(datalist_jux1[0]-datalist_jux1[-1])-(datalist_jux1_2[0]-datalist_jux1_2[-1]))/(1+10**(7.4-6.8)))
    male_transport_jux2.append(solute_conversion*neph_weight[2]*(10**(7.4-6.8)*(datalist_jux2[0]-datalist_jux2[-1])-(datalist_jux2_2[0]-datalist_jux2_2[-1]))/(1+10**(7.4-6.8)))
    male_transport_jux3.append(solute_conversion*neph_weight[3]*(10**(7.4-6.8)*(datalist_jux3[0]-datalist_jux3[-1])-(datalist_jux3_2[0]-datalist_jux3_2[-1]))/(1+10**(7.4-6.8)))
    male_transport_jux4.append(solute_conversion*neph_weight[4]*(10**(7.4-6.8)*(datalist_jux4[0]-datalist_jux4[-1])-(datalist_jux4_2[0]-datalist_jux4_2[-1]))/(1+10**(7.4-6.8)))
    male_transport_jux5.append(solute_conversion*neph_weight[5]*(10**(7.4-6.8)*(datalist_jux5[0]-datalist_jux5[-1])-(datalist_jux5_2[0]-datalist_jux5_2[-1]))/(1+10**(7.4-6.8)))
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
    number_of_transport = datalist[0]-datalist[-1]
    number_of_transport_2 = datalist_2[0]-datalist_2[-1]
    male_transport_number.append(solute_conversion*(10**(7.4-6.8)*number_of_transport-number_of_transport_2)/(1+10**(7.4-6.8)))

male_transport_number_reformed_sup = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux1 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux2 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux3 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux4 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed_jux5 = [0 for _ in segment_transport[:6]]
male_transport_number_reformed = [0 for _ in segment_transport]

male_transport_number_reformed[6] = male_transport_number[7]+male_transport_number[8]+male_transport_number[9]
print(male_transport_number_reformed)

male_transport_long_jux1 = []
male_transport_long_jux2 = []
male_transport_long_jux3 = []
male_transport_long_jux4 = []
male_transport_long_jux5 = []
for seg in segment_jux:
    file_jux1 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux5.txt','r')
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
    file_jux1_2 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux1.txt','r')
    file_jux2_2 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux2.txt','r')
    file_jux3_2 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux3.txt','r')
    file_jux4_2 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux4.txt','r')
    file_jux5_2 = open(male_normal_file+'/male_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux5.txt','r')
    datalist_jux1_2 = []
    datalist_jux2_2 = []
    datalist_jux3_2 = []
    datalist_jux4_2 = []
    datalist_jux5_2 = []
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
    male_transport_long_jux1.append(solute_conversion*neph_weight[1]*(10**(7.4-6.8)*(datalist_jux1[0]-datalist_jux1[-1])-(datalist_jux1_2[0]-datalist_jux1_2[-1]))/(1+10**(7.4-6.8)))
    male_transport_long_jux2.append(solute_conversion*neph_weight[2]*(10**(7.4-6.8)*(datalist_jux2[0]-datalist_jux2[-1])-(datalist_jux2_2[0]-datalist_jux2_2[-1]))/(1+10**(7.4-6.8)))
    male_transport_long_jux3.append(solute_conversion*neph_weight[3]*(10**(7.4-6.8)*(datalist_jux3[0]-datalist_jux3[-1])-(datalist_jux3_2[0]-datalist_jux3_2[-1]))/(1+10**(7.4-6.8)))
    male_transport_long_jux4.append(solute_conversion*neph_weight[4]*(10**(7.4-6.8)*(datalist_jux4[0]-datalist_jux4[-1])-(datalist_jux4_2[0]-datalist_jux4_2[-1]))/(1+10**(7.4-6.8)))
    male_transport_long_jux5.append(solute_conversion*neph_weight[5]*(10**(7.4-6.8)*(datalist_jux5[0]-datalist_jux5[-1])-(datalist_jux5_2[0]-datalist_jux5_2[-1]))/(1+10**(7.4-6.8)))


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

#==================================================================
# SGLT2i
#==================================================================
female_transport_number_nhe50 = []
female_transport_sup_nhe50 = []
female_transport_jux1_nhe50 = []
female_transport_jux2_nhe50 = []
female_transport_jux3_nhe50 = []
female_transport_jux4_nhe50 = []
female_transport_jux5_nhe50 = []
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

    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    female_transport_number_nhe50.append(0)

    female_transport_sup_nhe50.append(solute_conversion*neph_weight[0]*(10**(7.4-6.8)*(datalist_sup[0]-datalist_sup[-1])-(datalist_sup_2[0]-datalist_sup_2[-1]))/(1+10**(7.4-6.8)))
    female_transport_jux1_nhe50.append(solute_conversion*neph_weight[1]*(10**(7.4-6.8)*(datalist_jux1[0]-datalist_jux1[-1])-(datalist_jux1_2[0]-datalist_jux1_2[-1]))/(1+10**(7.4-6.8)))
    female_transport_jux2_nhe50.append(solute_conversion*neph_weight[2]*(10**(7.4-6.8)*(datalist_jux2[0]-datalist_jux2[-1])-(datalist_jux2_2[0]-datalist_jux2_2[-1]))/(1+10**(7.4-6.8)))
    female_transport_jux3_nhe50.append(solute_conversion*neph_weight[3]*(10**(7.4-6.8)*(datalist_jux3[0]-datalist_jux3[-1])-(datalist_jux3_2[0]-datalist_jux3_2[-1]))/(1+10**(7.4-6.8)))
    female_transport_jux4_nhe50.append(solute_conversion*neph_weight[4]*(10**(7.4-6.8)*(datalist_jux4[0]-datalist_jux4[-1])-(datalist_jux4_2[0]-datalist_jux4_2[-1]))/(1+10**(7.4-6.8)))
    female_transport_jux5_nhe50.append(solute_conversion*neph_weight[5]*(10**(7.4-6.8)*(datalist_jux5[0]-datalist_jux5[-1])-(datalist_jux5_2[0]-datalist_jux5_2[-1]))/(1+10**(7.4-6.8)))
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
    number_of_transport = datalist[0]-datalist[-1]
    number_of_transport_2 = datalist_2[0]-datalist_2[-1]
    female_transport_number_nhe50.append(solute_conversion*(10**(7.4-6.8)*number_of_transport-number_of_transport_2)/(1+10**(7.4-6.8)))

female_transport_number_reformed_sup_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux1_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux2_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux3_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux4_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux5_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_nhe50 = [0 for _ in segment_transport]

female_transport_number_reformed_nhe50[6] = female_transport_number_nhe50[7]+female_transport_number_nhe50[8]+female_transport_number_nhe50[9]

female_transport_long_jux1_nhe50 = []
female_transport_long_jux2_nhe50 = []
female_transport_long_jux3_nhe50 = []
female_transport_long_jux4_nhe50 = []
female_transport_long_jux5_nhe50 = []
for seg in segment_jux:
    file_jux1 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux5.txt','r')
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
    file_jux1_2 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux1.txt','r')
    file_jux2_2 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux2.txt','r')
    file_jux3_2 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux3.txt','r')
    file_jux4_2 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux4.txt','r')
    file_jux5_2 = open(female_nhe50_file+'/female_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux5.txt','r')
    datalist_jux1_2 = []
    datalist_jux2_2 = []
    datalist_jux3_2 = []
    datalist_jux4_2 = []
    datalist_jux5_2 = []
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
    female_transport_long_jux1_nhe50.append(solute_conversion*neph_weight[1]*(10**(7.4-6.8)*(datalist_jux1[0]-datalist_jux1[-1])-(datalist_jux1_2[0]-datalist_jux1_2[-1]))/(1+10**(7.4-6.8)))
    female_transport_long_jux2_nhe50.append(solute_conversion*neph_weight[2]*(10**(7.4-6.8)*(datalist_jux2[0]-datalist_jux2[-1])-(datalist_jux2_2[0]-datalist_jux2_2[-1]))/(1+10**(7.4-6.8)))
    female_transport_long_jux3_nhe50.append(solute_conversion*neph_weight[3]*(10**(7.4-6.8)*(datalist_jux3[0]-datalist_jux3[-1])-(datalist_jux3_2[0]-datalist_jux3_2[-1]))/(1+10**(7.4-6.8)))
    female_transport_long_jux4_nhe50.append(solute_conversion*neph_weight[4]*(10**(7.4-6.8)*(datalist_jux4[0]-datalist_jux4[-1])-(datalist_jux4_2[0]-datalist_jux4_2[-1]))/(1+10**(7.4-6.8)))
    female_transport_long_jux5_nhe50.append(solute_conversion*neph_weight[5]*(10**(7.4-6.8)*(datalist_jux5[0]-datalist_jux5[-1])-(datalist_jux5_2[0]-datalist_jux5_2[-1]))/(1+10**(7.4-6.8)))


female_transport_number_reformed_sup_nhe50[0] = female_transport_sup_nhe50[0]+female_transport_sup_nhe50[1]
female_transport_number_reformed_sup_nhe50[1] = female_transport_sup_nhe50[2]
female_transport_number_reformed_sup_nhe50[3] = female_transport_sup_nhe50[3]+female_transport_sup_nhe50[4]
female_transport_number_reformed_sup_nhe50[4] = female_transport_sup_nhe50[5]
female_transport_number_reformed_sup_nhe50[5] = female_transport_sup_nhe50[6]

female_transport_number_reformed_jux1_nhe50[0] = female_transport_jux1_nhe50[0]+female_transport_jux1_nhe50[1]
female_transport_number_reformed_jux1_nhe50[1] = female_transport_long_jux1_nhe50[0]+female_transport_long_jux1_nhe50[1]
female_transport_number_reformed_jux1_nhe50[2] = female_transport_long_jux1_nhe50[2]
female_transport_number_reformed_jux1_nhe50[3] = female_transport_jux1_nhe50[3]+female_transport_jux1_nhe50[4]
female_transport_number_reformed_jux1_nhe50[4] = female_transport_jux1_nhe50[5]
female_transport_number_reformed_jux1_nhe50[5] = female_transport_jux1_nhe50[6]

female_transport_number_reformed_jux2_nhe50[0] = female_transport_jux2_nhe50[0]+female_transport_jux2_nhe50[1]
female_transport_number_reformed_jux2_nhe50[1] = female_transport_long_jux2_nhe50[0]+female_transport_long_jux2_nhe50[1]
female_transport_number_reformed_jux2_nhe50[2] = female_transport_long_jux2_nhe50[2]
female_transport_number_reformed_jux2_nhe50[3] = female_transport_jux2_nhe50[3]+female_transport_jux2_nhe50[4]
female_transport_number_reformed_jux2_nhe50[4] = female_transport_jux2_nhe50[5]
female_transport_number_reformed_jux2_nhe50[5] = female_transport_jux2_nhe50[6]

female_transport_number_reformed_jux3_nhe50[0] = female_transport_jux3_nhe50[0]+female_transport_jux3_nhe50[1]
female_transport_number_reformed_jux3_nhe50[1] = female_transport_long_jux3_nhe50[0]+female_transport_long_jux3_nhe50[1]
female_transport_number_reformed_jux3_nhe50[2] = female_transport_long_jux3_nhe50[2]
female_transport_number_reformed_jux3_nhe50[3] = female_transport_jux3_nhe50[3]+female_transport_jux3_nhe50[4]
female_transport_number_reformed_jux3_nhe50[4] = female_transport_jux3_nhe50[5]
female_transport_number_reformed_jux3_nhe50[5] = female_transport_jux3_nhe50[6]

female_transport_number_reformed_jux4_nhe50[0] = female_transport_jux4_nhe50[0]+female_transport_jux4_nhe50[1]
female_transport_number_reformed_jux4_nhe50[1] = female_transport_long_jux4_nhe50[0]+female_transport_long_jux4_nhe50[1]
female_transport_number_reformed_jux4_nhe50[2] = female_transport_long_jux4_nhe50[2]
female_transport_number_reformed_jux4_nhe50[3] = female_transport_jux4_nhe50[3]+female_transport_jux4_nhe50[4]
female_transport_number_reformed_jux4_nhe50[4] = female_transport_jux4_nhe50[5]
female_transport_number_reformed_jux4_nhe50[5] = female_transport_jux4_nhe50[6]

female_transport_number_reformed_jux5_nhe50[0] = female_transport_jux5_nhe50[0]+female_transport_jux5_nhe50[1]
female_transport_number_reformed_jux5_nhe50[1] = female_transport_long_jux5_nhe50[0]+female_transport_long_jux5_nhe50[1]
female_transport_number_reformed_jux5_nhe50[2] = female_transport_long_jux5_nhe50[2]
female_transport_number_reformed_jux5_nhe50[3] = female_transport_jux5_nhe50[3]+female_transport_jux5_nhe50[4]
female_transport_number_reformed_jux5_nhe50[4] = female_transport_jux5_nhe50[5]
female_transport_number_reformed_jux5_nhe50[5] = female_transport_jux5_nhe50[6]

male_transport_number_nhe50 = []
male_transport_sup_nhe50 = []
male_transport_jux1_nhe50 = []
male_transport_jux2_nhe50 = []
male_transport_jux3_nhe50 = []
male_transport_jux4_nhe50 = []
male_transport_jux5_nhe50 = []
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

    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_transport_number_nhe50.append(0)

    male_transport_sup_nhe50.append(solute_conversion*neph_weight[0]*(10**(7.4-6.8)*(datalist_sup[0]-datalist_sup[-1])-(datalist_sup_2[0]-datalist_sup_2[-1]))/(1+10**(7.4-6.8)))
    male_transport_jux1_nhe50.append(solute_conversion*neph_weight[1]*(10**(7.4-6.8)*(datalist_jux1[0]-datalist_jux1[-1])-(datalist_jux1_2[0]-datalist_jux1_2[-1]))/(1+10**(7.4-6.8)))
    male_transport_jux2_nhe50.append(solute_conversion*neph_weight[2]*(10**(7.4-6.8)*(datalist_jux2[0]-datalist_jux2[-1])-(datalist_jux2_2[0]-datalist_jux2_2[-1]))/(1+10**(7.4-6.8)))
    male_transport_jux3_nhe50.append(solute_conversion*neph_weight[3]*(10**(7.4-6.8)*(datalist_jux3[0]-datalist_jux3[-1])-(datalist_jux3_2[0]-datalist_jux3_2[-1]))/(1+10**(7.4-6.8)))
    male_transport_jux4_nhe50.append(solute_conversion*neph_weight[4]*(10**(7.4-6.8)*(datalist_jux4[0]-datalist_jux4[-1])-(datalist_jux4_2[0]-datalist_jux4_2[-1]))/(1+10**(7.4-6.8)))
    male_transport_jux5_nhe50.append(solute_conversion*neph_weight[5]*(10**(7.4-6.8)*(datalist_jux5[0]-datalist_jux5[-1])-(datalist_jux5_2[0]-datalist_jux5_2[-1]))/(1+10**(7.4-6.8)))
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
    number_of_transport = datalist[0]-datalist[-1]
    number_of_transport_2 = datalist_2[0]-datalist_2[-1]
    male_transport_number_nhe50.append(solute_conversion*(10**(7.4-6.8)*number_of_transport-number_of_transport_2)/(1+10**(7.4-6.8)))

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
    file_jux1 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_H2PO4_in_Lumen_jux5.txt','r')
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
    file_jux1_2 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux1.txt','r')
    file_jux2_2 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux2.txt','r')
    file_jux3_2 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux3.txt','r')
    file_jux4_2 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux4.txt','r')
    file_jux5_2 = open(male_nhe50_file+'/male_hum_'+seg+'_flow_of_HPO4_in_Lumen_jux5.txt','r')
    datalist_jux1_2 = []
    datalist_jux2_2 = []
    datalist_jux3_2 = []
    datalist_jux4_2 = []
    datalist_jux5_2 = []
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
    male_transport_long_jux1_nhe50.append(solute_conversion*neph_weight[1]*(10**(7.4-6.8)*(datalist_jux1[0]-datalist_jux1[-1])-(datalist_jux1_2[0]-datalist_jux1_2[-1]))/(1+10**(7.4-6.8)))
    male_transport_long_jux2_nhe50.append(solute_conversion*neph_weight[2]*(10**(7.4-6.8)*(datalist_jux2[0]-datalist_jux2[-1])-(datalist_jux2_2[0]-datalist_jux2_2[-1]))/(1+10**(7.4-6.8)))
    male_transport_long_jux3_nhe50.append(solute_conversion*neph_weight[3]*(10**(7.4-6.8)*(datalist_jux3[0]-datalist_jux3[-1])-(datalist_jux3_2[0]-datalist_jux3_2[-1]))/(1+10**(7.4-6.8)))
    male_transport_long_jux4_nhe50.append(solute_conversion*neph_weight[4]*(10**(7.4-6.8)*(datalist_jux4[0]-datalist_jux4[-1])-(datalist_jux4_2[0]-datalist_jux4_2[-1]))/(1+10**(7.4-6.8)))
    male_transport_long_jux5_nhe50.append(solute_conversion*neph_weight[5]*(10**(7.4-6.8)*(datalist_jux5[0]-datalist_jux5[-1])-(datalist_jux5_2[0]-datalist_jux5_2[-1]))/(1+10**(7.4-6.8)))


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

male_sup=axarr[2,0].bar(np.arange(len(segment_transport[:6])),male_transport_number_reformed_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Male full ACEi')
male_jux=axarr[2,0].bar(np.arange(len(segment_transport[:6])),[male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i]+male_transport_number_reformed_jux5[i] for i in range(len(male_transport_number_reformed_sup))],bar_width,bottom=male_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
male_later=axarr[2,0].bar(np.arange(len(segment_transport)),male_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

male_sup_nhe50=axarr[2,0].bar(np.arange(len(segment_transport[:6]))+bar_width,male_transport_number_reformed_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue',label='Male proximal ACEi')
male_jux_nhe50=axarr[2,0].bar(np.arange(len(segment_transport[:6]))+bar_width,[male_transport_number_reformed_jux1_nhe50[i]+male_transport_number_reformed_jux2_nhe50[i]+male_transport_number_reformed_jux3_nhe50[i]+male_transport_number_reformed_jux4_nhe50[i]+male_transport_number_reformed_jux5_nhe50[i] for i in range(len(male_transport_number_reformed_sup_nhe50))],bar_width,bottom=male_transport_number_reformed_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
male_later_nhe50=axarr[2,0].bar(np.arange(len(segment_transport))+bar_width,male_transport_number_reformed_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

female_sup=axarr[2,0].bar(np.arange(len(segment_transport[:6]))+2*bar_width,female_transport_number_reformed_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta',label='Female full ACEi')
female_jux=axarr[2,0].bar(np.arange(len(segment_transport[:6]))+2*bar_width,[female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i]+female_transport_number_reformed_jux3[i]+female_transport_number_reformed_jux4[i]+female_transport_number_reformed_jux5[i] for i in range(len(female_transport_number_reformed_sup))],bar_width,bottom=female_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
female_later=axarr[2,0].bar(np.arange(len(segment_transport))+2*bar_width,female_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

female_sup_nhe50=axarr[2,0].bar(np.arange(len(segment_transport[:6]))+3*bar_width,female_transport_number_reformed_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink',label='Female proximal ACEi')
female_jux_nhe50=axarr[2,0].bar(np.arange(len(segment_transport[:6]))+3*bar_width,[female_transport_number_reformed_jux1_nhe50[i]+female_transport_number_reformed_jux2_nhe50[i]+female_transport_number_reformed_jux3_nhe50[i]+female_transport_number_reformed_jux4_nhe50[i]+female_transport_number_reformed_jux5_nhe50[i] for i in range(len(female_transport_number_reformed_sup_nhe50))],bar_width,bottom=female_transport_number_reformed_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
female_later_nhe50=axarr[2,0].bar(np.arange(len(segment_transport))+3*bar_width,female_transport_number_reformed_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')

axarr[2,0].set_xticks(np.arange(len(segment_transport))+1.5*bar_width)
axarr[2,0].set_xticklabels(segment_transport,fontsize=30)
axarr[2,0].tick_params(axis='both',labelsize=40)
#axarr[0,1].set_ylim(-0.2,0.5)
axarr[2,0].set_ylabel('TA transport (mol/Day)',fontsize=30)

#==================================================================
# Water volume
#==================================================================

#==========================
#   Baseline
#==========================

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

male_transport_number = []
male_transport_sup = []
male_transport_jux1 = []
male_transport_jux2 = []
male_transport_jux3 = []
male_transport_jux4 = []
male_transport_jux5 = []
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
    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_transport_number.append(0)
    male_transport_sup.append(volume_conversion*neph_weight[0]*(datalist_sup[0]-datalist_sup[-1]))
    male_transport_jux1.append(volume_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    male_transport_jux2.append(volume_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    male_transport_jux3.append(volume_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    male_transport_jux4.append(volume_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    male_transport_jux5.append(volume_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))
for seg in segment_late:
    file_data = open(male_normal_file+'/male_hum_'+seg+'_water_volume_in_Lumen.txt','r')
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
    file_jux1 = open(male_normal_file+'/male_hum_'+seg+'_water_volume_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_normal_file+'/male_hum_'+seg+'_water_volume_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_normal_file+'/male_hum_'+seg+'_water_volume_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_normal_file+'/male_hum_'+seg+'_water_volume_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_normal_file+'/male_hum_'+seg+'_water_volume_in_Lumen_jux5.txt','r')
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

#============================
#   SGLT2i
#============================

female_transport_number_nhe50 = []
female_transport_sup_nhe50 = []
female_transport_jux1_nhe50 = []
female_transport_jux2_nhe50 = []
female_transport_jux3_nhe50 = []
female_transport_jux4_nhe50 = []
female_transport_jux5_nhe50 = []
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
    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    female_transport_number_nhe50.append(0)
    female_transport_sup_nhe50.append(volume_conversion*neph_weight[0]*(datalist_sup[0]-datalist_sup[-1]))
    female_transport_jux1_nhe50.append(volume_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    female_transport_jux2_nhe50.append(volume_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    female_transport_jux3_nhe50.append(volume_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    female_transport_jux4_nhe50.append(volume_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    female_transport_jux5_nhe50.append(volume_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))
for seg in segment_late:
    file_data = open(female_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen.txt','r')
    datalist = []
    for i in file_data:
        line = i.split(' ')
        datalist.append(float(line[0]))
        number_of_transport = datalist[0]-datalist[-1]
    female_transport_number_nhe50.append(volume_conversion*number_of_transport)

female_transport_number_reformed_sup_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux1_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux2_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux3_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux4_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_jux5_nhe50 = [0 for _ in segment_transport[:6]]
female_transport_number_reformed_nhe50 = [0 for _ in segment_transport]

female_transport_number_reformed_nhe50[6] = female_transport_number_nhe50[7]+female_transport_number_nhe50[8]+female_transport_number_nhe50[9]

female_transport_long_jux1_nhe50 = []
female_transport_long_jux2_nhe50 = []
female_transport_long_jux3_nhe50 = []
female_transport_long_jux4_nhe50 = []
female_transport_long_jux5_nhe50 = []
for seg in segment_jux:
    file_jux1 = open(female_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux1.txt','r')
    file_jux2 = open(female_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux2.txt','r')
    file_jux3 = open(female_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux3.txt','r')
    file_jux4 = open(female_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux4.txt','r')
    file_jux5 = open(female_nhe50_file+'/female_hum_'+seg+'_water_volume_in_Lumen_jux5.txt','r')
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
    female_transport_long_jux1_nhe50.append(volume_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    female_transport_long_jux2_nhe50.append(volume_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    female_transport_long_jux3_nhe50.append(volume_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    female_transport_long_jux4_nhe50.append(volume_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    female_transport_long_jux5_nhe50.append(volume_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))

female_transport_number_reformed_sup_nhe50[0] = female_transport_sup_nhe50[0]+female_transport_sup_nhe50[1]
female_transport_number_reformed_sup_nhe50[1] = female_transport_sup_nhe50[2]
female_transport_number_reformed_sup_nhe50[3] = female_transport_sup_nhe50[3]+female_transport_sup_nhe50[4]
female_transport_number_reformed_sup_nhe50[4] = female_transport_sup_nhe50[5]
female_transport_number_reformed_sup_nhe50[5] = female_transport_sup_nhe50[6]

female_transport_number_reformed_jux1_nhe50[0] = female_transport_jux1_nhe50[0]+female_transport_jux1_nhe50[1]
female_transport_number_reformed_jux1_nhe50[1] = female_transport_long_jux1_nhe50[0]+female_transport_long_jux1_nhe50[1]
female_transport_number_reformed_jux1_nhe50[2] = female_transport_long_jux1_nhe50[2]
female_transport_number_reformed_jux1_nhe50[3] = female_transport_jux1_nhe50[3]+female_transport_jux1_nhe50[4]
female_transport_number_reformed_jux1_nhe50[4] = female_transport_jux1_nhe50[5]
female_transport_number_reformed_jux1_nhe50[5] = female_transport_jux1_nhe50[6]

female_transport_number_reformed_jux2_nhe50[0] = female_transport_jux2_nhe50[0]+female_transport_jux2_nhe50[1]
female_transport_number_reformed_jux2_nhe50[1] = female_transport_long_jux2_nhe50[0]+female_transport_long_jux2_nhe50[1]
female_transport_number_reformed_jux2_nhe50[2] = female_transport_long_jux2_nhe50[2]
female_transport_number_reformed_jux2_nhe50[3] = female_transport_jux2_nhe50[3]+female_transport_jux2_nhe50[4]
female_transport_number_reformed_jux2_nhe50[4] = female_transport_jux2_nhe50[5]
female_transport_number_reformed_jux2_nhe50[5] = female_transport_jux2_nhe50[6]

female_transport_number_reformed_jux3_nhe50[0] = female_transport_jux3_nhe50[0]+female_transport_jux3_nhe50[1]
female_transport_number_reformed_jux3_nhe50[1] = female_transport_long_jux3_nhe50[0]+female_transport_long_jux3_nhe50[1]
female_transport_number_reformed_jux3_nhe50[2] = female_transport_long_jux3_nhe50[2]
female_transport_number_reformed_jux3_nhe50[3] = female_transport_jux3_nhe50[3]+female_transport_jux3_nhe50[4]
female_transport_number_reformed_jux3_nhe50[4] = female_transport_jux3_nhe50[5]
female_transport_number_reformed_jux3_nhe50[5] = female_transport_jux3_nhe50[6]

female_transport_number_reformed_jux4_nhe50[0] = female_transport_jux4_nhe50[0]+female_transport_jux4_nhe50[1]
female_transport_number_reformed_jux4_nhe50[1] = female_transport_long_jux4_nhe50[0]+female_transport_long_jux4_nhe50[1]
female_transport_number_reformed_jux4_nhe50[2] = female_transport_long_jux4_nhe50[2]
female_transport_number_reformed_jux4_nhe50[3] = female_transport_jux4_nhe50[3]+female_transport_jux4_nhe50[4]
female_transport_number_reformed_jux4_nhe50[4] = female_transport_jux4_nhe50[5]
female_transport_number_reformed_jux4_nhe50[5] = female_transport_jux4_nhe50[6]

female_transport_number_reformed_jux5_nhe50[0] = female_transport_jux5_nhe50[0]+female_transport_jux5_nhe50[1]
female_transport_number_reformed_jux5_nhe50[1] = female_transport_long_jux5_nhe50[0]+female_transport_long_jux5_nhe50[1]
female_transport_number_reformed_jux5_nhe50[2] = female_transport_long_jux5_nhe50[2]
female_transport_number_reformed_jux5_nhe50[3] = female_transport_jux5_nhe50[3]+female_transport_jux5_nhe50[4]
female_transport_number_reformed_jux5_nhe50[4] = female_transport_jux5_nhe50[5]
female_transport_number_reformed_jux5_nhe50[5] = female_transport_jux5_nhe50[6]

male_transport_number_nhe50 = []
male_transport_sup_nhe50 = []
male_transport_jux1_nhe50 = []
male_transport_jux2_nhe50 = []
male_transport_jux3_nhe50 = []
male_transport_jux4_nhe50 = []
male_transport_jux5_nhe50 = []
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
    #number_of_delivery = neph_weight[0]*datalist_sup[0]+neph_weight[1]*datalist_jux1[0]+neph_weight[2]*datalist_jux2[0]+neph_weight[3]*datalist_jux3[0]+neph_weight[4]*datalist_jux4[0]+neph_weight[5]*datalist_jux5[0]
    male_transport_number_nhe50.append(0)
    male_transport_sup_nhe50.append(volume_conversion*neph_weight[0]*(datalist_sup[0]-datalist_sup[-1]))
    male_transport_jux1_nhe50.append(volume_conversion*neph_weight[1]*(datalist_jux1[0]-datalist_jux1[-1]))
    male_transport_jux2_nhe50.append(volume_conversion*neph_weight[2]*(datalist_jux2[0]-datalist_jux2[-1]))
    male_transport_jux3_nhe50.append(volume_conversion*neph_weight[3]*(datalist_jux3[0]-datalist_jux3[-1]))
    male_transport_jux4_nhe50.append(volume_conversion*neph_weight[4]*(datalist_jux4[0]-datalist_jux4[-1]))
    male_transport_jux5_nhe50.append(volume_conversion*neph_weight[5]*(datalist_jux5[0]-datalist_jux5[-1]))
for seg in segment_late:
    file_data = open(male_nhe50_file+'/male_hum_'+seg+'_water_volume_in_Lumen.txt','r')
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
    file_jux1 = open(male_nhe50_file+'/male_hum_'+seg+'_water_volume_in_Lumen_jux1.txt','r')
    file_jux2 = open(male_nhe50_file+'/male_hum_'+seg+'_water_volume_in_Lumen_jux2.txt','r')
    file_jux3 = open(male_nhe50_file+'/male_hum_'+seg+'_water_volume_in_Lumen_jux3.txt','r')
    file_jux4 = open(male_nhe50_file+'/male_hum_'+seg+'_water_volume_in_Lumen_jux4.txt','r')
    file_jux5 = open(male_nhe50_file+'/male_hum_'+seg+'_water_volume_in_Lumen_jux5.txt','r')
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

male_sup=axarr[2,1].bar(np.arange(len(segment_transport[:6])),male_transport_number_reformed_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue',label='Male full ACEi')
male_jux=axarr[2,1].bar(np.arange(len(segment_transport[:6])),[male_transport_number_reformed_jux1[i]+male_transport_number_reformed_jux2[i]+male_transport_number_reformed_jux3[i]+male_transport_number_reformed_jux4[i]+male_transport_number_reformed_jux5[i] for i in range(len(male_transport_number_reformed_sup))],bar_width,bottom=male_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
male_later=axarr[2,1].bar(np.arange(len(segment_transport)),male_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='royalblue')

male_sup_nhe50=axarr[2,1].bar(np.arange(len(segment_transport[:6]))+bar_width,male_transport_number_reformed_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue',label='Male proximal ACEi')
male_jux_nhe50=axarr[2,1].bar(np.arange(len(segment_transport[:6]))+bar_width,[male_transport_number_reformed_jux1_nhe50[i]+male_transport_number_reformed_jux2_nhe50[i]+male_transport_number_reformed_jux3_nhe50[i]+male_transport_number_reformed_jux4_nhe50[i]+male_transport_number_reformed_jux5_nhe50[i] for i in range(len(male_transport_number_reformed_sup_nhe50))],bar_width,bottom=male_transport_number_reformed_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
male_later_nhe50=axarr[2,1].bar(np.arange(len(segment_transport))+bar_width,male_transport_number_reformed_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='deepskyblue')

female_sup=axarr[2,1].bar(np.arange(len(segment_transport[:6]))+2*bar_width,female_transport_number_reformed_sup,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta',label='Female full ACEi')
female_jux=axarr[2,1].bar(np.arange(len(segment_transport[:6]))+2*bar_width,[female_transport_number_reformed_jux1[i]+female_transport_number_reformed_jux2[i]+female_transport_number_reformed_jux3[i]+female_transport_number_reformed_jux4[i]+female_transport_number_reformed_jux5[i] for i in range(len(female_transport_number_reformed_sup))],bar_width,bottom=female_transport_number_reformed_sup,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
female_later=axarr[2,1].bar(np.arange(len(segment_transport))+2*bar_width,female_transport_number_reformed,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='magenta')

female_sup_nhe50=axarr[2,1].bar(np.arange(len(segment_transport[:6]))+3*bar_width,female_transport_number_reformed_sup_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink',label='Female proximal ACEi')
female_jux_nhe50=axarr[2,1].bar(np.arange(len(segment_transport[:6]))+3*bar_width,[female_transport_number_reformed_jux1_nhe50[i]+female_transport_number_reformed_jux2_nhe50[i]+female_transport_number_reformed_jux3_nhe50[i]+female_transport_number_reformed_jux4_nhe50[i]+female_transport_number_reformed_jux5_nhe50[i] for i in range(len(female_transport_number_reformed_sup_nhe50))],bar_width,bottom=female_transport_number_reformed_sup_nhe50,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='White')
female_later_nhe50=axarr[2,1].bar(np.arange(len(segment_transport))+3*bar_width,female_transport_number_reformed_nhe50,bar_width,align='center',alpha=0.8,linewidth=2,edgecolor='black',color='hotpink')

axarr[2,1].set_xticks(np.arange(len(segment_transport))+1.5*bar_width)
axarr[2,1].set_xticklabels(segment_transport,fontsize=30)
axarr[2,1].tick_params(axis='both',labelsize=40)
#axarr[2,1].set_ylim(0,120)
axarr[2,1].set_ylabel('Volume transport (L/Day)',fontsize=30)
#axarr[3,0].legend(fontsize=30,markerscale=30)

axarr[0,0].text(-1.5,axarr[0,0].get_ylim()[1],'A',size=40,weight='bold')
axarr[0,1].text(-1.5,axarr[0,1].get_ylim()[1],'B',size=40,weight='bold')
axarr[1,0].text(-1.5,axarr[1,0].get_ylim()[1],'C',size=40,weight='bold')
axarr[1,1].text(-1.5,axarr[1,1].get_ylim()[1],'D',size=40,weight='bold')
axarr[2,0].text(-1.5,axarr[2,0].get_ylim()[1],'E',size=40,weight='bold')
axarr[2,1].text(-1.5,axarr[2,1].get_ylim()[1],'F',size=40,weight='bold')

plt.savefig('transport_diabetic_men_women',bbox_inches='tight')