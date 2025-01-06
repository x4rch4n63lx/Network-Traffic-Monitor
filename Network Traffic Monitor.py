# ===================================================================================
# Created By     : x_4rch4n63l_x
# Created On     : 10/23/2024 - 4:20PM 
# Script Purpose : Network Traffic Monitor coded in Python using psutil
# Description    : This script provides real-time monitoring of network traffic, specifically:
#                  1. Displays download and upload rates in Mbps.
#                  2. Updates network statistics every second.
#                  3. Formats and prints network traffic data in a user-friendly manner.
#
# Features       : 
#                  - Real-time network traffic monitoring.
#                  - Clear display of download and upload speeds.
#                  - Continuous update of network statistics for precise monitoring.
#
# Requirements   :
#                  - Install the psutil library using: pip install psutil
# ===================================================================================
import psutil
import time

def convert_to_mbps(bytes):
    return bytes / 1024 / 1024 * 8  

def main():
    interval = 1  
    print(f"{'Time':<20} {'Download (Mbps)':<20} {'Upload (Mbps)':<20}")
    
    while True:
        
        net_io_start = psutil.net_io_counters()
        
        
        time.sleep(interval)
        
        
        net_io_end = psutil.net_io_counters()
        
        
        download_rate = convert_to_mbps(net_io_end.bytes_recv - net_io_start.bytes_recv) / interval
        upload_rate = convert_to_mbps(net_io_end.bytes_sent - net_io_start.bytes_sent) / interval
        
        # Get the current time
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
        
        
        print(f"{current_time:<20} {download_rate:<20.2f} {upload_rate:<20.2f}")

if __name__ == '__main__':
    main()
