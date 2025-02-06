from src.commands.ab import AB
from src.commands.ac import AC
from src.commands.ad import AD
from src.commands.ar import AR
from src.commands.aw import AW

from src.commands.bc import BC
from src.commands.ba import BA
from src.commands.bn import BN

class CommandController:

    def __init__(self):
        self.commands = {
            "AB": AB, 
            "AC": AC,
            "AD": AD,
            "AW": AW,
            "AR": AR,
            "BC": BC,  
            "BA": BA,  
            "BN": BN,
        }

    def execute(self, command, args):
        if command in self.commands:
            try:
                command_instance = self.commands[command]()

                return command_instance.execute(*args)
        
            except Exception as e:
                return f"ER: {e}"
        
        else:
            return f"ER: Unknown command"