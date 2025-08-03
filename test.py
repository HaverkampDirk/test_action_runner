import os

def run_command(user_input):
    # Unsichere Nutzung von user_input in einem Shell-Befehl
    os.system(f"echo {user_input}")
    
if __name__ == "__main__":
    inp = input("Gib etwas ein: ")
    run_command(inp)
