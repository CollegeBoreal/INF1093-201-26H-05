# Projet Vétérina-Cité - Livrable 1

## Modèle Conceptuel de Données (MCD)

```mermaid
erDiagram
    CLIENT ||--o{ ANIMAL : "possède (1,n)"
    ANIMAL ||--o{ VISITE : "concerne (0,n)"
    VETERINAIRE ||--o{ VISITE : "assure (1,n)"
    VISITE ||--o{ LIGNE_TRAITEMENT : "contient (1,n)"
    TRAITEMENT ||--o{ LIGNE_TRAITEMENT : "est appliqué (0,n)"

    CLIENT {
        int id_client PK
        string nom
        string tel
        string courriel
        string ville
    }

    ANIMAL {
        int id_animal PK
        string nom_animal
        string espece
        string race
        date date_naissance
        float poids
        int id_client FK
    }

    VETERINAIRE {
        int id_vet PK
        string nom
        string specialite
    }

    VISITE {
        int id_visite PK
        date date_visite
        int id_animal FK
        int id_vet FK
    }

    LIGNE_TRAITEMENT {
        int id_visite FK
        int id_traitement FK
    }

    TRAITEMENT {
        int id_traitement PK
        string libelle
        float prix_base
    }
