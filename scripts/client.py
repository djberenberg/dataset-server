import logging

import hydra
from omegaconf import DictConfig, OmegaConf

from dataset_server import DatasetProxy

logging.basicConfig()

logger = logging.getLogger("client")
logger.setLevel(logging.INFO)


@hydra.main(version_base=None, config_name="client", config_path="./hydra_config")
def main(config: DictConfig):

    for line in OmegaConf.to_yaml(config).splitlines():
        logger.info(line)

    dataset: DatasetProxy = hydra.utils.instantiate(config.client)

    for i in range(len(dataset)):
        record = dataset[i]
        print(record)


if __name__ == "__main__":
    main()
