1. Server is backed up
2. Server is wiped
3. Server is remade
4. Server runs an init script that:
	- creates users
	- installs packages
	- configures the firewall
	- configures systemd (systemctl start rsyncd)
	- use epik api to programatically update dns for email
	- rsyncd config must be updated to enable the backup script to work
5. The backup is pushed onto the server:
	- /home/ is restored
	- some configs are updated
	- /var/ is restored
6. Server works perfectly with no human intervention
