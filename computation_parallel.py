# This file is used to check individiual segment for the multiple nephron model
# runs the superficial and jux1 - jux5 nephrons
# type 'python3 computation_parallel.py' in the terminal to run
# requires outlet files from previous simulation

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
import argparse

solute = ['Na','K','Cl','HCO3','H2CO3','CO2','HPO4','H2PO4','urea','NH3','NH4','H','HCO2','H2CO2','glu']
compart = ['Lumen','Cell','ICA','ICB','LIS','Bath']
cw=Vref*60e6

parser=argparse.ArgumentParser()
# required input
parser.add_argument('--sex',choices=['Male','Female'],required = True,type = str,help = 'Sex')
parser.add_argument('--species',choices=['human','rat', 'mouse'],required = True,type = str, help = 'human, rat or mouse model')
parser.add_argument('--segment', choices = ['PT','S3','SDL', 'LDL', 'LAL', 'mTAL','cTAL','DCT', 'CNT', 'CCD', 'OMCD', 'IMCD'], required=True, type=str, help = 'choose segment')
parser.add_argument('--savefile', required=True, type=str, help = 'where to save?')

# optional input
# diabetic options
parser.add_argument('--diabetes',choices = ['Severe','Moderate'],default='Non',type=str,help='diabete status (Severe/Moderate)')
parser.add_argument('--inhibition',choices=['ACE','SGLT2','NHE3-50','NHE3-80','NKCC2-70','NKCC2-100','NCC-70','NCC-100','ENaC-70','ENaC-100','SNB-70','SNB-100'],default = None,type = str,help = 'any transporter inhibition?')
parser.add_argument('--unx',choices=['N','Y'],default = 'N',type = str,help = 'uninephrectomy status')
# pregnancy option
parser.add_argument('--pregnant', choices=['mid','late'], default='non', type=str, help='pregnant female? (mid/late)')

args=parser.parse_args()

sex = args.sex
humOrrat = args.species
sup_or_multi = args.type
segment = args.segment

if segment[-2:] == 'CD':
    print('segment: ' + segment)
    raise Exception('use computation.py for CD segments')

diabete = args.diabetes
inhib = args.inhibition
unx = args.unx

preg = args.pregnant

if segment == 'PT':
    N = 176
elif segment == 'S3':
    N = 25
else:
    N = 200

file_to_save = args.savefile
if os.path.isdir(file_to_save) == False:
    os.makedirs(file_to_save)

if sex == 'Male':
	filename='./datafiles/'+segment+'params_M_'+humOrrat[0:3]+'.dat'
elif sex == 'Female':
	filename='./datafiles/'+segment+'params_F_'+humOrrat[0:3]+'.dat'
else:
	print('sex: ' + sex)
	raise Exception('must be male or female')