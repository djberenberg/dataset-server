import logging

import hydra
from omegaconf import DictConfig, OmegaConf

from dataset_server import DatasetServer

logging.basicConfig()

logger = logging.getLogger("start_dataset_server")
logger.setLevel(logging.INFO)


@hydra.main(version_base=None, config_name="server", config_path="./hydra_config")
def main(config: DictConfig):

    for line in OmegaConf.to_yaml(config).splitlines():
        logger.info(line)

    server: DatasetServer = hydra.utils.instantiate(config.server)

    try:
        server.serve()
    except KeyboardInterrupt:
        logger.info("Received KeyboardInterrupt. Quitting")


if __name__ == "__main__":
    main()
