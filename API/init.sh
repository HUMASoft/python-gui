# Para crear el .o meto en terminal:

g++ -c -fPIC foo.cpp -o foo.o


# Para crear la librería compartida, meto en el terminal:

g++ -shared -Wl,-install_name,libfctn.so -o libfctn.so  fctn.o

#Fin
