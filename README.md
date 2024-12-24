# dataset-server
A tiny, insecure client/server system for remote execution of `torch` datasets powered by ZeroMQ.

# install

To install, clone the repository, change directories inside and run:
```
pip install -e .
```

# running a server
Examples scripts for the client and server are provided in the `scripts` directory.

## server
The example server script will host data stored in a gzip-compressed `jsonl` file.
To run with the example data (1024 random protein sequence records I had lying around), invoke:

```bash
python scripts/start_dataset_server.py ++server.dataset.records.filename=example_data/swissprot.jsonl.gz ++server.name=swissprot
```

The output should look similar to this:
```
[2024-12-24 15:10:06,079][start_dataset_server][INFO] - server:
[2024-12-24 15:10:06,079][start_dataset_server][INFO] -   _target_: dataset_server.DatasetServer
[2024-12-24 15:10:06,079][start_dataset_server][INFO] -   port: 9990
[2024-12-24 15:10:06,079][start_dataset_server][INFO] -   name: swissprot
[2024-12-24 15:10:06,079][start_dataset_server][INFO] -   dataset:
[2024-12-24 15:10:06,079][start_dataset_server][INFO] -     _target_: dataset_server.datasets.JSONRecordDataset
[2024-12-24 15:10:06,079][start_dataset_server][INFO] -     records:
[2024-12-24 15:10:06,080][start_dataset_server][INFO] -       _target_: dataset_server.functional.read_jsonl
[2024-12-24 15:10:06,080][start_dataset_server][INFO] -       filename: example_data/swissprot.jsonl.gz
[2024-12-24 15:10:06,080][start_dataset_server][INFO] -       gzip_compressed: true
[2024-12-24 15:10:06,090][swissprot@tcp://canopy.home:9990][INFO] - Starting server
```

## client
With the server started, you can now access it remotely. To run the example client, you must know the server's address.

Run:
```
python scripts/client.py ++client.server_address=tcp://canopy.home:9990 ++first_n=3
```

See:
```
[2024-12-24 15:21:00,518][client][INFO] - first_n: 3
[2024-12-24 15:21:00,518][client][INFO] - client:
[2024-12-24 15:21:00,518][client][INFO] -   _target_: dataset_server.DatasetProxy
[2024-12-24 15:21:00,518][client][INFO] -   server_address: tcp://canopy.home:9990
[2024-12-24 15:21:00,518][client][INFO] -   get_method: __getitem__
[2024-12-24 15:21:00,518][client][INFO] -   len_method: __len__

{'accession': 'Q8YV98', 'uniprot_id': 'PYRR_NOSS1', 'sequence': 'MATPAKVIEILSAEDLRRTLTRLASQIVERTRDLSQLVLLGIYTRGVPLAELLARQIETLEGINVGVGALDITFYRDDLDQIGLRTPAKTSITLDLTGKTVVLVDDVIFKGRTIRAALNAVNEYGRPEVIRLAVLVDRGHREVPIHPDFVGKQLPTAKEEVVKVYLQDWDGRDAVELVGY', 'existence_code_string': 'Inferred from homology', 'sequence_length': 180}
{'accession': 'Q94EH8', 'uniprot_id': 'THO4C_ARATH', 'sequence': 'MSDALNMTLDEIVKKSKSERSAAARSGGKGVSRKSGRGRGGPNGVVGGGRGGGPVRRGPLAVNTRPSSSFSINKLARRKRSLPWQNQNDLYEETLRAVGVSGVEVGTTVYITNLDQGVTNEDIRELYAEIGELKRYAIHYDKNGRPSGSAEVVYMRRSDAIQAMRKYNNVLLDGRPMKLEILGGNTESAPVAARVNVTGLNGRMKRSVFIGQGVRGGRVGRGRGSGPSGRRLPLQQNQQGGVTAGRGGFRGRGRGNGGGRGNKSGGRGGKKPVEKSAADLDKDLESYHAEAMNIS', 'existence_code_string': 'Evidence at protein level', 'sequence_length': 295}
{'accession': 'A6QQJ8', 'uniprot_id': 'ZC12A_BOVIN', 'sequence': 'MSLWELEDRRSCQGTPRPAQEPTAEEATTAELQMKVDFFRKLGYSSAEIHSVLQKLGIQADTNTVLGELVKHGSAAERERQASPDPCPQLPLVPRGGGTPKAPTVETYPPEEDKEGSDLRPIVIDGSNVAMSHGNKDVFSCRGILLAVNWFLERGHTDITVFVPSWRKEQPRPDVPITDQHILRDLEKKKILVFTPSRRVGGKRVVCYDDRFIVKLAFESDGIVVSNDTYRDLQGERQEWKRFIEERLLMYSFVNDKFMPPDDPLGRHGPSLDNFLRKKPLTSEHKKQPCPYGRKCTYGIKCRFLHPERPSRPQRSVADELRANALLPPSRAASKDKNSRRPSPSSQPGSLPTEHEQCSPDRKKLGAQASPGTPREGLMQTFAPTGRSLPPSGSSGGSFGPSEWFPQTLDSLPYASQDCLDSGIGSLESQMSELWGVRGGGPGEPGPPRGPYAGYCTYGAELPATPAFSAFSRALGAGHFSVPADYAPPPAAFPPREYWSEPYQLPPPTQRLQEPQAPGPGADRGPWGGAGRLAKERASVYTKLCGVFPPHLVEAVMSRFPQLLDPQQLAAEILSYKSQHLSE', 'existence_code_string': 'Evidence at transcript level', 'sequence_length': 583}
```
