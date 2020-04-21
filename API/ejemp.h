#include <iostream> 
using namespace std;
 
class pareja {
   private:
      // Datos miembro de la clase "pareja"
      int a, b; 
   public:
      // Funciones miembro de la clase "pareja"
      void Lee(int &a2, int &b2);
      void Guarda(int a2, int b2) {
         a = a2;
         b = b2;
      }
};

