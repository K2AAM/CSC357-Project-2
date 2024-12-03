import socket
import time

# Define server IP, port, and userID
SERVER_IP = '75.69.29.126'
SERVER_PORT = 2956
USER_ID = 'amore020' 
MAX_RETRIES = 5

def udp_client():
    responses_received = 0
    retries = 0

    while responses_received < MAX_RETRIES:
        try:
            # Create a UDP socket
            udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            udp_socket.settimeout(5)  # Set timeout to 5 seconds

            # Send USER_ID to Dr. Kevin's Server
            print(f"Attempt {retries + 1}: Sending USER_ID '{USER_ID}' to server...")
            print(f"Sending raw bytes: {USER_ID.encode('utf-8')}")  
            udp_socket.sendto(USER_ID.encode('utf-8'), (SERVER_IP, SERVER_PORT))

            # Listen for the server to respond 
            response, server_address = udp_socket.recvfrom(2048)  
            print(f"Received raw bytes: {response}")  
            print(f"Received response from server: {response.decode('utf-8')}") 
            responses_received += 1 

        except socket.timeout:
            print("Timeout - No response received from server")
            retries += 1
            time.sleep(1)  

        except Exception as e:  # Catch any exception
            print(f"An error occurred: {e}") 

        finally:
            udp_socket.close() 

if __name__ == "__main__":
    # Redirect output to log file
    with open('myUDPClient.log', 'a') as f:
        import sys
        sys.stdout = f  # Redirect print statements to the same log file

        udp_client()
