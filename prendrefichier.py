import boto3
import os

class GestionFichierS3:
    def __init__(self, aws_access_key_id, aws_secret_access_key, bucket_name):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.bucket_name = bucket_name

    def download_file_from_s3(self, file_name_s3, local_file_path):
        try:
            s3 = boto3.client('s3', aws_access_key_id=self.aws_access_key_id, aws_secret_access_key=self.aws_secret_access_key)
            s3.download_file(self.bucket_name, file_name_s3, local_file_path)
            print(f"Le fichier {file_name_s3} a été téléchargé avec succès vers {local_file_path}")            
        except Exception as e:
            print(f"Fichier non existant dans AWS")

