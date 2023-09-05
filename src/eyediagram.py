import numpy as np
import matplotlib.pyplot as plt

"""
  This file has several functions：
  1. plot eyediagram
  2. Measure Eye Height
  3. Measure Eye width
  4. Plot Bathtub curve
"""

class eyediagram(SerDesSys):
  def __init__(self, SymbolTime, SamplePerSymbol, SampleInterval, SymbolNums, Modulation):
    super().__init__(SymbolTime, SamplePerSymbol, SampleInterval, SymbolNums, Modulation)
          
  def ploteye(self, inputdata, TraceNum, UI_num=2, Offset=0.5):
    """
      The function "ploteye" reference Warrem Weckesser's eyediagram function.
      His/Her github address is "https://github.com/WarrenWeckesser/eyediagram/tree/master" 
    """
    # detect the input "inputdata"    
    if not isinstance(inputdata, (np.ndarray, list)):
      raise TypeError("the inputdata should be a list or a numpy.array")    
    else:
      if len(inputdata) < (self.SamplePerSymbol * 2):
        raise ValueError("the mimimun length should be larger than 2*SamplerInterval")     
      else:
        self.inputdata = inputdata
        self.length = len(self.inputdata)    
        self.max_window_num = np.floor((self.length - self.SamplePerSymbol)/self.SymbolNums)

    # detect the input "UI_num"
    if UI_num is None:
      self.UI_num = 2
    elif not isinstance(UI_num,int):
      raise TypeError("UI_num should be an integer and larger than 0")    
    elif UI_num < 1 or UI_num > 4:
      raise ValueError("UI_num should be larger than 1 and less than 4")    
    else:
      self.UI_num = UI_num    
          
    # detect the input "TraceNum"
    if TraceNum is None:
      self.TraceNum = np.floor((self.length - self.SamplePerSymbol)/self.SymbolNums)
    elif self.TraceNum > self.max_window_num:
      raise ValueError("TraceNum is larger than the maximum clipped window number %f" %self.max_window_num)
    else:
      self.TraceNum = TraceNum

    # detect the input "Offset"
    if Offset <= 1 or Offset > 0:
      raise ValueError("Offset should be less than 1 and larger than 0")
    else:
      self.Offset = Offset    

    # create the eye density from the inputdata
  


    # Bresenham's algorithm for the inputdata
