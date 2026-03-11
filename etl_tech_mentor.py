import pandas as pd
import requests
import openai
import json

# ==========================================
# ⚙️ CONFIGURAÇÕES
# ==========================================
# IMPORTANTE: Para testar, insira sua chave. 
OPENAI_API_KEY = "TODO_INSIRA_SUA_KEY_AQUI" 

# URL da API do desafio (Simulada para este cenário)
API_URL = "https://sdw-2023-prd.up.railway.app/users"

# Configura a chave da OpenAI
openai.api_key = OPENAI_API_KEY


# 📥 1. EXTRACT (Extração)
# ==========================================
def get_user_data(id):
    """ Busca dados do usuário na API. """
    try:
        response = requests.get(f"{API_URL}/{id}")
        return response.json() if response.status_code == 200 else None
    except:
        return None

# Lê o arquivo CSV com os IDs dos alunos alvo
df = pd.read_csv('alunos.csv')
user_ids = df['UserID'].tolist()

# Obtém os dados de cada usuário válido
users = [user for id in user_ids if (user := get_user_data(id)) is not None]
print(f"✅ {len(users)} usuários extraídos com sucesso.")

# ==========================================
# 🧠 2. TRANSFORM (Transformação com IA)
# ==========================================
def generate_ai_news(user):
    """ Gera uma mensagem de mentoria personalizada usando GPT-4. """
    
    # PROMPT ÚNICO: Personalizado para o contexto de Educação e Tecnologia
    prompt = f"Você é um mentor de tecnologia. Crie uma frase curta e motivacional (max 100 caracteres) para {user['name']} que está estudando {user['course']}. Inclua um emoji técnico."

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um especialista em EdTech."},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content.strip('\"')
    except Exception as e:
        return "Continue codando! O futuro é tech. 🚀"

for user in users:
    news = generate_ai_news(user)
    print(f"🤖 Dica gerada para {user['name']}: {news}")
    
    # Estrutura a mensagem para devolver à API (formato News)
    user['news'].append({
        "icon": "https://digitalinnovationone.github.io/santander-2023-net-bootcamp/icons/credit.svg",
        "description": news
    })

# ==========================================
# 📤 3. LOAD (Carregamento)
# ==========================================
def update_user(user):
    """ Envia os dados enriquecidos de volta para a API. """
    try:
        response = requests.put(f"{API_URL}/{user['id']}", json=user)
        return True if response.status_code == 200 else False
    except:
        return False

# Atualiza na API
for user in users:
    success = update_user(user)

    print(f"User {user['name']} atualizado? {'✅ Sim' if success else '❌ Falha'}")

