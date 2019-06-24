docker run -it --cidfile cid reconer <target>
cid=`cat cid` 
docker cp $cid:/reconer/output .