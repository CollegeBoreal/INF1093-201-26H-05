#!/usr/bin/env bash

# --------------------------------------
# Rapport de participation + vérification de structure
# --------------------------------------

# Charge la liste des étudiants (tableau ETUDIANTS avec items "id|github|avatar")
# Exemple d'entrée : "abc123|prenomnom|1234567"
# Le script students.sh doit définir : ETUDIANTS=( "id|github|avatar" ... )
source ../.scripts/students.sh --source-only

# ---------- Fonctions ----------

# Vérifie la structure de répertoires/fichiers exigée
# ID/
# ├─ insertion/ (main.py, entree_insertion.txt)
# ├─ shell/     (main.py, entree_shell.txt)
# └─ quick/     (main.py, entree_quick.txt)
check_structure() {
    local base="$1"
    local paths=(
        "${base}/insertion/main.py"
        "${base}/insertion/entree_insertion.txt"
        "${base}/shell/main.py"
        "${base}/shell/entree_shell.txt"
        "${base}/quick/main.py"
        "${base}/quick/entree_quick.txt"
    )

    for f in "${paths[@]}"; do
        if [[ ! -f "$f" ]]; then
            return 1   # Manque au moins un fichier
        fi
    done

    return 0  # Structure complète
}

# ---------- En-tête du rapport ----------

echo "# Participations"
echo ""

echo "| Table des matières                      | Description                                             |"
echo "|-----------------------------------------|---------------------------------------------------------|"
echo "| :a: [Présence](#a-présence)             | L'étudiant.e a fait son travail    :heavy_check_mark:   |"
echo "| :b: [Précision](#b-précision)           | L'étudiant.e a réussi son travail  :tada:               |"

echo ""
echo "## Légende"
echo ""
echo "| Signe              | Signification                               |"
echo "|--------------------|---------------------------------------------|"
echo "| :heavy_check_mark: | Prêt à être corrigé                         |"
echo "| :x:                | Projet inexistant / Incomplet / Non conforme|"
echo "| :rocket:           | Commit validé (auteur ≠ *noreply*)          |"
echo "| Structure          | Arborescence + fichiers exigés présents     |"

echo ""
echo "## :a: Présence"
echo ""
echo "| :hash: | Boréal :id:                         | :id:/README.md    | :rocket: | Structure |"
echo "|--------|-------------------------------------|-------------------|----------|-----------|"

# ---------- Corps ----------

i=0      # total traités
s=0      # nombre d'OK (README présent + auteur ≠ noreply)

for entry in "${ETUDIANTS[@]}"; do
    IFS='|' read -r id github avatar <<< "$entry"

    # Lien Github + avatar (rendu Markdown avec <img>)
    URL="[${github}](https://github.com/${github}) <img src='https://avatars0.githubusercontent.com/u/${avatar}?s=460&v=4' width='20' height='20'/>"

    FILE="${id}/README.md"

    # Par défaut
    readme_status=":x:"
    work_status=":x:"
    struct_status=":x:"

    if [[ -f "$FILE" ]]; then
        readme_status=":heavy_check_mark:"
        # Vérifie si le dernier auteur est "noreply" (soumission web)
        if git log --format=fuller -- "${FILE}" | grep Author | grep -q "noreply"; then
            work_status=":x:"
        else
            work_status=":heavy_check_mark:"
            ((s++))
        fi
    fi

    # Vérifie la structure (indépendamment du README)
    if check_structure "${id}"; then
        struct_status=":heavy_check_mark:"
    else
        struct_status=":x:"
    fi

    echo "| ${i} | [${id}](../${FILE}) ${URL} | ${readme_status} | ${work_status} | ${struct_status} |"

    ((i++))
done

# ---------- Statistiques ----------

COUNT="\$\\frac{${s}}{${i}}$"
if (( i > 0 )); then
    STATS=$(echo "scale=0; (${s}*100)/${i}" | bc)
else
    STATS=0
fi
SUM="\$\displaystyle\sum_{i=1}^{${i}} s_i$"

echo "| :abacus: | ${COUNT} = ${STATS}% | ${SUM} = ${s} |"

echo ""
echo "## :b: Précision"
echo ""
echo "> Cette section peut détailler des critères de réussite supplémentaires, tests unitaires, etc."
