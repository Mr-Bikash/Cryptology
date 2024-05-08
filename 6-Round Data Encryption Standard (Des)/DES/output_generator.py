import pexpect
import time

# Constants for SSH connection and interaction
SSH_COMMAND = 'ssh student@172.27.26.188'
PASSWORD_PROMPT = "student@172.27.26.188's password:"
PASSWORD = 'cs641'
INITIAL_PROMPT = '.*'
MOD3_COMMAND = 'mod3'
SPIDERMAN_COMMAND = 'Spiderman@2'
FINAL_PROMPT = '.* '
PROCEED_COMMAND = '4'
COMMANDS_FILE = 'commands.txt'
TEXT_STARTS_PROMPT = "Slowly, a new text starts*"
TEXT_VANISHES_PROMPT = 'The text in the screen vanishes!'

def ciphertext_generator(plaintext_file, ciphertext_file):
    child = pexpect.spawn(SSH_COMMAND)
    child.expect(PASSWORD_PROMPT)
    child.sendline(PASSWORD)
    child.expect(INITIAL_PROMPT, timeout=50)
    child.sendline(MOD3_COMMAND)
    child.expect(INITIAL_PROMPT, timeout=50)
    child.sendline(SPIDERMAN_COMMAND)
    child.expect(FINAL_PROMPT, timeout=50)
    child.sendline(PROCEED_COMMAND)

    with open(COMMANDS_FILE, 'r') as cmd_file:
        for command in cmd_file:
            child.expect(INITIAL_PROMPT)
            child.sendline(command.strip())

    with open(plaintext_file, 'r') as plaintext, open(ciphertext_file, 'w') as ciphertext:
        for line in plaintext:
            child.sendline(line.strip())
            child.expect(TEXT_STARTS_PROMPT)
            child.sendline("c")
            child.expect(TEXT_VANISHES_PROMPT)
            output = str(child.before)
            print(output)
            ciphertext.write(output[48:64] + "\n")  # Assuming the relevant output is always in this slice

    child.close()
    print("Session closed. Last output:", child.before, child.after)

# Example usage
ciphertext_generator("input_strings1.txt", "output_strings1.txt")
time.sleep(5)
ciphertext_generator("input_strings2.txt", "output_strings2.txt")

