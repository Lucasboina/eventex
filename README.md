# Eventex
Sistema de eventos encomendado

## Como desenvolver

 1. Clone o repositório.
 2. Crie um virtual env com python 3.5.
 3. Ative o virtual env.
 4. Istale as dependencias.
 5. Configure a intância com .env
 6. Execute os testes.


```console
git clone git@github.com:lucasboina/eventex.git wttd
cd wttd 
python -m venv .venv
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python3 manage.py test
```
## Como fazer o deploy

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY para o projeto.
4. Defina DEBUG = False 
5. Configure o serviço de email.
6. Envie o código para o heroku


```console
heroku:create minhainstancia
heroku config:push
heroku config:set SECRET_KEY= `python3 contrib/secret_gen.py`
heroku config:set DEBUG=False
#Configuro email
git push heroku master --force
```