# analise-log

## Você pode baixar o projeto em:
https://github.com/giovanececcon/analise-log


## Autor
Giovane Ceccon

## Para que serve o *analise-log*?

É um programa escrito em Python para buscar respostar dentro de um banco de dados, as perguntas ja estão pré-definidas, 
basta o usuario executar o arquivo python e as respostas apareceram no console.

## Como utilizar o *analise-log*?

### PRÉ-REQUISITOS:

#### Instale o VirtualBox

VirtualBox é o software que na verdade executa a máquina virtual. Você pode baixá-lo no virtualbox.org, aqui. 
Instale o plataform package para seu sistema operacional. Você não precisa do pacote de extensão ou do SDK. 
Você não precisa iniciar o VirtualBox após instalá-lo; Vagrant vai fazer isso.

Usuários Ubuntu: Se você estiver executando Ubuuntu 14.04 instale o VirtualBox usando o Ubuntu Software Center em vez disso. 
Devido a um bug reportado, instalar o VirtualBox a partir do site pode desinstalar outros softwares que você precisa.

#### Instale o Vagrant
Vargrant é o software que configura a VM e permite que você compartilhe arquivos entre seu computador host e o sistema de arquivos da VM.
Baixe no [vagrantup.com.](https://www.vagrantup.com/downloads.html) Instale a versão de seu sistema operacional.

Usuários Windows: O instalador pode lhe pedir para dar permissões de rede ao Vagrant ou para fazer uma exceção no firewall. 
Certifique-se de permitir isto.

#### Download a configuração da VM

Existem algumas maneiras diferentes para você baixar a configuração da VM.

Você pode baixar e extrair este arquivo: [FSND-Virtual-Machine.zip](https://d17h27t6h515a5.cloudfront.net/topher/2017/June/5948287e_fsnd-virtual-machine/fsnd-virtual-machine.zip) Isso lhe dará um diretório chamado FSND-Virtual-Machine. 
Ele pode ser localizado dentro de sua pasta de Downloads.

De qualquer forma, você vai acabar com um novo diretório contendo os arquivos da VM. Mude para este diretório no seu terminal com cd. Dentro, você encontrará outro diretório chamado vagrant. Altere o diretório para o diretório vagrant.

#### Iniciando a máquina virtual

De seu terminal, dentro do subdiretório vagrant, execute o comando `vagrant up`. Isso fará com que Vagrant baixe o sistema operacional Linux e instale. Isto pode demorar um pouco (muitos minutos) dependendo do quão rápida é sua conexão de Internet.

Quando `vagrant up` terminar de executar, você terá eu shell prompt de volta. Neste ponto, você pode executar `vagrant ssh` para logar eu seu Linux VM recentemente instalado!

#### Baixando os dados
Em seguida, baixe os [dados aqui](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Você precisará descompactar este arquivo após o download. O arquivo dentro é chamado de `newsdata.sql`. Coloque este arquivo no diretório `vagrant` que é compartilhado com a máquina virtual, juntamente com o arquivo `main.py`.

### Próximos passos

Depois de iniciar a Máquina Virtual, basta executar o arquivo `main.py` utilizando o comando `python main.py` e os resultados aparecerão no seu terminal.



