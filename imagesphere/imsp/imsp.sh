cd /tmp/imsp
ffmpeg -i input/* -frames:v 1 -y input/input.png
xvfb-run /tmp/imsp/blender/blender -b anysphere.blend -P sphere.py -o ./out/ input/input.png
cd out
gifski *.png --fps 30 -o out.gif
rm *.png