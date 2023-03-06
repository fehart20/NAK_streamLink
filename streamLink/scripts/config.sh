#!/bin/bash

cd ~/NAK_streamLink/streamLink/scripts

sed -i '/link/d' ../config.ini # Clear current link config.ini
sed -i '/location/d' ../config.ini # Clear current location config.ini

PS3="Select streaming location: "

select linkOpt in Nuertingen Metzingen Muensingen Oberboihingen Aichtal Other; do
    case $linkOpt in
        Nuertingen)
            echo -e "=> Adding Streamlink for $linkOpt to config ...\n"
            echo "link: http://nactube.datagis.com/c/NAKNuertingen" >> ../config.ini
            echo "location: Nürtingen" >> ../config.ini
            break
            ;;
        Metzingen)
            echo -e "=> Adding Streamlink for $linkOpt to config ...\n"
            echo "link: http://nactube.datagis.com/v/SIyvExJfyuM" >> ../config.ini
            echo "location: Metzingen" >> ../config.ini
            break
            ;;
        Muensingen)
            echo -e "=> Adding Streamlink for $linkOpt to config ...\n"
            echo "link: http://nactube.datagis.com/v/Q-MIeFojxsE" >> ../config.ini
            echo "location: Münsingen" >> ../config.ini
            break
            ;;
        Oberboihingen)
            echo -e "=> Adding Streamlink for $linkOpt to config ...\n"
            echo "link: http://nactube.datagis.com/v/mpMCZzs7wFS" >> ../config.ini
            echo "location: Oberboihingen" >> ../config.ini
            break
            ;;
        Aichtal)
            echo -e "=> Adding Streamlink for $linkOpt to config ...\n"
            echo "link: http://nactube.datagis.com/v/FQGmVQ-VqZy" >> ../config.ini
            echo "location: Aichtal" >> ../config.ini
            break
            ;;
        Other)
            echo "Please provide a YouTube-Livestream URL (Shortlink): "
            read otherLink
            read otherLocation
            echo -e "=> Adding Streamlink for $otherLocation to config ...\n"
            echo "link: $otherLink" >> ../config.ini
            echo "location: $otherLocation" >> ../config.ini
            break
            ;;
        *)
            echo -e "Invalid option $REPLY!"
            ;;
    esac
done