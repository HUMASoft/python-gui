#include "Cia402device.h"
#include "CiA301CommPort.h"
#include "SocketCanPort.h"
#include <iostream>
#include <stdio.h>


int main ()
{
    //--Can port communications--
    SocketCanPort pm1("vcan1");


    m.GetMsg();
    //m.SwitchOn();
    // m.Setup_Velocity_Mode();

    // cout << "Enter to stop." <<endl;

    // // position  [rads]
    // m.SetVelocity(2);

    // getchar();

    // m.SetVelocity(0);


}