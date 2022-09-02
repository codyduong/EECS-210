to_zip = $1
zip -r CodyDuong_$1.zip $1 -x "$1/node_modules/*"