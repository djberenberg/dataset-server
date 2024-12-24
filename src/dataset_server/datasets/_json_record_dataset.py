from torch.utils.data import Dataset

from dataset_server.typing import JSONSerializeable


class JSONRecordDataset(Dataset):
    def __init__(self, records: list[JSONSerializeable]):

        self.records = records

    def __getitem__(self, index: int) -> JSONSerializeable:
        return self.records[index]

    def __len__(self) -> int:
        return len(self.records)
