import logging
import os
import sys

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "src"))
)

import config as appConfig


# Removes Blackbird's log file once a search has finished.
# Exported results (CSV, PDF, JSON, dumps) are never touched.
def cleanLogs(config):
    logPath = appConfig.LOG_PATH

    # Release the log file before deleting it, otherwise the open handler
    # keeps writing to an unlinked descriptor.
    logging.shutdown()
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
        try:
            handler.close()
        except Exception:
            pass

    try:
        if os.path.exists(logPath):
            os.remove(logPath)
            if config.verbose:
                config.console.print(f"🧹 Removed log file '{logPath}'")
        return True
    except Exception:
        # Logging is already torn down at this point, so report to the console.
        config.console.print(f"⛔  Couldn't remove log file '{logPath}'")
        return False
