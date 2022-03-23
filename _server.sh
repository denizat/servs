#!/bin/sh


# needs to be run with sudo to handle perms

mode=$1

case $mode in
	pull)
		text="backing up"
		cmd() {
			# mkdir -p $bk/$dir # && echo making directory $bk/$dir
			rsync --numeric-ids -a --mkpath  --info=progress2  --delete rsync://root@$addr/root/$1 $bk/$1
			# rsync --numeric-ids -aAXSHPr  --info=progress2 --no-i-r --delete rsync://root@$addr/root/$1 $bk/$1
		}
		;;
	push)
		# echo do not push for now
		# exit
		text="restoring"
		cmd() {
			ssh root@$addr mkdir -p /$dir # && echo making directory $bk/$dir on server
			rsync -a --info=progress2 --no-i-r --delete-after $bk/$1 rsync://root@$addr/root/$1
		}
		;;
	*) echo GIVE ME THE ARG && exit ;;
esac

# server address (ip or url
addr="telci.org"
# default backup folder name
bk="/home/deniz/.local/src/server/test_client"

# default directories to backup from the server
# we want to backup directories that hold data/configuration, things that were created manually
# we do not want to backup binaries and automatically generated system data

# note: must use parent directory to get proper sub file permissions
DIRS="
# var/www/
# var/spool/

home/
root/

# etc/ssh/
# etc/nginx/
# etc/ufw/
# etc/rsyncd.conf
# etc/cron.d/
# etc/cron.daily/
# etc/cron.hourly/
# etc/cron.monthly/
# etc/cron.weekly/
# etc/group
# etc/group-
# etc/gshadow
# etc/gshadow-
# etc/passwd
# etc/passwd-
# etc/systemd/
"
# [deniz@tp ~rr/server/test_client]$ sudo rsync -a --delete -r --numeric-ids git@telci.org:test ./cars.txt

c="f"
for dir in $DIRS
do
	if [[ $dir == '#' ]]; then c="t"; continue; fi
	if [[ $c == 't' ]]; then c="f"; continue; fi

	echo $text $bk/$dir
	cmd $dir
done
