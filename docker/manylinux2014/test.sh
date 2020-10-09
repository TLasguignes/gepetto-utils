#!/bin/bash -eu

while read tgt
do  echo -e "\n================================ $tgt ===================================\n"
    pip install --find-links=/ "$tgt"
    python "/$tgt/test.py"
done < targets
