# Perguntas
## 1. Você abriu o Youtube pra ver um vídeo. Descreva com suas palavras e com o máximo de detalhes técnicos que você puder lembrar o que acontece durante o processo.
O navegador faz a requisição da url da respectiva página,
depois disso o cliente faz uma consulta em algum servidor dns publico e recebe a resposta com o endereço do servidor do site.
com o numero de ip do servidor o navegador faz a solicitação da página com base no protocolo TCP/IP (ACK), quando essa solicitação chega ao servidor do site processa a requisição e responde (PUSH/ACK) com o html da página solicitada, junto com um video e assim o navegador renderiza o html e processa o video.
Todo o processo pode ser visto no arquivo cap.dump (tcpdump).
[tcp.dump](tcp.dump)

## 2. Faça um breve resumo da última coisa que você aprendeu. Vale seminário da faculdade, workshop, vídeo do Youtube...
Descobri que o proprio framework django pode fazer o dump dos dados do banco e criar um arquivo em vários formatos como por exemplo json e xml, não conhecia essa funcionalidade.
[Serialização de objetos Django](https://docs.djangoproject.com/pt-br/2.1/topics/serialization/)


# Front-end
A solução proposta é simples, apenas uma página contendo a tabela de jogos da copa do mundo de 2002 feita apenas com bootstrap, tentei utilizar webscrap, porem por conta do tempo abandonei a ideia inicial.

# Back-end
# Probabilidades:
12 = 2.8%
11 = 5.55%
10 = 8.33%
9 = 11%
8 = 13%
7 = 16.33%
6 = 63.88%
5 = 41%
4 = 39%
3 = 36%
2 = 33%
1 = 30%

# Checagem:
```python
    >>> python3.7 Parcheesi/resultados.py
```
