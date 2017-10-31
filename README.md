# DesafioSemantix
Respostas do Desafio

Pergunta 1 - A função Main no python funciona para garantir que um módulo importado não seja executado sem ser chamado.

Pergunta 4 - Solr é uma plataforma de busca open source montada a partir da biblioteca Lucene do Java, funciona com HTTP, XML e oferece APIs para Javascript JSON, Python, e Ruby.
ElasticSearch é uma ferramenta de busca open souce acessível através de uma extensiva e elaborada API, ele proporcia buscas extremamente rápidas que ajudam as aplicações de descobrimento de data.
Apache Cassandra é uma Base de dados distribuida para gerenciar grandes volumes de dados estruturados entre vários servidores
MongoDB é uma Base de dados open source que utiliza um modelo orientado a documentos, ele é uma base de dados não relacional contruiída numa arquitetura de coleções e documentos.

Pergunta 5 -Quando é realizada uma busca em solr esse pedido é encaminhado para um "request handler" que é um plugin do Solr que define a lógica do processo do pedido. Para realizar o processo o request handler chama um query parser que interpreta os termos do parâmetro do query, após isso a busca pode passar por diversas ferramentas, como por exemplo o uso de um filter query ou então o uso de highlights.
O solr também apresenta dois meios de agrupar as respostas da sua busca, sendo uma "clustering" onde as buscas são agrupadas por similaridade e a ourta "faceting" onde a organização da busca é feita em categorias baseadas nos termos indexados.Após essas etapas um componente com o nome de "response writer" chama a resposta do query.

Pergunta 6 - O parâmetro q é a query principal, os documentos recebem uma pontuação pela similaridade que tem com os termos nesse parâmetro, já o fq restringe a busca para oque foi pedido no parâmetro afetando a pontuação.

Pergunta 7 - É um paradigma de programação focado em transformar data através do uso de expressões curtas que idealmente não possuem efeitos colaterais. Ele é imutável, trabalha com funções de alto nível, gerenciamento explícito de estado. Até então não havia entrado em contato com nenhuma programação funcional, mas já ouvi falar de Haskell e Scala.

Pergunta 8 - Linguagem funcional são mais úteis para Bigdata, pois são mais fáceis de se paralelizar os códigos, sendo assim capazes de cuidar de um grande volume de data sem muito esforço, o fato dela trabalhar com variáveis imutáveis também simplifica o processo de paralelização e serialização. Podemos citar também a função MapReduce, apesar de não ser exclusiva de linguagem funcional ela essencial para o BigData.
