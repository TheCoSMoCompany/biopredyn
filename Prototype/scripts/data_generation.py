#!/usr/bin/env python
# coding=utf-8

from biopredyn import resources, workflow, result as res
import csv

# input values required for data generation
simulation_file = 'generate_data.xml'
noise = 'heteroscedastic'
std = 0.1 # experimental data standard deviation
data_file = 'artificial_data.txt'
calibration_file = 'calibration_data.txt'
validation_file = 'validation_data.txt'

rm = resources.ResourceManager()
wf = workflow.WorkFlow(rm, source=simulation_file)

wf.get_tasks()[0].set_tool('copasi') # choosing COPASI as simulation engine
wf.get_tasks()[1].run(True) # applying changes and running the simulation

report = wf.get_outputs()[0] # processing output with noise
report.write_as_csv(data_file, artificial=True, noise_type=noise, std_dev=std)

# splitting generated data set into two smaller sets
data = res.TimeSeries()
metabolites = data.import_from_csv_file(data_file, rm)
num_exp = 0
for m in metabolites:
  n = data.get_num_experiments(m)
  if n > num_exp:
    num_exp = n

cal = open(calibration_file, "w")
cal_writer = csv.writer(cal, delimiter=',')
cal_writer.writerow(metabolites)
val = open(validation_file, "w")
val_writer = csv.writer(val, delimiter=',')
val_writer.writerow(metabolites)

for l in range(len(data.get_time_steps())):
  for e in range(num_exp):
    row = []
    for m in metabolites:
      if (str.lower(m).__contains__('time')):
        row.append(data.get_quantities_per_species(m)[l])
      else:
        row.append(data.get_quantities_per_species(m)[l][e])
    if (l+e)%2 == 0: # even case
      cal_writer.writerow(row)
    else: # odd case
      val_writer.writerow(row)

cal.close()
val.close()
