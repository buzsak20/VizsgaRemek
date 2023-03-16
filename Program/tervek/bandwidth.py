import psutil
import time

# Define the interval between data samples (in seconds)
interval = 3

# Define the network interface you want to monitor (e.g., "eth0" or "wlan0")
network_interface = "Lan" #eth0

# Define the hosts you want to monitor (e.g., ["192.168.1.1", "192.168.1.2"])
hosts = ["172.16.16.40", "172.16.16.246"]

# Define a dictionary to store the previous network usage data for each host
previous_data = {}

while True:
    # Get the current network usage data for the specified interface
    current_data = psutil.net_io_counters(pernic=True)[network_interface]
    
    # Iterate over each host and calculate the network usage since the last sample
    for host in hosts:
        if host not in previous_data:
            # If there is no previous data, skip this host for now
            continue
            
        # Get the previous network usage data for this host
        previous_bytes_sent, previous_bytes_received = previous_data[host]
        
        # Get the current network usage data for this host
        current_bytes_sent, current_bytes_received = current_data.packets_sent, current_data.packets_recv
        
        # Calculate the network usage since the last sample for this host
        bytes_sent = current_bytes_sent - previous_bytes_sent
        bytes_received = current_bytes_received - previous_bytes_received
        
        # Print the network usage data for this host
        print(f"Host: {host} | Bytes sent: {bytes_sent} | Bytes received: {bytes_received}")
    
    # Store the current network usage data for each host as the previous data for the next sample
    for host in hosts:
        previous_data[host] = (current_data.packets_sent, current_data.packets_recv)
    
    # Wait for the specified interval before taking the next sample
    time.sleep(interval)
