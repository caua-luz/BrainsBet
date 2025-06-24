🧠 BrainsBet – Um Aplicativo de Incentivo ao Estudo
Projeto desenvolvido por Cauã Luz A. de Almeida
Engenharia de Controle e Automação - UFMG

📌 Descrição
O BrainsBet é um aplicativo educacional desenvolvido em Python utilizando Programação Orientada a Objetos (POO) e banco de dados em JSON, com o objetivo de incentivar o estudo e combater a evasão nos cursos de engenharia.

A proposta do app é transformar a rotina de estudos em uma experiência interativa, utilizando recompensas virtuais (BrainCoins), competição entre estudantes e torneios acadêmicos baseados em disciplinas reais das engenharias.

🎯 Objetivos
Incentivar estudantes de engenharia a manterem o foco nos estudos.

Aumentar o engajamento por meio de mecânicas de gamificação.

Fornecer uma ferramenta educacional simples, acessível e escalável.

⚙️ Funcionalidades
👤 Registro e Login
Registro de novos usuários com base na sua instituição e curso.

Login com verificação de dados persistidos em JSON.

🎮 Modos de Estudo
Solo: o estudante estuda individualmente e ganha BrainCoins de acordo com a dificuldade da matéria.

Multiplayer: os estudantes participam de torneios entre si, organizados por outros usuários.

🏆 Torneios Acadêmicos
Criação e gerenciamento de torneios por administradores.

Participação de outros usuários como concorrentes.

Recompensa em BrainCoins com base no desempenho e dificuldade da matéria.

Encerramento de torneios com distribuição de prêmios.

📚 Gerenciamento Acadêmico
Inserção e remoção de matérias cursadas.

Classificação das matérias por dificuldade (peso).

📁 Estrutura do Projeto
main.py: Arquivo principal para execução do app.

Aluno_Engenharia.py: Define as classes base dos alunos e seus comportamentos.

Materia.py: Banco local de matérias para cada curso.

Torneio.py: Implementação da lógica de criação e gestão de torneios.

pessoas.json: Base de dados com os usuários registrados.

torneios.json: Base de dados com os torneios ativos ou encerrados.

🖼️ Diagramas
O projeto foi modelado com base em:

Diagramas de Código: Fluxo de funcionalidades principais.

Diagramas UML: Relação entre as classes de Aluno, Torneio, Materia, etc.

🛠️ Tecnologias Utilizadas
📌 Python 3.x

📦 JSON para persistência de dados

💡 Paradigma de Programação Orientada a Objetos

🚀 Como Executar
Clone este repositório:

bash
Copiar
Editar
git clone https://github.com/seu-usuario/BrainsBet.git
cd BrainsBet
Execute o aplicativo:

bash
Copiar
Editar
python main.py
Siga as instruções no terminal para registrar ou logar.

📈 Trabalhos Futuros
Adição de interface gráfica (GUI) para maior usabilidade.

Criação de versão web com back-end baseado neste protótipo.

Novas funcionalidades administrativas (remover usuário, editar torneios, etc).

👨‍🎓 Autor
Cauã Luz A. de Almeida
Graduando em Engenharia de Controle e Automação - UFMG
📫 caualuz18@ufmg.br

🧠 Referências Teóricas
Este projeto se fundamenta em teorias clássicas da psicologia social, como o behaviorismo de Skinner, e explora os pilares de socialização, competitividade e recompensa para motivar o engajamento estudantil.
