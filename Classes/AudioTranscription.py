import whisper
import yt_dlp
from markitdown import MarkItDown
from crewai import Crew, Process
from Classes.Agent import AgentCreator
from Classes.Task import TaskCreator
from crewai_tools import FileWriterTool

class AudioTranscription:
    def __init__(self, file_path = None):
        self.file_path = file_path
    
    def transcript_to_markdown(self, input_content, output_path):
        agent_writer = AgentCreator(llm=None).create(
            role='Especialista em Formatação de Documentos',
            goal='Estruturar documentos de forma otimizada para sistemas RAG',
            backstory="""Você é um especialista em preparar documentos para sistemas de 
            recuperação de informação, com foco em maximizar a relevância semântica."""
        )

        task_creator = TaskCreator(agent=agent_writer).create(
            description=f"""
            Analise e formate o conteudo {input_content} seguindo estas diretrizes:
            1. Adicione metadados relevantes (título, seção, tipo)
            2. Estruture o conteúdo com headers hierárquicos
            3. Identifique conceitos-chave e termos técnicos
            4. Crie resumos para seções longas
            5. Mantenha contexto suficiente em cada chunk
            """,
            expected_output="Documento estruturado e otimizado para RAG",
            output_file=output_path,
        )

        crew = Crew(
            agents=[agent_writer],
            tasks=[task_creator],
            process=Process.sequential
        )

        crew.kickoff()


    def transcribe_and_save(self):
        model = whisper.load_model("turbo")
        result = model.transcribe(self.file_path)
        self.transcript_to_markdown(result['text'], output_path="output/entrega_futura.md")
        # with open("output/entrega_futura_2.md", "w") as file:
        #     file.write(result['text'])
        return True
    
    def transcribe(self, url):
        ydl_options = {
            'format':'bestaudio/best',
            'outtmpl':'-'
        }
        
        with yt_dlp.YoutubeDL(ydl_options) as ydl:
            info = ydl.extract_info(url=url, download=False)
            # print(info.keys())
            url_audio = info['url']
            model = whisper.load_model("turbo")
            result = model.transcribe(url_audio, language='pt')
            self.transcript_to_markdown(result['text'], output_path=f"output/{info['title']}.md")
            # with open("output/entrega_futura.md", "w") as file:
            #     file.write(result['text'])