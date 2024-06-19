import json
import pickle
from argparse import ArgumentParser
from pathlib import Path

import utils

def read_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

def save_to_pkl(data, file_path):
    with open(file_path, 'wb') as pkl_file:
        pickle.dump(data, pkl_file)

def read_pkl(file_path):
    with open(file_path, 'rb') as pkl_file:
        data = pickle.load(pkl_file)
    return data

def prepare_data(overrides={}):
    default_data = read_json('default_data.json')
    data = {**default_data, **overrides}
    save_to_pkl(data, 'data.pkl')

def run_uvr():
    utils.cli = True
    import UVR
    UVR.root = UVR.MainWindow(cli=True)
    UVR.root.process_initialize()

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-m", "--vr_model", type=str, default="Choose Model", help="VR model filename (without extension)")
    parser.add_argument("-o", "--export_path", type=Path, default=Path("outputs"), help="Output folder")
    parser.add_argument("-i", "--input_path", type=Path, default=Path("vocal.wav"), help="Input .wav file path")
    args = parser.parse_args()

    prepare_data({
        "vr_model": args.vr_model,
        "export_path": str(args.export_path),
        "input_paths": [str(args.input_path)]
    })

    run_uvr()
