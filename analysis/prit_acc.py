import csv
import numpy as np
import sys
sys.path.append('../')

fields = ['iteration', "HIP", "MIP", "EM shower", "Delta rays", "Michel electron", "mean"]
with open('log/9/metrics_log-0000000.csv') as f:
    reader = csv.DictReader(f)
    acc = np.array([[np.float32(row[key]) for key in ['iteration']+[f"class_{i}_acc" for i in range(5)]+["acc"]] for row in reader])
    
mean = np.nanmean(acc,axis=0)
mean[1:]=mean[1:]*100
assert len(mean) == 7
print(f"mean accuracy over {len(acc)} events: ")
for i, label in enumerate(fields):
    print('%s\t%.1f'%(label,mean[i]))
with open('analysis/acc.csv', 'w') as f:
    writer = csv.DictWriter(f,fields)
    writer.writeheader()
    writer.writerow({fields[0]:'%.0f'%(mean[0]), 
                     fields[1]:'%.1f'%mean[1],
                     fields[2]:'%.1f'%mean[2],
                     fields[3]:'%.1f'%mean[3],
                     fields[4]:'%.1f'%mean[4],
                     fields[5]:'%.1f'%mean[5],
                     fields[6]:'%.1f'%mean[6]
                     })
    writer.writerow({fields[0]:'>30k', 
                     fields[1]:'%.1f'%96,
                     fields[2]:'%.1f'%96.2,
                     fields[3]:'%.1f'%97.6,
                     fields[4]:'%.1f'%74.3,
                     fields[5]:'%.1f'%36.5,
                     fields[6]:'%.1f'%98
                     })