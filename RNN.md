RNN is a class of #artificialneuralnetworks commonly used in speechrecognition and naturallanguageprocessing (NLP) where connections between nodes form a directed graph along a sequence. This allows it to exhibit dynamic temporal behavior for a time sequence. 

RNNs are designed to recognize a data's sequential characteristics and use patterns to predict the next likely scenario.

Unlike feedforward neural networks (FNN), RNNs can use their internal state memory to process sequences of inputs. That makes them commonly to be applied the following domains:
  (*) speech recognition,
  (*) natural language processing (NLP)
  (*) handwriting recognition, 
  (*) time-series predictions, 
  (*) time-series #anomalydetection  
  (*) rhythm learning 

RNNs are designed to take a series of inputs with no predetermined limit on size. It remembers the past and its decisions are influenced by what it has learned from the past. 

Note: Basic feedforward networks (FNN) remember things too, but they remember things they learnt during the training.

While RNNs learn similarly during the training, in addition, they remember things learned from prior inputs, albeit generating outputs.
 
RNNs come in many variants. There are essentially 4 effective ways to learn RNN:

·      Long Short-Term Memory: Make the RNN out of little modules that are designed to remember values for a long time.

·      Hessian Free Optimization: Deal with the vanishing gradients problem by using a fancy optimizer that can detect directions with a tiny gradient but even smaller curvature.

·      Echo State Networks: Initialize the input -> hidden and hidden -> hidden and output -> hidden connections very carefully so that the hidden state has a huge reservoir of weakly coupled oscillators which can be selectively driven by the input

·      Good initialization with momentum: Initialize like in Echo State Networks, but then learn all of the connections using momentum
