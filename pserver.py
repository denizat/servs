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
            system(f"{base} --mkpath  --exclude '*' {protocol}{addr}/root/{d} {bk}{d}")
            pull(d, dirs[d]["include"])
        else:
            system(f"{base} {protocol}{addr}/root/{root}{d} {bk}{root}{d}")


def push():
    for i in listdir(bk):
        print(i)
        system(f"{base} {bk}/{i}/ server_test/{i}")


dirs = {
    # "home/": {},
    # "root/": {},

    # "etc/": {
    #     "include": [

    #         "ufw/",
    #         "systemd/",


              # we want this backed up and version controlled
    #         "ssh/",
    #         "nginx/",


              # we want this backed up and version controlled
    #         "rsyncd.conf",
    #         "cron.d/",
    #         "cron.daily/",
    #         "cron.hourly/",
    #         "cron.monthly/",
    #         "cron.weekly/",

    #        # it is actually a good idea to back these up so that we don't need to
    #        # deal with adding users in our shell scripts
    #         "group",
    #         "group-",
    #         "gshadow",
    #         "gshadow-",
    #         "passwd",
    #         "passwd-",

    #     ]
    # },

    # "lib/": {
    #     "include": [
    #         # note, probably don't want to reproduce systemd configuration like this
    #         # it would be better to do it with shell scripts (systemctl start/enable xyz)
    #         "systemd/",
    #     ]
    # },

    # "var/": {"include": ["www/", "spool/"]},
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
