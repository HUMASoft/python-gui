# Para crear el .o meto en terminal:
g++ -c -fPIC foo.cpp -o foo.o
# Para crear la librería compartida, meto en el terminal:
g++ -shared -o libfoo.so foo.o
#Fin
