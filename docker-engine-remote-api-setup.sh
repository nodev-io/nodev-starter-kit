# Ubuntu 16.04
#
# run docker-engine-setup.sh first

# enable insecure remote API
cat << EOF | sudo tee /etc/systemd/system/docker-tcp.socket
[Unit]
Description=Docker Socket for the API
[Socket]
ListenStream=4243
BindIPv6Only=both
Service=docker.service
[Install]
WantedBy=sockets.target
EOF

sudo systemctl enable docker-tcp.socket
sudo systemctl enable docker.socket
sudo systemctl stop docker
sudo systemctl start docker-tcp.socket
sudo systemctl start docker

# check that everything is running
sudo netstat --inet --inet6 -lnp
