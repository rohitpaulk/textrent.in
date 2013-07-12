echo "Preparing for deployment to Openshift"
mkdir php
mv _site/* php/*
for i in $( ls ); do
    if [ $i != "php" ]; then
        echo $i
        rm $i -r
    fi
done
ls ./*

