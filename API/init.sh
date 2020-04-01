# Para crear el .o meto en terminal:
g++ -c -fPIC SocketCanPort.cpp -o SocketCanPort.o
# Para crear la librería compartida, meto en el terminal:
g++ -shared -o libSocket.so SocketCanPort.o
#Fin
