from pathlib import Path
import sys

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parent.parent))

from projetoti102 import database, app
from projetoti102.models import Usuario, Foto

with app.app_context():
    database.create_all()
