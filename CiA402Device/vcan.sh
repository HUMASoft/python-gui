sudo ip link add dev vcan0 type vcan
sudo ip link add dev vcan1 type vcan
sudo ip link set up vcan0
sudo ip link set up vcan1

#Son dos puertos que se comunican
en una pestaña terminal haces:
candump vcan1 #esto hara que todos los cansend se muestren aqui
en la otra mandas mensajes haciendo:
cansend vcan0 123#0011

#hecho esto se muestra en la terminal de candump:
vcan1 123 [2] 00 11

