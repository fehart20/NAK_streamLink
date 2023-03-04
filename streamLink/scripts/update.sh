#!/bin/bash
echo -e "=> Updating streamLink via GitHub ... \n"
git reset --hard
git fetch --all
git pull --no-rebase