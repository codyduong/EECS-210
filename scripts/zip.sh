to_zip = $1

# cleanup old zips
rm -r "CodyDuong_$1"
rm -r "CodyDuong_$1.zip"
cp -R $1 "CodyDuong_$1"
zip -r CodyDuong_$1.zip "CodyDuong_$1" -x "$1/node_modules/* $1/target/*"

# cleanup temp
rm -r "CodyDuong_$1"