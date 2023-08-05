import numpy as np


def calculate(list):

  #check list length
  if len(list) == 9:

    array = np.array(list).reshape(3, 3)

    calculations = {

      #calculate mean
      'mean': [
        np.mean(array, axis=0).tolist(),
        np.mean(array, axis=1).tolist(),
        np.mean(array)
      ],
      # calculate variance
      'variance': [
        np.var(array, axis=0).tolist(),
        np.var(array, axis=1).tolist(),
        np.var(array)
      ],
      #calculate STD
      'standard deviation': [
        np.std(array, axis=0).tolist(),
        np.std(array, axis=1).tolist(),
        np.std(array)
      ],
      #calculate max
      'max': [
        np.max(array, axis=0).tolist(),
        np.max(array, axis=1).tolist(),
        np.max(array)
      ],
      #calculate min
      'min': [
        np.min(array, axis=0).tolist(),
        np.min(array, axis=1).tolist(),
        np.min(array)
      ],
      #calculate sum
      'sum': [
        np.sum(array, axis=0).tolist(),
        np.sum(array, axis=1).tolist(),
        np.sum(array)
      ]
    }
  else:
    raise ValueError('List must contain nine numbers.')

  return calculations
