import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame
from collections import Counter 

from pylab import plot, show, savefig, xlim, figure, \
                 ylim, legend, boxplot, setp, axes


 
def unique(list1):
 
    # initialize a null list
    unique_list = []
 
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    return unique_list

allNums = []
total = []
source_node = []
dest_node = []
receive_time = []
seq_number = []
generation_time = []
network_PDR = []
network_latency1 = []
network_latency2 = []
network_latency3 = []
network_latency4 = []

network_burst_packet_loss1 = []
network_burst_packet_loss2 = []
network_burst_packet_loss3 = []
network_burst_packet_loss4 = []



node = []
nodes = []
latency1 = []
latency2 = []
latency3 = []
latency4 = []

seq1 = []
seq2 = []
seq3 = []
seq4 = []



nodes_PDR1 = []
nodes_PDR2 = []
nodes_PDR3 = []
nodes_PDR4 = []

nodes_PDR1 = []
nodes_PDR2 = []
nodes_PDR3 = []
nodes_PDR4 = []


source = []

burst_packet_loss1 = []
burst_packet_loss2 = []
burst_packet_loss3 = []
burst_packet_loss4 = []

burst_packet_loss_mean1 = []
burst_packet_loss_mean2 = []
burst_packet_loss_mean3 = []
burst_packet_loss_mean4 = []

burst_packet_loss_all1 = []
burst_packet_loss_all2 = []
burst_packet_loss_all3 = []
burst_packet_loss_all4 = []



all_latency1 = []
all_latency2 = []
all_latency3 = []
all_latency4 = []
network_PDR_mean = []
all_latency1_mean = []
all_latency2_mean = []
all_latency3_mean = []
all_latency4_mean = []
NUMBER_NODES = 49
relay_node = 1  # number of nodes that do not generate any packet
ax = axes()
# the maximum sequence number for each node is required for calculating PDR
max_seq = [0 for x in range(NUMBER_NODES)] 
# reading the network_detail log file and saving it in the total array
with open('network_detail'+'.log', "r+") as f:
    data = f.readlines()
    for line in data:
        allNums += line.strip().split("    ")
    for num in allNums:
        if num == '':
            continue
        else:
            total.append(float(num))
# saving the maximum sequence number for each node



for i_m in range(NUMBER_NODES):
    max_seq[NUMBER_NODES-i_m-1] = total[len(total)-1]
    total.pop(len(total)-1)



for i in range(0, len(total), 5):
    source_node.append(total[i])

for i1 in range(2, len(total), 5):
    receive_time.append(total[i1])

for i2 in range(3, len(total), 5):
    seq_number.append(total[i2])

for i3 in range(4, len(total), 5):
    generation_time.append(total[i3])

for i4 in range(1, len(total), 5):
    dest_node.append(total[i4])
    
dests =  unique(dest_node)   
dest1 = dests[0]
dest2 = dests[1]
dest3 = dests[2]
dest4 = dests[3]

total = []
j = 0
# adding source node, receiving time, sequence number, and generation time to the node array,
# index of the array is node number
while j < NUMBER_NODES:
    for i5 in range(len(source_node)):
        if source_node[i5] == j:
            node.append([source_node[i5], generation_time[i5], receive_time[i5], seq_number[i5], dest_node[i5]])
    nodes.append(node)
    node = []
    j += 1

# calculating latency 
for s in range(NUMBER_NODES):
    
    for d in range(len(nodes[s])):
        
        if (nodes[s][d][4]==dest1):
            latency1.append(nodes[s][d][2]-nodes[s][d][1])  # receive time - generation time
            
        if (nodes[s][d][4]==dest2):
            latency2.append(nodes[s][d][2]-nodes[s][d][1])  # receive time - generation 
        
        if (nodes[s][d][4]==dest3):
            latency3.append(nodes[s][d][2]-nodes[s][d][1])  # receive time - generation time
            
        if (nodes[s][d][4]==dest4):
            latency4.append(nodes[s][d][2]-nodes[s][d][1])  # receive time - generation time
      
    
    
    if len(latency1) == 0:
        latency1.append(0)
    all_latency1.append(latency1)
    if np.mean(latency1) > 0:
        all_latency1_mean.append(np.mean(latency1))
    else:
        all_latency1_mean.append(0)
            
    
    if len(latency2) == 0:
        latency2.append(0)
    all_latency2.append(latency2)
    if np.mean(latency1) > 0:
        all_latency2_mean.append(np.mean(latency2))
    else:
        all_latency2_mean.append(0)
    
    
    if len(latency3) == 0:
        latency3.append(0)
    all_latency3.append(latency3)
    if np.mean(latency3) > 0:
        all_latency3_mean.append(np.mean(latency3))
    else:
        all_latency3_mean.append(0)
    
    
    if len(latency4) == 0:
        latency4.append(0)
    all_latency4.append(latency4)
    if np.mean(latency1) > 0:
        all_latency4_mean.append(np.mean(latency4))
    else:
        all_latency4_mean.append(0)
    
    latency1 = []
    latency2 = []
    latency3 = []
    latency4 = []



