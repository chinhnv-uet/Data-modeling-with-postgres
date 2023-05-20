#! /usr/bin/bash
cd data/log_data/2018/11

#import web log data
touch data.json
echo '[' > data.json

for file in `ls | grep 2018`
do
fileName=${file:0:10}
cat $file | sed 's|}|,"date":"'"$fileName"'"},|g' >> data.json
done

truncate -s -1 data.json
echo ']' >> data.json

mongoimport --db products --collection musicWebLog --file data.json --jsonArray

# import song data
cd ..
cd ..
cd ..
cd song_data/A/

for folder in `ls`; do
    cd $folder
    for subfolder in `ls`; do
        cd $subfolder
        touch data.json
        for fileName in `ls | grep TRA`; do
            echo '[' > data.json
            cat $fileName >> data.json
            echo ']' >> data.json
            mongoimport --db products --collection songs --file data.json --jsonArray
        done
        cd ..
    done
    cd ..
done