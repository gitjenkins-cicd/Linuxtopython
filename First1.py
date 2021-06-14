import subprocess
subprocess.call(["ls","-lrth","/tmp/"])

dickspace="df"
diskspacearg="-h"
#subprocess.call([dickspace,diskspacearg])

subprocess.call("df -h",shell=True)
#subprocess.call("find / -type f -exec ls -lrth {} \;",shell=True)

def disk_func():
    dickspace="df"
    diskspacearg="-h"
    subprocess.call([dickspace,diskspacearg])

def uname_func():
    uname = "uname"
    uname_arg = "-a"
    subprocess.call([uname, uname_arg])


def main():
    uname_func()
    disk_func()

print("Printinng from main function")
main()