# the boxplot figure of the mean of the nodes' Latency
# destination 1
network_latency1.append(all_latency1_mean)
df1 = DataFrame(network_latency1)
df1 = df1.T
df1.plot.box(patch_artist=True)
plt.xlabel("network", fontsize=10)
plt.ylabel("latency (ms)", fontsize=10)
plt.savefig('latency_boxplot_destination1.pdf', dpi=200)

# the boxplots figure of the nodes' Latency
# destination 1
df2 = DataFrame(all_latency1)
df2.fillna(0, inplace = True)
df2 = df2.T
df2.plot.box(patch_artist=True, figsize=(10,7))
plt.xlabel("Node Number", fontsize=5)
plt.ylabel("Latency (ms)", fontsize=10)
plt.savefig('latency1.pdf', dpi=200)

# destination 2
network_latency2.append(all_latency2_mean)
df3 = DataFrame(network_latency2)
df3 = df3.T
df3.plot.box(patch_artist=True)
plt.xlabel("network", fontsize=10)
plt.ylabel("latency (ms)", fontsize=10)
plt.savefig('latency_boxplot_destination2.pdf', dpi=200)

# the boxplots figure of the nodes' Latency
# destination 2
df4 = DataFrame(all_latency2)
df4.fillna(0, inplace = True)
df4 = df4.T
df4.plot.box(patch_artist=True, figsize=(10,7))
plt.xlabel("Node Number", fontsize=5)
plt.ylabel("Latency (ms)", fontsize=10)
plt.savefig('latency2.pdf', dpi=200)

# destination 3
network_latency3.append(all_latency3_mean)
df5 = DataFrame(network_latency3)
df5 = df5.T
df5.plot.box(patch_artist=True)
plt.xlabel("network", fontsize=10)
plt.ylabel("latency (ms)", fontsize=10)
plt.savefig('latency_boxplot_destination3.pdf', dpi=200)

# the boxplots figure of the nodes' Latency
# destination 4
df6 = DataFrame(all_latency3)
df6.fillna(0, inplace = True)
df6 = df6.T
df6.plot.box(patch_artist=True, figsize=(10,7))
plt.xlabel("Node Number", fontsize=5)
plt.ylabel("Latency (ms)", fontsize=10)
plt.savefig('latency3.pdf', dpi=200)


# destination 4
network_latency4.append(all_latency4_mean)
df7 = DataFrame(network_latency4)
df7 = df7.T
df7.plot.box(patch_artist=True)
plt.xlabel("network", fontsize=10)
plt.ylabel("latency (ms)", fontsize=10)
plt.savefig('latency_boxplot_destination4.pdf', dpi=200)

# the boxplots figure of the nodes' Latency
# destination 4
df8 = DataFrame(all_latency4)
df8.fillna(0, inplace = True)
df8 = df8.T
df8.plot.box(patch_artist=True, figsize=(10,7))
plt.xlabel("Node Number", fontsize=5)
plt.ylabel("Latency (ms)", fontsize=10)
plt.savefig('latency4.pdf', dpi=200)



