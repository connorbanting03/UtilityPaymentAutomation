from EnbridgeGasAutopay import EnbridgeGasPayBot
from EnercareAutopay import EnercarePayBot
from HydroOttawaAutopay import HydroOttawaLoginPayBot
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    EnbridgeGasPayBot().run()
    print("test")
    EnercarePayBot().run()
    HydroOttawaLoginPayBot().run()