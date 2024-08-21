from bot_abstract import BotAbstract

class BotNazi(BotAbstract)

    @property
    def Nombre(sefl) -> str:
        return "Bot Nazi"
    
    def jugar (self, jugada_numero: int, jugada_anterior: str) -> str:
        if jugada_anterior is None:
            return "M"
        elif jugada_anterior == "M":
            return "S"
        elif jugada_anterior == "M":
            return "M"
        else:
            return "S"
        