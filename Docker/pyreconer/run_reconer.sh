docker run -it --cidfile cid pyreconer <target>
cid=`cat cid` 
<<<<<<< HEAD
docker cp $cid:/PyReconer/output .
rm cid
=======
docker cp $cid:/reconer/output .
>>>>>>> 0c97a88e5b871db9f903f42f2ee4bca37d3c635a
