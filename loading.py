import time  
import threading  

# Moon phase symbol list  
moon_phases = ['🌑', '🌒', '🌓', '🌔', '🌕', '🌘', '🌗', '🌖', '🌕']  

def update_moon_phase():  
    while True:  
        for phase in moon_phases:  
            # Use \r to return to the beginning of the line and overwrite content  
            print(f"\r{phase}", end='', flush=True)  
            time.sleep(0.5)  # Wait for 0.5 seconds  

# Start a new thread to update the moon phase  
thread = threading.Thread(target=update_moon_phase)  
thread.daemon = True  # Set the thread as a daemon, will exit when the main program exits  
thread.start()  

try:  
    while True:  
        time.sleep(1)  # Keep the main thread running  
except KeyboardInterrupt:  
    print("\nProgram has exited.")
