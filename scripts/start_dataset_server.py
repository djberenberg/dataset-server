import hydra
from omegaconf import DictConfig

from dataset_server import DatasetServer


@hydra.main(version_base=None, config_name="server", config_path="./hydra_config")
def main(config: DictConfig):

    server: DatasetServer = hydra.utils.instantiate(config.server)
    server.serve()
