pelican ./content -o ./output -s ./pelicanconf.py
mv ./output/index.html ./output/index1.html
cp ./output/download.html ./output/index.html
