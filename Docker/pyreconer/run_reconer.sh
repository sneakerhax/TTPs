docker run -it --cidfile cid pyreconer <target>
cid=`cat cid` 
docker cp $cid:/PyReconer/output .
rm cid
