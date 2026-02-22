
erDiagram
    CLIENT ||--o{ POSSEDER : "1,n"
    ANIMAL ||--|| POSSEDER : "1,1"
    
    ANIMAL ||--o{ CONCERNER : "0,n"
    VETERINAIRE ||--o{ CONCERNER : "1,n"
    VISITE ||--|| CONCERNER : "1,1"
    
    VISITE ||--o{ CONTENIR : "1,n"
    TRAITEMENT ||--o{ CONTENIR : "0,n"

    CLIENT {
        int id_client
        string nom
        string tel
        string courriel
        string ville
    }

    ANIMAL {
        int id_animal
        string nom_animal
        string espece
        string race
        date date_naissance
        float poids
    }

    VETERINAIRE {
        int id_vet
        string nom
        string specialite
    }

    VISITE {
        int id_visite
        date date_visite
    }

    TRAITEMENT {
        int id_traitement
        string libelle
        float prix_base
    }

    %% Note: Les bulles de l'image sont représentées ici par les verbes sur les liens
