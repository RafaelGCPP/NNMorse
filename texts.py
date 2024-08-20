import random
from typing import List, Optional

_ANATEL_TEXTS=[
    "SERVICO DE RADIODIFUSAO EH DEFINIDO COMO UM SERVICO DE RADIOCOMUNICACAO CUJAS EMISSOES ESTAO DESTINADAS A RECEPCAO DIRETA PELO PUBLICO EM GERAL PT", 
    "A ARCA DE NOE QUE PODE NOS SALVAR DO DILUVIO DE PAPEL EH O MICROFILME, QUE TEM O CONDAO NAO APENAS DE RESOLVER ESTE, MAS TODOS OS PROBLEMAS DE ARQUIVO.", 
    "EH NECESSARIO O USO DE RADIOFAROIS, ESTACOES DE EMBARCACOES E DISPOSITIVOS DE SALVAMENTO PARA SEGURANCA DA NAVEGACAO E SALVAR VIDAS HUMANAS NO MAR PT", 
    "EXISTINDO COMUNICACAO ENTRE DOIS PONTOS PODEMOS TRANSMITIR A MENSAGEM DESEJADA ATRAVES DE CODIGOS OU DA PROPRIA VOZ USANDO VOZ TEMOS A TELEFONIA.", 
    "A HISTORIA TEM NOS ENSINADO QUE UM LIBERALISMO EXCESSIVO CONDUZ A DESORDEM E A INTRANQUILIDADE, PELO MENOS ATE O ATUAL ESTAGIO DA EVOLUCAO HUMANA PT", 
    "ADMINISTRAR ESPECTRO DE RADIOFREQUENCIA IMPLICA EM GERIR RACIONALMENTE A UTILIZACAO DE DIVERSAS FREQUENCIAS DISTRIBUIDAS PELOS SEUS USUARIOS.", 
    "A ULTIMA CONFERENCIA DA U.I.T VG QUE REVISOU O PLANO DE DISTRIBUICAO DE FREQUENCIAS PARA O SERVICO MOVEL AERONAUTICO VG FOI REALIZADA NO ANO DE 1966.", 
    "NUM RITUAL QUE SE REPETE TODOS OS ANOS, EM OLIMPIA, NA GRECIA, A TOCHA OLIMPICA EH ACESA, PARTINDO LOGO EM SEGUIDA PARA O PAIS SEDE DOS JOGOS OLIMPICOS PT", 
    "A INDEXACAO EH O FATOR BASICO VG FUNDAMENTAL VG INDISPENSAVEL VG PARA O EXITO DE QUALQUER SISTEMA DE MICROFILMAGEM OU DE ARMAZENAMENTO EM COMPUTADOR.", 
    "MEIO UTILIZADO PARA A PROPAGACAO DAS ONDAS ELETROMAGNETICAS VG EH A CAMADA ATMOSFERICA ADJACENTE A SUPERFICIE TERRESTRE DENOMINADA TROPOSFERA PT", 
    "A FIBRA OTICA CONSISTE, EM PRINCIPIO, NUM NUCLEO INTERNO DE VIDRO DE ALTISSIMO GRAU DE PUREZA ENVOLVIDO POR UMA CAMADA EXTERNA OU INVOLUCRO DE VIDRO.", 
    "REGULAMENTO DE RADIOCOMUNICACOES DA UIT, COBRE A FAIXA DE ESPECTRO ELETRICO DE 1O KHZ A 275 KHZ E ESTABELECE ATRIBUICOES A 41 DIFERENTES SERVICOS PT", 
    "A VOZ DO COMANDO SOH CHEGA ATE ONDE VAI O FIO TELEFONICO OU ONDE CHEGAM AS ONDAS ELETROMAGNETICAS DOS CONJUNTOS RADIO E EQUIPAMENTOS DE MULTICANAIS PT", 
    "RADIO, NO BRASIL, FOI UTILIZADO ANTES DA PRIMEIRA GUERRA MUNDIAL, PELA REPARTICAO GERAL DOS TELEGRAFOS, PELO EXERCITO E PELA MARINHA BRASILEIRA.", 
    "VIVER EH ATRAVES DE UM SORRISO BUSCAR O OUTRO. EH SABER PARTIR E SABER VOLTAR. EH TRANSFORMAR SONHOS EM REALIDADES CERTOS DE QUE SERIA TOLICE INVERTE-LOS.", 
    "VOCE SABIA QUE: EM 1874 FOI LANCADO O PRIMEIRO CABO SUBMARINO E QUE ESTE LIGAVA RECIFE E LISBOA? QUE O BRASIL FOI O PRIMEIRO PAIS DO MUNDO A EMITIR SELOS?", 
    "VOCE SABIA QUE: O TELEGRAFO FOI INVENTADO NO ANO DE 1838 POR SAMUEL MORRE E QUE A PRIMEIRA MENSAGEM TRANSMITIDA ATRAVES DELE FOI: ATENCAO UNIVERSO?", 
    "A COMUNICACAO PODE SER DEFINIDA COMO A EMISSAO E A RECEPCAO DE INFORMACOES, IDEIAS, EMOCOES, ETC, POR MEIO DO USO DE SIMBOLOS, DE IMAGENS, SONS, ETC PT", 
    "VIVER EH IR CONSUMINDO O AMANHA, NA EXPECTATIVA DE UM OUTRO AMANHA. EH PERCORRER CAMINHOS E ESTRADAS ABRACANDO A CADA CHEGADA O MEDO E A CORAGEM.", 
    "CADA UM DEVE FABRICAR SEU SEGREDO E GUARDA-LO O PERFUME DA FLOR, POR EXEMPLO, EH UM SEGREDO. SE A ARRANCAMOS DO JARDIM ELA MORRE. E MORTA AINDA PERFUMA.", 
    "SABER VIVER NAO EH VIAJAR PELO ESPACO QUANDO NO CHAO SE TEM TANTO PARA ENSINAR TANTO PARA APRENDER. SABER VIVER EH SONHAR SEM SE AFASTAR, SEM SE ESQUECER.", 
    "SISTEMA DE TELECOMUNICACOES VG EM NOSSO PAIS VG DEPENDE DE UM GRANDE NUMERO DE FATORES DISTINTOS VG IMPLICANDO EM CONTINUA REVISAO E ATUALIZACAO PT", 
    "ATRAVES DAS COMUNICACOES, O HOMEM EVITA A SOLIDAO FRUSTRANTE DO ISOLAMENTO E, AINDA, ENCONTRA UM MEIO DE SATISFAZER AS SUAS NECESSIDADES E DESEJOS.", 
    "A INCAPACIDADE PARA AFIRMAR A SUPREMACIA DA POLITICA SOBRE A TECNOLOGIA, EH UM FENOMENO BASTANTE ALARMANTE E CADA VEZ MAIS PERIGOSO NO MUNDO MODERNO.", 
    "COMPUTADOR CONTINUARA INVADINDO TODOS OS DOMINIOS DA VIDA HUMANA E, PARTICULARMENTE AS TELECOMUNICACOES. SERA BOM QUE TODOS APRENDAM A PALAVRA.", 
    "ORA AQUI TENS, MEU CARO CIDADAO: SUPOE QUE TU QUERES TER NA TUA SALA A IMAGEM DE NAPOLEAO I PASSANDO PELOS ALPES (ESTAS FANTASIAS SAO-TE PERMITIDAS) PT", 
    "VIDA NAO EH O QUE GERA NO VENTRE E FINALIZA NO TUMULO, PORQUE ESTES ESPACOS DE ANO SAO INSTANTES DE UMA VIDA SECULAR E ETERNA EH ESTA MESQUINHA EXISTENCIA.", 
    "NINGUEM SERA SUJEITO A INTERFERENCIA EM SUA VIDA PRIVADA, SUA FAMILIA, EM SEU LUGAR OU SUA CORRESPONDENCIA, NEM A ATAQUES A SUA HONRA E SUA REPUTACAO.", 
    "MINUTO DIVIDE O CRESCER DA EXISTENCIA E O SEU ACORDAR; EH A PRIMEIRA CHAMA QUE ILUMINA OS RECANTOS DA ALMA E O PRIMEIRO SOM ENCANTADO NA PRIMEIRA CORDA.", 
    "A SOCIEDADE DA INFORMACAO IRA DEFLAGRAR VG NECESSARIAMENTE VG CONFLITOS CULTURAIS PT O PRIMEIRO DELES VG SERA AS AMEACAS DA INVASAO DA PRIVACIDADE PT", 
    "OS PRODUTOS ARTESANAIS ESTAO INVADINDO O MERCADO E OS ARTESOES, QUE, ALEM DA ADMIRACAO, ESTAO GANHANDO MAIS DINHEIRO, MUITO MAIS DO QUE PLANEJARAM.", 
    "OS BRASILEIROS FICARAM DESCONFIADOS, EM MARCO DE 1994. QUANDO O GOVERNO FEDERAL ANUNCIOU UM PACOTE DE MEDIDAS, QUE MUDAVA NOVAMENTE O NOME DA MOEDA.", 
    "EM 1984, ARMACAO DE BUZIOS ERA APENAS UM COLAR DE PRAIAS, ILHAS E ENSEADAS, NÃO MUITO DIFERENTE DOS TEMPOS EM QUE FORA UM PORTO DE PIRATAS E BALEEIROS.", 
    "SAI ANO, ENTRA ANO E A TELEVISAO BRASILEIRA NÃO CONSEGUE DAR CABO DE UM TIPO DE ATRACAO QUE REMONTA A EPOCA DE OURO DO RADIO: O PROGRAMA DE CALOUROS AO VIVO.", 
    "O PROGRAMA SITIO DO PICA-PAU AMARELO VIRA MANIA ENTRE AS CRIANCAS. PROFESSORES APROVEITAM PARA ENSINAR MITOLOGIA, HISTORIA E CULTURA BRASILEIRA.", 
    "MONTEIRO LOBATO ESCREVEU 17 OBRAS E CONQUISTA AS CRIANCAS MESMO NA ERA POKEMON, E AINDA AJUDA PROFESSORES A ENSINAR TEMAS COMPLEXOS COMO FOLCLORE."
]


def get_random_text(text_list: Optional[List[str]] = _ANATEL_TEXTS) -> str:
    """
    Returns a random text from the given list of texts.

    Parameters:
    text_list (List[str], optional): A list of texts to choose from. If not provided, the default list _ANATEL_TEXTS will be used.

    Returns:
    str: A randomly selected text from the list.
    """
    return random.choice(text_list)

