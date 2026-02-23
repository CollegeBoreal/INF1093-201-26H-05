#!/bin/sh

# --------------------------------------
# Participation report generator (v2)
# - Version nettoyée (colonne req supprimée)
# --------------------------------------

set -e

# Charge la liste des étudiants : ETUDIANTS=("id|github|avatar" ...)
source ../.scripts/students.sh --source-only

# --- Utilitaires ---

num_to_emoji() {
    case "$1" in
        0) echo ":zero:" ;;
        1) echo ":one:" ;;
        2) echo ":two:" ;;
        3) echo ":three:" ;;
        4) echo ":four:" ;;
        5) echo ":five:" ;;
        6) echo ":six:" ;;
        7) echo ":seven:" ;;
        8) echo ":eight:" ;;
        9) echo ":nine:" ;;
        *) echo ":keycap_ten:" ;;
    esac
}

check_file () {
    [ -f "$1" ] && echo ":heavy_check_mark:" || echo ":x:"
}

check_dir () {
    [ -d "$1" ] && echo ":heavy_check_mark:" || echo ":x:"
}

# --- En-tête ---

echo "# Participations"
echo ""
echo "| Table des matières            | Description                                             |"
echo "|-------------------------------|---------------------------------------------------------|"
echo "| :a: [Présence](#a-présence)   | L'étudiant.e a fait son travail    :heavy_check_mark:   |"
echo "| :b: #b-précision | L'étudiant.e a réussi son travail  :tada:               |"
echo ""
echo "## Légende"
echo ""
echo "| Signe              | Signification                        |"
echo "|--------------------|--------------------------------------|"
echo "| :heavy_check_mark: | Prêt à être corrigé                  |"
echo "| :x:                | Projet inexistant                    |"
echo "| :rocket:           | Script Python IO.py exécutable       |"
echo "| :receipt:          | Notebook présent                     |"
echo "| :writing_hand:     | Signature (ID) trouvée dans le .ipynb|"
echo "| :framed_picture:   | Figures présentes dans le .ipynb     |"
echo "| :boom:             | Erreurs dans le notebook             |"
echo ""

echo "## :a: Présence"
echo ""
echo "|:hash:| Boréal :id: | README.md | images | :rocket: IO.py | :receipt: RAPPORT | :writing_hand: Sgn | :framed_picture: Figures | etudiants.txt | resultats.txt | :boom: Erreurs |"
echo "|------|-------------|-----------|--------|----------------|-------------------|--------------------|-------------------------|---------------|---------------|----------------|"

# --- Boucle étudiants ---

i=0
s=0
total_figures=0
ok_full=0

for entry in "${ETUDIANTS[@]}"; do

    IFS='|' read -r id github avatar <<EOF
$entry
EOF

    URL="[<image src='https://avatars0.githubusercontent.com/u/${avatar}?s=460&v=4' width=20 height=20></image>](https://github.com/${github})"

    FILE="${id}/README.md"
    FOLDER="${id}/images"
    PY="${id}/IO.py"
    NB="${id}/RAPPORT.ipynb"
    IN="${id}/etudiants.txt"
    OUT="${id}/resultats.txt"

    README_ICON=$(check_file "$FILE")
    IMAGES_ICON=$(check_dir "$FOLDER")
    IN_ICON=$(check_file "$IN")
    OUT_ICON=$(check_file "$OUT")

    # — Test IO.py —
    EXEC_PY_ICON=":x:"
    if [ -f "$PY" ]; then
        if python3 "$PY" >/dev/null 2>&1; then
            EXEC_PY_ICON=":rocket:"
        fi
    fi

    # — Notebook —
    RAPPORT_ICON=":x:"
    ERROR_ICON=":x:"
    SIGN_ICON=":x:"
    FIGURES_ICON=":zero:"

    if [ -f "$NB" ]; then
        RAPPORT_ICON=":receipt:"

        ERROR_COUNT=$(jq '[.cells[].outputs[]? | select(.output_type=="error")] | length' "$NB" 2>/dev/null)
        [ -z "$ERROR_COUNT" ] && ERROR_COUNT=1

        if [ "$ERROR_COUNT" -eq 0 ]; then
            ERROR_ICON=""
            FIGURES_COUNT=$(jq '
                [.cells[].outputs[]?
                    | select(.output_type=="display_data")
                    | .data."text/plain"?
                    | arrays | .[]
                    | select(test("Figure"))
                ] | length
            ' "$NB" 2>/dev/null)

            [ -z "$FIGURES_COUNT" ] && FIGURES_COUNT=0
            FIGURES_ICON=$(num_to_emoji "$FIGURES_COUNT")
            total_figures=$((total_figures + FIGURES_COUNT))
        else
            ERROR_ICON=":boom:"
        fi

        ID_PRESENT=$(jq -r --arg id "$id" '
            .cells[] | select(.cell_type=="markdown")
            | .source[]? | select(test($id))
        ' "$NB" 2>/dev/null)

        [ -n "$ID_PRESENT" ] && SIGN_ICON=":writing_hand:"
    fi

    echo "| ${i} | [${id}](../${FILE}) ${URL} | ${README_ICON} | ${IMAGES_ICON} | ${EXEC_PY_ICON} | [${RAPPORT_ICON}](${NB}) | ${SIGN_ICON} | ${FIGURES_ICON} | ${IN_ICON} | ${OUT_ICON} | ${ERROR_ICON} |"

    # Critère minimal
    if [ "$README_ICON" = ":heavy_check_mark:" ] &&
       [ "$IMAGES_ICON" = ":heavy_check_mark:" ] &&
       [ "$RAPPORT_ICON" = ":receipt:" ]; then
        s=$((s+1))
    fi

    # Critère « tout OK »
    if [ "$README_ICON$IMAGES_ICON$EXEC_PY_ICON$RAPPORT_ICON$IN_ICON$OUT_ICON" = ":heavy_check_mark::heavy_check_mark::rocket::receipt::heavy_check_mark::heavy_check_mark:" ]; then
        ok_full=$((ok_full+1))
    fi

    i=$((i+1))
done

# --- Résumé ---

COUNT="\$\\frac{${s}}{${i}}$"
STATS=$(echo "$s*100/$i" | bc)
SUM_EXEC="\$\displaystyle\sum_{i=1}^{${i}} e_i$"

echo "| :abacus: | ${COUNT} = ${STATS}% | | | | | | | ${SUM_EXEC} = ${total_figures} | | | |"
echo ""
echo "> Rappel (tout OK) : ${ok_full}/${i}"
