import numpy as np 
import chunk
import math

#Load both packets as an array
with open('packet_base.txt','r') as file:
    packet_base = file.readlines()
    packet_base = [line.strip() for line in packet_base]
       
with open('packet_weight.txt','r') as file:
    packet_weight=file.readlines()
    packet_weight= [line.strip() for line in packet_weight]
    
#combining those files as combined_data
combined_data= np.concatenate((packet_base,packet_weight))

#Seperate your data chunks into 8
chunked_data= np.array_split(combined_data,8)

#multiply your base by your weight for every element
multiplied_array= packet_base * packet_weight

# For each chunk, find your min,max,mean// result will be (max-mean) * min
chunk_results = []
chunk_min = np.min(chunk)
chunk_max = np.max(chunk)
chunk_mean = np.mean(chunk)
chunk_result = (chunk_max - chunk_mean)*chunk_min
chunk_results.append(chunk_result)

#Find the sum and round down to the next integer
total_sum=sum(chunk_results)
rounded_sum=math.floor(total_sum)

#Find the remainder if you divide by 4096
remainder=rounded_sum % 4096

print(remainder)
