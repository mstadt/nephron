from driver import compute
from values import *
from defs import *
import electrochemical 
import water
import glucose
import cotransport
import NHE3
import ATPase
import NKCC
import KCC
import NCC
import ENaC
import Pendrin
import AE1
import NHE1
import flux
import os
import sys
import argparse
import multiprocessing
from set_params import set_torq_params

solute = ['Na','K','Cl','HCO3','H2CO3','CO2','HPO4','H2PO4','urea','NH3','NH4','H','HCO2','H2CO2','glu']
compart = ['Lumen','Cell','ICA','ICB','LIS','Bath']
cw=Vref*60e6

parser = argparse.ArgumentParser()
# required input
parser.add_argument('--sex',choices=['Male','Female'],required = True,type = str,help = 'Sex')
parser.add_argument('--species',choices=['human','rat'],required = True,type = str, help = 'Human model or Rat model')
parser.add_argument('--type',choices = ['superficial','multiple'],required = True,type=str,help='superficial nephron or multiple nephrons?')
parser.add_argument('--file2save', required = True, type = str, help = 'where to save?')

# diabetic options
parser.add_argument('--diabetes',choices = ['Severe','Moderate'],default='Non',type=str,help='diabete status (Severe/Moderate)')
parser.add_argument('--inhibition',choices=['ACE','SGLT2','NHE3-50','NHE3-80','NKCC2-70','NKCC2-100','NCC-70','NCC-100','ENaC-70','ENaC-100','SNB-70','SNB-100'],default = None,type = str,help = 'any transporter inhibition?')
parser.add_argument('--unx',choices=['N','Y'],default = 'N',type = str,help = 'uninephrectomy status')
# pregnancy option
parser.add_argument('--pregnant', choices=['mid','late'], default='non', type=str, help='pregnant female? (mid/late)')

args = parser.parse_args()
sex = args.sex
humOrrat = args.species
sup_or_multi = args.type
diabete = args.diabetes
inhib = args.inhibition
unx = args.unx
preg = args.pregnant

if diabete != 'Non':
    if preg != 'non':
        raise Exception('pregnant diabetic not done')
    # if inhib != None:
    #     file_to_save = inhib+'_'+sex+'_'+humOrrat[0:3]+'_'+diabete+'_diab'+'_'+unx+'_unx'
    # else:
    #     file_to_save = sex+'_'+humOrrat[0:3]+'_'+diabete+'_diab'+'_'+unx+'_unx'
elif preg != 'non':
    if sex == 'Male':
        raise Exception('pregnant only for female')
    if humOrrat[0:3] == 'hum':
        raise Exception('pregnant model not set up for human yet')
    if inhib != None:
        raise Exception('pregnant model does not have inhibition set up yet')

    #file_to_save = preg+'pregnant_'+humOrrat[0:3]
# else:
#     file_to_save = sex + '_' + humOrrat[0:3] +'_normal'

file_to_save = args.file2save
    
if os.path.isdir(file_to_save) == False:
    os.makedirs(file_to_save)
    
if sup_or_multi == 'superficial':
    parts = ['sup']
else:
    parts = ['sup','jux1','jux2','jux3','jux4','jux5']

