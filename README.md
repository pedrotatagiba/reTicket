# ReTicket

Plataforma colaborativa para revenda de ingressos.

##  Integrantes

- João Castro  
- Pedro Tatagiba  
- Diogo Augusto  
- João Rosauro  

##  Descrição:

A **reTicket** é uma plataforma online que facilita a revenda de ingressos de maneira segura. Os usuários podem disponibilizar seus ingressos em uma aba da comunidade, permitindo que outros interessados vejam e comprem. Ao clicar em um ingresso, o comprador será direcionado para uma página com mais detalhes da oferta e poderá concluir a transação. Caso o cliente desista da compra ele pode cancelar a compra e continuar navegando na plataforma para achar outros ingressos. Haverá uma aba também para o usuario colocar seu ingresso a venda, onde ele colocorá o ingresso, a data do evento e o valor que será revendido e um botão para publicar. Logo no momento que entrar na plataforma, haverá uma página para o usuário se logar our criar uma conta. 


- Criar o repesitório

```sh
mkdir reTicket
cd reTicket
```

- Crie o ambiente virtual

```sh
python -m venv venv
source venv/bin/activate
```

- Instale requirements.txt

```sh
pip install -r requirements.txt
```

- Crie o projeto Ingressos

```sh
django-admin startproject Ingressos
```

- Executar o projeto

```sh
cd Ingressos
python manage.py runserver
```