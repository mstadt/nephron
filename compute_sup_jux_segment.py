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

def compute_segment(sup_or_jux,sex,humOrrat,sup_or_multi,diabete,inhib,unx,file_to_save):
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

    pt=compute(NPT,filename,'Broyden',sup_or_jux,diabete,humOrrat,sup_or_multi=sup_or_multi,inhibition = inhib,unx = unx)
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
                if pt[j].humOrrat == 'hum':
                    Radref = 0.0037/2.0e0  # Fortran:Change this to be half of the male diameter given in PTparams_M.dat.diam=0.0036 but this is changed to match Fortran code.
                    torqR = 0.0014 #Reference radius
                    torqL = 2.50e-4 #Microvillous length
                    torqd = 1.5e-05 #Height above the microvillous tip
                    torqvm = 0.020 #Compliance Fortran Code
                    PbloodPT = 20.0e0 #Reference pressure
                elif pt[j].humOrrat == 'rat':
                    Radref = 0.0025/2.0
                    torqR = 0.0011
                    torqL = 2.50e-4
                    torqd = 1.50e-5
                    torqvm = 0.030
                    PbloodPT = 9.0e0
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
    s3=compute(NS3,filename,'Newton',sup_or_jux,diabete,humOrrat,sup_or_multi=sup_or_multi,inhibition = inhib,unx = unx)
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
                if s3[j].humOrrat == 'hum':
                    Radref = 0.0037/2.0e0  # Fortran:Change this to be half of the male diameter given in PTparams_M.dat.diam=0.0036 but this is changed to match Fortran code.
                    torqR = 0.0014 #Reference radius
                    torqL = 2.50e-4 #Microvillous length
                    torqd = 1.5e-05 #Height above the microvillous tip
                    torqvm = 0.020 #Compliance Fortran Code
                    PbloodPT = 20.0e0 #Reference pressure
                elif s3[j].humOrrat == 'rat':
                    Radref = 0.0025/2.0
                    torqR = 0.0011
                    torqL = 2.50e-4
                    torqd = 1.50e-5
                    torqvm = 0.030
                    PbloodPT = 9.0e0
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
    #========================================================
    # Short descending limb
    #========================================================
    print('%s SDL start' %(sup_or_jux))
    NSDL = 200
    if humOrrat == 'human':
        method = 'Newton'
    elif humOrrat == 'rat':
        method = 'Broyden'
    if sex == 'Male':
        filename = './datafiles/SDLparams_M_'+humOrrat[0:3]+'.dat'
    elif sex == 'Female':
        filename = './datafiles/SDLparams_F_'+humOrrat[0:3]+'.dat'
    else:
        filename ='./datafiles/SDLparams_F_'+humOrrat[0:3]+'.dat'
    #sdl=compute(NSDL,filename,'Broyden',diabete)
    sdl=compute(NSDL,filename,method,sup_or_jux,diabete,humOrrat,sup_or_multi=sup_or_multi,inhibition = inhib,unx = unx)
    #========================================================
    # output SDL Concentrations in Lumen and Cell
    #========================================================
    for i in range(NS):
        file=open('./'+file_to_save+'/'+sdl[0].sex+'_'+humOrrat[0:3]+'_sdl_con_of_'+solute[i]+'_in_Lumen_'+sup_or_jux+'.txt','w')
        for j in range(NSDL):
            file.write(str(sdl[j].conc[i,0])+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+sdl[0].sex+'_'+humOrrat[0:3]+'_sdl_con_of_'+solute[i]+'_in_Cell_'+sup_or_jux+'.txt','w')
        for j in range(NSDL):
            file.write(str(sdl[j].conc[i,1])+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+sdl[0].sex+'_'+humOrrat[0:3]+'_sdl_con_of_'+solute[i]+'_in_Bath_'+sup_or_jux+'.txt','w')
        for j in range(NSDL):
            file.write(str(sdl[j].conc[i,5])+'\n')
        file.close()
    #========================================================
    # output SDL Water volume in Lumen and Cell
    #========================================================
    file=open('./'+file_to_save+'/'+sdl[0].sex+'_'+humOrrat[0:3]+'_sdl_water_volume_in_Lumen_'+sup_or_jux+'.txt','w')
    for j in range(NSDL):
        file.write(str(sdl[j].vol[0]*cw)+'\n')
    file.close()
    file=open('./'+file_to_save+'/'+sdl[0].sex+'_'+humOrrat[0:3]+'_sdl_water_volume_in_Cell_'+sup_or_jux+'.txt','w')
    for j in range(NSDL):
        file.write(str(sdl[j].vol[1]*cw)+'\n')
    file.close()
    #========================================================
    # output SDL solute flows in Lumen and Cell
    #========================================================
    for i in range(NS):
        file=open('./'+file_to_save+'/'+sdl[0].sex+'_'+humOrrat[0:3]+'_sdl_flow_of_'+solute[i]+'_in_Lumen_'+sup_or_jux+'.txt','w')
        for j in range(NSDL):
            file.write(str(sdl[j].conc[i,0]*sdl[j].vol[0]*cw)+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+sdl[0].sex+'_'+humOrrat[0:3]+'_sdl_flow_of_'+solute[i]+'_in_Cell_'+sup_or_jux+'.txt','w')
        for j in range(NSDL):
            file.write(str(sdl[j].conc[i,1]*sdl[j].vol[1]*cw)+'\n')
        file.close()
    #========================================================
    # output SDL osmolality in Lumen, Cell, LIS, Bath
    #========================================================
    file_lumen = open('./'+file_to_save+'/'+sdl[0].sex+'_'+humOrrat[0:3]+'_'+sdl[0].segment+'_osmolality_in_Lumen_'+sup_or_jux+'.txt','w')
    file_cell = open('./'+file_to_save+'/'+sdl[0].sex+'_'+humOrrat[0:3]+'_'+sdl[0].segment+'_osmolality_in_Cell_'+sup_or_jux+'.txt','w')
    file_lis = open('./'+file_to_save+'/'+sdl[0].sex+'_'+humOrrat[0:3]+'_'+sdl[0].segment+'_osmolality_in_LIS_'+sup_or_jux+'.txt','w')
    file_bath = open('./'+file_to_save+'/'+sdl[0].sex+'_'+humOrrat[0:3]+'_'+sdl[0].segment+'_osmolality_in_Bath_'+sup_or_jux+'.txt','w')
    for j in range(NSDL):
        osm_l = 0
        osm_c = 0
        osm_lis = 0
        osm_b = 0
        for i in range(NS):
            osm_l = osm_l +sdl[j].conc[i,0]
            osm_c = osm_c +sdl[j].conc[i,1]
            osm_lis = osm_lis+sdl[j].conc[i,4]
            osm_b = osm_b +sdl[j].conc[i,5]

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
    file=open('./'+file_to_save+'/'+sdl[0].sex+'_'+humOrrat[0:3]+'_'+sdl[0].segment+'_pressure_in_Lumen_'+sup_or_jux+'.txt','w')
    for j in range(NSDL):
        file.write(str(sdl[j].pres[0])+'\n')
    file.close()
    #========================================================
    # Na transcellular and paracellular transport
    #========================================================
    for j in range(NSDL):

        sdl[j].area[4][5] = 0.02*max(sdl[j].vol[4]/sdl[j].volref[4],1.0)
        sdl[j].area[5][4] = sdl[j].area[4][5]

        jvol = np.zeros([6,6])
        jsol = np.zeros([15,6,6])

        jvol,jsol = flux.compute_fluxes(sdl[j],j)

        file_Na_apical = open('./'+file_to_save+'/'+sdl[j].sex+'_'+humOrrat[0:3]+'_'+sdl[j].segment+'_apical_Na_'+sup_or_jux+'.txt','a')
        file_Na_apical.write(str(jsol[0,0,1])+'\n')

        file_Na_para = open('./'+file_to_save+'/'+sdl[j].sex+'_'+humOrrat[0:3]+'_'+sdl[j].segment+'_paracellular_Na_'+sup_or_jux+'.txt','a')
        file_Na_para.write(str(jsol[0,0,4])+'\n')

    print('%s SDL finished.' %(sup_or_jux))
    print('\n')
    #========================================================
    # Long descending limb
    #========================================================
    if sup_or_jux != 'sup':
        print('%s LDL start' %(sup_or_jux))
        NLDL = 200
        if sex == 'Male':
            filename = './datafiles/LDLparams_M_'+humOrrat[0:3]+'.dat'
        elif sex == 'Female':
            filename = './datafiles/LDLparams_F_'+humOrrat[0:3]+'.dat'
        else:
            filename ='./datafiles/LDLparams_F_'+humOrrat[0:3]+'.dat'
        ldl=compute(NLDL,filename,'Newton',sup_or_jux,diabete,humOrrat,sup_or_multi=sup_or_multi,inhibition = inhib,unx = unx)
    #========================================================
    # output LDL Concentrations in Lumen and Cell
    #========================================================
        for i in range(NS):
            file=open('./'+file_to_save+'/'+ldl[0].sex+'_'+humOrrat[0:3]+'_ldl_con_of_'+solute[i]+'_in_Lumen_'+sup_or_jux+'.txt','w')
            for j in range(NLDL):
                file.write(str(ldl[j].conc[i,0])+'\n')
            file.close()
        for i in range(NS):
            file=open('./'+file_to_save+'/'+ldl[0].sex+'_'+humOrrat[0:3]+'_ldl_con_of_'+solute[i]+'_in_Cell_'+sup_or_jux+'.txt','w')
            for j in range(NLDL):
                file.write(str(ldl[j].conc[i,1])+'\n')
            file.close()
        for i in range(NS):
            file=open('./'+file_to_save+'/'+ldl[0].sex+'_'+humOrrat[0:3]+'_ldl_con_of_'+solute[i]+'_in_Bath_'+sup_or_jux+'.txt','w')
            for j in range(NLDL):
                file.write(str(ldl[j].conc[i,5])+'\n')
            file.close()
    #========================================================
    # output LDL Water volume in Lumen and Cell
    #========================================================
        file=open('./'+file_to_save+'/'+ldl[0].sex+'_'+humOrrat[0:3]+'_ldl_water_volume_in_Lumen_'+sup_or_jux+'.txt','w')
        for j in range(NLDL):
            file.write(str(ldl[j].vol[0]*cw)+'\n')
        file.close()
        file=open('./'+file_to_save+'/'+ldl[0].sex+'_'+humOrrat[0:3]+'_ldl_water_volume_in_Cell_'+sup_or_jux+'.txt','w')
        for j in range(NLDL):
            file.write(str(ldl[j].vol[1]*cw)+'\n')
        file.close()
    #========================================================
    # output LDL solute flows in Lumen and Cell
    #========================================================
        for i in range(NS):
            file=open('./'+file_to_save+'/'+ldl[0].sex+'_'+humOrrat[0:3]+'_ldl_flow_of_'+solute[i]+'_in_Lumen_'+sup_or_jux+'.txt','w')
            for j in range(NLDL):
                file.write(str(ldl[j].conc[i,0]*ldl[j].vol[0]*cw)+'\n')
            file.close()
        for i in range(NS):
            file=open('./'+file_to_save+'/'+ldl[0].sex+'_'+humOrrat[0:3]+'_ldl_flow_of_'+solute[i]+'_in_Cell_'+sup_or_jux+'.txt','w')
            for j in range(NLDL):
                file.write(str(ldl[j].conc[i,1]*ldl[j].vol[1]*cw)+'\n')
            file.close()
    #========================================================
    # output LDL osmolality in Lumen, Cell, LIS, Bath
    #========================================================
        file_lumen = open('./'+file_to_save+'/'+ldl[0].sex+'_'+humOrrat[0:3]+'_'+ldl[0].segment+'_osmolality_in_Lumen_'+sup_or_jux+'.txt','w')
        file_cell = open('./'+file_to_save+'/'+ldl[0].sex+'_'+humOrrat[0:3]+'_'+ldl[0].segment+'_osmolality_in_Cell_'+sup_or_jux+'.txt','w')
        file_lis = open('./'+file_to_save+'/'+ldl[0].sex+'_'+humOrrat[0:3]+'_'+ldl[0].segment+'_osmolality_in_LIS_'+sup_or_jux+'.txt','w')
        file_bath = open('./'+file_to_save+'/'+ldl[0].sex+'_'+humOrrat[0:3]+'_'+ldl[0].segment+'_osmolality_in_Bath_'+sup_or_jux+'.txt','w')
        for j in range(NLDL):
            osm_l = 0
            osm_c = 0
            osm_lis = 0
            osm_b = 0
            for i in range(NS):
                osm_l = osm_l +ldl[j].conc[i,0]
                osm_c = osm_c +ldl[j].conc[i,1]
                osm_lis = osm_lis+ldl[j].conc[i,4]
                osm_b = osm_b +ldl[j].conc[i,5]

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
        file=open('./'+file_to_save+'/'+ldl[0].sex+'_'+humOrrat[0:3]+'_'+ldl[0].segment+'_pressure_in_Lumen_'+sup_or_jux+'.txt','w')
        for j in range(NLDL):
            file.write(str(ldl[j].pres[0])+'\n')
        file.close()

    #========================================================
    # Na transcellular and paracellular transport
    #========================================================
        for j in range(NLDL):

            ldl[j].area[4][5] = 0.02*max(ldl[j].vol[4]/ldl[j].volref[4],1.0)
            ldl[j].area[5][4] = ldl[j].area[4][5]

            jvol = np.zeros([6,6])
            jsol = np.zeros([15,6,6])        

            jvol,jsol = flux.compute_fluxes(ldl[j],j)

            file_Na_apical = open('./'+file_to_save+'/'+ldl[j].sex+'_'+humOrrat[0:3]+'_'+ldl[j].segment+'_apical_Na_'+sup_or_jux+'.txt','a')
            file_Na_apical.write(str(jsol[0,0,1])+'\n')

            file_Na_para = open('./'+file_to_save+'/'+ldl[j].sex+'_'+humOrrat[0:3]+'_'+ldl[j].segment+'_paracellular_Na_'+sup_or_jux+'.txt','a')
            file_Na_para.write(str(jsol[0,0,4])+'\n')


        print('%s LDL finished.' %(sup_or_jux))
        print('\n')
    #========================================================
    # Long ascending limb
    #========================================================
        print('%s LAL start' %(sup_or_jux))
        NLAL = 200
        if sex == 'Male':
            filename = './datafiles/LALparams_M_rat.dat'
        elif sex == 'Female':
            filename = './datafiles/LALparams_F_rat.dat'
        else:
            filename ='./datafiles/LALparams_F_rat.dat'
        lal=compute(NLAL,filename,'Newton',sup_or_jux,diabete,humOrrat,sup_or_multi=sup_or_multi,inhibition = inhib,unx = unx)
    #========================================================
    # output LAL Concentrations in Lumen and Cell
    #========================================================
        for i in range(NS):
            file=open('./'+file_to_save+'/'+lal[0].sex+'_'+humOrrat[0:3]+'_lal_con_of_'+solute[i]+'_in_Lumen_'+sup_or_jux+'.txt','w')
            for j in range(NLAL):
                file.write(str(lal[j].conc[i,0])+'\n')
            file.close()
        for i in range(NS):
            file=open('./'+file_to_save+'/'+lal[0].sex+'_'+humOrrat[0:3]+'_lal_con_of_'+solute[i]+'_in_Cell_'+sup_or_jux+'.txt','w')
            for j in range(NLAL):
                file.write(str(lal[j].conc[i,1])+'\n')
            file.close()
        for i in range(NS):
            file=open('./'+file_to_save+'/'+lal[0].sex+'_'+humOrrat[0:3]+'_lal_con_of_'+solute[i]+'_in_Bath_'+sup_or_jux+'.txt','w')
            for j in range(NLAL):
                file.write(str(lal[j].conc[i,5])+'\n')
            file.close()
    #========================================================
    # output LAL Water volume in Lumen and Cell
    #========================================================
        file=open('./'+file_to_save+'/'+lal[0].sex+'_'+humOrrat[0:3]+'_lal_water_volume_in_Lumen_'+sup_or_jux+'.txt','w')
        for j in range(NLAL):
            file.write(str(lal[j].vol[0]*cw)+'\n')
        file.close()
        file=open('./'+file_to_save+'/'+lal[0].sex+'_'+humOrrat[0:3]+'_lal_water_volume_in_Cell_'+sup_or_jux+'.txt','w')
        for j in range(NLAL):
            file.write(str(lal[j].vol[1]*cw)+'\n')
        file.close()
    #========================================================
    # output LAL solute flows in Lumen and Cell
    #========================================================
        for i in range(NS):
            file=open('./'+file_to_save+'/'+lal[0].sex+'_'+humOrrat[0:3]+'_lal_flow_of_'+solute[i]+'_in_Lumen_'+sup_or_jux+'.txt','w')
            for j in range(NLAL):
                file.write(str(lal[j].conc[i,0]*lal[j].vol[0]*cw)+'\n')
            file.close()
        for i in range(NS):
            file=open('./'+file_to_save+'/'+lal[0].sex+'_'+humOrrat[0:3]+'_lal_flow_of_'+solute[i]+'_in_Cell_'+sup_or_jux+'.txt','w')
            for j in range(NLAL):
                file.write(str(lal[j].conc[i,1]*lal[j].vol[1]*cw)+'\n')
            file.close()
    #========================================================
    # output LAL osmolality in Lumen, Cell, LIS, Bath
    #========================================================
        file_lumen = open('./'+file_to_save+'/'+lal[0].sex+'_'+humOrrat[0:3]+'_'+lal[0].segment+'_osmolality_in_Lumen_'+sup_or_jux+'.txt','w')
        file_cell = open('./'+file_to_save+'/'+lal[0].sex+'_'+humOrrat[0:3]+'_'+lal[0].segment+'_osmolality_in_Cell_'+sup_or_jux+'.txt','w')
        file_lis = open('./'+file_to_save+'/'+lal[0].sex+'_'+humOrrat[0:3]+'_'+lal[0].segment+'_osmolality_in_LIS_'+sup_or_jux+'.txt','w')
        file_bath = open('./'+file_to_save+'/'+lal[0].sex+'_'+humOrrat[0:3]+'_'+lal[0].segment+'_osmolality_in_Bath_'+sup_or_jux+'.txt','w')
        for j in range(NLAL):
            osm_l = 0
            osm_c = 0
            osm_lis = 0
            osm_b = 0
            for i in range(NS):
                osm_l = osm_l +lal[j].conc[i,0]
                osm_c = osm_c +lal[j].conc[i,1]
                osm_lis = osm_lis+lal[j].conc[i,4]
                osm_b = osm_b +lal[j].conc[i,5]

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
        file=open('./'+file_to_save+'/'+lal[0].sex+'_'+humOrrat[0:3]+'_'+lal[0].segment+'_pressure_in_Lumen_'+sup_or_jux+'.txt','w')
        for j in range(NLAL):
            file.write(str(lal[j].pres[0])+'\n')
        file.close()
    
    #========================================================
    # Na transcellular and paracellular transport
    #========================================================
        for j in range(NLAL):

            lal[j].area[4][5] = 0.02*max(lal[j].vol[4]/lal[j].volref[4],1.0)
            lal[j].area[5][4] = lal[j].area[4][5]

            jvol = np.zeros([6,6])
            jsol = np.zeros([15,6,6])

            jvol,jsol = flux.compute_fluxes(lal[j],j)

            file_Na_apical = open('./'+file_to_save+'/'+lal[j].sex+'_'+humOrrat[0:3]+'_'+lal[j].segment+'_apical_Na_'+sup_or_jux+'.txt','a')
            file_Na_apical.write(str(jsol[0,0,1])+'\n')

            file_Na_para = open('./'+file_to_save+'/'+lal[j].sex+'_'+humOrrat[0:3]+'_'+lal[j].segment+'_paracellular_Na_'+sup_or_jux+'.txt','a')
            file_Na_para.write(str(jsol[0,0,4])+'\n')


        print('%s LAL finished.' %(sup_or_jux))
        print('\n')
    #========================================================
    # Medulla thick ascending limb
    #========================================================
    print('%s mTAL start' %(sup_or_jux))
    NmTAL = 200
    if sex == 'Male':
        filename = './datafiles/mTALparams_M_'+humOrrat[0:3]+'.dat'
    elif sex == 'Female':
        filename = './datafiles/mTALparams_F_'+humOrrat[0:3]+'.dat'
    else:
        filename ='./datafiles/mTALparams_F_'+humOrrat[0:3]+'.dat'
    mtal=compute(NmTAL,filename,'Newton',sup_or_jux,diabete,humOrrat,sup_or_multi,inhib,unx = unx)
    #========================================================
    # output mTAL Concentrations in Lumen and Cell
    #========================================================
    for i in range(NS):
        file=open('./'+file_to_save+'/'+mtal[0].sex+'_'+humOrrat[0:3]+'_mtal_con_of_'+solute[i]+'_in_Lumen_'+sup_or_jux+'.txt','w')
        for j in range(NmTAL):
            file.write(str(mtal[j].conc[i,0])+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+mtal[0].sex+'_'+humOrrat[0:3]+'_mtal_con_of_'+solute[i]+'_in_Cell_'+sup_or_jux+'.txt','w')
        for j in range(NmTAL):
            file.write(str(mtal[j].conc[i,1])+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+mtal[0].sex+'_'+humOrrat[0:3]+'_mtal_con_of_'+solute[i]+'_in_Bath_'+sup_or_jux+'.txt','w')
        for j in range(NmTAL):
            file.write(str(mtal[j].conc[i,5])+'\n')
        file.close()
    #========================================================
    # output mTAL Water volume in Lumen and Cell
    #========================================================
    file=open('./'+file_to_save+'/'+mtal[0].sex+'_'+humOrrat[0:3]+'_mtal_water_volume_in_Lumen_'+sup_or_jux+'.txt','w')
    for j in range(NmTAL):
        file.write(str(mtal[j].vol[0]*cw)+'\n')
    file.close()
    file=open('./'+file_to_save+'/'+mtal[0].sex+'_'+humOrrat[0:3]+'_mtal_water_volume_in_Cell_'+sup_or_jux+'.txt','w')
    for j in range(NmTAL):
        file.write(str(mtal[j].vol[1]*cw)+'\n')
    file.close()
    #========================================================
    # output mTAL solute flows in Lumen and Cell
    #========================================================
    for i in range(NS):
        file=open('./'+file_to_save+'/'+mtal[0].sex+'_'+humOrrat[0:3]+'_mtal_flow_of_'+solute[i]+'_in_Lumen_'+sup_or_jux+'.txt','w')
        for j in range(NmTAL):
            file.write(str(mtal[j].conc[i,0]*mtal[j].vol[0]*cw)+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+mtal[0].sex+'_'+humOrrat[0:3]+'_mtal_flow_of_'+solute[i]+'_in_Cell_'+sup_or_jux+'.txt','w')
        for j in range(NmTAL):
            file.write(str(mtal[j].conc[i,1]*mtal[j].vol[1]*cw)+'\n')
        file.close()
    #========================================================
    # output mTAL osmolality in Lumen, Cell, LIS, Bath
    #========================================================
    file_lumen = open('./'+file_to_save+'/'+mtal[0].sex+'_'+humOrrat[0:3]+'_'+mtal[0].segment+'_osmolality_in_Lumen_'+sup_or_jux+'.txt','w')
    file_cell = open('./'+file_to_save+'/'+mtal[0].sex+'_'+humOrrat[0:3]+'_'+mtal[0].segment+'_osmolality_in_Cell_'+sup_or_jux+'.txt','w')
    file_lis = open('./'+file_to_save+'/'+mtal[0].sex+'_'+humOrrat[0:3]+'_'+mtal[0].segment+'_osmolality_in_LIS_'+sup_or_jux+'.txt','w')
    file_bath = open('./'+file_to_save+'/'+mtal[0].sex+'_'+humOrrat[0:3]+'_'+mtal[0].segment+'_osmolality_in_Bath_'+sup_or_jux+'.txt','w')
    for j in range(NmTAL):
        osm_l = 0
        osm_c = 0
        osm_lis = 0
        osm_b = 0
        for i in range(NS):
            osm_l = osm_l +mtal[j].conc[i,0]
            osm_c = osm_c +mtal[j].conc[i,1]
            osm_lis = osm_lis+mtal[j].conc[i,4]
            osm_b = osm_b +mtal[j].conc[i,5]

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
    file=open('./'+file_to_save+'/'+mtal[0].sex+'_'+humOrrat[0:3]+'_'+mtal[0].segment+'_pressure_in_Lumen_'+sup_or_jux+'.txt','w')
    for j in range(NmTAL):
        file.write(str(mtal[j].pres[0])+'\n')
    file.close()
    #========================================================
    # output fluxes through transporters
    #========================================================
    for j in range(NmTAL):

        mtal[j].area[4][5] = 0.02*max(mtal[j].vol[4]/mtal[j].volref[4],1.0)
        mtal[j].area[5][4] = mtal[j].area[4][5]

        jvol = np.zeros([6,6])
        jsol = np.zeros([15,6,6])

        jvol,jsol = flux.compute_fluxes(mtal[j],j)

        file_Na_apical = open('./'+file_to_save+'/'+mtal[j].sex+'_'+humOrrat[0:3]+'_'+mtal[j].segment+'_apical_Na_'+sup_or_jux+'.txt','a')
        file_Na_apical.write(str(jsol[0,0,1])+'\n')

        file_Na_para = open('./'+file_to_save+'/'+mtal[j].sex+'_'+humOrrat[0:3]+'_'+mtal[j].segment+'_paracellular_Na_'+sup_or_jux+'.txt','a')
        file_Na_para.write(str(jsol[0,0,4])+'\n')

        for i in range(len(mtal[j].trans)):
            transporter_type = mtal[j].trans[i].type
            memb_id = mtal[j].trans[i].membrane_id

            if transporter_type == 'SGLT1':
                solute_id,fluxs = glucose.sglt1(mtal[j],mtal[j].ep,memb_id,mtal[j].trans[i].act,mtal[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+mtal[j].sex+'_'+humOrrat[0:3]+'_'+mtal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'SGLT2':
                solute_id,fluxs = glucose.sglt2(mtal[j],mtal[j].ep,memb_id,mtal[j].trans[i].act,mtal[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+mtal[j].sex+'_'+humOrrat[0:3]+'_'+mtal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'GLUT1':
                solute_id,fluxs=glucose.glut1(mtal[j],mtal[j].ep,memb_id,mtal[j].trans[i].act,mtal[j].area)
                for k in range(len([solute_id])):
                    file = open('./'+file_to_save+'/'+mtal[j].sex+'_'+humOrrat[0:3]+'_'+mtal[j].segment+'_'+transporter_type+'_'+solute[solute_id]+str(memb_id[0])+str(memb_id[1])+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs)+'\n')
            elif transporter_type == 'GLUT2':
                solute_id,fluxs=glucose.glut2(mtal[j],mtal[j].ep,memb_id,mtal[j].trans[i].act,mtal[j].area)
                for k in range(len([solute_id])):
                    file = open('./'+file_to_save+'/'+mtal[j].sex+'_'+humOrrat[0:3]+'_'+mtal[j].segment+'_'+transporter_type+'_'+solute[solute_id]+str(memb_id[0])+str(memb_id[1])+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs)+'\n')			
            elif transporter_type == 'NHE3':
                solute_id,fluxs=NHE3.nhe3(mtal[j],mtal[j].ep,memb_id,mtal[j].trans[i].act,mtal[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+mtal[j].sex+'_'+humOrrat[0:3]+'_'+mtal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NaKATPase':
                solute_id,fluxs=ATPase.nakatpase(mtal[j],mtal[j].ep,memb_id,mtal[j].trans[i].act,mtal[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+mtal[j].sex+'_'+humOrrat[0:3]+'_'+mtal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+str(memb_id[0])+str(memb_id[1])+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')

            elif transporter_type == 'HATPase':
                solute_id,fluxs=ATPase.hatpase(mtal[j],mtal[j].ep,memb_id,mtal[j].trans[i].act,mtal[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+mtal[j].sex+'_'+humOrrat[0:3]+'_'+mtal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NKCC2A':
                solute_id,fluxs=NKCC.nkcc2(mtal[j],memb_id,mtal[j].trans[i].act,mtal[j].area,'A')
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+mtal[j].sex+'_'+humOrrat[0:3]+'_'+mtal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NKCC2B':
                solute_id,fluxs=NKCC.nkcc2(mtal[j],memb_id,mtal[j].trans[i].act,mtal[j].area,'B')
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+mtal[j].sex+'_'+humOrrat[0:3]+'_'+mtal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NKCC2F':
                solute_id,fluxs=NKCC.nkcc2(mtal[j],memb_id,mtal[j].trans[i].act,mtal[j].area,'F')
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+mtal[j].sex+'_'+humOrrat[0:3]+'_'+mtal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')       
            elif transporter_type == 'KCC4':
                solute_id,fluxs=KCC.kcc4(mtal[j].conc,memb_id,mtal[j].trans[i].act,mtal[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+mtal[j].sex+'_'+humOrrat[0:3]+'_'+mtal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'ENaC':
                solute_id,fluxs=ENaC.ENaC(mtal[j],j,memb_id,mtal[j].trans[i].act,mtal[j].area,jvol)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+mtal[j].sex+'_'+humOrrat[0:3]+'_'+mtal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NCC':
                solute_id,fluxs=NCC.NCC(mtal[j],j,memb_id,mtal[j].trans[i].act,mtal[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+mtal[j].sex+'_'+humOrrat[0:3]+'_'+mtal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'Pendrin':
                solute_id,fluxs=Pendrin.Pendrin(mtal[j],memb_id,mtal[j].trans[i].act,mtal[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+mtal[j].sex+'_'+humOrrat[0:3]+'_'+mtal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type =='AE1':
                solute_id,fluxs=AE1.AE1(mtal[j],memb_id,mtal[j].trans[i].act,mtal[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+mtal[j].sex+'_'+humOrrat[0:3]+'_'+mtal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'HKATPase':
                solute_id,fluxs=ATPase.hkatpase(mtal[j],memb_id,mtal[j].trans[i].act,mtal[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+mtal[j].sex+'_'+humOrrat[0:3]+'_'+mtal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NHE1':
                solute_id,fluxs=NHE1.NHE1(mtal[j],memb_id,mtal[j].trans[i].act,mtal[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+mtal[j].sex+'_'+humOrrat[0:3]+'_'+mtal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NKCC1':
                solute_id,fluxs=NKCC.nkcc1(mtal[j],memb_id,mtal[j].trans[i].act,delmu)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+mtal[j].sex+'_'+humOrrat[0:3]+'_'+mtal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            else:
                raise Exception('What is this?',transporter_type)
    print('%s mTAL finished.' %(sup_or_jux))
    print('\n')
    #========================================================
    # Cortex thick ascending limb
    #========================================================
    print('%s cTAL start' %(sup_or_jux))
    NcTAL = 200
    if sex == 'Male':
        filename = './datafiles/cTALparams_M_'+humOrrat[0:3]+'.dat'
    elif sex == 'Female':
        filename = './datafiles/cTALparams_F_'+humOrrat[0:3]+'.dat'
    else:
        filename ='./datafiles/cTALparams_F_'+humOrrat[0:3]+'.dat'
    ctal=compute(NcTAL,filename,'Newton',sup_or_jux,diabete,humOrrat,sup_or_multi,inhib,unx = unx)
    #========================================================
    # output cTAL Concentrations in Lumen and Cell
    #========================================================
    for i in range(NS):
        file=open('./'+file_to_save+'/'+ctal[0].sex+'_'+humOrrat[0:3]+'_ctal_con_of_'+solute[i]+'_in_Lumen_'+sup_or_jux+'.txt','w')
        for j in range(NcTAL):
            file.write(str(ctal[j].conc[i,0])+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+ctal[0].sex+'_'+humOrrat[0:3]+'_ctal_con_of_'+solute[i]+'_in_Cell_'+sup_or_jux+'.txt','w')
        for j in range(NcTAL):
            file.write(str(ctal[j].conc[i,1])+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+ctal[0].sex+'_'+humOrrat[0:3]+'_ctal_con_of_'+solute[i]+'_in_Bath_'+sup_or_jux+'.txt','w')
        for j in range(NcTAL):
            file.write(str(ctal[j].conc[i,5])+'\n')
        file.close()
    #========================================================
    # output cTAL Water volume in Lumen and Cell
    #========================================================
    file=open('./'+file_to_save+'/'+ctal[0].sex+'_'+humOrrat[0:3]+'_ctal_water_volume_in_Lumen_'+sup_or_jux+'.txt','w')
    for j in range(NcTAL):
        file.write(str(ctal[j].vol[0]*cw)+'\n')
    file.close()
    file=open('./'+file_to_save+'/'+ctal[0].sex+'_'+humOrrat[0:3]+'_ctal_water_volume_in_Cell_'+sup_or_jux+'.txt','w')
    for j in range(NcTAL):
        file.write(str(ctal[j].vol[1]*cw)+'\n')
    file.close()
    #========================================================
    # output cTAL solute flows in Lumen and Cell
    #========================================================
    for i in range(NS):
        file=open('./'+file_to_save+'/'+ctal[0].sex+'_'+humOrrat[0:3]+'_ctal_flow_of_'+solute[i]+'_in_Lumen_'+sup_or_jux+'.txt','w')
        for j in range(NcTAL):
            file.write(str(ctal[j].conc[i,0]*ctal[j].vol[0]*cw)+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+ctal[0].sex+'_'+humOrrat[0:3]+'_ctal_flow_of_'+solute[i]+'_in_Cell_'+sup_or_jux+'.txt','w')
        for j in range(NcTAL):
            file.write(str(ctal[j].conc[i,1]*ctal[j].vol[1]*cw)+'\n')
        file.close()
    #========================================================
    # output cTAL osmolality in Lumen, Cell, LIS, Bath
    #========================================================
    file_lumen = open('./'+file_to_save+'/'+ctal[0].sex+'_'+humOrrat[0:3]+'_'+ctal[0].segment+'_osmolality_in_Lumen_'+sup_or_jux+'.txt','w')
    file_cell = open('./'+file_to_save+'/'+ctal[0].sex+'_'+humOrrat[0:3]+'_'+ctal[0].segment+'_osmolality_in_Cell_'+sup_or_jux+'.txt','w')
    file_lis = open('./'+file_to_save+'/'+ctal[0].sex+'_'+humOrrat[0:3]+'_'+ctal[0].segment+'_osmolality_in_LIS_'+sup_or_jux+'.txt','w')
    file_bath = open('./'+file_to_save+'/'+ctal[0].sex+'_'+humOrrat[0:3]+'_'+ctal[0].segment+'_osmolality_in_Bath_'+sup_or_jux+'.txt','w')
    for j in range(NcTAL):
        osm_l = 0
        osm_c = 0
        osm_lis = 0
        osm_b = 0
        for i in range(NS):
            osm_l = osm_l +ctal[j].conc[i,0]
            osm_c = osm_c +ctal[j].conc[i,1]
            osm_lis = osm_lis+ctal[j].conc[i,4]
            osm_b = osm_b +ctal[j].conc[i,5]

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
    file=open('./'+file_to_save+'/'+ctal[0].sex+'_'+humOrrat[0:3]+'_'+ctal[0].segment+'_pressure_in_Lumen_'+sup_or_jux+'.txt','w')
    for j in range(NcTAL):
        file.write(str(ctal[j].pres[0])+'\n')
    file.close()
    #========================================================
    # output fluxes through transporters
    #========================================================
    for j in range(NcTAL):

        ctal[j].area[4][5] = 0.02*max(ctal[j].vol[4]/ctal[j].volref[4],1.0)
        ctal[j].area[5][4] = ctal[j].area[4][5]

        jvol = np.zeros([6,6])
        jsol = np.zeros([15,6,6])

        jvol,jsol = flux.compute_fluxes(ctal[j],j)

        file_Na_apical = open('./'+file_to_save+'/'+ctal[j].sex+'_'+humOrrat[0:3]+'_'+ctal[j].segment+'_apical_Na_'+sup_or_jux+'.txt','a')
        file_Na_apical.write(str(jsol[0,0,1])+'\n')

        file_Na_para = open('./'+file_to_save+'/'+ctal[j].sex+'_'+humOrrat[0:3]+'_'+ctal[j].segment+'_paracellular_Na_'+sup_or_jux+'.txt','a')
        file_Na_para.write(str(jsol[0,0,4])+'\n')

        for i in range(len(ctal[j].trans)):
            transporter_type = ctal[j].trans[i].type
            memb_id = ctal[j].trans[i].membrane_id

            if transporter_type == 'SGLT1':
                solute_id,fluxs = glucose.sglt1(ctal[j],ctal[j].ep,memb_id,ctal[j].trans[i].act,ctal[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ctal[j].sex+'_'+humOrrat[0:3]+'_'+ctal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'SGLT2':
                solute_id,fluxs = glucose.sglt2(ctal[j],ctal[j].ep,memb_id,ctal[j].trans[i].act,ctal[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ctal[j].sex+'_'+humOrrat[0:3]+'_'+ctal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'GLUT1':
                solute_id,fluxs=glucose.glut1(ctal[j],ctal[j].ep,memb_id,ctal[j].trans[i].act,ctal[j].area)
                for k in range(len([solute_id])):
                    file = open('./'+file_to_save+'/'+ctal[j].sex+'_'+humOrrat[0:3]+'_'+ctal[j].segment+'_'+transporter_type+'_'+solute[solute_id]+str(memb_id[0])+str(memb_id[1])+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs)+'\n')
            elif transporter_type == 'GLUT2':
                solute_id,fluxs=glucose.glut2(ctal[j],ctal[j].ep,memb_id,ctal[j].trans[i].act,ctal[j].area)
                for k in range(len([solute_id])):
                    file = open('./'+file_to_save+'/'+ctal[j].sex+'_'+humOrrat[0:3]+'_'+ctal[j].segment+'_'+transporter_type+'_'+solute[solute_id]+str(memb_id[0])+str(memb_id[1])+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs)+'\n')			
            elif transporter_type == 'NHE3':
                solute_id,fluxs=NHE3.nhe3(ctal[j],ctal[j].ep,memb_id,ctal[j].trans[i].act,ctal[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ctal[j].sex+'_'+humOrrat[0:3]+'_'+ctal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NaKATPase':
                solute_id,fluxs=ATPase.nakatpase(ctal[j],ctal[j].ep,memb_id,ctal[j].trans[i].act,ctal[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ctal[j].sex+'_'+humOrrat[0:3]+'_'+ctal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+str(memb_id[0])+str(memb_id[1])+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')

            elif transporter_type == 'HATPase':
                solute_id,fluxs=ATPase.hatpase(ctal[j],ctal[j].ep,memb_id,ctal[j].trans[i].act,ctal[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ctal[j].sex+'_'+humOrrat[0:3]+'_'+ctal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NKCC2A':
                solute_id,fluxs=NKCC.nkcc2(ctal[j],memb_id,ctal[j].trans[i].act,ctal[j].area,'A')
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ctal[j].sex+'_'+humOrrat[0:3]+'_'+ctal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NKCC2B':
                solute_id,fluxs=NKCC.nkcc2(ctal[j],memb_id,ctal[j].trans[i].act,ctal[j].area,'B')
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ctal[j].sex+'_'+humOrrat[0:3]+'_'+ctal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NKCC2F':
                solute_id,fluxs=NKCC.nkcc2(ctal[j],memb_id,ctal[j].trans[i].act,ctal[j].area,'F')
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ctal[j].sex+'_'+humOrrat[0:3]+'_'+ctal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')       
            elif transporter_type == 'KCC4':
                solute_id,fluxs=KCC.kcc4(ctal[j].conc,memb_id,ctal[j].trans[i].act,ctal[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ctal[j].sex+'_'+humOrrat[0:3]+'_'+ctal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'ENaC':
                solute_id,fluxs=ENaC.ENaC(ctal[j],j,memb_id,ctal[j].trans[i].act,ctal[j].area,jvol)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ctal[j].sex+'_'+humOrrat[0:3]+'_'+ctal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NCC':
                solute_id,fluxs=NCC.NCC(ctal[j],j,memb_id,ctal[j].trans[i].act,ctal[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ctal[j].sex+'_'+humOrrat[0:3]+'_'+ctal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'Pendrin':
                solute_id,fluxs=Pendrin.Pendrin(ctal[j],memb_id,ctal[j].trans[i].act,ctal[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ctal[j].sex+'_'+humOrrat[0:3]+'_'+ctal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type =='AE1':
                solute_id,fluxs=AE1.AE1(ctal[j],memb_id,ctal[j].trans[i].act,ctal[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ctal[j].sex+'_'+humOrrat[0:3]+'_'+ctal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'HKATPase':
                solute_id,fluxs=ATPase.hkatpase(ctal[j],memb_id,ctal[j].trans[i].act,ctal[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ctal[j].sex+'_'+humOrrat[0:3]+'_'+ctal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NHE1':
                solute_id,fluxs=NHE1.NHE1(ctal[j],memb_id,ctal[j].trans[i].act,ctal[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ctal[j].sex+'_'+humOrrat[0:3]+'_'+ctal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NKCC1':
                solute_id,fluxs=NKCC.nkcc1(ctal[j],memb_id,ctal[j].trans[i].act,delmu)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+ctal[j].sex+'_'+humOrrat[0:3]+'_'+ctal[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            else:
                raise Exception('What is this?',transporter_type)
    print('%s cTAL finished.' %(sup_or_jux))
    print('\n')
    #========================================================
    # Distal convoluted tubule
    #========================================================
    print('%s DCT start' %(sup_or_jux))
    NDCT = 200
    if sex == 'Male':
        filename = './datafiles/DCTparams_M_'+humOrrat[0:3]+'.dat'
    elif sex == 'Female':
        filename = './datafiles/DCTparams_F_'+humOrrat[0:3]+'.dat'
    else:
        filename ='./datafiles/DCTparams_F_'+humOrrat[0:3]+'.dat'
    dct=compute(NDCT,filename,'Newton',sup_or_jux,diabete,humOrrat,sup_or_multi,inhib,unx = unx)
    #========================================================
    # output DCT Concentrations in Lumen and Cell
    #========================================================
    for i in range(NS):
        file=open('./'+file_to_save+'/'+dct[0].sex+'_'+humOrrat[0:3]+'_dct_con_of_'+solute[i]+'_in_Lumen_'+sup_or_jux+'.txt','w')
        for j in range(NDCT):
            file.write(str(dct[j].conc[i,0])+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+dct[0].sex+'_'+humOrrat[0:3]+'_dct_con_of_'+solute[i]+'_in_Cell_'+sup_or_jux+'.txt','w')
        for j in range(NDCT):
            file.write(str(dct[j].conc[i,1])+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+dct[0].sex+'_'+humOrrat[0:3]+'_dct_con_of_'+solute[i]+'_in_Bath_'+sup_or_jux+'.txt','w')
        for j in range(NDCT):
            file.write(str(dct[j].conc[i,5])+'\n')
        file.close()
    #========================================================
    # output DCT Water volume in Lumen and Cell
    #========================================================
    file=open('./'+file_to_save+'/'+dct[0].sex+'_'+humOrrat[0:3]+'_dct_water_volume_in_Lumen_'+sup_or_jux+'.txt','w')
    for j in range(NDCT):
        file.write(str(dct[j].vol[0]*cw)+'\n')
    file.close()
    file=open('./'+file_to_save+'/'+dct[0].sex+'_'+humOrrat[0:3]+'_dct_water_volume_in_Cell_'+sup_or_jux+'.txt','w')
    for j in range(NDCT):
        file.write(str(dct[j].vol[1]*cw)+'\n')
    file.close()
    #========================================================
    # output DCT solute flows in Lumen and Cell
    #========================================================
    for i in range(NS):
        file=open('./'+file_to_save+'/'+dct[0].sex+'_'+humOrrat[0:3]+'_dct_flow_of_'+solute[i]+'_in_Lumen_'+sup_or_jux+'.txt','w')
        for j in range(NDCT):
            file.write(str(dct[j].conc[i,0]*dct[j].vol[0]*cw)+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+dct[0].sex+'_'+humOrrat[0:3]+'_dct_flow_of_'+solute[i]+'_in_Cell_'+sup_or_jux+'.txt','w')
        for j in range(NDCT):
            file.write(str(dct[j].conc[i,1]*dct[j].vol[1]*cw)+'\n')
        file.close()
    #========================================================
    # output DCT osmolality in Lumen, Cell, LIS, Bath
    #========================================================
    file_lumen = open('./'+file_to_save+'/'+dct[0].sex+'_'+humOrrat[0:3]+'_'+dct[0].segment+'_osmolality_in_Lumen_'+sup_or_jux+'.txt','w')
    file_cell = open('./'+file_to_save+'/'+dct[0].sex+'_'+humOrrat[0:3]+'_'+dct[0].segment+'_osmolality_in_Cell_'+sup_or_jux+'.txt','w')
    file_lis = open('./'+file_to_save+'/'+dct[0].sex+'_'+humOrrat[0:3]+'_'+dct[0].segment+'_osmolality_in_LIS_'+sup_or_jux+'.txt','w')
    file_bath = open('./'+file_to_save+'/'+dct[0].sex+'_'+humOrrat[0:3]+'_'+dct[0].segment+'_osmolality_in_Bath_'+sup_or_jux+'.txt','w')
    for j in range(NDCT):
        osm_l = 0
        osm_c = 0
        osm_lis = 0
        osm_b = 0
        for i in range(NS):
            osm_l = osm_l +dct[j].conc[i,0]
            osm_c = osm_c +dct[j].conc[i,1]
            osm_lis = osm_lis+dct[j].conc[i,4]
            osm_b = osm_b +dct[j].conc[i,5]

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
    file=open('./'+file_to_save+'/'+dct[0].sex+'_'+humOrrat[0:3]+'_'+dct[0].segment+'_pressure_in_Lumen_'+sup_or_jux+'.txt','w')
    for j in range(NDCT):
        file.write(str(dct[j].pres[0])+'\n')
    file.close()
    #========================================================
    # output fluxes through transporters
    #========================================================
    for j in range(NDCT):

        dct[j].area[4][5] = 0.02*max(dct[j].vol[4]/dct[j].volref[4],1.0)
        dct[j].area[5][4] = dct[j].area[4][5]
        
        jvol = np.zeros([6,6])
        jsol = np.zeros([15,6,6])
        
        jvol,jsol = flux.compute_fluxes(dct[j],j)

        file_Na_apical = open('./'+file_to_save+'/'+dct[j].sex+'_'+humOrrat[0:3]+'_'+dct[j].segment+'_apical_Na_'+sup_or_jux+'.txt','a')
        file_Na_apical.write(str(jsol[0,0,1])+'\n')

        file_Na_para = open('./'+file_to_save+'/'+dct[j].sex+'_'+humOrrat[0:3]+'_'+dct[j].segment+'_paracellular_Na_'+sup_or_jux+'.txt','a')
        file_Na_para.write(str(jsol[0,0,4])+'\n')
        
        jvol = np.zeros([6,6])
        jsol = np.zeros([15,6,6])

        jvol = water.compute_water_fluxes(dct[j])
        jsol,delmu = electrochemical.compute_ecd_fluxes(dct[j],jvol)
        for i in range(len(dct[j].trans)):
            transporter_type = dct[j].trans[i].type
            memb_id = dct[j].trans[i].membrane_id

            if transporter_type == 'SGLT1':
                solute_id,fluxs = glucose.sglt1(dct[j],dct[j].ep,memb_id,dct[j].trans[i].act,dct[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+dct[j].sex+'_'+humOrrat[0:3]+'_'+dct[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'SGLT2':
                solute_id,fluxs = glucose.sglt2(dct[j],dct[j].ep,memb_id,dct[j].trans[i].act,dct[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+dct[j].sex+'_'+humOrrat[0:3]+'_'+dct[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'GLUT1':
                solute_id,fluxs=glucose.glut1(dct[j],dct[j].ep,memb_id,dct[j].trans[i].act,dct[j].area)
                for k in range(len([solute_id])):
                    file = open('./'+file_to_save+'/'+dct[j].sex+'_'+humOrrat[0:3]+'_'+dct[j].segment+'_'+transporter_type+'_'+solute[solute_id]+str(memb_id[0])+str(memb_id[1])+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs)+'\n')
            elif transporter_type == 'GLUT2':
                solute_id,fluxs=glucose.glut2(dct[j],dct[j].ep,memb_id,dct[j].trans[i].act,dct[j].area)
                for k in range(len([solute_id])):
                    file = open('./'+file_to_save+'/'+dct[j].sex+'_'+humOrrat[0:3]+'_'+dct[j].segment+'_'+transporter_type+'_'+solute[solute_id]+str(memb_id[0])+str(memb_id[1])+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs)+'\n')			
            elif transporter_type == 'NHE3':
                solute_id,fluxs=NHE3.nhe3(dct[j],dct[j].ep,memb_id,dct[j].trans[i].act,dct[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+dct[j].sex+'_'+humOrrat[0:3]+'_'+dct[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NaKATPase':
                solute_id,fluxs=ATPase.nakatpase(dct[j],dct[j].ep,memb_id,dct[j].trans[i].act,dct[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+dct[j].sex+'_'+humOrrat[0:3]+'_'+dct[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+str(memb_id[0])+str(memb_id[1])+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')

            elif transporter_type == 'HATPase':
                solute_id,fluxs=ATPase.hatpase(dct[j],dct[j].ep,memb_id,dct[j].trans[i].act,dct[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+dct[j].sex+'_'+humOrrat[0:3]+'_'+dct[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NKCC2A':
                solute_id,fluxs=NKCC.nkcc2(dct[j],memb_id,dct[j].trans[i].act,dct[j].area,'A')
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+dct[j].sex+'_'+humOrrat[0:3]+'_'+dct[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NKCC2B':
                solute_id,fluxs=NKCC.nkcc2(dct[j],memb_id,dct[j].trans[i].act,dct[j].area,'B')
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+dct[j].sex+'_'+humOrrat[0:3]+'_'+dct[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NKCC2F':
                solute_id,fluxs=NKCC.nkcc2(dct[j],memb_id,dct[j].trans[i].act,dct[j].area,'F')
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+dct[j].sex+'_'+humOrrat[0:3]+'_'+dct[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')       
            elif transporter_type == 'KCC4':
                solute_id,fluxs=KCC.kcc4(dct[j].conc,memb_id,dct[j].trans[i].act,dct[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+dct[j].sex+'_'+humOrrat[0:3]+'_'+dct[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'ENaC':
                solute_id,fluxs=ENaC.ENaC(dct[j],j,memb_id,dct[j].trans[i].act,dct[j].area,jvol)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+dct[j].sex+'_'+humOrrat[0:3]+'_'+dct[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NCC':
                solute_id,fluxs=NCC.NCC(dct[j],j,memb_id,dct[j].trans[i].act,dct[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+dct[j].sex+'_'+humOrrat[0:3]+'_'+dct[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'Pendrin':
                solute_id,fluxs=Pendrin.Pendrin(dct[j],memb_id,dct[j].trans[i].act,dct[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+dct[j].sex+'_'+humOrrat[0:3]+'_'+dct[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type =='AE1':
                solute_id,fluxs=AE1.AE1(dct[j],memb_id,dct[j].trans[i].act,dct[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+dct[j].sex+'_'+humOrrat[0:3]+'_'+dct[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'HKATPase':
                solute_id,fluxs=ATPase.hkatpase(dct[j],memb_id,dct[j].trans[i].act,dct[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+dct[j].sex+'_'+humOrrat[0:3]+'_'+dct[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NHE1':
                solute_id,fluxs=NHE1.NHE1(dct[j],memb_id,dct[j].trans[i].act,dct[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+dct[j].sex+'_'+humOrrat[0:3]+'_'+dct[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NKCC1':
                solute_id,fluxs=NKCC.nkcc1(dct[j],memb_id,dct[j].trans[i].act,delmu)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+dct[j].sex+'_'+humOrrat[0:3]+'_'+dct[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            else:
                raise Exception('What is this?',transporter_type)
    print('%s DCT finished.'%(sup_or_jux))
    print('\n')
    #========================================================
    # Connecting tubule
    #========================================================
    print('%s CNT start' %(sup_or_jux))
    NCNT = 200
    if sex == 'Male':
        filename = './datafiles/CNTparams_M_'+humOrrat[0:3]+'.dat'
    elif sex == 'Female':
        filename = './datafiles/CNTparams_F_'+humOrrat[0:3]+'.dat'
    else:
        filename ='./datafiles/CNTparams_F_'+humOrrat[0:3]+'.dat'
    cnt=compute(NCNT,filename,'Newton',sup_or_jux,diabete,humOrrat,sup_or_multi,inhib,unx = unx)
    #========================================================
    # output CNT Concentrations in Lumen and Cell
    #========================================================
    for i in range(NS):
        file=open('./'+file_to_save+'/'+cnt[0].sex+'_'+humOrrat[0:3]+'_cnt_con_of_'+solute[i]+'_in_Lumen_'+sup_or_jux+'.txt','w')
        for j in range(NCNT):
            file.write(str(cnt[j].conc[i,0])+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+cnt[0].sex+'_'+humOrrat[0:3]+'_cnt_con_of_'+solute[i]+'_in_Cell_'+sup_or_jux+'.txt','w')
        for j in range(NCNT):
            file.write(str(cnt[j].conc[i,1])+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+cnt[0].sex+'_'+humOrrat[0:3]+'_cnt_con_of_'+solute[i]+'_in_Bath_'+sup_or_jux+'.txt','w')
        for j in range(NCNT):
            file.write(str(cnt[j].conc[i,5])+'\n')
        file.close()
    #========================================================
    # output CNT Water volume in Lumen and Cell
    #========================================================
    file=open('./'+file_to_save+'/'+cnt[0].sex+'_'+humOrrat[0:3]+'_cnt_water_volume_in_Lumen_'+sup_or_jux+'.txt','w')
    for j in range(NCNT):
        file.write(str(cnt[j].vol[0]*cw)+'\n')
    file.close()
    file=open('./'+file_to_save+'/'+cnt[0].sex+'_'+humOrrat[0:3]+'_cnt_water_volume_in_Cell_'+sup_or_jux+'.txt','w')
    for j in range(NCNT):
        file.write(str(cnt[j].vol[1]*cw)+'\n')
    file.close()
    #========================================================
    # output CNT solute flows in Lumen and Cell
    #========================================================
    for i in range(NS):
        file=open('./'+file_to_save+'/'+cnt[0].sex+'_'+humOrrat[0:3]+'_cnt_flow_of_'+solute[i]+'_in_Lumen_'+sup_or_jux+'.txt','w')
        for j in range(NCNT):
            file.write(str(cnt[j].conc[i,0]*cnt[j].vol[0]*cw)+'\n')
        file.close()
    for i in range(NS):
        file=open('./'+file_to_save+'/'+cnt[0].sex+'_'+humOrrat[0:3]+'_cnt_flow_of_'+solute[i]+'_in_Cell_'+sup_or_jux+'.txt','w')
        for j in range(NCNT):
            file.write(str(cnt[j].conc[i,1]*cnt[j].vol[1]*cw)+'\n')
        file.close()
    #========================================================
    # output CNT osmolality in Lumen, Cell, LIS, Bath
    #========================================================
    file_lumen = open('./'+file_to_save+'/'+cnt[0].sex+'_'+humOrrat[0:3]+'_'+cnt[0].segment+'_osmolality_in_Lumen_'+sup_or_jux+'.txt','w')
    file_cell = open('./'+file_to_save+'/'+cnt[0].sex+'_'+humOrrat[0:3]+'_'+cnt[0].segment+'_osmolality_in_Cell_'+sup_or_jux+'.txt','w')
    file_lis = open('./'+file_to_save+'/'+cnt[0].sex+'_'+humOrrat[0:3]+'_'+cnt[0].segment+'_osmolality_in_LIS_'+sup_or_jux+'.txt','w')
    file_bath = open('./'+file_to_save+'/'+cnt[0].sex+'_'+humOrrat[0:3]+'_'+cnt[0].segment+'_osmolality_in_Bath_'+sup_or_jux+'.txt','w')
    for j in range(NCNT):
        osm_l = 0
        osm_c = 0
        osm_lis = 0
        osm_b = 0
        for i in range(NS):
            osm_l = osm_l +cnt[j].conc[i,0]
            osm_c = osm_c +cnt[j].conc[i,1]
            osm_lis = osm_lis+cnt[j].conc[i,4]
            osm_b = osm_b +cnt[j].conc[i,5]

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
    file=open('./'+file_to_save+'/'+cnt[0].sex+'_'+humOrrat[0:3]+'_'+cnt[0].segment+'_pressure_in_Lumen_'+sup_or_jux+'.txt','w')
    for j in range(NCNT):
        file.write(str(cnt[j].pres[0])+'\n')
    file.close()
    #========================================================
    # output fluxes through transporters
    #========================================================
    for j in range(NCNT):

        cnt[j].area[4][5] = 0.02*max(cnt[j].vol[4]/cnt[j].volref[4],1.0)
        cnt[j].area[5][4] = cnt[j].area[4][5]
        
        jvol = np.zeros([6,6])
        jsol = np.zeros([15,6,6])
        
        jvol,jsol = flux.compute_fluxes(cnt[j],j)

        file_Na_apical = open('./'+file_to_save+'/'+cnt[j].sex+'_'+humOrrat[0:3]+'_'+cnt[j].segment+'_apical_Na_'+sup_or_jux+'.txt','a')
        file_Na_apical.write(str(jsol[0,0,1])+'\n')

        file_Na_para = open('./'+file_to_save+'/'+cnt[j].sex+'_'+humOrrat[0:3]+'_'+cnt[j].segment+'_paracellular_Na_'+sup_or_jux+'.txt','a')
        file_Na_para.write(str(jsol[0,0,4])+'\n')
        
        jvol = np.zeros([6,6])
        jsol = np.zeros([15,6,6])

        jvol = water.compute_water_fluxes(cnt[j])
        jsol,delmu = electrochemical.compute_ecd_fluxes(cnt[j],jvol)
        for i in range(len(cnt[j].trans)):
            transporter_type = cnt[j].trans[i].type
            memb_id = cnt[j].trans[i].membrane_id

            if transporter_type == 'SGLT1':
                solute_id,fluxs = glucose.sglt1(cnt[j],cnt[j].ep,memb_id,cnt[j].trans[i].act,cnt[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+cnt[j].sex+'_'+humOrrat[0:3]+'_'+cnt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'SGLT2':
                solute_id,fluxs = glucose.sglt2(cnt[j],cnt[j].ep,memb_id,cnt[j].trans[i].act,cnt[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+cnt[j].sex+'_'+humOrrat[0:3]+'_'+cnt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'GLUT1':
                solute_id,fluxs=glucose.glut1(cnt[j],cnt[j].ep,memb_id,cnt[j].trans[i].act,cnt[j].area)
                for k in range(len([solute_id])):
                    file = open('./'+file_to_save+'/'+cnt[j].sex+'_'+humOrrat[0:3]+'_'+cnt[j].segment+'_'+transporter_type+'_'+solute[solute_id]+str(memb_id[0])+str(memb_id[1])+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs)+'\n')
            elif transporter_type == 'GLUT2':
                solute_id,fluxs=glucose.glut2(cnt[j],cnt[j].ep,memb_id,cnt[j].trans[i].act,cnt[j].area)
                for k in range(len([solute_id])):
                    file = open('./'+file_to_save+'/'+cnt[j].sex+'_'+humOrrat[0:3]+'_'+cnt[j].segment+'_'+transporter_type+'_'+solute[solute_id]+str(memb_id[0])+str(memb_id[1])+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs)+'\n')			
            elif transporter_type == 'NHE3':
                solute_id,fluxs=NHE3.nhe3(cnt[j],cnt[j].ep,memb_id,cnt[j].trans[i].act,cnt[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+cnt[j].sex+'_'+humOrrat[0:3]+'_'+cnt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NaKATPase':
                solute_id,fluxs=ATPase.nakatpase(cnt[j],cnt[j].ep,memb_id,cnt[j].trans[i].act,cnt[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+cnt[j].sex+'_'+humOrrat[0:3]+'_'+cnt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+str(memb_id[0])+str(memb_id[1])+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')

            elif transporter_type == 'HATPase':
                solute_id,fluxs=ATPase.hatpase(cnt[j],cnt[j].ep,memb_id,cnt[j].trans[i].act,cnt[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+cnt[j].sex+'_'+humOrrat[0:3]+'_'+cnt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NKCC2A':
                solute_id,fluxs=NKCC.nkcc2(cnt[j],memb_id,cnt[j].trans[i].act,cnt[j].area,'A')
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+cnt[j].sex+'_'+humOrrat[0:3]+'_'+cnt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NKCC2B':
                solute_id,fluxs=NKCC.nkcc2(cnt[j],memb_id,cnt[j].trans[i].act,cnt[j].area,'B')
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+cnt[j].sex+'_'+humOrrat[0:3]+'_'+cnt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NKCC2F':
                solute_id,fluxs=NKCC.nkcc2(cnt[j],memb_id,cnt[j].trans[i].act,cnt[j].area,'F')
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+cnt[j].sex+'_'+humOrrat[0:3]+'_'+cnt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')       
            elif transporter_type == 'KCC4':
                solute_id,fluxs=KCC.kcc4(cnt[j].conc,memb_id,cnt[j].trans[i].act,cnt[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+cnt[j].sex+'_'+humOrrat[0:3]+'_'+cnt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'ENaC':
                solute_id,fluxs=ENaC.ENaC(cnt[j],j,memb_id,cnt[j].trans[i].act,cnt[j].area,jvol)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+cnt[j].sex+'_'+humOrrat[0:3]+'_'+cnt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NCC':
                solute_id,fluxs=NCC.NCC(cnt[j],j,memb_id,cnt[j].trans[i].act,cnt[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+cnt[j].sex+'_'+humOrrat[0:3]+'_'+cnt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'Pendrin':
                solute_id,fluxs=Pendrin.Pendrin(cnt[j],memb_id,cnt[j].trans[i].act,cnt[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+cnt[j].sex+'_'+humOrrat[0:3]+'_'+cnt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type =='AE1':
                solute_id,fluxs=AE1.AE1(cnt[j],memb_id,cnt[j].trans[i].act,cnt[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+cnt[j].sex+'_'+humOrrat[0:3]+'_'+cnt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'HKATPase':
                solute_id,fluxs=ATPase.hkatpase(cnt[j],memb_id,cnt[j].trans[i].act,cnt[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+cnt[j].sex+'_'+humOrrat[0:3]+'_'+cnt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NHE1':
                solute_id,fluxs=NHE1.NHE1(cnt[j],memb_id,cnt[j].trans[i].act,cnt[j].area)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+cnt[j].sex+'_'+humOrrat[0:3]+'_'+cnt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            elif transporter_type == 'NKCC1':
                solute_id,fluxs=NKCC.nkcc1(cnt[j],memb_id,cnt[j].trans[i].act,delmu)
                for k in range(len(solute_id)):
                    file = open('./'+file_to_save+'/'+cnt[j].sex+'_'+humOrrat[0:3]+'_'+cnt[j].segment+'_'+transporter_type+'_'+solute[solute_id[k]]+'_'+sup_or_jux+'.txt','a')
                    file.write(str(fluxs[k])+'\n')
            else:
                raise Exception('What is this?',transporter_type)
    print('%s CNT finished.'%(sup_or_jux))
    print(sup_or_jux+' finished.')
    print('\n')