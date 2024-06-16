# Char Rnn PyTorch TFT
This project addresses the unique vocabulary within the Teamfight Tactics (TFT) community of practice by training a character-level recurrent neural network (char RNN) to reproduce the specific language used in TFT-related texts. The primary data sources include tweets from popular TFT content creators and transcriptions of YouTube videos by the popular TFT player, k3soju. The findings reveal that the char RNN effectively learns and generates text that mimics the TFT lexicon when trained on a focused dataset of tweets, achieving a significant reduction in loss and producing coherent outputs. However, training on a combined dataset of tweets and YouTube transcripts resulted in poor performance, indicating the challenge of dealing with more complex and noisy data. This research contributes to understanding the complexities of the TFT lexicon and demonstrates the potential for char RNNs in generating unique output in specific fields. The full paper can be found [here](https://docs.google.com/document/d/1WCHIrq1HsDz_W6CnUCctdESzv3bIEBYy8BiKxyViQHI/edit?usp=sharing).

This repository includes the data collection scripts, the implementation of the character-level recurrent neural network, and the trained models.

## Acknowledgements
This code is based on [char-rnn-pytorch](https://github.com/nikhilbarhate99/Char-RNN-PyTorch/blob/master/CharRNN.py) which in turn is based on the [char-rnn](https://github.com/karpathy/char-rnn) and [min-char-rnn](https://gist.github.com/karpathy/d4dee566867f8291f086) code by Andrej Karpathy, which is in turn based on Oxford University Machine Learning class [practical 6](https://github.com/oxford-cs-ml-2015/practical6), which is in turn based on [learning to execute](https://github.com/wojciechz/learning_to_execute) code from Wojciech Zaremba.
