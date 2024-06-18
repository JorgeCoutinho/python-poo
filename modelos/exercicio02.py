class ContaBancaria:
    contas = []
    def __init__(self, titular, saldo=0, ativa=False):
        self._titular = titular
        self._saldo = saldo
        self._ativa = ativa
        ContaBancaria.contas.append(self)

    def __str__(self):
        print(f'{self._titular.ljust(25)} {self._saldo.ljust(25)}')

    def ativar_conta(self):
        self._ativa = not self._ativa
    
    @classmethod
    class lista_contas(cls):
        print(f'{"Titular".ljust(25)}  {"Saldo".ljust(25)}')
        for conta in cls.contas:
            print(f'{conta._titular.ljust(25)}  {conta._saldo.ljust(25)}')

            

