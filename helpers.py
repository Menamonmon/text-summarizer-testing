import os

def load_data_files(data_dir):
    if not os.path.exists(data_dir):
        raise Exception(f"Dir given does not exist: ({data_dir})")

    docstrs = []
    for doc_dir in os.listdir(data_dir):
        with open(f"{data_dir}/{doc_dir}") as f:
            docstrs.append(f.read())

    return docstrs
