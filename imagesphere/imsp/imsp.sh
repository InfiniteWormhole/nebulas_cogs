cd /opt/imsp
ffmpeg -i input/* -frames:v 1 -y input/input.png > /dev/null 2>&1
xvfb-run /tmp/imsp/blender/blender -b anysphere.blend -P sphere.py -o ./out/ input/input.png > /dev/null 2>&1
cd out
gifski *.png --fps 30 -o out.gif > /dev/null 2>&1
rm *.png