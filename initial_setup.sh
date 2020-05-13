
cd CiA402Device
python3 setup_PortBase.py  build_ext --inplace
mv *_PortBase.cpy*  _PortBase.so
python3 setup_SocketCanPort.py  build_ext --inplace
mv *_SocketCanPort.cpy*  _SocketCanPort.so
python3 setup_CiA301CommPort.py  build_ext --inplace
mv *_CiA301CommPort.cpy*  _CiA301CommPort.so
python3 setup_CiA402SetupData.py  build_ext --inplace
mv *_CiA402SetupData.cpy*  _CiA402SetupData.so
python3 setup_Cia402device.py  build_ext --inplace

