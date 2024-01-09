import prendrefichier
import final

class MainExecution:
    def __init__(self):
        # Initialiser les paramètres nécessaires ici
        self.aws_access_key_id = 'AKIAWUBR7KZH34UZJA2F'
        self.aws_secret_access_key = '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'
        self.bucket_name = 'devoirpythonan'
        self.file_name_s3 = 'reponses_sondage.json'
        self.local_file_path = 'reponses_sondage.json'

    def run(self):        
        restart=True
        while restart:
            gestion_fichier_s3 = prendrefichier.GestionFichierS3(self.aws_access_key_id, self.aws_secret_access_key, self.bucket_name)
            gestion_fichier_s3.download_file_from_s3(self.file_name_s3, self.local_file_path)
            gestion_sondage = final.GestionSondage()
            gestion_sondage.repondre_sondage()
            choix=input("Voulez-vous continuer a entrer des nom(O=Oui/N=Non): ")
            choix=choix.upper()
            while choix!="O" and choix!="N":
                choix=input("Voulez-vous continuer a entrer des nom(O=Oui/N=Non): ")
            if choix=="N":
                restart=False
        

# Exécution de la classe MainExecution

if __name__ == "__main__":
    main_execution = MainExecution()
    main_execution.run()