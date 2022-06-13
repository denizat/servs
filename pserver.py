# depends on rsync  version v3.2.3  protocol version 31
from sys import argv
from os import system, listdir

if len(argv) < 2:
    print("GIVE ME THE ARG")
    quit()

op = argv[1]
bk = "./test_client/"

# need sudo for file perms
base = "sudo rsync --numeric-ids -a --info=progress2  --delete"


# base+=" --list-only"
# base = "echo " + base
# base = "# " + base

addr = "root@telci.org"
protocol = "rsync://"


def pull(root, dirs):
    print(root, dirs)
    for d in dirs:
        print(d)
        if type(dirs) is dict and "include" in dirs[d]:
            # system(f"{base} --mkpath  --exclude '*' {protocol}{addr}/root/{d} {bk}{d}")
            system(f"{base} --mkpath  --exclude '*' {protocol}{addr}/rootdir/{d} {bk}{d}")
            pull(d, dirs[d]["include"])
        else:
            # i dont want to use mkpath because it breaks something I think
            system(f"{base} {'--mkpath' if d.count('/') > 1 else ''} {protocol}{addr}/rootdir/{root}{d} {bk}{root}{d}")


def push():
    for i in listdir(bk):
        print(i)
        system(f"{base} {bk}/{i}/ server_test/{i}")


dirs = {
    # "home/": {},
    "root/": {},
    # "etc/": {
    #     "include": [
    #         "ssh/",
    #         "nginx/",
    #         "group",
    #         "group-",
    #         "gshadow",
    #         "gshadow-",
    #         "passwd",
    #         "passwd-",
    #     ]
    # },
    "var/www/": {},
}


if op == "pull":
    pull("", dirs)
elif op == "push":
    push()
elif op == "clear":
    system("sudo rm -rf ./test_client/* ./server_test/* >> /dev/null")
elif op == "clearc":
    system("sudo rm -rf ./test_client/* >> /dev/null")
elif op == "clears":
    system("sudo rm -rf ./server_test/* >> /dev/null")
