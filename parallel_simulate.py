from compute_sup_jux_segment import compute_segment 
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

solute = ['Na','K','Cl','HCO3','H2CO3','CO2','HPO4','H2PO4','urea','NH3','NH4','H','HCO2','H2CO2','glu']
compart = ['Lumen','Cell','ICA','ICB','LIS','Bath']
cw=Vref*60e6

parser = argparse.ArgumentParser()
parser.add_argument('--sex',choices=['Male','Female'],required = True,type = str,help = 'Sex')
parser.add_argument('--species',choices=['human','rat'],required = True,type = str, help = 'Human model or Rat model')
parser.add_argument('--type',choices = ['superficial','multiple'],required = True,type=str,help='superficial nephron or multiple nephrons?')
parser.add_argument('--diabetes',choices = ['Severe','Moderate','Non'],required = True,type=str,help='diabete status (Severe/Moderate/Non)')
parser.add_argument('--inhibition',choices=['ACE','SGLT2','NHE3-50','NHE3-80','NKCC2-70','NKCC2-100','NCC-70','NCC-100','ENaC-70','ENaC-100','SNB-70','SNB-100'],default = None,type = str,help = 'any transporter inhibition')
parser.add_argument('--unx',choices=['N','Y'],default = 'N',type = str,help = 'uninephrectomy status')
args = parser.parse_args()
gender = args.sex
humOrrat = args.species
sup_or_multi = args.type
diabete = args.diabetes
inhib = args.inhibition
unx = args.unx

if inhib != None:
    file_to_save = inhib+'_'+gender+'_'+humOrrat[0:3]+'_'+diabete+'_diab'+'_'+unx+'_unx'
else:
    file_to_save = gender+'_'+humOrrat[0:3]+'_'+diabete+'_diab'+'_'+unx+'_unx'
if os.path.isdir(file_to_save) == False:
    os.makedirs(file_to_save)

def multiprocessing_func(seg):
    compute_segment(seg,gender,humOrrat,sup_or_multi,diabete,inhib,unx,file_to_save)

parts = ['sup','jux1','jux2','jux3','jux4','jux5']

