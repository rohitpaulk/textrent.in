echo "Preparing for deployment to Openshift"
mkdir php
mv _site/* php/*
for i in $( ls ); do
    if [ $i != "php" ]; then
        rm $i -r
    fi
done
mkdir libs
mkdir misc
touch deplist.txt
touch README.md
echo "final ls"
ls ./*
