echo "Preparing for deployment to Openshift"
mkdir php
ls
echo "no php should be there below"
for i in $( ls ); do
    if [ $i != "php" ]; then
        echo $i
    fi
done
echo "final ls"
ls
