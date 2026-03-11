# 🤖 Pipeline ETL com Python & IA Generativa (EdTech)

**Desafio de Projeto:** TOTVS DIO - Fundamentos de Engenharia de Dados e Machine Learning  
**Autora:** Roberto Santos

## 🏆 O Desafio
O objetivo deste projeto foi criar um pipeline **ETL (Extract, Transform, Load)** completo. Para criar uma solução única, reimaginei o cenário original bancário para um cenário de **Tecnologia e Ensino**.

## 🚀 O Cenário: "Assistente de Tecnologia IA"
O problema: Uma plataforma de ensino quer engajar os estudntes enviando mensagens personalizadas baseadas no curso que eles estão realizando no momento na plataforma.

### O Pipeline
1.  **Extract (Extração):**
    * Lê uma lista de IDs de estudantes em um arquivo `CSV`.
    * Consome a API da Santander Dev Week para buscar os detalhes (Nome, Curso) de cada ID.
2.  **Transform (Transformação):**
    * Utiliza a **OpenAI API (GPT-3.5)** como um "Assistente de Tecnologia Virtual".
    * Gera frases motivacionais únicas focadas na tecnologia específica que o aluno estuda (Ex: Dica de Python para quem estuda Ciências de Dados).
3.  **Load (Carregamento):**
    * Envia as mensagens geradas de volta para a API, atualizando o perfil do estudante no app.

## 🛠️ Tecnologias
* **Python:** Linguagem base.
* **Pandas:** Manipulação de dados (CSV).
* **OpenAI API:** Geração de texto por IA.
* **Requests:** Consumo de API REST.

## 📂 Como Rodar
1.  Instale as dependências: `pip install -r requirements.txt`
2.  Insira sua API Key da OpenAI no código.

3.  Execute: `python etl_tech_mentor.py`
