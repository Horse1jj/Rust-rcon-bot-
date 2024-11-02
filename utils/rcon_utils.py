import socket

def execute_rcon_command(server, command):
    try:
        # This function should connect to the RCON server and send commands.
        # Replace with actual implementation.
        ip = server["ip"]
        port = int(server["port"])
        rcon_password = server["rcon_password"]

        # Placeholder for actual RCON connection logic
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            # Send command here and receive response...
            response = f"Executed '{command}' on {ip}:{port}"  # Placeholder response
            return response
    except Exception as e:
        return f"Error: {str(e)}"
