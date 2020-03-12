#Banco de dados improvisado e mocado para o BrasaBot
class Extratos:
        def __init__(self):
                self.extractM = "\
                        05/03/2020    Jogos       R$ 250.00\n\
                        16/03/2020    Cantina     R$ 10.00\n \
                        17/03/2020    Papelaria   R$ 15.00\n\
                        20/03/2020    Eventos     R$ 300.00\n\
                        25/03/2020    Gasolina    R$ 170.00\n\
                        27/03/2020    Mercado     R$ 150.00\n\
                        Total:                    R$ 895.00\n\
                        "
                self.extractW = "\
                        20/03/2020    Eventos     R$ 300.00\n\
                        25/03/2020    Gasolina    R$ 170.00\n\
                        27/03/2020    Mercado     R$ 150.00\n\
                        27/03/2020    Lojinha     R$ 7.00\n\
                        Total:                    R$ 627.00\
                        "
                self.extractD = "\
                        27/03/2020    Mercado     R$ 150.00\n\
                        27/03/2020    Lojinha     R$ 7.00\n\
                        Total:                    R$ 157.00\n\
                        "
class Usuario:
    def __init__(self, cpf, name, balance, extractM, extractW, extractD):
        self.cpf = cpf
        self.name = name
        self.balance = balance
        self.extractM = extractM
        self.extractW = extractW
        self.extractD = extractD
"""
extractM = "\
        05/03/2020    Jogos       R$ 250.00\n\
        16/03/2020    Cantina     R$ 10.00\n \
        17/03/2020    Papelaria   R$ 15.00\n\
        20/03/2020    Eventos     R$ 300.00\n\
        25/03/2020    Gasolina    R$ 170.00\n\
        27/03/2020    Mercado     R$ 150.00\n\
        Total:                    R$ 895.00\n\
        "
extractW = "\
        20/03/2020    Eventos     R$ 300.00\n\
        25/03/2020    Gasolina    R$ 170.00\n\
        27/03/2020    Mercado     R$ 150.00\n\
        27/03/2020    Lojinha     R$ 7.00\n\
        Total:                    R$ 627.00\
        "
extractD = "\
        27/03/2020    Mercado     R$ 150.00\n\
        27/03/2020    Lojinha     R$ 7.00\n\
        Total:                    R$ 157.00\n\
        "

usuario1 = Usuario(999, "Cleber", 1400, extractM, extractW, extractD)
usuario2 = Usuario(888, "Joana", 7000, extractM, extractW, extractD)
usuario3 = Usuario(777, "Lucas", -200 , extractM, extractW, extractD)
"""






