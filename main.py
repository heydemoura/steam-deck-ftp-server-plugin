import subprocess
import logging
import pathlib
import os

HOME_DIR = str(pathlib.Path(os.getcwd()).parent.parent.resolve())
PARENT_DIR = str(pathlib.Path(__file__).parent.resolve())

logging.basicConfig(filename="/tmp/template.log",
                    format='[Template] %(asctime)s %(levelname)s %(message)s',
                    filemode='w+',
                    force=True)
logger=logging.getLogger()
logger.setLevel(logging.INFO) # can be changed to logging.DEBUG for debugging issues

class Plugin:
    backend_proc = None

    async def start(self):
        logger.info("Starting FTP server.")
        self.backend_proc = subprocess.Popen([ PARENT_DIR + "/bin/server" ])

    async def stop(self):
        logger.info("Stopping FTP server.")
        self.backend_proc.terminate()

    # Asyncio-compatible long-running code, executed in a task when the plugin is loaded
    async def _main(self):
        logger.info("Starting backend.")
        # self.backend_proc = subprocess.Popen([ PARENT_DIR + "/bin/server" ]);

    # Function called first during the unload process, utilize this to handle your plugin being removed
    async def _unload(self):
        logger.info("Goodbye World!")
        pass
