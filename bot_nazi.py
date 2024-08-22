from bot_abstract import BotAbstract

class BotNazi(BotAbstract):

    @property
    def Nombre(sefl) -> str:
        return "Bot Nazi"
    
    def jugar (self, jugada_numero: int, jugada_previa_oponente: str) -> str:
        if jugada_previa_oponente is None:
            return "M"
        elif jugada_previa_oponente == "M":
            return "S"
        elif jugada_previa_oponente == "M":
            return "M"
        else:
            return "S"
        