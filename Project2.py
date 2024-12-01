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

            # Send USER_ID to server
            print(f"Attempt {retries + 1}: Sending USER_ID '{USER_ID}' to server...")
            udp_socket.sendto(USER_ID.encode(), (SERVER_IP, SERVER_PORT))

            # Listen for server response
            response, server_address = udp_socket.recvfrom(1024)
            responses_received += 1
            print(f"Received response from server: {response.decode()}")

        except socket.timeout:
            print("Timeout - No response received from server")

        finally:
            udp_socket.close()
            retries += 1
            time.sleep(1)  

if __name__ == "__main__":
    udp_client()