def compute_segmentPTS3(sup_or_jux,sex,humOrrat,sup_or_multi,diabete,inhib,unx,preg,file_to_save):
    solute = ['Na','K','Cl','HCO3','H2CO3','CO2','HPO4','H2PO4','urea','NH3','NH4','H','HCO2','H2CO2','glu']
    compart = ['Lumen','Cell','ICA','ICB','LIS','Bath']
    cw=Vref*60e6
    #========================================================
    # Proximal convolute tubule
    #========================================================
    print('%s PCT start' %(sup_or_jux))
    if humOrrat == 'human':
        NPT = 181
    elif humOrrat == 'rat':
        NPT = 176
    if sex == 'Male':
        filename = './datafiles/PTparams_M_'+humOrrat[0:3]+'.dat'
    elif sex == 'Female':
        filename = './datafiles/PTparams_F_'+humOrrat[0:3]+'.dat'
    else:
        filename ='./datafiles/PTparams_F_'+humOrrat[0:3]+'.dat'

    pt=compute(NPT,filename,'Broyden',sup_or_jux,diabete,humOrrat,sup_or_multi=sup_or_multi,inhibition = inhib,unx = unx, preg = preg)
    #========================================================
    # output PT Concentrations in Lumen and Cell
    #========================================================
    for i in range(NS):
        file=open('./'+file_to_save+'/'+pt[0].sex+'_'+humOrrat[0:3]+'_pt_con_of_'+solute[i]+'_in_Lumen_'+sup_or_jux+'.txt','w')
        for j in range(NPT):
            file.write(str(pt[j].conc[i,0])+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+pt[0].sex+'_'+humOrrat[0:3]+'_pt_con_of_'+solute[i]+'_in_Cell_'+sup_or_jux+'.txt','w')
        for j in range(NPT):
            file.write(str(pt[j].conc[i,1])+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+pt[0].sex+'_'+humOrrat[0:3]+'_pt_con_of_'+solute[i]+'_in_Bath_'+sup_or_jux+'.txt','w')
        for j in range(NPT):
            file.write(str(pt[j].conc[i,5])+'\n')
        file.close()
    #========================================================
    # output PT Water volume in Lumen and Cell
    #========================================================
    file=open('./'+file_to_save+'/'+pt[0].sex+'_'+humOrrat[0:3]+'_pt_water_volume_in_Lumen_'+sup_or_jux+'.txt','w')
    for j in range(NPT):
        file.write(str(pt[j].vol[0]*cw)+'\n')
    file.close()
    file=open('./'+file_to_save+'/'+pt[0].sex+'_'+humOrrat[0:3]+'_pt_water_volume_in_Cell_'+sup_or_jux+'.txt','w')
    for j in range(NPT):
        file.write(str(pt[j].vol[1]*cw)+'\n')
    file.close()
    #========================================================
    # output PT solute flows in Lumen and Cell
    #========================================================
    for i in range(NS):
        file=open('./'+file_to_save+'/'+pt[0].sex+'_'+humOrrat[0:3]+'_pt_flow_of_'+solute[i]+'_in_Lumen_'+sup_or_jux+'.txt','w')
        for j in range(NPT):
            file.write(str(pt[j].conc[i,0]*pt[j].vol[0]*cw)+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+pt[0].sex+'_'+humOrrat[0:3]+'_pt_flow_of_'+solute[i]+'_in_Cell_'+sup_or_jux+'.txt','w')
        for j in range(NPT):
            file.write(str(pt[j].conc[i,1]*pt[j].vol[1]*cw)+'\n')
        file.close()
    #========================================================
    # output PCT osmolality in Lumen, Cell, LIS, Bath
    #========================================================
    file_lumen = open('./'+file_to_save+'/'+pt[0].sex+'_'+humOrrat[0:3]+'_'+pt[0].segment+'_osmolality_in_Lumen_'+sup_or_jux+'.txt','w')
    file_cell = open('./'+file_to_save+'/'+pt[0].sex+'_'+humOrrat[0:3]+'_'+pt[0].segment+'_osmolality_in_Cell_'+sup_or_jux+'.txt','w')
    file_lis = open('./'+file_to_save+'/'+pt[0].sex+'_'+humOrrat[0:3]+'_'+pt[0].segment+'_osmolality_in_LIS_'+sup_or_jux+'.txt','w')
    file_bath = open('./'+file_to_save+'/'+pt[0].sex+'_'+humOrrat[0:3]+'_'+pt[0].segment+'_osmolality_in_Bath_'+sup_or_jux+'.txt','w')
    for j in range(NPT):
        osm_l = 0
        osm_c = 0
        osm_lis = 0
        osm_b = 0
        for i in range(NS):
            osm_l = osm_l +pt[j].conc[i,0]
            osm_c = osm_c +pt[j].conc[i,1]
            osm_lis = osm_lis+pt[j].conc[i,4]
            osm_b = osm_b +pt[j].conc[i,5]

        file_lumen.write(str(osm_l)+'\n')
        file_cell.write(str(osm_c)+'\n')
        file_lis.write(str(osm_lis)+'\n')
        file_bath.write(str(osm_b)+'\n')
    file_lumen.close()
    file_cell.close()
    file_lis.close()
    file_bath.close()
    #========================================================
    # output luminal pressure
    #========================================================
    file=open('./'+file_to_save+'/'+pt[0].sex+'_'+humOrrat[0:3]+'_'+pt[0].segment+'_pressure_in_Lumen_'+sup_or_jux+'.txt','w')
    for j in range(NPT):
        file.write(str(pt[j].pres[0])+'\n')
    file.close()
    #========================================================
    # output fluxes through transporters
    #========================================================
    for j in range(NPT):
        pt[j].area[4][5] = 0.02*max(pt[j].vol[4]/pt[j].volref[4],1.0)
        pt[j].area[5][4] = pt[j].area[4][5]

        jvol,jsol = flux.compute_fluxes(pt[j],j)

        file_Na_apical = open('./'+file_to_save+'/'+pt[j].sex+'_'+humOrrat[0:3]+'_'+pt[j].segment+'_apical_Na_'+sup_or_jux+'.txt','a')
        file_Na_apical.write(str(jsol[0,0,1])+'\n')

        file_Na_para = open('./'+file_to_save+'/'+pt[j].sex+'_'+humOrrat[0:3]+'_'+pt[j].segment+'_paracellular_Na_'+sup_or_jux+'.txt','a')
        file_Na_para.write(str(jsol[0,0,4])+'\n')

        jvol = np.zeros([6,6])
        jsol = np.zeros([15,6,6])

        for i in range(len(pt[j].trans)):
            transporter_type = pt[j].trans[i].type
            memb_id = pt[j].trans[i].membrane_id

            if pt[j].segment=='PT' or pt[j].segment == 'S3':

                if pt[j].segment == 'PT':
                    TS = 1.3
                    scaleT = 1.0
                elif pt[j].segment == 'S3':
                    TS = 1.3
                    scaleT = 0.5

                #torque-modulated effects
                
                PM=pt[j].pres[0]

                Radref,torqR,torqvm,PbloodPT,torqL,torqd = set_torq_params(pt[j].humOrrat,pt[j].sex,pt[j].preg)

                if pt[j].humOrrat == 'rat':
                    fac1 = 8.0*visc*(pt[j].vol_init[0]*Vref)*torqL/(Radref**2)
                elif pt[j].humOrrat == 'hum':
                    fac1 = 8.0*visc*(pt[j].volref[0]*Vref)*torqL/(Radref**2)
                fac2 = 1.0 + (torqL+torqd)/Radref + 0.50*((torqL/Radref)**2)
                TM0= fac1*fac2
            
                RMtorq = torqR*(1.0e0+torqvm*(PM - PbloodPT))

                factor1 = 8.0*visc*(pt[j].vol[0]*Vref)*torqL/(RMtorq**2) 
                factor2 = 1.0 + (torqL+torqd)/RMtorq + 0.50*((torqL/RMtorq)**2)
                Torque = factor1*factor2
            
                Scaletorq = 1.0 + TS*scaleT*(Torque/TM0-1.0)

            if transporter_type == 'SGLT1':
                solute_id,fluxs = glucose.sglt1(pt[j],pt[j].ep,memb_id,pt[j].trans[i].act,pt[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+pt[j].sex+'_'+humOrrat[0:3]+'_'+pt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')
            elif transporter_type == 'SGLT2':
                solute_id,fluxs = glucose.sglt2(pt[j],pt[j].ep,memb_id,pt[j].trans[i].act,pt[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+pt[j].sex+'_'+humOrrat[0:3]+'_'+pt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')
            elif transporter_type == 'GLUT1':
                solute_id,fluxs=glucose.glut1(pt[j],pt[j].ep,memb_id,pt[j].trans[i].act,pt[j].area)
                for k in range(len([solute_id])):
                    file = open('./'+file_to_save+'/'+pt[j].sex+'_'+humOrrat[0:3]+'_'+pt[j].segment+'_'+transporter_type+'_'+solute[solute_id]+str(memb_id[0])+str(memb_id[1])+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs*Scaletorq)+'\n')
            elif transporter_type == 'GLUT2':
                solute_id,fluxs=glucose.glut2(pt[j],pt[j].ep,memb_id,pt[j].trans[i].act,pt[j].area)
                for k in range(len([solute_id])):
                    file = open('./'+file_to_save+'/'+pt[j].sex+'_'+humOrrat[0:3]+'_'+pt[j].segment+'_'+transporter_type+'_'+solute[solute_id]+str(memb_id[0])+str(memb_id[1])+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs*Scaletorq)+'\n')			
            elif transporter_type == 'NHE3':
                solute_id,fluxs=NHE3.nhe3(pt[j],pt[j].ep,memb_id,pt[j].trans[i].act,pt[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+pt[j].sex+'_'+humOrrat[0:3]+'_'+pt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')
            elif transporter_type == 'NaKATPase':
                solute_id,fluxs=ATPase.nakatpase(pt[j],pt[j].ep,memb_id,pt[j].trans[i].act,pt[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+pt[j].sex+'_'+humOrrat[0:3]+'_'+pt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+str(memb_id[0])+str(memb_id[1])+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')

            elif transporter_type == 'HATPase':
                solute_id,fluxs=ATPase.hatpase(pt[j],pt[j].ep,memb_id,pt[j].trans[i].act,pt[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+pt[j].sex+'_'+humOrrat[0:3]+'_'+pt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')
            elif transporter_type == 'NKCC2A':
                solute_id,fluxs=NKCC.nkcc2(pt[j],memb_id,pt[j].trans[i].act,pt[j].area,'A')
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+pt[j].sex+'_'+humOrrat[0:3]+'_'+pt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')
            elif transporter_type == 'NKCC2B':
                solute_id,fluxs=NKCC.nkcc2(pt[j],memb_id,pt[j].trans[i].act,pt[j].area,'B')
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+pt[j].sex+'_'+humOrrat[0:3]+'_'+pt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')
            elif transporter_type == 'NKCC2F':
                solute_id,fluxs=NKCC.nkcc2(pt[j],memb_id,pt[j].trans[i].act,pt[j].area,'F')
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+pt[j].sex+'_'+humOrrat[0:3]+'_'+pt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')       
            elif transporter_type == 'KCC4':
                solute_id,fluxs=KCC.kcc4(pt[j].conc,memb_id,pt[j].trans[i].act,pt[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+pt[j].sex+'_'+humOrrat[0:3]+'_'+pt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')
            elif transporter_type == 'ENaC':
                solute_id,fluxs=ENaC.ENaC(pt[j],j,memb_id,pt[j].trans[i].act,pt[j].area,jvol)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+pt[j].sex+'_'+humOrrat[0:3]+'_'+pt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')
            elif transporter_type == 'NCC':
                solute_id,fluxs=NCC.NCC(pt[j],j,memb_id,pt[j].trans[i].act,pt[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+pt[j].sex+'_'+humOrrat[0:3]+'_'+pt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')
            elif transporter_type == 'Pendrin':
                solute_id,fluxs=Pendrin.Pendrin(pt[j],memb_id,pt[j].trans[i].act,pt[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+pt[j].sex+'_'+humOrrat[0:3]+'_'+pt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')
            elif transporter_type =='AE1':
                solute_id,fluxs=AE1.AE1(pt[j],memb_id,pt[j].trans[i].act,pt[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+pt[j].sex+'_'+humOrrat[0:3]+'_'+pt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')
            elif transporter_type == 'HKATPase':
                solute_id,fluxs=ATPase.hkatpase(pt[j],memb_id,pt[j].trans[i].act,pt[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+pt[j].sex+'_'+humOrrat[0:3]+'_'+pt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')
            elif transporter_type == 'NHE1':
                solute_id,fluxs=NHE1.NHE1(pt[j],memb_id,pt[j].trans[i].act,pt[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+pt[j].sex+'_'+humOrrat[0:3]+'_'+pt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')
            elif transporter_type == 'NKCC1':
                solute_id,fluxs=NKCC.nkcc1(pt[j],memb_id,pt[j].trans[i].act,delmu)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+pt[j].sex+'_'+humOrrat[0:3]+'_'+pt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')
            else:
                raise Exception('What is this?',transporter_type)	
    print('%s PCT finished.' %(sup_or_jux))
    print('\n')
    #================================
    # print diameter along PT 
    #================================
    file = open('./'+file_to_save+'/'+pt[j].sex+'_'+pt[0].humOrrat+'_'+pt[j].segment+'_diameter.txt', 'a')
    file.write(str(pt[j].diam))
    file.close()
    #========================================================
    # S3
    #========================================================
    print('%s S3 start' %(sup_or_jux))
    if humOrrat == 'human':
        NS3 = 20
    elif humOrrat == 'rat':
        NS3 = 25
    if sex == 'Male':
        filename = './datafiles/S3params_M_'+humOrrat[0:3]+'.dat'
    elif sex == 'Female':
        filename = './datafiles/S3params_F_'+humOrrat[0:3]+'.dat'
    else:
        filename ='./datafiles/S3params_F_'+humOrrat[0:3]+'.dat'
    s3=compute(NS3,filename,'Newton',sup_or_jux,diabete,humOrrat,sup_or_multi=sup_or_multi,inhibition = inhib,unx = unx,preg = preg)
    #========================================================
    # output S3 Concentrations in Lumen and Cell
    #========================================================
    for i in range(NS):
        file=open('./'+file_to_save+'/'+s3[0].sex+'_'+humOrrat[0:3]+'_s3_con_of_'+solute[i]+'_in_Lumen_'+sup_or_jux+'.txt','w')
        for j in range(NS3):
            file.write(str(s3[j].conc[i,0])+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+s3[0].sex+'_'+humOrrat[0:3]+'_s3_con_of_'+solute[i]+'_in_Cell_'+sup_or_jux+'.txt','w')
        for j in range(NS3):
            file.write(str(s3[j].conc[i,1])+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+s3[0].sex+'_'+humOrrat[0:3]+'_s3_con_of_'+solute[i]+'_in_Bath_'+sup_or_jux+'.txt','w')
        for j in range(NS3):
            file.write(str(s3[j].conc[i,5])+'\n')
        file.close()
    #========================================================
    # output S3 Water volume in Lumen and Cell
    #========================================================
    file=open('./'+file_to_save+'/'+s3[0].sex+'_'+humOrrat[0:3]+'_s3_water_volume_in_Lumen_'+sup_or_jux+'.txt','w')
    for j in range(NS3):
        file.write(str(s3[j].vol[0]*cw)+'\n')
    file.close()
    file=open('./'+file_to_save+'/'+s3[0].sex+'_'+humOrrat[0:3]+'_s3_water_volume_in_Cell_'+sup_or_jux+'.txt','w')
    for j in range(NS3):
        file.write(str(s3[j].vol[1]*cw)+'\n')
    file.close()
    #================================
    # print diameter along PT 
    #================================
    file = open('./'+file_to_save+'/'+s3[j].sex+'_'+s3[0].humOrrat+'_'+s3[j].segment+'_diameter.txt', 'a')
    file.write(str(s3[j].diam))
    file.close()
    #========================================================
    # output S3 solute flows in Lumen and Cell
    #========================================================
    for i in range(NS):
        file=open('./'+file_to_save+'/'+s3[0].sex+'_'+humOrrat[0:3]+'_s3_flow_of_'+solute[i]+'_in_Lumen_'+sup_or_jux+'.txt','w')
        for j in range(NS3):
            file.write(str(s3[j].conc[i,0]*s3[j].vol[0]*cw)+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+s3[0].sex+'_'+humOrrat[0:3]+'_s3_flow_of_'+solute[i]+'_in_Cell_'+sup_or_jux+'.txt','w')
        for j in range(NS3):
            file.write(str(s3[j].conc[i,1]*s3[j].vol[1]*cw)+'\n')
        file.close()
    #========================================================
    # output S3 osmolality in Lumen, Cell, LIS, Bath
    #========================================================
    file_lumen = open('./'+file_to_save+'/'+s3[0].sex+'_'+humOrrat[0:3]+'_'+s3[0].segment+'_osmolality_in_Lumen_'+sup_or_jux+'.txt','w')
    file_cell = open('./'+file_to_save+'/'+s3[0].sex+'_'+humOrrat[0:3]+'_'+s3[0].segment+'_osmolality_in_Cell_'+sup_or_jux+'.txt','w')
    file_lis = open('./'+file_to_save+'/'+s3[0].sex+'_'+humOrrat[0:3]+'_'+s3[0].segment+'_osmolality_in_LIS_'+sup_or_jux+'.txt','w')
    file_bath = open('./'+file_to_save+'/'+s3[0].sex+'_'+humOrrat[0:3]+'_'+s3[0].segment+'_osmolality_in_Bath_'+sup_or_jux+'.txt','w')
    for j in range(NS3):
        osm_l = 0
        osm_c = 0
        osm_lis = 0
        osm_b = 0
        for i in range(NS):
            osm_l = osm_l +s3[j].conc[i,0]
            osm_c = osm_c +s3[j].conc[i,1]
            osm_lis = osm_lis+s3[j].conc[i,4]
            osm_b = osm_b +s3[j].conc[i,5]

        file_lumen.write(str(osm_l)+'\n')
        file_cell.write(str(osm_c)+'\n')
        file_lis.write(str(osm_lis)+'\n')
        file_bath.write(str(osm_b)+'\n')
    file_lumen.close()
    file_cell.close()
    file_lis.close()
    file_bath.close()
    #========================================================
    # output luminal pressure
    #========================================================
    file=open('./'+file_to_save+'/'+s3[0].sex+'_'+humOrrat[0:3]+'_'+s3[0].segment+'_pressure_in_Lumen_'+sup_or_jux+'.txt','w')
    for j in range(NS3):
        file.write(str(s3[j].pres[0])+'\n')
    file.close()
    #========================================================
    # output fluxes through transporters
    #========================================================
    for j in range(NS3):

        s3[j].area[4][5] = 0.02*max(s3[j].vol[4]/s3[j].volref[4],1.0)
        s3[j].area[5][4] = s3[j].area[4][5]

        jvol = np.zeros([6,6])
        jsol = np.zeros([15,6,6])

        jvol,jsol = flux.compute_fluxes(s3[j],j)

        file_Na_apical = open('./'+file_to_save+'/'+s3[j].sex+'_'+humOrrat[0:3]+'_'+s3[j].segment+'_apical_Na_'+sup_or_jux+'.txt','a')
        file_Na_apical.write(str(jsol[0,0,1])+'\n')

        file_Na_para = open('./'+file_to_save+'/'+s3[j].sex+'_'+humOrrat[0:3]+'_'+s3[j].segment+'_paracellular_Na_'+sup_or_jux+'.txt','a')
        file_Na_para.write(str(jsol[0,0,4])+'\n')

        for i in range(len(s3[j].trans)):
            transporter_type = s3[j].trans[i].type
            memb_id = s3[j].trans[i].membrane_id

            if s3[j].segment=='PT' or s3[j].segment == 'S3':

                if s3[j].segment == 'PT':
                    TS = 1.3
                    scaleT = 1.0
                elif s3[j].segment == 'S3':
                    TS = 1.3
                    scaleT = 0.5

                #torque-modulated effects
                
                PM=s3[j].pres[0]
                Radref,torqR,torqvm,PbloodPT,torqL,torqd = set_torq_params(s3[j].humOrrat,s3[j].sex,s3[j].preg)
                if s3[j].humOrrat == 'rat':
                    fac1 = 8.0*visc*(s3[j].vol_init[0]*Vref)*torqL/(Radref**2)
                elif s3[j].humOrrat == 'hum':
                    fac1 = 8.0*visc*(s3[j].volref[0]*Vref)*torqL/(Radref**2)
                fac2 = 1.0 + (torqL+torqd)/Radref + 0.50*((torqL/Radref)**2)
                TM0= fac1*fac2
            
                RMtorq = torqR*(1.0e0+torqvm*(PM - PbloodPT))

                factor1 = 8.0*visc*(s3[j].vol[0]*Vref)*torqL/(RMtorq**2) 
                factor2 = 1.0 + (torqL+torqd)/RMtorq + 0.50*((torqL/RMtorq)**2)
                Torque = factor1*factor2
            
                Scaletorq = 1.0 + TS*scaleT*(Torque/TM0-1.0)

            if transporter_type == 'SGLT1':
                solute_id,fluxs = glucose.sglt1(s3[j],s3[j].ep,memb_id,s3[j].trans[i].act,s3[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+s3[j].sex+'_'+humOrrat[0:3]+'_'+s3[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')
            elif transporter_type == 'SGLT2':
                solute_id,fluxs = glucose.sglt2(s3[j],s3[j].ep,memb_id,s3[j].trans[i].act,s3[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+s3[j].sex+'_'+humOrrat[0:3]+'_'+s3[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')
            elif transporter_type == 'GLUT1':
                solute_id,fluxs=glucose.glut1(s3[j],s3[j].ep,memb_id,s3[j].trans[i].act,s3[j].area)
                for k in range(len([solute_id])):
                    file = open('./'+file_to_save+'/'+s3[j].sex+'_'+humOrrat[0:3]+'_'+s3[j].segment+'_'+transporter_type+'_'+solute[solute_id]+str(memb_id[0])+str(memb_id[1])+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs*Scaletorq)+'\n')
            elif transporter_type == 'GLUT2':
                solute_id,fluxs=glucose.glut2(s3[j],s3[j].ep,memb_id,s3[j].trans[i].act,s3[j].area)
                for k in range(len([solute_id])):
                    file = open('./'+file_to_save+'/'+s3[j].sex+'_'+humOrrat[0:3]+'_'+s3[j].segment+'_'+transporter_type+'_'+solute[solute_id]+str(memb_id[0])+str(memb_id[1])+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs*Scaletorq)+'\n')			
            elif transporter_type == 'NHE3':
                solute_id,fluxs=NHE3.nhe3(s3[j],s3[j].ep,memb_id,s3[j].trans[i].act,s3[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+s3[j].sex+'_'+humOrrat[0:3]+'_'+s3[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')
            elif transporter_type == 'NaKATPase':
                solute_id,fluxs=ATPase.nakatpase(s3[j],s3[j].ep,memb_id,s3[j].trans[i].act,s3[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+s3[j].sex+'_'+humOrrat[0:3]+'_'+s3[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+str(memb_id[0])+str(memb_id[1])+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')

            elif transporter_type == 'HATPase':
                solute_id,fluxs=ATPase.hatpase(s3[j],s3[j].ep,memb_id,s3[j].trans[i].act,s3[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+s3[j].sex+'_'+humOrrat[0:3]+'_'+s3[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')
            elif transporter_type == 'NKCC2A':
                solute_id,fluxs=NKCC.nkcc2(s3[j],memb_id,s3[j].trans[i].act,s3[j].area,'A')
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+s3[j].sex+'_'+humOrrat[0:3]+'_'+s3[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')
            elif transporter_type == 'NKCC2B':
                solute_id,fluxs=NKCC.nkcc2(s3[j],memb_id,s3[j].trans[i].act,s3[j].area,'B')
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+s3[j].sex+'_'+humOrrat[0:3]+'_'+s3[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')
            elif transporter_type == 'NKCC2F':
                solute_id,fluxs=NKCC.nkcc2(s3[j],memb_id,s3[j].trans[i].act,s3[j].area,'F')
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+s3[j].sex+'_'+humOrrat[0:3]+'_'+s3[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')       
            elif transporter_type == 'KCC4':
                solute_id,fluxs=KCC.kcc4(s3[j].conc,memb_id,s3[j].trans[i].act,s3[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+s3[j].sex+'_'+humOrrat[0:3]+'_'+s3[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')
            elif transporter_type == 'ENaC':
                solute_id,fluxs=ENaC.ENaC(s3[j],j,memb_id,s3[j].trans[i].act,s3[j].area,jvol)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+s3[j].sex+'_'+humOrrat[0:3]+'_'+s3[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')
            elif transporter_type == 'NCC':
                solute_id,fluxs=NCC.NCC(s3[j],j,memb_id,s3[j].trans[i].act,s3[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+s3[j].sex+'_'+humOrrat[0:3]+'_'+s3[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')
            elif transporter_type == 'Pendrin':
                solute_id,fluxs=Pendrin.Pendrin(s3[j],memb_id,s3[j].trans[i].act,s3[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+s3[j].sex+'_'+humOrrat[0:3]+'_'+s3[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')
            elif transporter_type =='AE1':
                solute_id,fluxs=AE1.AE1(s3[j],memb_id,s3[j].trans[i].act,s3[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+s3[j].sex+'_'+humOrrat[0:3]+'_'+s3[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')
            elif transporter_type == 'HKATPase':
                solute_id,fluxs=ATPase.hkatpase(s3[j],memb_id,s3[j].trans[i].act,s3[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+s3[j].sex+'_'+humOrrat[0:3]+'_'+s3[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')
            elif transporter_type == 'NHE1':
                solute_id,fluxs=NHE1.NHE1(s3[j],memb_id,s3[j].trans[i].act,s3[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+s3[j].sex+'_'+humOrrat[0:3]+'_'+s3[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')
            elif transporter_type == 'NKCC1':
                solute_id,fluxs=NKCC.nkcc1(s3[j],memb_id,s3[j].trans[i].act,delmu)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+s3[j].sex+'_'+humOrrat[0:3]+'_'+s3[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k]*Scaletorq)+'\n')
            else:
                raise Exception('What is this?',transporter_type)	
    print('%s S3 finished.' %(sup_or_jux))
    print('\n')
#=============================
# end compute_segmentPTS3
#=============================

def multiprocessing_funcPTS3(sup_or_jux):
    compute_segmentPTS3(sup_or_jux, sex, humOrrat, sup_or_multi, diabete, inhib, unx, preg, file_to_save)

if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pool.map(multiprocessing_funcPTS3, parts)
    pool.close()
