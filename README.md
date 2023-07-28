# Lembretes para usar a API Django em outra máquina:

# 1. Certifique-se de ter o Python instalado
Verifique se a outra máquina possui o Python instalado. Você pode fazer o download da versão mais recente do Python em [https://www.python.org/downloads/].
python --version

# 2. Realize as migrações do banco de dados
Primeiro, crie as migrações para os modelos do banco de dados usando o seguinte comando:
python manage.py makemigrations

# 3. Aplicar migrações do banco de dados
Em seguida, aplique as migrações usando o seguinte comando:
python manage.py migrate

# 4. Crie um superusuário
Crie um superusuário para acessar a área de administração usando o seguinte comando e siga as instruções:
python manage.py createsuperuser

# 5. Inicie o servidor
Inicie o servidor de desenvolvimento com o seguinte comando:
python manage.py runserver

# 6. Acesse a API
Acesse a API em [http://localhost:8000/api/]. Certifique-se de que o servidor esteja em execução para acessar a API corretamente.

# 7. Acesse a área de administração
Para acessar a área de administração, acesse [http://localhost:8000/admin/] e faça login usando o superusuário criado anteriormente.

# 8. Explore os endpoints da API
Utilize ferramentas como Postman ou cURL para interagir com os endpoints da API, como GET, POST, PUT e DELETE.

# 9. Documentação da API
Acesse a documentação da API em [http://localhost:8000/swagger/] ou [http://localhost:8000/redoc/] para obter informações detalhadas sobre os endpoints disponíveis.

# Lembre-se de que você precisa ter todas as dependências, como Django, Django Rest Framework e outras especificadas no arquivo "requirements.txt", instaladas na máquina para que a API funcione corretamente.**

# Nota:** Substitua "localhost" pelo endereço IP da máquina onde a API está sendo executada, caso você esteja acessando a API de outra máquina na mesma rede local.