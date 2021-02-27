mkdir -p /tmp/imsp/{input,out}
cp ./* /tmp/imsp
cd /tmp/imsp
wget https://builder.blender.org/download/blender-2.93.0-f7933d0744df-linux64.tar.xz
tar -xf blender-2.93.0-f7933d0744df-linux64.tar.xz
mv blender-2.93.0-f7933d0744df-linux64 blender
rm blender-2.93.0-f7933d0744df-linux64.tar.xz