# calculating burst packet loss
for s1 in range(NUMBER_NODES):
    for d1 in range(len(nodes[s1])):
  
        if (nodes[s1][d1][4]==dest1):
            seq1.append(nodes[s1][d1][3])
            if d1 >= (len((nodes[s1]))-1):
                burst_packet_loss1.append(0)
            else:
                burst_packet_loss1.append((nodes[s1][d1+1][3]-nodes[s1][d1][3])-1) # sequence number (n+1) - sequence number (n)
        
        if (nodes[s1][d1][4]==dest2):
            seq2.append(nodes[s1][d1][3])
            if d1 >= (len((nodes[s1]))-1):
                burst_packet_loss2.append(0)
            else:
                burst_packet_loss2.append((nodes[s1][d1+1][3]-nodes[s1][d1][3])-1) # sequence number (n+1) - sequence number (n)
        
        if (nodes[s1][d1][4]==dest3):
            seq3.append(nodes[s1][d1][3])
            if d1 >= (len((nodes[s1]))-1):
                burst_packet_loss3.append(0)
            else:
                burst_packet_loss3.append((nodes[s1][d1+1][3]-nodes[s1][d1][3])-1) # sequence number (n+1) - sequence number (n)
        
        if (nodes[s1][d1][4]==dest4):
            seq4.append(nodes[s1][d1][3])
            if d1 >= (len((nodes[s1]))-1):
                burst_packet_loss4.append(0)
            else:
                burst_packet_loss4.append((nodes[s1][d1+1][3]-nodes[s1][d1][3])-1) # sequence number (n+1) - sequence number (n)
        
                          
    if len(burst_packet_loss1) == 0:
        burst_packet_loss1.append(0)
    burst_packet_loss_all1.append(burst_packet_loss1)
    # calculating the mean of burst packet loss
    if np.mean(burst_packet_loss1) > 0:
        burst_packet_loss_mean1.append(np.mean(burst_packet_loss1))
    else:
        burst_packet_loss_mean1.append(0)
    # calculating PDR 
    if max_seq[s1] != 0:
        PDR1 = (len(Counter(seq1).keys())/max_seq[s1]) * 100
    else:
        PDR1 = 0
    nodes_PDR1.append(PDR1)
    seq1 = []
    burst_packet_loss1 = []
    
    if len(burst_packet_loss2) == 0:
        burst_packet_loss2.append(0)
    burst_packet_loss_all2.append(burst_packet_loss2)
    # calculating the mean of burst packet loss
    if np.mean(burst_packet_loss2) > 0:
        burst_packet_loss_mean2.append(np.mean(burst_packet_loss2))
    else:
        burst_packet_loss_mean2.append(0)
    # calculating PDR 
    if max_seq[s1] != 0:
        PDR2 = (len(Counter(seq2).keys())/max_seq[s1]) * 100
    else:
        PDR2 = 0
    nodes_PDR2.append(PDR2)
    seq2 = []
    burst_packet_loss2 = []
    
    
    if len(burst_packet_loss3) == 0:
        burst_packet_loss3.append(0)
    burst_packet_loss_all3.append(burst_packet_loss3)
    # calculating the mean of burst packet loss
    if np.mean(burst_packet_loss3) > 0:
        burst_packet_loss_mean3.append(np.mean(burst_packet_loss3))
    else:
        burst_packet_loss_mean3.append(0)
    # calculating PDR 
    if max_seq[s1] != 0:
        PDR3 = (len(Counter(seq3).keys())/max_seq[s1]) * 100
    else:
        PDR3 = 0
    nodes_PDR3.append(PDR3)
    seq3 = []
    burst_packet_loss3 = []
    
    
    
    if len(burst_packet_loss4) == 0:
        burst_packet_loss4.append(0)
    burst_packet_loss_all4.append(burst_packet_loss4)
    # calculating the mean of burst packet loss
    if np.mean(burst_packet_loss4) > 0:
        burst_packet_loss_mean4.append(np.mean(burst_packet_loss4))
    else:
        burst_packet_loss_mean4.append(0)
    # calculating PDR 
    if max_seq[s1] != 0:
        PDR4 = (len(Counter(seq4).keys())/max_seq[s1]) * 100
    else:
        PDR4 = 0
    nodes_PDR4.append(PDR4)
    seq4 = []
    burst_packet_loss4 = []
  
    
  




# the figure of the nodes' PDR
# destination 1
df9 = DataFrame(nodes_PDR1)
df9.plot(kind='bar')
plt.xlabel("Node Number", fontsize=10)
plt.ylabel("PDR", fontsize=10)
plt.savefig('PDR1.pdf', dpi=200)
print("-----------------destination1-------------------------")
print("nodes PDR1 ", nodes_PDR1)
print("------------------------------------------")
print("average latency in each node", all_latency1_mean)


# the figure of the nodes' PDR
# destination 2
df10 = DataFrame(nodes_PDR2)
df10.plot(kind='bar')
plt.xlabel("Node Number", fontsize=10)
plt.ylabel("PDR", fontsize=10)
plt.savefig('PDR2.pdf', dpi=200)
print("-----------------destination2-------------------------")
print("nodes PDR2 ", nodes_PDR2)
print("------------------------------------------")
print("average latency in each node", all_latency2_mean)


