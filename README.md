GUI for Radiotherapy facility primary walls Shielding calculations
Introduction 

This is a simple GUI program for calculating the required thickness for primary walls in a radiotherapy facility. Primary barriers or walls are defined as the walls directly facing the beam. They are designed to attenuate the photon beam emanating from the treatment unit that is directly incident on the barrier. All definitions and calculations in this program are done based on NRCP-151 document. The general formula to calculate the transmission factor of the primary barrier (B pri) that will reduce the radiation field to an acceptable level is as shown below  
 

P = shielding design goal (expressed as dose equivalent) beyond the barrier and is usually given for a weekly time frame (Sv/ week).  

dpri = distance from the x-ray target to the point protected (meters) 

W = workload or photon absorbed dose delivered at 1 m from the x-ray target per week (Gy/week) 

U = use factor or fraction of the workload that the primary beam is directed at the barrier in question 

T = occupancy factor for the protected location or fraction of the workweek that a person is present beyond the barrier. 

 

The barrier thickness required is then calculated based on material used by the user using TVL tables (table B.2) given in NCRP-151 for each material using the formula. 

Entry Widgets 

The GUI has two entry boxes for workload(W) and Distance (dpri ) with units mentioned. 

There are drop downs for selecting Energy (4 MV,6 MV, 10 MV). This is later used for TVL calculations. 

Area Type drop down gives two choices (controlled area and uncontrolled area) these areas and the recommended dose limits (P) are given in the NCRP-151. Dose limits used for controlled area and uncontrolled area are 5mSv/year and 1mSv/year, respectively. 

Use factor drop down uses values based on table 3.1 NCRP-151 for roof wall (180°), Lateral Walls (90°,270°), floor wall (0°). 

Occupancy factors drop down gives the user option of six values which can be selected based on table B.1. 

Material Drop down gives three options (Concrete, lead, steel) as TVL values of only these materials were provided in the document. 

Buttons 

CALCULATE: once all values are selected and entered, the user must click the calculate button. Every time the user changes any entry value, they must click on calculate again.  

Clear: it clears all selections and entries. The user is recommended to use the clear button before new calculations to avoid error. 

Exit Program: it exits the program. 
Thanks. 
