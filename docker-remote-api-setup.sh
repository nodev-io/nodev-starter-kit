# sync
sudo apt-get update
sudo apt-get -y dist-upgrade

# install docker-engine on ubuntu 16.04
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" | sudo tee /etc/apt/sources.list.d/docker.list
sudo apt-get update
sudo apt-get install -y docker-engine

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
sudo docker ps
