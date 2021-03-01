mkdir -p /opt/imsp/{input,out}
cp ./* /opt/imsp
cd /opt/imsp
wget https://mirror.clarkson.edu/blender/release/Blender2.92/blender-2.92.0-linux64.tar.xz
tar -xf blender-2.92.0-linux64.tar.xz
mv blender-2.92.0-linux64 blender
rm blender-2.92.0-linux64.tar.xz