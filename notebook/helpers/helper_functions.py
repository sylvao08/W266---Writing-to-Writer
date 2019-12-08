import tensorflow as tf
import pandas as pd

# Callback functions used to monitor the training process
class LossAndErrorPrintingCallback(tf.keras.callbacks.Callback):
  def on_train_batch_end(self, batch, logs=None):
    print('For batch {}, loss is {:7.2f}.'.format(batch, logs['loss']))

  def on_test_batch_end(self, batch, logs=None):
    print('For batch {}, loss is {:7.2f}.'.format(batch, logs['loss']))

#   def on_epoch_end(self, epoch, logs=None):
#     print('The average loss for epoch {} is {:7.2f}.'.format(epoch, logs['loss']))

def prep_dataset(df, input_col, target_col):
    '''Select the target variable column and convert it to numerical value for modeling
    Argument: df: the output dataframe from data preparation
            target_col: the name of the target variable column
    Return: a new dataframe after target variable selection and conversion, the column name will be chaged to 'target'
    '''
    df = df.loc[:,[input_col,target_col]]
    df = df.astype({target_col: 'category'})
    df[target_col] = df[target_col].cat.codes
    df = df.rename(columns = {target_col:'target'})
    return df
