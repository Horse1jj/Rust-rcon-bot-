import socket

def execute_rcon_command(server, command):
    try:
        ip = server["ip"]
        port = int(server["port"])
        rcon_password = server["rcon_password"]

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            response = f"Executed '{command}' on {ip}:{port}"  
            return response
    except Exception as e:
        return f"Error: {str(e)}"