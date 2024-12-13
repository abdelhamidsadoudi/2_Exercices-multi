# Projet 0 : Automatisation de la Classification de Dossiers par Extension

import os
import shutil
import logging
from datetime import datetime

# Configuration des logs
log_filename = f"classification_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Fonction principale
def classify_files_by_extension(source_directory):
    if not os.path.exists(source_directory):
        logging.error(f"Le répertoire source '{source_directory}' n'existe pas.")
        print(f"Erreur : Le répertoire source '{source_directory}' n'existe pas.")
        return

    # Parcourir les fichiers dans le répertoire source
    try:
        files = [f for f in os.listdir(source_directory) if os.path.isfile(os.path.join(source_directory, f))]
    except Exception as e:
        logging.error(f"Erreur lors de l'accès au répertoire : {e}")
        print(f"Erreur : Impossible d'accéder au répertoire. {e}")
        return

    if not files:
        logging.info("Aucun fichier trouvé dans le répertoire source.")
        print("Aucun fichier à classer dans le répertoire source.")
        return

    # Classification des fichiers par extension
    for file in files:
        file_path = os.path.join(source_directory, file)
        file_extension = os.path.splitext(file)[1].lower()  # Extension en minuscule

        if not file_extension:  # Fichiers sans extension
            file_extension = "sans_extension"

        destination_folder = os.path.join(source_directory, file_extension[1:] if file_extension != "sans_extension" else file_extension)

        try:
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)  # Crée le dossier si nécessaire

            destination_path = os.path.join(destination_folder, file)
            shutil.move(file_path, destination_path)

            logging.info(f"Fichier déplacé : {file} | Origine : {file_path} | Destination : {destination_path}")
        except Exception as e:
            logging.error(f"Erreur lors du déplacement de '{file}' : {e}")

    # Résumé final
    logging.info("Classification terminée.")
    print("Classification des fichiers terminée. Consultez le fichier de log pour plus de détails.")

# Exécution du script
if __name__ == "__main__":
    print("=== Automatisation de la Classification de Fichiers ===")
    source_dir = input("Veuillez entrer le chemin complet du répertoire source : ").strip()
    classify_files_by_extension(source_dir)
    print(f"Les logs ont été enregistrés dans le fichier : {log_filename}")
