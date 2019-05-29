./tools.py
cd cowpatty-4.6/
sudo make
echo Cowpatty maked, copying links
cp cowpatty /usr/bin/cowpatty
cp genpmk /usr/bin/genpmk
cd ..
echo Removing temp files
rm -r cowpatty-4.6
rm cowpatty-4.6.tgz
echo
echo WiCC installed
echo
echo You can now execute it with: wicc
echo
echo You can view the help with options -h or --help : wicc --help