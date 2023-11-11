import socket
import threading

printlock = threading.Lock()

def scanport(target, startport, endport):
  for port in range(startport, endport + 1):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
      sock.settimeout(1)
      result = sock.connect_ex((target, port))
      with printlock:
        if result == 0:
          print(f"Port {port} is open.")

def main(target, startport, endport):
  threads=[]
  print("Scanning!")
  for i in range(5):
    thread = threading.Thread(target=scanport, args=(target, startport, endport))
    threads.append(thread)
    thread.start()
  for thread in threads:
    thread.join()
  print("Scanning complete")

if __name__ == "__main__":
  target = input("Please enter target: ")
  startport = int(input("Enter start port: "))
  endport = int(input("Enter end port: "))
  main(target, startport, endport)
