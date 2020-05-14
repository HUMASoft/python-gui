
import SocketCanPort
import Cia402device

pm1 = SocketCanPort.SocketCanPort("can1")
#sd1 = Cia402device.CiA402SetupData.CiA402SetupData()

cia402_pos = Cia402device.CiA402Device(31, pm1);
#cia402_pos = Cia402device.CiA402Device(31, pm1, sd1);

cia402_pos.Reset();
cia402_pos.SwitchOn();
cia402_pos.GetPosition();


