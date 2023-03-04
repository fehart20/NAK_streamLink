#!/bin/bash
# Clear current link config
sed -i '/link/d' ../config.ini

PS3="Select streaming location: "

select linkOpt in Nuertingen Metzingen Muensingen Oberboihingen Aichtal Other; do
    case $linkOpt in
        Nuertingen)
            echo -e "=> Adding Streamlink for $linkOpt to config ...\n"
            echo -e "#link for $linkOpt \nlink: http://nactube.datagis.com/c/NAKNuertingen" >> ../config.ini
            break
            ;;
        Metzingen)
            echo -e "=> Adding Streamlink for $linkOpt to config ...\n"
            echo -e "#link for $linkOpt \nlink: http://nactube.datagis.com/v/SIyvExJfyuM" >> ../config.ini
            break
            ;;
        Muensingen)
            echo -e "=> Adding Streamlink for $linkOpt to config ...\n"
            echo -e "#link for $linkOpt \nlink: http://nactube.datagis.com/v/Q-MIeFojxsE" >> ../config.ini
            break
            ;;
        Oberboihingen)
            echo -e "=> Adding Streamlink for $linkOpt to config ...\n"
            echo -e "#link for $linkOpt \nlink: http://nactube.datagis.com/v/mpMCZzs7wFS" >> ../config.ini
            break
            ;;
        Aichtal)
            echo -e "=> Adding Streamlink for $linkOpt to config ...\n"
            echo -e "#link for $linkOpt \nlink: http://nactube.datagis.com/v/FQGmVQ-VqZy" >> ../config.ini
            break
            ;;
        Other)
            echo "Please provide a YouTube-Livestream URL (Shortlink): "
            read otherLink
            echo -e "=> Adding Streamlink $otherLink to config ...\n"
           echo -e "#link for $linkOpt \nlink: $otherLink" >> ../config.ini
            break
            ;;
        *)
            echo "Invalid option $REPLY!"
            ;;
    esac
done