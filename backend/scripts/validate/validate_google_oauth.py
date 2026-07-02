from pathlib import Path
import sys

BACKEND_ROOT = Path(__file__).resolve().parents[2]

sys.path.insert(0, str(BACKEND_ROOT))

from scripts.validate.validators import GoogleOAuthValidator

if __name__ == "__main__":

    GoogleOAuthValidator().run()
