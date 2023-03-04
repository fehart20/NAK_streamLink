#!/bin/bash

sed -i '/link/d' ../config.ini # Clear current link config.ini
sed -i '/location/d' ../config.ini # Clear current location config.ini

PS3="Select streaming location: "

select linkOpt in Nuertingen Metzingen Muensingen Oberboihingen Aichtal Other; do
    case $linkOpt in
        Nuertingen)
            echo -e "=> Adding Streamlink for $linkOpt to config ...\n"
            sudo echo "link: http://nactube.datagis.com/c/NAKNuertingen" >> ../config.ini
            sudo echo "location: Nürtingen" >> ../config.ini
            break
            ;;
        Metzingen)
            echo -e "=> Adding Streamlink for $linkOpt to config ...\n"
            sudo echo "link: http://nactube.datagis.com/v/SIyvExJfyuM" >> ../config.ini
            sudo echo "location: Metzingen" >> ../config.ini
            break
            ;;
        Muensingen)
            echo -e "=> Adding Streamlink for $linkOpt to config ...\n"
            sudo echo "link: http://nactube.datagis.com/v/Q-MIeFojxsE" >> ../config.ini
            sudo echo "location: Münsingen" >> ../config.ini
            break
            ;;
        Oberboihingen)
            echo -e "=> Adding Streamlink for $linkOpt to config ...\n"
            sudo echo "link: http://nactube.datagis.com/v/mpMCZzs7wFS" >> ../config.ini
            sudo echo "location: Oberboihingen" >> ../config.ini
            break
            ;;
        Aichtal)
            echo -e "=> Adding Streamlink for $linkOpt to config ...\n"
            sudo echo "link: http://nactube.datagis.com/v/FQGmVQ-VqZy" >> ../config.ini
            sudo echo "location: Aichtal" >> ../config.ini
            break
            ;;
        Other)
            echo "Please provide a YouTube-Livestream URL (Shortlink): "
            read otherLink
            echo -e "=> Adding Streamlink $otherLink to config ...\n"
            sudo echo "link: $otherLink" >> ../config.ini
            sudo echo "location: Anderswo" >> ../config.ini
            break
            ;;
        *)
            echo -e "Invalid option $REPLY!"
            ;;
    esac
done