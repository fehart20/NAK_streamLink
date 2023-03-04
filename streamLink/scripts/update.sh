#!/bin/bash
set -e
echo '=> Updating streamLink via GitHub ... \n'
git reset --hard
git fetch --all
git pull --no-rebase