#!/bin/sh

# --------------------------------------
#
#
#
# --------------------------------------

source ../.scripts/students.sh --source-only
   
echo "# Participation"
echo ""


echo "| Table des matières            | Description                                             |"
echo "|-------------------------------|---------------------------------------------------------|"
echo "| :a: [Présence](#a-présence)   | L'étudiant.e a fait son travail    :heavy_check_mark:   |"
echo "| :b: [Précision](#b-précision) | L'étudiant.e a réussi son travail  :tada:               |"

echo ""
echo "## Légende"
echo ""

echo "| Signe              | Signification                 |"
echo "|--------------------|-------------------------------|"
echo "| :heavy_check_mark: | Prêt à être corrigé           |"
echo "| :x:                | Projet inexistant             |"


echo ""
echo "## :a: Présence"
echo ""
echo "|:hash:| Boréal :id:                | README.md    | images | IO.py | RAPPORT.ipynb | etudiants.txt | resultats.txt |"
echo "|------|----------------------------|--------------|--------|-------|---------------|---------------|---------------|"


i=0
s=0

for entry in "${ETUDIANTS[@]}"; do

   IFS='|' read -r id github avatar <<< "$entry"

   URL="[<image src='https://avatars0.githubusercontent.com/u/${avatar}?s=460&v=4' width=20 height=20></image>](https://github.com/${github})"

   FILE=${id}/README.md
   FOLDER=${id}/images
   PY=${id}/IO.py
   NB=${id}/RAPPORT.ipynb
   IN=${id}/etudiants.txt
   OUT=${id}/resultats.txt

   check_file () {
       [ -f "$1" ] && echo ":heavy_check_mark:" || echo ":x:"
   }

   check_dir () {
       [ -d "$1" ] && echo ":heavy_check_mark:" || echo ":x:"
   }

   README_OK=$(check_file "$FILE")
   IMG_OK=$(check_dir "$FOLDER")
   PY_OK=$(check_file "$PY")
   NB_OK=$(check_file "$NB")
   IN_OK=$(check_file "$IN")
   OUT_OK=$(check_file "$OUT")

   echo "| ${i} | [${id}](../${FILE}) ${URL} | ${README_OK} | ${IMG_OK} | ${PY_OK} | [${NB_OK}](../${NB}) | ${IN_OK} | ${OUT_OK} |"

   if [ "$README_OK$IMG_OK$PY_OK$NB_OK$IN_OK$OUT_OK" = ":heavy_check_mark::heavy_check_mark::heavy_check_mark::heavy_check_mark::heavy_check_mark::heavy_check_mark:" ]; then
       let "s++"
   fi

   let "i++"
   COUNT="\$\\frac{${s}}{${i}}$"
   STATS=$(echo "$s*100/$i" | bc)
   SUM="$\displaystyle\sum_{i=1}^{${i}} s_i$"
 done
 
echo "| :abacus: | " ${COUNT} " = " ${STATS}% "|" ${SUM} = ${s} "|"
