## Juntos Somos Mais - teste

### O que foi feito?

1. Transformacao dos contatos telefonicos para o formato `E.164`.
2. Inserido a nacionalidade no payload para cada objeto.
3. Alterado os valores de `gender` de `female` e `male` para `f` e `m`.
4. Retirado o campo `age` de `dob` e `registered`.
5. Modificado os campos `phone` e `cell` para `telephoneNumbers` e `mobileNumbers` e tambem adicionado os valores dentro de uma lista.
6. Regra de typo de usuarios incluida.*
7. Sistema de paginacao como os valores `pageNumber`, `pageSize` e  `totalCount`. Tomei a liberdade de adicionar outros dois campos como `nextPage` e `previousPage` como link para a proxima ou pagina anterior.
8. Foi adicionado testes com coverage para api.
9. Foi adicionado `cors_headers` com `whitelable` dando acesso a requests.


## Como testar:
Pode-se usar tanto o docker para subir o container quanto criando um virtual environment e instalando o requirements.

1. No root do projeto crie um arquivo `.env` e adicione os seguintes valores:
```
DATABASE_URL=postgresql://tutorial:tutorial@db/tutorial
REDIS_URL=redis://redis/0
DJANGO_SECRET_KEY=django-insecure-q+yoifn3#z_m0wp43cra=j+7inz^3xz5i76ik110xaf97gqxv(
DJANGO_DEBUG=True
```

2. No root do projeto adicione o seguinte comando:
```
$ docker-compose up --build
```



* Nao entendi perfeitamente como era para passar/acessar as coordenadas em termos de localizacao. Se era para gerar novos enderecos e inclui-los nos campos de location baseados nas coordenadas passadas no teste e depois tipa-los baseados nesses valores gerados. O que fiz foi unir os dois tipos de usuarios `SPECIAL` e criar uma funcao `Serivices.check_user_type({"longitude":"latitude"})` para checar se o mesmo era `special`, `normal` ou `laborious`.


