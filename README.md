The term _neural network_ is an evocative one, suggesting machines capable of
human-level intelligence, autonomy, and even sentience. More than any other
technology in the discipline of [machine
learning](https://en.wikipedia.org/wiki/Machine_learning), neural networks are
redolent of science fiction, bringing to mind the malevolent intellect of [HAL
9000](https://en.wikipedia.org/wiki/HAL_9000) from _2001: A Space Odyssey_, or
the genial wisdom of [Data](https://en.wikipedia.org/wiki/Data_%28Star_Trek%29)
from _Star Trek_. Yet neural networks are now ubiquitous, if invisible.  They
are not sentient AIs, but rather increasingly useful tools for solving problems
that simply cannot be tackled by other methods. Voice recognition, machine
language translation, and image recognition are now possible due to the rise of
practical neural networks. 

The aim of this book is to demystify neural networks and deep learning. The
focus is on developing a practical understanding of the underlying mathematics,
as well as learning how to implement deep neural networks that solve real world
problems. For this purpose, we use the [TensorFlow](http://www.tensorflow.org/)
machine intelligence package [recently](http://goo.gl/pBU1hy) open-sourced by
Google. 

Why TensorFlow? There are many computational frameworks out there, including
the excellent [Torch7](http://torch.ch),
[Theano](http://deeplearning.net/software/theano/), and
[PyBrain](http://pybrain.org/) libraries. First, we write TensorFlow models in
Python. Python is a delightful, easy to learn language that has a vast array of
supporting libraries for machine learning, data handling, interfacing with
hardware, _etc_.  TensorFlow does the heavy computational lifting with fast,
optimized C++ libraries. TensorFlow strikes a good balance between abstraction
and control. The framework allows us to quickly develop sophisticated networks;
it provides transparent integration with the GPU, allowing us to speed our
models up by more than an order of magnitude; the TensorBoard tool allows us to
visualize our computation graph and inspect our models as they are being
trained. 

Although we write TensorFlow models in Python, TensorFlow does the heavy
computational lifting with fast, optimized C++ libraries — we get the benefits
of C++ without the hassle of actually having to write in C++.   In short,
TensorFlow allows us to create, compute, and visualize complex neural network
models without burying the gory details under too many layers of abstraction. 

