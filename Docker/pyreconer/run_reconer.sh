docker run -it --cidfile cid pyreconer <target>
cid=`cat cid` 
docker cp $cid:/reconer/output .
