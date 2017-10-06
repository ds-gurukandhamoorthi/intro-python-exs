cat *py| sed -e 's/[ ()]\+/\n/g' |sort |uniq -c |sort -n -k1,1

