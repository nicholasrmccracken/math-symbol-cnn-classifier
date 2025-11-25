## NN Project

Project set up
1. Download the Data from Kaggle https://www.kaggle.com/datasets/clarencezhao/handwritten-math-symbol-dataset/data
    - In the kaggle dataset, there are a few folders that will need to be deleted
    - In eval, delete the numbers folder
    - In train, delete the folders titled original number, original sign, other number, other sign
    - Remove all spaces, ie. convert decimal val to just decimal, plus cleaned to just plus
2. Create folder named Datasets in the project. This is where the training and eval datasets will be located
3. Run the Dataload ipynb to create the eval_dataset and training_dataset.pt files