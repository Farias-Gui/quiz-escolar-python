from os import system
from time import sleep


def executar_quiz(perguntas, nome_materia):
    pontos = 0

    for i, p in enumerate(perguntas):
        system('cls')
        print('-=' * 40)
        print(f'--- Pergunta {i+1} de {len(perguntas)} ---')
        print(f"\n{p['pergunta']}\n")

        for opcao in p['resposta']:
            print(opcao)

        print()
        resposta = input('Digite a letra da sua resposta: ').upper().strip()

        if resposta and resposta[0] == p['certa']:
            print('✅ Resposta correta!')
            pontos += 1
        else:
            print(f"❌ Errado! A alternativa correta era {p['certa']}")

        sleep(1.3)

    return pontos


portugues = [
                {'pergunta': 'Leia a Frase: | Embora estivesse cansado, continuou estudando para prova | A palavra EMBORA indica ideia de:',
                'resposta': ['A) Causa', 'B) Consequência', 'C) Concessão', 'D) Condição'],
                'certa': 'C'
                },
                {
                'pergunta': 'Na Frase: | Os alunos atentos fizeram a atividade rapidamente | A palavra RAPIDAMENTE é classificada como:',
                'resposta': ['A) Substantivo', 'B) Adjetivo', 'C) Advérbio', 'D) Verbo'],
                'certa': 'C'
                },
                {'pergunta': 'Assinale a alternativa em que todas as palavras estão escritas corretamente:',
                'resposta': ['A) Excessão - Previlégio - Anciosidade', 'B) Exceção - Privilégio - Ansiedade', 'C) Excessão - Privilégio - Ansiedade', 'D) Excessão - Privilégio - Ansiedade'],   
                'certa': 'B'  
                },
                {'pergunta': 'Assinale a alternativa correta:',
                'resposta': ['A) Fazem dois anos que não o vejo.', 'B) Faz dois anos que não o vejo.', 'C) Fazem dois anos que não vejo ele.', 'D) Faz dois anos que não vejo ele.'],
                'certa': 'B'
                },
                {'pergunta': 'Na frase: | O tempo voa | Temos um exemplo de:',
                'resposta': ['A) Metáfora', 'B) Ironia', 'C) Eufemismo', 'D) Onomatopeia'],
                'certa': 'A'
                }
    ]

matematica = [
                {'pergunta': 'Qual é o resultado da expressão: | -5 + 12 - 3?',
                'resposta': ['A) 4', 'B) 2', 'C) 5', 'D) -4'],
                'certa': 'A'
                },
                {'pergunta': 'Resolva a equação: | 2x + 6 = 14',
                'resposta': ['A) x = 3', 'B) x = 4', 'C) x = 5', 'D) x = 6'],
                'certa': 'B'
                },
                {'pergunta': 'Um produto que custava R$ 200,00 recebeu um desconto de 10%. Qual é o novo valor do produto?',
                'resposta': ['A) R$180', 'B) R$190', 'C) R$170', 'D) R$160'],
                'certa': 'A'
                },
                {'pergunta': 'Qual é a área de um retângulo que possui base 8 cm e altura 5 cm?',
                'resposta': ['A) 13cm²', 'B) 25cm²', 'C) 40cm²', 'D) 80cm²'],
                'certa': 'C'
                },
                {'pergunta': 'Em um triângulo retângulo, os catetos medem 6 cm e 8 cm. Qual é a medida da hipotenusa?',
                'resposta': ['A) 10cm', 'B) 12cm', 'C) 14cm', 'D) 48cm'],
                'certa': 'A'
                }
    ]

historia = [
                {'pergunta': 'Qual foi o principal produto explorado pelos portugueses no início da colonização do Brasil?',
                'resposta': ['A) Ouro', 'B) Café', 'C) Pau-Brasil', 'D) Algodão'],
                'certa': 'C'
                },
                {'pergunta': 'Em que ano ocorreu a Independência do Brasil?',
                'resposta': ['A) 1500', 'B) 1822', 'C) 1889', 'D) 1789'],
                'certa': 'B'
                },
                {'pergunta': 'Quem foi o primeiro presidente do Brasil?',
                'resposta': ['A) Dom Pedro I', 'B) Getúlio Vargas', 'C) Marechal Deodoro da Fonseca', 'D) Juscelino Kubitschek'],
                'certa': 'C'
                },
                {'pergunta': 'A Segunda Guerra Mundial ocorreu entre quais anos?',
                'resposta': ['A) 1914-1918', 'B) 1939-1945', 'C) 1929-1933', 'D) 1945-1950'],
                'certa': 'B'
                },
                {'pergunta': 'Em que ano foi assinada a Lei Áurea, que aboliu a escravidão no Brasil?',
                'resposta': ['A) 1822', 'B) 1888', 'C) 1889', 'D) 1808'],
                'certa': 'B'
                }
    ] 

geografia = [
                {'pergunta': 'Qual é a maior região do Brasil em extensão territorial?',
                'resposta': ['A) Sul', 'B) Nordeste', 'C) Norte', 'D) Centro-Oeste'],
                'certa': 'C'
                },
                {'pergunta': 'Qual é o tipo de clima predominante na Região Norte do Brasil?',
                'resposta': ['A) Tropical', 'B) Semiárido', 'C) Equatorial', 'D) SubTropical'],
                'certa': 'C'
                },
                {'pergunta': 'A maior floresta tropical do mundo está localizada em qual continente?',
                'resposta': ['A) África', 'B) América do Sul', 'C) Ásia', 'D) Oceania'],
                'certa': 'B'
                },
                {'pergunta': 'Qual é o maior rio do mundo em volume de água?',
                'resposta': ['A) Rio Nilo', 'B) Rio Mississippi', 'C) Rio Amazonas', 'D) Rio São Francisco'],
                'certa': 'C'
                },
                {'pergunta': 'A globalização é caracterizada principalmente por:',
                'resposta': ['A) Isolamento entre países', 'B) Diminuição das trocas comerciais', 'C) Integração econômica, cultural e tecnológica entre países', 'D) Fim das fronteiras nacionais'],
                'certa': 'C'
                }
    ]

while True:
    print('='*25)
    print('     SEJA BEM VINDO')
    print('='*25)
    print('Vamos começar nossas perguntas!')
    print('[1] Perguntas de Lingua Portuguesa')
    print('[2] Perguntas de Matemática')
    print('[3] Perguntas de Historia')
    print('[4] Perguntas de Geografia')
    print('[5] SAIR')
    resp = int(input('Digite: '))
    if resp < 1 or resp > 5:
        print('Numero invalido')

    if resp == 1:
        tot = executar_quiz(portugues, 'Portugues')
        print(f'Parabens! Voce acertou {tot} questões de Portugues')

    elif resp == 2:
        tot = executar_quiz()
        print(f'Parabens! Voce acertou {tot} questôes de matemática')

    elif resp == 3:
        tot = executar_quiz()
        print(f'Parabens! Voce acertou {tot} questões de historia')

    elif resp == 4:
        tot = executar_quiz()
        print(f'Parabens! Voce acertou {tot} questões de geografia')

    elif resp == 5:
        print('SAINDO...')
        break
