import sys

def main():
  print("hello python")
  
def on():
  print("status on")
 
def off():
  print("status off")
 
def passed():
  pass


def on():
    print("[+] status on")

def off():
    print("[-] status off")

def passed():
    sys.exit(1)


if __name__=="__main__":
    main()
    on()
    off()
    passed()
