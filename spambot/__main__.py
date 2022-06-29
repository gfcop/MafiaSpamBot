import sys
import glob
import importlib
import logging
from pathlib import Path
from sys import argv
from spambot import *
from spambot import MafiaBot1, MafiaBot2, MafiaBot3, MafiaBot4, MafiaBot5

def load_plugs(plugname):
    modules = Path(f"spambot/plugins/{plugname}.py")
    myfiles = f"spambot.plugins.{plugname}"
    spec = importlib.util.spec_from_file_location(myfiles, modules)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugname)
    spec.loader.exec_module(load)
    sys.modules["spambot.plugins." + plugname] = load
    print("MafiaSpamBot - Successfully Imported " + plugname)

if __name__ == "__main__":
    modules = "spambot/plugins/*.py"
    plugins = glob.glob(modules)
    for myfiles in plugins:
        with open(myfiles) as f:
            module = Path(f.name)
            plugname = module.stem
            load_plugs(plugname.replace(".py", ""))

import spambot
import spambot.userNeeds
import spambot.help
import spambot.helpers.callbackQuery

print("\n\nMafia Spam Bot Deployed Successfully!\n\n")

if len(argv) not in (1, 3, 4):
    try:
        MafiaBot1.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        MafiaBot2.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        MafiaBot3.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        MafiaBot4.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        MafiaBot5.disconnect()
    except Exception as e:
        print(e)
        pass
else:
    try:
        MafiaBot1.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        MafiaBot2.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        MafiaBot3.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        MafiaBot4.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        MafiaBot5.run_until_disconnected()
    except Exception as e:
        print(e)
        pass