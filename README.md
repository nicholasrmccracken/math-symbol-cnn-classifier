# CSE 5524 Final Project: Handwritten Math Symbol Identification

## Project Set-up

1. Download the [handwritten math symbol dataset](https://www.kaggle.com/datasets/clarencezhao/handwritten-math-symbol-dataset/data) as a zip.
2. Unzip the dataset into the **Math-Symbol-Vision** project.
3. Pre-process the subdirectories:
    - In the `eval/` directory, delete the `number/` subdirectory.
    - In the `train/` directory, delete the `original number/`, `original sign/`, `other number/`, and `other sign/` subdirectories.
    - Remove all whitespaces from the names of subdirectories in `eval/` and `train/`. For example, `decimal val/` should be renamed to `decimal_val`.
4. Create a directory named `datasets` in the project. This is where the eval and train datasets will be located.
5. Run `dataload.ipynb`, which will create the `eval_dataset.pt` and `training_dataset.pt` files.
