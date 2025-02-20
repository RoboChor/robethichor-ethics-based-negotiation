import re
import numpy as np

def extract_ping_times(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    
    ping_times = []
    
    pattern = re.compile(r'time=([\d\.]+) ms')
    for line in data:
        match = pattern.search(line)
        if match:
            ping_times.append(float(match.group(1)))
    
    return ping_times

def compute_statistics(ping_times):
    if not ping_times:
        return None
    
    min_time = np.min(ping_times)
    max_time = np.max(ping_times)
    avg_time = np.mean(ping_times)
    std_dev = np.std(ping_times)
    
    return min_time, avg_time, max_time, std_dev

filename = '../results/ping_results.txt'
ping_times = extract_ping_times(filename)

if ping_times:
    min_time, avg_time, max_time, std_dev = compute_statistics(ping_times)
    print(f"Min: {min_time:.3f} ms, Avg: {avg_time:.3f} ms, Max: {max_time:.3f} ms, Std Dev: {std_dev:.3f} ms")
else:
    print("Nessun valore di ping trovato.")