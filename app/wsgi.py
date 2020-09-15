import os
from .run import app

port = int(os.environ.get("PORT", 5000))

application = app.run(host="0.0.0.0", port=port, debug=True)
