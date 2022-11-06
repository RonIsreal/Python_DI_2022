

class Membros:

    def __init__(self):

        self.membros = [{'nome':'ronny',
                'apelidos':['ron','judeu','soldado corneta'],
                'psn':'RonIsreal',
                'votos':{'call of duty: warzone': 0,
                        'dying light': 0,
                        'predator': 0,
                        'star wars battlefront 2': 0,
                        'ghost of tsushima: legends': 0,
                        'path of exile': 0,
                        'naruto to boruto: shinobi striker': 0,
                        'titanfall 2': 0}
                },
                {'nome':'wagner junior',
                'apelidos':['junao','juno','rouba loot'],
                'psn':'wagnerjunior08',
                'votos':{'warzone': 0,
                        'dying light': 0,
                        'predator': 0,
                        'star wars battlefront': 0,
                        'ghost of tsushima legends': 0,
                        'path of exile': 0,
                        'naruto to boruto': 0,
                        'titanfall2': 0}
                },
               {'nome': 'rodrigo',
                'apelidos': ['jamaicon', 'himura', 'mamajeibs'],
                'psn': 'RDG_369',
                'votos':{'warzone': 0,
                        'dying light': 0,
                        'predator': 0,
                        'star wars battlefront': 0,
                        'ghost of tsushima legends': 0,
                        'path of exile': 0,
                        'naruto to boruto': 0,
                        'titanfall2': 0}
                },
                {'nome': 'marcel',
                'apelidos': ['sznajder', 'sznajda', 'gardenajder'],
                'psn': 'martchee',
                'votos':{'warzone': 0,
                        'dying light': 0,
                        'predator': 0,
                        'star wars battlefront': 0,
                        'ghost of tsushima legends': 0,
                        'path of exile': 0,
                        'naruto to boruto': 0,
                        'titanfall2': 0}
                },
                {'nome': 'leonardo',
                'apelidos': ['leo', 'leozera', 'atrasado'],
                'psn': 'Leowfa',
                'votos':{'warzone': 0,
                        'dying light': 0,
                        'predator': 0,
                        'star wars battlefront': 0,
                        'ghost of tsushima legends': 0,
                        'path of exile': 0,
                        'naruto to boruto': 0,
                        'titanfall2': 0}
                },
                {'nome': 'rafael',
                'apelidos': ['rafa', 'marombinha', 'deixa que eu cubro'],
                'psn': 'RafaMaedaDevidE',
                'votos':{'warzone': 0,
                        'dying light': 0,
                        'predator': 0,
                        'star wars battlefront': 0,
                        'ghost of tsushima legends': 0,
                        'path of exile': 0,
                        'naruto to boruto': 0,
                        'titanfall2': 0}
                },
                {'nome': 'raul',
                'apelidos': ['raulzito', 'encoleirado'],
                'psn': 'MaedaDevidE',
                'votos':{'warzone': 0,
                        'dying light': 0,
                        'predator': 0,
                        'star wars battlefront': 0,
                        'ghost of tsushima legends': 0,
                        'path of exile': 0,
                        'naruto to boruto': 0,
                        'titanfall2': 0}
                },
                {'nome': 'richard',
                'apelidos': ['ricky', 'vrickale', 'smoky joint', 'sr. da razao'],
                'psn': 'RickyHero85',
                'votos':{'warzone': 0,
                        'dying light': 0,
                        'predator': 0,
                        'star wars battlefront': 0,
                        'ghost of tsushima legends': 0,
                        'path of exile': 0,
                        'naruto to boruto': 0,
                        'titanfall2': 0}
                },
                {'nome': 'renan',
                'apelidos': ['lobo', 'lobete', 'cadelo'],
                'psn': 'Lobo-Norte32',
                'votos':{'warzone': 0,
                        'dying light': 0,
                        'predator': 0,
                        'star wars battlefront': 0,
                        'ghost of tsushima legends': 0,
                        'path of exile': 0,
                        'naruto to boruto': 0,
                        'titanfall2': 0}
                },
                {'nome': 'gabriel',
                'apelidos': ['poo', 'gasparzinho', 'traveco lover'],
                'psn': 'Usa Xbosta',
                'votos':{'call of duty: warzone': 0,
                        'dying light': 0,
                        'predator': 0,
                        'star wars battlefront II': 0,
                        'ghost of tsushima - legends': 0,
                        'path of exile': 0,
                        'naruto to boruto: shinobi striker': 0,
                        'titanfall 2': 0}
                }
               ]

    def available_games(self):
        print(f"Esses sao os jogos em que voce pode eleger o melhor jogador do regimento:")
        jogos = list(self.membros[0]['votos'].keys())
        for game in jogos:
            print(game.title())

    def vote_games(self):
        pass

brabo6 = Membros()
brabo6.available_games()

