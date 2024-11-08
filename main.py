import argparse
from utils.compare_anns import compare_annotations_main
from pathlib import Path 

#gold_folder_path = "/home/lsalas/Desktop/prueba_compare_anns/gold_standard"
#predictions_folder_path = "/home/lsalas/Desktop/prueba_compare_anns/predictions_v1_igual"



parser = argparse.ArgumentParser(
                    prog="CompareBratAnnotations",
                    description="This Programme compares two folder paths containing .ann files. One path contains the gold standard annotations, and the other the predictions of a model. The output are some metrics, like F1-Score, Recall and Precision",
                    )

parser.add_argument("gold_folder_path", type=str, help="Path to the gold standard folder")           # positional argument
parser.add_argument("predictions_folder_path", type=str, help="Path to the model predictions folder")

args = parser.parse_args()




if __name__ == "__main__":
    """
    This function uses the arguments taken by argsparser and runs the programme. 
    """
    gold_folder_path = Path(args.gold_folder_path).resolve()
    predictions_folder_path= Path(args.predictions_folder_path).resolve()
    print(f"Starting programme\n Computing metrics for:\n{gold_folder_path} \nAND\n {predictions_folder_path}")
    compare_annotations_main(gold_folder_path= gold_folder_path, predictions_folder_path=predictions_folder_path)
