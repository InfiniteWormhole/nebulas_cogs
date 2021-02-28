mkdir -p /tmp/imsp/{input,out}
cp ./* /tmp/imsp
cd /tmp/imsp
wget https://builder.blender.org/download/blender-2.93.0-f3d60c68ef46-linux64.tar.xz
tar -xf blender-2.93.0-f3d60c68ef46-linux64.tar.xz
mv blender-2.93.0-f3d60c68ef46-linux64 blender
rm blender-2.93.0-f3d60c68ef46-linux64.tar.xz