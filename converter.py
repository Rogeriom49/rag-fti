from Classes.AudioTranscription import AudioTranscription
import logging

def configurar_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('log/log.log', encoding='utf-8'),
            logging.StreamHandler()
        ],
        force=True  # Força reconfiguração se já existe
    )

def main():
    configurar_logging()

    logger = logging.getLogger(__name__) 
    try:
        with open("source/links.txt", "rb") as file:   
            for linha in file:
                linha_text = linha.decode('utf-8')
                try:
                    logger.info(f"Processando linha {linha_text.strip()}")
                    audio = AudioTranscription().transcribe(linha_text.strip())
                    logger.info(f"Arquivo {linha_text.strip()} processado com sucesso")
                except Exception as e:
                    logger.error(f"ERRO durante a execução do link {linha_text.strip()}: {str(e)}")
                    
    except FileNotFoundError:
        logger.error("Arquivo 'source/links.txt' não encontrado")
    except Exception as e:
        logger.error(f"Erro geral: {str(e)}")

    logger.info("Execução finalizada")

if __name__ == "__main__":
    main()
                
    # audio = AudioTranscription(file_path=file).transcribe_and_save()