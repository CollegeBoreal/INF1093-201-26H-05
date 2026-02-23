#!/bin/sh

# --------------------------------------
# Participation report generator (v2)
# - Basé sur votre 2e script, enrichi avec les idées du 1er
# --------------------------------------

set -e

# Charge la liste des étudiants : ETUDIANTS=("id|github|avatar" "...")
# shellcheck disable=SC1091
source ../.scripts/students.sh --source-only

# --- Utilitaires ---

# Convertit 0..9 -> emoji, sinon :keycap_ten:
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

echo "# Participation au $(date +"%d-%m-%Y %H:%M")"
echo ""
echo "| Table des matières            | Description                                             |"
echo "|-------------------------------|---------------------------------------------------------|"
echo "| :a: [Présence](#a-présence)   | L'étudiant.e a fait son travail    :heavy_check_mark:   |"
echo "| :b: [Précision](#b-précision) | L'étudiant.e a réussi son travail  :tada:               |"
echo ""
echo "## Légende"
echo ""
echo "| Signe              | Signification                        |"
echo "|--------------------|--------------------------------------|"
echo "| :heavy_check_mark: | Prêt à être corrigé                  |"
echo "| :x:                | Projet inexistant                    |"
echo "| :page_facing_up:   | requirements.txt présent             |"
echo "| :rocket:           | Script Python IO.py exécutable       |"
echo "| :receipt:          | Notebook présent                     |"
echo "| :writing_hand:     | Signature (ID) trouvée dans le .ipynb|"
echo "| :framed_picture:   | Figures présentes dans le .ipynb     |"
echo "| :boom:             | Erreurs dans le notebook             |"
echo ""

echo "## :a: Présence"
echo ""
echo "|:hash:| Boréal :id: | README.md | images | :page_facing_up: req | :rocket: IO.py | :receipt: RAPPORT | :writing_hand: Sgn | :framed_picture: Figures | etudiants.txt | resultats.txt | :boom: Erreurs |"
echo "|------|-------------|-----------|--------|----------------------|----------------|-------------------|--------------------|-------------------------|---------------|---------------|----------------|"

# --- Boucle étudiants ---

i=0                # total d'étudiants parcourus
s=0                # critère minimal atteint (README + images + RAPPORT)
total_figures=0    # somme des figures dans les notebooks
ok_full=0          # nombre d'étudiants avec tout OK (pour rappel de votre 2e script)

for entry in "${ETUDIANTS[@]}"; do
    IFS='|' read -r id github avatar <<EOF
$entry
EOF

    URL="[<img src='https://avatars0.githubusercontent.com/u/${avatar}?s=460&amp;v=4' width=20 height=20></img>](https://github.com/${github})"

    FILE="${id}/README.md"
    FOLDER="${id}/images"
    REQUIRE="${id}/requirements.txt"
    PY="${id}/IO.py"
    NB="${id}/RAPPORT.ipynb"
    IN="${id}/etudiants.txt"
    OUT="${id}/resultats.txt"

    # Icônes par défaut
    README_ICON=":x:"
    IMAGES_ICON=":x:"
    REQUIRE_ICON=":x:"
    EXEC_PY_ICON=":x:"
    RAPPORT_ICON=":x:"
    SIGN_ICON=":x:"
    FIGURES_ICON=":zero:"
    ERROR_ICON=":x:"
    IN_ICON=":x:"
    OUT_ICON=":x:"

    # Fichiers / Dossiers simples
    [ -f "$FILE" ]    && README_ICON=":heavy_check_mark:"
    [ -d "$FOLDER" ]  && IMAGES_ICON=":heavy_check_mark:"
    [ -f "$REQUIRE" ] && REQUIRE_ICON=":page_facing_up:"
    [ -f "$IN" ]      && IN_ICON=":heavy_check_mark:"
    [ -f "$OUT" ]     && OUT_ICON=":heavy_check_mark:"

    # Test d'exécution silencieuse de IO.py (compile/exécute)
    if [ -f "$PY" ]; then
        # Redirection stdout+stderr -> /dev/null
        if python3 "$PY" >/dev/null 2>&1; then
            EXEC_PY_ICON=":rocket:"
        else
            EXEC_PY_ICON=":x:"
        fi
    fi

    # Notebook : présence + analyse via jq
    if [ -f "$NB" ]; then
        RAPPORT_ICON=":receipt:"

        # 1) Comptage des erreurs
        ERROR_COUNT=$(jq '
            [.cells[].outputs[]? | select(.output_type=="error")] | length
        ' "$NB" 2>/dev/null)

        # Si jq échoue, considérer comme erreurs
        if [ -z "$ERROR_COUNT" ]; then
            ERROR_COUNT=1
        fi

        if [ "$ERROR_COUNT" -eq 0 ]; then
            ERROR_ICON=""
            # 2) Comptage des figures (heuristique “Figure” dans text/plain)
            FIGURES_COUNT=$(jq '
                [.cells[].outputs[]?
                 | select(.output_type=="display_data")
                 | .data."text/plain"?
                 | arrays
                 | .[]
                 | select(test("Figure"))
                ] | length
            ' "$NB" 2>/dev/null)

            [ -z "$FIGURES_COUNT" ] && FIGURES_COUNT=0
            FIGURES_ICON=$(num_to_emoji "$FIGURES_COUNT")
            total_figures=$((total_figures + FIGURES_COUNT))
        else
            ERROR_ICON=":boom:"
            FIGURES_ICON=":zero:"
        fi

        # 3) Signature (ID dans une cellule markdown)
        ID_PRESENT=$(jq -r --arg id "$id" '
            .cells[]
            | select(.cell_type=="markdown")
            | .source[]? 
            | select(test($id))
        ' "$NB" 2>/dev/null)

        [ -n "$ID_PRESENT" ] && SIGN_ICON=":writing_hand:"
    fi

    echo "| ${i} | [${id}](../${FILE}) ${URL} | ${README_ICON} | ${IMAGES_ICON} | ${REQUIRE_ICON} | ${EXEC_PY_ICON} | [${RAPPORT_ICON}](../${NB}) | ${SIGN_ICON} | ${FIGURES_ICON} | ${IN_ICON} | ${OUT_ICON} | ${ERROR_ICON} |"

    # Critère minimal (comme demandé) : README + images + RAPPORT
    if [ "$README_ICON" = ":heavy_check_mark:" ] && \
       [ "$IMAGES_ICON" = ":heavy_check_mark:" ] && \
       [ "$RAPPORT_ICON" = ":receipt:" ]; then
        s=$((s+1))
    fi

    # Critère "tout OK" comme votre 2e script (6/6)
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
echo "> Rappel (tout OK façon script 2) : ${ok_full}/${i}"