if __name__ == '__main__':

    pool = multiprocessing.Pool()
    pool.map(multiprocessing_func,parts)
    pool.close()

    #========================================================
    # Cortical collecting duct
    #========================================================
    NCCD = 200
    if gender == 'Male':
        filename = './datafiles/CCDparams_M_'+humOrrat[0:3]+'.dat'
    elif gender == 'Female':
        filename = './datafiles/CCDparams_F_'+humOrrat[0:3]+'.dat'
    else:
        filename ='./datafiles/CCDparams_F_'+humOrrat[0:3]+'.dat'
    ccd=compute(NCCD,filename,'Newton',diabete=diabete,humOrrat=humOrrat,sup_or_multi=sup_or_multi,inhibition = inhib,unx = unx)
    #========================================================
    # output CCD Concentrations in Lumen and Cell
    #========================================================
    for i in range(NS):
        file=open('./'+file_to_save+'/'+ccd[0].sex+'_'+humOrrat[0:3]+'_ccd_con_of_'+solute[i]+'_in_Lumen.txt','w')
        for j in range(NCCD):
            file.write(str(ccd[j].conc[i,0])+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+ccd[0].sex+'_'+humOrrat[0:3]+'_ccd_con_of_'+solute[i]+'_in_Cell.txt','w')
        for j in range(NCCD):
            file.write(str(ccd[j].conc[i,1])+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+ccd[0].sex+'_'+humOrrat[0:3]+'_ccd_con_of_'+solute[i]+'_in_Bath.txt','w')
        for j in range(NCCD):
            file.write(str(ccd[j].conc[i,5])+'\n')
        file.close()
    #========================================================
    # output CCD Water volume in Lumen and Cell
    #========================================================
    file=open('./'+file_to_save+'/'+ccd[0].sex+'_'+humOrrat[0:3]+'_ccd_water_volume_in_Lumen.txt','w')
    for j in range(NCCD):
        file.write(str(ccd[j].vol[0]*cw)+'\n')
    file.close()
    file=open('./'+file_to_save+'/'+ccd[0].sex+'_'+humOrrat[0:3]+'_ccd_water_volume_in_Cell.txt','w')
    for j in range(NCCD):
        file.write(str(ccd[j].vol[1]*cw)+'\n')
    file.close()
    #========================================================
    # output CCD solute flows in Lumen and Cell
    #========================================================
    for i in range(NS):
        file=open('./'+file_to_save+'/'+ccd[0].sex+'_'+humOrrat[0:3]+'_ccd_flow_of_'+solute[i]+'_in_Lumen.txt','w')
        for j in range(NCCD):
            file.write(str(ccd[j].conc[i,0]*ccd[j].vol[0]*cw)+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+ccd[0].sex+'_'+humOrrat[0:3]+'_ccd_flow_of_'+solute[i]+'_in_Cell.txt','w')
        for j in range(NCCD):
            file.write(str(ccd[j].conc[i,1]*ccd[j].vol[1]*cw)+'\n')
        file.close()
    #========================================================
    # output CCD osmolality in Lumen, Cell, LIS, Bath
    #========================================================
    file_lumen = open('./'+file_to_save+'/'+ccd[0].sex+'_'+humOrrat[0:3]+'_'+ccd[0].segment+'_osmolality_in_Lumen.txt','w')
    file_cell = open('./'+file_to_save+'/'+ccd[0].sex+'_'+humOrrat[0:3]+'_'+ccd[0].segment+'_osmolality_in_Cell.txt','w')
    file_lis = open('./'+file_to_save+'/'+ccd[0].sex+'_'+humOrrat[0:3]+'_'+ccd[0].segment+'_osmolality_in_LIS.txt','w')
    file_bath = open('./'+file_to_save+'/'+ccd[0].sex+'_'+humOrrat[0:3]+'_'+ccd[0].segment+'_osmolality_in_Bath.txt','w')
    for j in range(NCCD):
        osm_l = 0
        osm_c = 0
        osm_lis = 0
        osm_b = 0
        for i in range(NS):
            osm_l = osm_l +ccd[j].conc[i,0]
            osm_c = osm_c +ccd[j].conc[i,1]
            osm_lis = osm_lis+ccd[j].conc[i,4]
            osm_b = osm_b +ccd[j].conc[i,5]

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
    file=open('./'+file_to_save+'/'+ccd[0].sex+'_'+humOrrat[0:3]+'_'+ccd[0].segment+'_pressure_in_Lumen.txt','w')
    for j in range(NCCD):
        file.write(str(ccd[j].pres[0])+'\n')
    file.close()
    #========================================================
    # output flux through transporters
    #========================================================
    for j in range(NCCD):

        ccd[j].area[4][5] = 0.02*max(ccd[j].vol[4]/ccd[j].volref[4],1.0)
        ccd[j].area[5][4] = ccd[j].area[4][5]
            
        jvol = np.zeros([6,6])
        jsol = np.zeros([15,6,6])
            
        jvol,jsol = flux.compute_fluxes(ccd[j],j)

        file_Na_apical = open('./'+file_to_save+'/'+ccd[j].sex+'_'+humOrrat[0:3]+'_'+ccd[j].segment+'_apical_Na.txt','a')
        file_Na_apical.write(str(jsol[0,0,1])+'\n')

        file_Na_para = open('./'+file_to_save+'/'+ccd[j].sex+'_'+humOrrat[0:3]+'_'+ccd[j].segment+'_paracellular_Na.txt','a')        
        file_Na_para.write(str(jsol[0,0,4])+'\n')
            
        jvol = np.zeros([6,6])
        jsol = np.zeros([15,6,6])


        jvol = water.compute_water_fluxes(ccd[j])
        jsol,delmu = electrochemical.compute_ecd_fluxes(ccd[j],jvol)
        for i in range(len(ccd[j].trans)):
            transporter_type = ccd[j].trans[i].type
            memb_id = ccd[j].trans[i].membrane_id

            if transporter_type == 'SGLT1':
                solute_id,fluxs = glucose.sglt1(ccd[j],ccd[j].ep,memb_id,ccd[j].trans[i].act,ccd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ccd[j].sex+'_'+humOrrat[0:3]+'_'+ccd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'SGLT2':
                solute_id,fluxs = glucose.sglt2(ccd[j],ccd[j].ep,memb_id,ccd[j].trans[i].act,ccd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ccd[j].sex+'_'+humOrrat[0:3]+'_'+ccd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'GLUT1':
                solute_id,fluxs=glucose.glut1(ccd[j],ccd[j].ep,memb_id,ccd[j].trans[i].act,ccd[j].area)
                for k in range(len([solute_id])):
                    file = open('./'+file_to_save+'/'+ccd[j].sex+'_'+humOrrat[0:3]+'_'+ccd[j].segment+'_'+transporter_type+'_'+solute[solute_id]+str(memb_id[0])+str(memb_id[1])+'.txt','a')
                    file.write(str(fluxs)+'\n')
            elif transporter_type == 'GLUT2':
                solute_id,fluxs=glucose.glut2(ccd[j],ccd[j].ep,memb_id,ccd[j].trans[i].act,ccd[j].area)
                for k in range(len([solute_id])):
                    file = open('./'+file_to_save+'/'+ccd[j].sex+'_'+humOrrat[0:3]+'_'+ccd[j].segment+'_'+transporter_type+'_'+solute[solute_id]+str(memb_id[0])+str(memb_id[1])+'.txt','a')
                    file.write(str(fluxs)+'\n')			
            elif transporter_type == 'NHE3':
                solute_id,fluxs=NHE3.nhe3(ccd[j],ccd[j].ep,memb_id,ccd[j].trans[i].act,ccd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ccd[j].sex+'_'+humOrrat[0:3]+'_'+ccd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NaKATPase':
                solute_id,fluxs=ATPase.nakatpase(ccd[j],ccd[j].ep,memb_id,ccd[j].trans[i].act,ccd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ccd[j].sex+'_'+humOrrat[0:3]+'_'+ccd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+str(memb_id[0])+str(memb_id[1])+'.txt','a')
                    file.write(str(fluxs[k])+'\n')

            elif transporter_type == 'HATPase':
                solute_id,fluxs=ATPase.hatpase(ccd[j],ccd[j].ep,memb_id,ccd[j].trans[i].act,ccd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ccd[j].sex+'_'+humOrrat[0:3]+'_'+ccd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NKCC2A':
                solute_id,fluxs=NKCC.nkcc2(ccd[j],memb_id,ccd[j].trans[i].act,ccd[j].area,'A')
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ccd[j].sex+'_'+humOrrat[0:3]+'_'+ccd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NKCC2B':
                solute_id,fluxs=NKCC.nkcc2(ccd[j],memb_id,ccd[j].trans[i].act,ccd[j].area,'B')
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ccd[j].sex+'_'+humOrrat[0:3]+'_'+ccd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NKCC2F':
                solute_id,fluxs=NKCC.nkcc2(ccd[j],memb_id,ccd[j].trans[i].act,ccd[j].area,'F')
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ccd[j].sex+'_'+humOrrat[0:3]+'_'+ccd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')       
            elif transporter_type == 'KCC4':
                solute_id,fluxs=KCC.kcc4(ccd[j].conc,memb_id,ccd[j].trans[i].act,ccd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ccd[j].sex+'_'+humOrrat[0:3]+'_'+ccd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'ENaC':
                solute_id,fluxs=ENaC.ENaC(ccd[j],j,memb_id,ccd[j].trans[i].act,ccd[j].area,jvol)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ccd[j].sex+'_'+humOrrat[0:3]+'_'+ccd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NCC':
                solute_id,fluxs=NCC.NCC(ccd[j],j,memb_id,ccd[j].trans[i].act,ccd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ccd[j].sex+'_'+humOrrat[0:3]+'_'+ccd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'Pendrin':
                solute_id,fluxs=Pendrin.Pendrin(ccd[j],memb_id,ccd[j].trans[i].act,ccd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ccd[j].sex+'_'+humOrrat[0:3]+'_'+ccd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type =='AE1':
                solute_id,fluxs=AE1.AE1(ccd[j],memb_id,ccd[j].trans[i].act,ccd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ccd[j].sex+'_'+humOrrat[0:3]+'_'+ccd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'HKATPase':
                solute_id,fluxs=ATPase.hkatpase(ccd[j],memb_id,ccd[j].trans[i].act,ccd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ccd[j].sex+'_'+humOrrat[0:3]+'_'+ccd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NHE1':
                solute_id,fluxs=NHE1.NHE1(ccd[j],memb_id,ccd[j].trans[i].act,ccd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ccd[j].sex+'_'+humOrrat[0:3]+'_'+ccd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NKCC1':
                solute_id,fluxs=NKCC.nkcc1(ccd[j],memb_id,ccd[j].trans[i].act,delmu)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ccd[j].sex+'_'+humOrrat[0:3]+'_'+ccd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            else:
                print('What is this?',transporter_type)
    print('CCD finished.')
    #========================================================
    # Outer medullary collecting duct
    #========================================================
    NOMCD = 200
    if gender == 'Male':
        filename = './datafiles/OMCDparams_M_'+humOrrat[0:3]+'.dat'
    elif gender == 'Female':
        filename = './datafiles/OMCDparams_F_'+humOrrat[0:3]+'.dat'
    else:
        filename ='./datafiles/OMCDparams_F_'+humOrrat[0:3]+'.dat'
    if ccd[0].sex == 'male':
        omcd=compute(NOMCD,filename,'Newton',diabete=diabete,humOrrat=humOrrat,sup_or_multi=sup_or_multi,inhibition = inhib,unx = unx)
    elif ccd[0].sex == 'female':
        omcd=compute(NOMCD,filename,'Newton',diabete=diabete,humOrrat=humOrrat,sup_or_multi=sup_or_multi,inhibition = inhib,unx = unx)
    #========================================================
    # output OMCD Concentrations in Lumen and Cell
    #========================================================
    for i in range(NS):
        file=open('./'+file_to_save+'/'+omcd[0].sex+'_'+humOrrat[0:3]+'_omcd_con_of_'+solute[i]+'_in_Lumen.txt','w')
        for j in range(NOMCD):
            file.write(str(omcd[j].conc[i,0])+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+omcd[0].sex+'_'+humOrrat[0:3]+'_omcd_con_of_'+solute[i]+'_in_Cell.txt','w')
        for j in range(NOMCD):
            file.write(str(omcd[j].conc[i,1])+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+omcd[0].sex+'_'+humOrrat[0:3]+'_omcd_con_of_'+solute[i]+'_in_Bath.txt','w')
        for j in range(NOMCD):
            file.write(str(omcd[j].conc[i,5])+'\n')
        file.close()
    #========================================================
    # output OMCD Water volume in Lumen and Cell
    #========================================================
    file=open('./'+file_to_save+'/'+omcd[0].sex+'_'+humOrrat[0:3]+'_omcd_water_volume_in_Lumen.txt','w')
    for j in range(NOMCD):
        file.write(str(omcd[j].vol[0]*cw)+'\n')
    file.close()
    file=open('./'+file_to_save+'/'+omcd[0].sex+'_'+humOrrat[0:3]+'_omcd_water_volume_in_Cell.txt','w')
    for j in range(NOMCD):
        file.write(str(omcd[j].vol[1]*cw)+'\n')
    file.close()
    #========================================================
    # output OMCD solute flows in Lumen and Cell
    #========================================================
    for i in range(NS):
        file=open('./'+file_to_save+'/'+omcd[0].sex+'_'+humOrrat[0:3]+'_omcd_flow_of_'+solute[i]+'_in_Lumen.txt','w')
        for j in range(NOMCD):
            file.write(str(omcd[j].conc[i,0]*omcd[j].vol[0]*cw)+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+omcd[0].sex+'_'+humOrrat[0:3]+'_omcd_flow_of_'+solute[i]+'_in_Cell.txt','w')
        for j in range(NOMCD):
            file.write(str(omcd[j].conc[i,1]*omcd[j].vol[1]*cw)+'\n')
        file.close()
    #========================================================
    # output OMCD osmolality in Lumen, Cell, LIS, Bath
    #========================================================
    file_lumen = open('./'+file_to_save+'/'+omcd[0].sex+'_'+humOrrat[0:3]+'_'+omcd[0].segment+'_osmolality_in_Lumen.txt','w')
    file_cell = open('./'+file_to_save+'/'+omcd[0].sex+'_'+humOrrat[0:3]+'_'+omcd[0].segment+'_osmolality_in_Cell.txt','w')
    file_lis = open('./'+file_to_save+'/'+omcd[0].sex+'_'+humOrrat[0:3]+'_'+omcd[0].segment+'_osmolality_in_LIS.txt','w')
    file_bath = open('./'+file_to_save+'/'+omcd[0].sex+'_'+humOrrat[0:3]+'_'+omcd[0].segment+'_osmolality_in_Bath.txt','w')
    for j in range(NOMCD):
        osm_l = 0
        osm_c = 0
        osm_lis = 0
        osm_b = 0
        for i in range(NS):
            osm_l = osm_l +omcd[j].conc[i,0]
            osm_c = osm_c +omcd[j].conc[i,1]
            osm_lis = osm_lis+omcd[j].conc[i,4]
            osm_b = osm_b +omcd[j].conc[i,5]

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
    file=open('./'+file_to_save+'/'+omcd[0].sex+'_'+humOrrat[0:3]+'_'+omcd[0].segment+'_pressure_in_Lumen.txt','w')
    for j in range(NOMCD):
        file.write(str(omcd[j].pres[0])+'\n')
    file.close()
    #========================================================
    # output flux through transporters
    #========================================================
    for j in range(NOMCD):

        omcd[j].area[4][5] = 0.02*max(omcd[j].vol[4]/omcd[j].volref[4],1.0)
        omcd[j].area[5][4] = omcd[j].area[4][5]
            
        jvol = np.zeros([6,6])
        jsol = np.zeros([15,6,6])
            
        jvol,jsol = flux.compute_fluxes(omcd[j],j)

        file_Na_apical = open('./'+file_to_save+'/'+omcd[j].sex+'_'+humOrrat[0:3]+'_'+omcd[j].segment+'_apical_Na.txt','a')
        file_Na_apical.write(str(jsol[0,0,1])+'\n')

        file_Na_para = open('./'+file_to_save+'/'+omcd[j].sex+'_'+humOrrat[0:3]+'_'+omcd[j].segment+'_paracellular_Na.txt','a')
        file_Na_para.write(str(jsol[0,0,4])+'\n')
            
        jvol = np.zeros([6,6])
        jsol = np.zeros([15,6,6])


        jvol = water.compute_water_fluxes(omcd[j])
        jsol,delmu = electrochemical.compute_ecd_fluxes(omcd[j],jvol)
        for i in range(len(omcd[j].trans)):
            transporter_type = omcd[j].trans[i].type
            memb_id = omcd[j].trans[i].membrane_id

            if transporter_type == 'SGLT1':
                solute_id,fluxs = glucose.sglt1(omcd[j],omcd[j].ep,memb_id,omcd[j].trans[i].act,omcd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+omcd[j].sex+'_'+humOrrat[0:3]+'_'+omcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'SGLT2':
                solute_id,fluxs = glucose.sglt2(omcd[j],omcd[j].ep,memb_id,omcd[j].trans[i].act,omcd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+omcd[j].sex+'_'+humOrrat[0:3]+'_'+omcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'GLUT1':
                solute_id,fluxs=glucose.glut1(omcd[j],omcd[j].ep,memb_id,omcd[j].trans[i].act,omcd[j].area)
                for k in range(len([solute_id])):
                    file = open('./'+file_to_save+'/'+omcd[j].sex+'_'+humOrrat[0:3]+'_'+omcd[j].segment+'_'+transporter_type+'_'+solute[solute_id]+str(memb_id[0])+str(memb_id[1])+'.txt','a')
                    file.write(str(fluxs)+'\n')
            elif transporter_type == 'GLUT2':
                solute_id,fluxs=glucose.glut2(omcd[j],omcd[j].ep,memb_id,omcd[j].trans[i].act,omcd[j].area)
                for k in range(len([solute_id])):
                    file = open('./'+file_to_save+'/'+omcd[j].sex+'_'+humOrrat[0:3]+'_'+omcd[j].segment+'_'+transporter_type+'_'+solute[solute_id]+str(memb_id[0])+str(memb_id[1])+'.txt','a')
                    file.write(str(fluxs)+'\n')			
            elif transporter_type == 'NHE3':
                solute_id,fluxs=NHE3.nhe3(omcd[j],omcd[j].ep,memb_id,omcd[j].trans[i].act,omcd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+omcd[j].sex+'_'+humOrrat[0:3]+'_'+omcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NaKATPase':
                solute_id,fluxs=ATPase.nakatpase(omcd[j],omcd[j].ep,memb_id,omcd[j].trans[i].act,omcd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+omcd[j].sex+'_'+humOrrat[0:3]+'_'+omcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+str(memb_id[0])+str(memb_id[1])+'.txt','a')
                    file.write(str(fluxs[k])+'\n')

            elif transporter_type == 'HATPase':
                solute_id,fluxs=ATPase.hatpase(omcd[j],omcd[j].ep,memb_id,omcd[j].trans[i].act,omcd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+omcd[j].sex+'_'+humOrrat[0:3]+'_'+omcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NKCC2A':
                solute_id,fluxs=NKCC.nkcc2(omcd[j],memb_id,omcd[j].trans[i].act,omcd[j].area,'A')
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+omcd[j].sex+'_'+humOrrat[0:3]+'_'+omcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NKCC2B':
                solute_id,fluxs=NKCC.nkcc2(omcd[j],memb_id,omcd[j].trans[i].act,omcd[j].area,'B')
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+omcd[j].sex+'_'+humOrrat[0:3]+'_'+omcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NKCC2F':
                solute_id,fluxs=NKCC.nkcc2(omcd[j],memb_id,omcd[j].trans[i].act,omcd[j].area,'F')
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+omcd[j].sex+'_'+humOrrat[0:3]+'_'+omcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')       
            elif transporter_type == 'KCC4':
                solute_id,fluxs=KCC.kcc4(omcd[j].conc,memb_id,omcd[j].trans[i].act,omcd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+omcd[j].sex+'_'+humOrrat[0:3]+'_'+omcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'ENaC':
                solute_id,fluxs=ENaC.ENaC(omcd[j],j,memb_id,omcd[j].trans[i].act,omcd[j].area,jvol)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+omcd[j].sex+'_'+humOrrat[0:3]+'_'+omcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NCC':
                solute_id,fluxs=NCC.NCC(omcd[j],j,memb_id,omcd[j].trans[i].act,omcd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+omcd[j].sex+'_'+humOrrat[0:3]+'_'+omcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'Pendrin':
                solute_id,fluxs=Pendrin.Pendrin(omcd[j],memb_id,omcd[j].trans[i].act,omcd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+omcd[j].sex+'_'+humOrrat[0:3]+'_'+omcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type =='AE1':
                solute_id,fluxs=AE1.AE1(omcd[j],memb_id,omcd[j].trans[i].act,omcd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+omcd[j].sex+'_'+humOrrat[0:3]+'_'+omcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'HKATPase':
                solute_id,fluxs=ATPase.hkatpase(omcd[j],memb_id,omcd[j].trans[i].act,omcd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+omcd[j].sex+'_'+humOrrat[0:3]+'_'+omcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NHE1':
                solute_id,fluxs=NHE1.NHE1(omcd[j],memb_id,omcd[j].trans[i].act,omcd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+omcd[j].sex+'_'+humOrrat[0:3]+'_'+omcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NKCC1':
                solute_id,fluxs=NKCC.nkcc1(omcd[j],memb_id,omcd[j].trans[i].act,delmu)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+omcd[j].sex+'_'+humOrrat[0:3]+'_'+omcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            else:
                print('What is this?',transporter_type)
    print('OMCD finished.')
    #========================================================
    # Inner medullary collecting duct
    #========================================================
    NIMCD = 200
    if gender == 'Male':
        filename = './datafiles/IMCDparams_M_'+humOrrat[0:3]+'.dat'
    elif gender == 'Female':
        filename = './datafiles/IMCDparams_F_'+humOrrat[0:3]+'.dat'
    else:
        filename ='./datafiles/IMCDparams_F_'+humOrrat[0:3]+'.dat'
    imcd=compute(NIMCD,filename,'Newton',diabete=diabete,humOrrat=humOrrat,sup_or_multi=sup_or_multi,inhibition = inhib,unx = unx)
    #========================================================
    # output IMCD Concentrations in Lumen and Cell
    #========================================================
    for i in range(NS):
        file=open('./'+file_to_save+'/'+imcd[0].sex+'_'+humOrrat[0:3]+'_imcd_con_of_'+solute[i]+'_in_Lumen.txt','w')
        for j in range(NIMCD): 
            file.write(str(imcd[j].conc[i,0])+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+imcd[0].sex+'_'+humOrrat[0:3]+'_imcd_con_of_'+solute[i]+'_in_Cell.txt','w')
        for j in range(NIMCD):
            file.write(str(imcd[j].conc[i,1])+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+imcd[0].sex+'_'+humOrrat[0:3]+'_imcd_con_of_'+solute[i]+'_in_Bath.txt','w')
        for j in range(NIMCD):
            file.write(str(imcd[j].conc[i,5])+'\n')
        file.close()
    #========================================================
    # output IMCD Water volume in Lumen and Cell
    #========================================================
    file=open('./'+file_to_save+'/'+imcd[0].sex+'_'+humOrrat[0:3]+'_imcd_water_volume_in_Lumen.txt','w')
    for j in range(NIMCD):
        file.write(str(imcd[j].vol[0]*cw)+'\n')
    file.close()
    file=open('./'+file_to_save+'/'+imcd[0].sex+'_'+humOrrat[0:3]+'_imcd_water_volume_in_Cell.txt','w')
    for j in range(NIMCD):
        file.write(str(imcd[j].vol[1]*cw)+'\n')
    file.close()
    #========================================================
    # output IMCD solute flows in Lumen and Cell
    #========================================================
    for i in range(NS):
        file=open('./'+file_to_save+'/'+imcd[0].sex+'_'+humOrrat[0:3]+'_imcd_flow_of_'+solute[i]+'_in_Lumen.txt','w')
        for j in range(NIMCD):
            file.write(str(imcd[j].conc[i,0]*imcd[j].vol[0]*cw)+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+imcd[0].sex+'_'+humOrrat[0:3]+'_imcd_flow_of_'+solute[i]+'_in_Cell.txt','w')
        for j in range(NIMCD):
            file.write(str(imcd[j].conc[i,1]*imcd[j].vol[1]*cw)+'\n')
        file.close()
    #========================================================
    # output IMCD osmolality in Lumen, Cell, LIS, Bath
    #========================================================
    file_lumen = open('./'+file_to_save+'/'+imcd[0].sex+'_'+humOrrat[0:3]+'_'+imcd[0].segment+'_osmolality_in_Lumen.txt','w')
    file_cell = open('./'+file_to_save+'/'+imcd[0].sex+'_'+humOrrat[0:3]+'_'+imcd[0].segment+'_osmolality_in_Cell.txt','w')
    file_lis = open('./'+file_to_save+'/'+imcd[0].sex+'_'+humOrrat[0:3]+'_'+imcd[0].segment+'_osmolality_in_LIS.txt','w')
    file_bath = open('./'+file_to_save+'/'+imcd[0].sex+'_'+humOrrat[0:3]+'_'+imcd[0].segment+'_osmolality_in_Bath.txt','w')
    for j in range(NIMCD):
        osm_l = 0
        osm_c = 0
        osm_lis = 0
        osm_b = 0
        for i in range(NS):
            osm_l = osm_l +imcd[j].conc[i,0]
            osm_c = osm_c +imcd[j].conc[i,1]
            osm_lis = osm_lis+imcd[j].conc[i,4]
            osm_b = osm_b +imcd[j].conc[i,5]

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
    file=open('./'+file_to_save+'/'+imcd[0].sex+'_'+humOrrat[0:3]+'_'+imcd[0].segment+'_pressure_in_Lumen.txt','w')
    for j in range(NIMCD):
        file.write(str(imcd[j].pres[0])+'\n')
    file.close()
    #========================================================
    # output flux through transporters
    #========================================================
    for j in range(NIMCD):

        imcd[j].area[4][5] = 0.02*max(imcd[j].vol[4]/imcd[j].volref[4],1.0)
        imcd[j].area[5][4] = imcd[j].area[4][5]
            
        jvol = np.zeros([6,6])
        jsol = np.zeros([15,6,6])
            
        jvol,jsol = flux.compute_fluxes(imcd[j],j)

        file_Na_apical = open('./'+file_to_save+'/'+imcd[j].sex+'_'+humOrrat[0:3]+'_'+imcd[j].segment+'_apical_Na.txt','a')
        file_Na_apical.write(str(jsol[0,0,1])+'\n')

        file_Na_para = open('./'+file_to_save+'/'+imcd[j].sex+'_'+humOrrat[0:3]+'_'+imcd[j].segment+'_paracellular_Na.txt','a')
        file_Na_para.write(str(jsol[0,0,4])+'\n')
            
        jvol = np.zeros([6,6])
        jsol = np.zeros([15,6,6])


        jvol = water.compute_water_fluxes(imcd[j])
        jsol,delmu = electrochemical.compute_ecd_fluxes(imcd[j],jvol)
        for i in range(len(imcd[j].trans)):
            transporter_type = imcd[j].trans[i].type
            memb_id = imcd[j].trans[i].membrane_id

            if transporter_type == 'SGLT1':
                solute_id,fluxs = glucose.sglt1(imcd[j],imcd[j].ep,memb_id,imcd[j].trans[i].act,imcd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+imcd[j].sex+'_'+humOrrat[0:3]+'_'+imcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'SGLT2':
                solute_id,fluxs = glucose.sglt2(imcd[j],imcd[j].ep,memb_id,imcd[j].trans[i].act,imcd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+imcd[j].sex+'_'+humOrrat[0:3]+'_'+imcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'GLUT1':
                solute_id,fluxs=glucose.glut1(imcd[j],imcd[j].ep,memb_id,imcd[j].trans[i].act,imcd[j].area)
                for k in range(len([solute_id])):
                    file = open('./'+file_to_save+'/'+imcd[j].sex+'_'+humOrrat[0:3]+'_'+imcd[j].segment+'_'+transporter_type+'_'+solute[solute_id]+str(memb_id[0])+str(memb_id[1])+'.txt','a')
                    file.write(str(fluxs)+'\n')
            elif transporter_type == 'GLUT2':
                solute_id,fluxs=glucose.glut2(imcd[j],imcd[j].ep,memb_id,imcd[j].trans[i].act,imcd[j].area)
                for k in range(len([solute_id])):
                    file = open('./'+file_to_save+'/'+imcd[j].sex+'_'+humOrrat[0:3]+'_'+imcd[j].segment+'_'+transporter_type+'_'+solute[solute_id]+str(memb_id[0])+str(memb_id[1])+'.txt','a')
                    file.write(str(fluxs)+'\n')			
            elif transporter_type == 'NHE3':
                solute_id,fluxs=NHE3.nhe3(imcd[j],imcd[j].ep,memb_id,imcd[j].trans[i].act,imcd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+imcd[j].sex+'_'+humOrrat[0:3]+'_'+imcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NaKATPase':
                solute_id,fluxs=ATPase.nakatpase(imcd[j],imcd[j].ep,memb_id,imcd[j].trans[i].act,imcd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+imcd[j].sex+'_'+humOrrat[0:3]+'_'+imcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+str(memb_id[0])+str(memb_id[1])+'.txt','a')
                    file.write(str(fluxs[k])+'\n')

            elif transporter_type == 'HATPase':
                solute_id,fluxs=ATPase.hatpase(imcd[j],imcd[j].ep,memb_id,imcd[j].trans[i].act,imcd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+imcd[j].sex+'_'+humOrrat[0:3]+'_'+imcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NKCC2A':
                solute_id,fluxs=NKCC.nkcc2(imcd[j],memb_id,imcd[j].trans[i].act,imcd[j].area,'A')
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+imcd[j].sex+'_'+humOrrat[0:3]+'_'+imcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NKCC2B':
                solute_id,fluxs=NKCC.nkcc2(imcd[j],memb_id,imcd[j].trans[i].act,imcd[j].area,'B')
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+imcd[j].sex+'_'+humOrrat[0:3]+'_'+imcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NKCC2F':
                solute_id,fluxs=NKCC.nkcc2(imcd[j],memb_id,imcd[j].trans[i].act,imcd[j].area,'F')
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+imcd[j].sex+'_'+humOrrat[0:3]+'_'+imcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')       
            elif transporter_type == 'KCC4':
                solute_id,fluxs=KCC.kcc4(imcd[j].conc,memb_id,imcd[j].trans[i].act,imcd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+imcd[j].sex+'_'+humOrrat[0:3]+'_'+imcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'ENaC':
                solute_id,fluxs=ENaC.ENaC(imcd[j],j,memb_id,imcd[j].trans[i].act,imcd[j].area,jvol)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+imcd[j].sex+'_'+humOrrat[0:3]+'_'+imcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NCC':
                solute_id,fluxs=NCC.NCC(imcd[j],j,memb_id,imcd[j].trans[i].act,imcd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+imcd[j].sex+'_'+humOrrat[0:3]+'_'+imcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'Pendrin':
                solute_id,fluxs=Pendrin.Pendrin(imcd[j],memb_id,imcd[j].trans[i].act,imcd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+imcd[j].sex+'_'+humOrrat[0:3]+'_'+imcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type =='AE1':
                solute_id,fluxs=AE1.AE1(imcd[j],memb_id,imcd[j].trans[i].act,imcd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+imcd[j].sex+'_'+humOrrat[0:3]+'_'+imcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'HKATPase':
                solute_id,fluxs=ATPase.hkatpase(imcd[j],memb_id,imcd[j].trans[i].act,imcd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+imcd[j].sex+'_'+humOrrat[0:3]+'_'+imcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NHE1':
                solute_id,fluxs=NHE1.NHE1(imcd[j],memb_id,imcd[j].trans[i].act,imcd[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+imcd[j].sex+'_'+humOrrat[0:3]+'_'+imcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NKCC1':
                solute_id,fluxs=NKCC.nkcc1(imcd[j],memb_id,imcd[j].trans[i].act,delmu)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+imcd[j].sex+'_'+humOrrat[0:3]+'_'+imcd[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            else:
                print('What is this?',transporter_type)
    print('IMCD finished.')