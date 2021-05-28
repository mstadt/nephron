This is latest version of sex-specific mathematical models implemented in Python. To speed up the computation time, paralle computation of different types of nephron is implemented. To run the paralle simulation code:

Use commend: **Python3 paralle_simulate.py --sex [option] --species [option] --type [option] --diabetes [option] --inhibition [option]**

The options here are:

sex: **Male, Female**;

species: **human, rat**;

type: **superficial, multiple**;

diabetes: **Severe, Moderate, Non**;

inhibition: **ACE, SGLT2, NHE3-50, NHE3-80, NKCC2-70, NKCC2-100, NCC-70, NCC-100, ENaC-70, ENaC-100, SNB-70, SNB-100**.

Human only have ACE and SGLT2 inhibition cases. The others are for rats.

The Way to understand output files:

All the output files' names are in following structure: 'sex_species_segment_concentration/flow_of_solute_in_compartment.txt'. 

Here is an example: female_rat_ccd_con_of_Cl_in_Bath.txt. It contains interstitial concentration of Chloride along cortical collecting duct in female rat.

Another example: male_hum_pt_flow_of_Na_in_Lumen.txt. It contains luminal flow of Sodium along proximal convolute tubule in male human.

These results are scaled per nephron.

The unit of concentration from outputs is **mmol/L (mM)**.

The unit of volume is **nl/min**.

The unit of flow is **pmol/min**.
