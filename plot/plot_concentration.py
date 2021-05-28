import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os
import argparse

solute = ['Na','K','Cl','HCO3','H2CO3','CO2','HPO4','H2PO4','urea','NH3','NH4','H','HCO2','H2CO2','glu']
parser = argparse.ArgumentParser()

parser.add_argument('--solute',choices=solute,required = True,type = str,help='select a solute to plot')
parser.add_argument('--nephrontype',choices = ['sup','jux1','jux2','jux3','jux4','jux5'],required = True,type = str,help='select the type of nephron')
parser.add_argument('--inhibition',choices=['NHE3','NKCC2'],default = 'normal',type = str,help = 'any transporter inhibition')
parser.add_argument('--percentage',default = 0,type = float,help='percentage of inhibition')
parser.add_argument('--output',required = True,type = str,help = 'save plots into output file')

args = parser.parse_args()
s = args.solute
neph_type = args.nephrontype
inhib = args.inhibition
perc = args.percentage
output = args.output

if inhib == 'normal' and perc == 0:
    male_file_name = 'male_normal_check'
    female_file_name = 'female_normal_check'
elif inhib == 'NHE3':
    male_file_name = 'male_nhe'+str(int(perc*100))+'_check'
    female_file_name = 'female_nhe'+str(int(perc*100))+'_check'
elif inhib == 'NKCC2':
    male_file_name = 'male_nkcc'+str(int(perc*100))+'_check'
    female_file_name = 'female_nkcc'+str(int(perc*100))+'_check'

os.makedirs(output)

if neph_type == 'sup':
    pos_pt=[1.1*i/199 for i in range(176)]
    pos_s3=[1.1*i/199 for i in range(175,200)]
    pos_sdl=[1.1+0.14*i/199 for i in range(200)]
    pos_mtal=[1.1+0.14+0.2*i/199 for i in range(200)]
    pos_ctal=[1.1+0.14+0.2+0.2*i/199 for i in range(200)]
    pos_dct=[1.1+0.14+0.2+0.2+0.1*i/199 for i in range(200)]
    pos_cnt=[1.1+0.14+0.2+0.2+0.1+0.2*i/199 for i in range(200)]
    pos=pos_pt+pos_s3+pos_sdl+pos_mtal+pos_ctal+pos_dct+pos_cnt
else:
    if neph_type == 'jux1':
        looplen = 0.2
    elif neph_type == 'jux2':
    	looplen = 0.4
    elif neph_type == 'jux3':
    	looplen = 0.6
    elif neph_type == 'jux4':
    	looplen = 0.8
    elif neph_type == 'jux5':
    	looplen = 1.0
    pos_pt=[1.1*i/199 for i in range(176)]
    pos_s3=[1.1*i/199 for i in range(175,200)]
    pos_sdl=[1.1+0.14*i/199 for i in range(200)]
    pos_ldl=[1.1+0.14+0.5*looplen*i/199 for i in range(200)]
    pos_lal=[1.1+0.14+0.5*looplen+0.5*looplen*i/199 for i in range(200)]
    pos_mtal=[1.1+0.14+0.5*looplen+0.5*looplen+0.2*i/199 for i in range(200)]
    pos_ctal=[1.1+0.14+0.5*looplen+0.5*looplen+0.2+0.05*i/199 for i in range(200)]
    pos_dct=[1.1+0.14+0.5*looplen+0.5*looplen+0.2+0.05+0.1*i/199 for i in range(200)]
    pos_cnt=[1.1+0.14+0.5*looplen+0.5*looplen+0.2+0.05+0.1+0.3*i/199 for i in range(200)]
    pos=pos_pt+pos_s3+pos_sdl+pos_ldl+pos_lal+pos_mtal+pos_ctal+pos_dct+pos_cnt

if neph_type == 'sup':
    segs = ['pt','s3','sdl','mtal','ctal','dct','cnt']
    #pos = [pos_pt,pos_s3,pos_sdl,pos_mtal,pos_ctal,pos_dct,pos_cnt]
else:
    segs = ['pt','s3','sdl','ldl','lal','mtal','ctal','dct','cnt']
    #pos = [pos_pt,pos_s3,pos_sdl,pos_ldl,pos_lal,pos_mtal,pos_ctal,pos_dct,pos_cnt]
male_list = []
female_list = []
for seg in segs:
    male = open(male_file_name+'/male'+seg+'_con_of_'+s+'_in_Lumen_'+neph_type+'.txt','r')
    female = open(female_file_name+'/female'+seg+'_con_of_'+s+'_in_Lumen_'+neph_type+'.txt','r')

    for i in male:
        line = i.split(' ')
        #print(line)
        #pos.append(float(line[5]))
        male_list.append(float(line[0]))
        #male_ph=[-np.log(i/1000)/np.log(10) for i in male_list]
    for i in female:
        line = i.split(' ')
        female_list.append(float(line[0]))
        #female_ph=[-np.log(i/1000)/np.log(10) for i in female_list]
plt.figure(figsize=[20,20])
plt.plot(pos,male_list,'-',label='Male')
plt.plot(pos,female_list,'--',label='Female')
if neph_type == 'sup':
    plt.plot(pos_pt+pos_s3,[130 for i in pos_pt+pos_s3],'--',pos_sdl,[140 for i in pos_sdl],'--',pos_mtal+pos_ctal,[145 for i in pos_mtal+pos_ctal],'--',pos_dct,[55 for i in pos_dct],'--',pos_cnt,[50 for i in pos_cnt],'--')
    #plt.text(0.5,132,'PT',fontsize=20)
    #plt.text(1.12,142,'SDL',fontsize=20)
    #plt.text(1.36,147,'TAL',fontsize=20)
    #plt.text(1.63,57,'DCT',fontsize=20)
    #plt.text(1.78,52,'CNT',fontsize=20)
    #plt.text(2.4,62,'CD',fontsize=20)
else:
    plt.plot(pos_pt+pos_s3,[130 for i in pos_pt+pos_s3],'--',pos_sdl,[140 for i in pos_sdl],'--',pos_mtal+pos_ctal,[145 for i in pos_mtal+pos_ctal],'--',pos_dct,[55 for i in pos_dct],'--',pos_cnt,[50 for i in pos_cnt],'--')
    plt.text(0.5,132,'PT',fontsize=20)
    plt.text(1.12,142,'SDL',fontsize=20)
    plt.text(2.36,147,'TAL',fontsize=20)
    plt.text(2.5,57,'DCT',fontsize=20)
    plt.text(2.7,52,'CNT',fontsize=20)
plt.legend(fontsize=20,markerscale=5)
plt.tick_params(labelsize=20)
plt.ylabel('Concentration of '+s,fontsize=20)
plt.savefig(output+'/concentration_of_'+s,bbox_inches = 'tight')