# the figure of the nodes' PDR
# destination 3
df11 = DataFrame(nodes_PDR3)
df11.plot(kind='bar')
plt.xlabel("Node Number", fontsize=10)
plt.ylabel("PDR", fontsize=10)
plt.savefig('PDR3.pdf', dpi=200)
print("-------------------destination3-----------------------")
print("nodes PDR3 ", nodes_PDR3)
print("------------------------------------------")
print("average latency in each node", all_latency3_mean)



# the figure of the nodes' PDR
# destination 4
df12 = DataFrame(nodes_PDR4)
df12.plot(kind='bar')
plt.xlabel("Node Number", fontsize=10)
plt.ylabel("PDR", fontsize=10)
plt.savefig('PDR4.pdf', dpi=200)
print("------------------destination4------------------------")
print("nodes PDR4 ", nodes_PDR4)
print("------------------------------------------")
print("average latency in each node", all_latency4_mean)




#--------------------------------------------------------------------------------------------------------------------

voltage = 3  # V
C_tx = 8.45  # mA
C_rx = 13.9
C_sw = 3.66
C_sleep = 0.015
NUMBER_NODES = 50
relay_node = 1
allNums = []
total = []
scan_time = []
switch_time = []
sleep_time = []
transmit_time = []
scan_energy = []
sleep_energy = []
switch_energy = []
transmit_energy = []
# reading the energy log file and saving it in the total array
with open('energy.log', "r+") as f:
    data = f.readlines()
    for line in data:
        allNums += line.strip().split("   ")
    for num in allNums:
        if num == '':
            continue
        else:
            total.append(float(num))
# saving the scan time, switch time, and transmit time in the separated arrays
# calculating scan energy, switch energy and transmit energy

for i in range(1, len(total), 5):
    scan_time.append(total[i])
    scan_energy.append(total[i] * (C_rx * voltage)/1000)

dfs = DataFrame(scan_energy)
dfs.plot(kind='bar')
plt.xlabel("Node Number", fontsize=10)
plt.ylabel("Scanning Energy (mJ)", fontsize=10)
plt.savefig('scan_energy.pdf', dpi=200)
print("---------------------------------------")
print("scanning energy in each node", scan_energy)

for i1 in range(2, len(total), 5):
    switch_time.append(total[i1])
    switch_energy.append(total[i1]*(C_sw * voltage)/1000)
print("---------------------------------------")
print("switching energy in each node", switch_energy)

df_sw = DataFrame(switch_energy)
df_sw.plot(kind='bar')
plt.xlabel("Node Number", fontsize=10)
plt.ylabel("Switching Energy (mJ)", fontsize=10)
plt.savefig('switch_energy.pdf', dpi=200)

for i2 in range(3, len(total), 5):
    transmit_time.append(total[i2])
    transmit_energy.append(total[i2]*(C_tx * voltage)/1000)
print("---------------------------------------")
print("transmitting energy in each node", transmit_energy)

df_t = DataFrame(transmit_energy)
df_t.plot(kind='bar')
plt.xlabel("Node Number", fontsize=10)
plt.ylabel("Transmitting Energy (mJ)", fontsize=10)
plt.savefig('transmit_energy.pdf', dpi=200)

for i3 in range(4, len(total), 5):
    sleep_time.append(total[i3])
    sleep_energy.append(round(total[i3] * (C_sleep * voltage)/1000, 4))
print("---------------------------------------")
print("sleeping energy in each node", sleep_energy)

df_sl = DataFrame(sleep_energy)
df_sl.plot(kind='bar')
plt.xlabel("Node Number", fontsize=10)
plt.ylabel("Sleeping Energy (mJ)", fontsize=10)
plt.savefig('sleep_energy.pdf', dpi=200)


# calculating the network energy consumption
total_energy = [scan_energy[en1] + transmit_energy[en1] + switch_energy[en1] + sleep_energy[en1]
                for en1 in range(len(scan_energy))]
print("---------------------------------------")
print("total energy in each node", total_energy)

df_total = DataFrame(total_energy)
df_total.plot(kind='bar')
plt.xlabel("Node Number", fontsize=10)
plt.ylabel("Total Energy (mJ)", fontsize=10)
plt.savefig('total_energy.pdf', dpi=200)

network_energy = sum(scan_energy) + sum(transmit_energy) + sum(switch_energy) + sum(sleep_energy)

print("---------------------------------------")
print("network energy consumption (mJ)", network_energy)
