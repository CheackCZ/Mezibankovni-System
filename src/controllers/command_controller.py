from src.commands.ab import AB
from src.commands.ac import AC
from src.commands.ad import AD
from src.commands.ar import AR
from src.commands.aw import AW

from src.commands.bc import BC
from src.commands.ba import BA
from src.commands.bn import BN

class CommandController:
    """
    Handles the execution of various commands in the system.
    """

    def __init__(self):
        """
        Initializes the command controller and maps command identifiers to their corresponding classes.
        """
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
        """
        Executes a given command with the provided arguments.

        :param command (str): The command identifier to execute.
        :param args (list): A list of arguments for the command.
        
        :return: The result of the command execution or an error message.
        """
        if command in self.commands:
            try:
                command_instance = self.commands[command]()

                return command_instance.execute(*args)
        
            except Exception as e:
                return f"ER {e}"
        
        else:
            return f"ER Unknown command"