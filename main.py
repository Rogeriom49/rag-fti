import os
from crewai import Crew, Process
from dotenv import load_dotenv
from Classes.LLM import LLMCreator 
from Classes.Agent import AgentCreator
from Classes.Task import TaskCreator
from Classes.AudioTranscription import AudioTranscription
from crewai_tools import DirectorySearchTool
import streamlit as st
import time

load_dotenv()

def stream_data(text):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.05)



llm = LLMCreator(model=os.getenv("MODEL"), key=os.getenv("GEMINI_API_KEY")).create()
# transcricao = AudioTranscription(file_path="source/entrega_futura.mp3").transcribe()

directory_serch = DirectorySearchTool(
    directory='output',
    file_types=['.md'],
    config=dict(
        llm=dict(
            provider='google',
            config=dict(
                model='models/gemini-2.0-flash-001',
                api_key=os.getenv("GEMINI_API_KEY"),
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model='models/text-embedding-004',
                # api_key=os.getenv("GEMINI_API_KEY"),
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )    
)

researcher_agent = AgentCreator(llm=llm).create(
    role='Pesquisador de Documentos',
    goal='Encontrar informações relevantes nos documentos da base de conhecimento. As informações apresentadas devem estar apenas na documentação disponibilizada.',
    backstory="""Você é um especialista em pesquisa de documentos. Sua função é 
    encontrar informações precisas e relevantes nos documentos disponíveis para 
    responder às perguntas dos usuários.""",
    tools=[directory_serch],
    verbose=True
)

analyst_agent = AgentCreator(llm=llm).create(
    role='Analista de Informações',
    goal='Analisar e sintetizar as informações encontradas para gerar respostas precisas. As informações apresentadas devem estar apenas na documentação disponibilizada.',
    backstory="""Você é um analista experiente que consegue interpretar informações 
    complexas e fornecer respostas claras e bem estruturadas baseadas nos dados 
    disponíveis.""",
    verbose=True    
)

researcher_task = TaskCreator(agent=researcher_agent).create(
    description="""Pesquise na base de conhecimento informações relevantes sobre: {query}
    
    Use a ferramenta de busca para encontrar documentos que contenham informações 
    relacionadas à pergunta. Foque em encontrar dados específicos, exemplos, 
    definições e contexto relevante. As informações apresentadas devem estar apenas na documentação disponibilizada.
    
    Retorne os trechos mais relevantes encontrados com referência aos arquivos fonte.""",
    expected_output="Lista de informações relevantes encontradas nos documentos com suas respectivas fontes, as respostas devem sempre estar em português do Brasil"
)

analyst_task = TaskCreator(agent=analyst_agent).create(
    description="""Baseado nas informações coletadas pelo pesquisador, forneça uma 
    resposta completa e bem estruturada para a pergunta: {query}
    
    Sua resposta deve:
    1. Ser clara e objetiva
    2. Incluir exemplos quando relevante
    3. Citar as fontes das informações
    4. Indicar se alguma informação não foi encontrada na base de conhecimento
    
    Se as informações forem insuficientes, indique claramente essa limitação. As informações apresentadas devem estar apenas na documentação disponibilizada.""",
    context=[researcher_task],  # Depende da task anterior
    expected_output="Resposta completa e bem estruturada com citação de fontes, as respostas devem sempre estar em português do Brasil"
)

crew = Crew(
    agents=[researcher_agent, analyst_agent],
    tasks=[researcher_task, analyst_task],
    process=Process.sequential,
    verbose=True
)

st.title("Assistente Farol TI")

tab1, tab2 = st.tabs(["Asisstente", "Enviar arquivos"])

with tab1:
    prompt = st.chat_input("Digite sua pergunta")
    with st.chat_message("Farol TI"):
        if(prompt != None):
            if not os.path.exists:
                print("ERRO: Diretório 'output' não encontrado!")
            else:
                try:
                    with st.spinner("Processando..."):
                        crew_output = crew.kickoff(inputs={"query": prompt})
                        st.write_stream(stream_data(crew_output.raw))
                except Exception as e:
                    print(f"ERRO durante a execução: {str(e)}")
                    print("Verifique se:")
                    print("1. O diretório 'output' existe e contém arquivos .md")
                    print("2. A API key do Gemini está correta")
                    print("3. Todas as dependências estão instaladas")            