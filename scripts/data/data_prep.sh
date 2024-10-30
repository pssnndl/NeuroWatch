export PATH_TO_EEG="../../datasets/raw_data/v2.0.1/"
python preprocess_data.py --data_type train --cpu_num 4 --label_type  "tse" --save_directory "../../datasets/processed_data"
