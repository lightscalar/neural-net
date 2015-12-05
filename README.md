An Introduction to Neural Networks
=======

# Introduction

The term _neural network_ is an evocative one, suggesting machines capable of
human-level intelligence, autonomy, and even sentience. More than any other
technology in the discipline of [machine
learning](https://en.wikipedia.org/wiki/Machine_learning), neural networks are
redolent of science fiction, bringing to mind the malevolent intellect of [HAL
9000](https://en.wikipedia.org/wiki/HAL_9000) from _2001: A Space Odyssey_, or
the genial wisdom of [Data](https://en.wikipedia.org/wiki/Data_(Star_Trek) from
_Star Trek_. Yet neural networks are now ubiquitous, if largely invisible. They
are not sentient AIs, but rather increasingly useful tools for solving
problems that simply cannot be tackled by other methods. Voice recognition,
machine language translation, and image recognition are now possible due to the
rise of practical neural networks. 

For decades, programmers carefully engineered pattern recognition

For the power and flexibility that neural networks provide, they are
surprisingly simple to understand. 

The aim of this book is to demystify neural networks and deep learning, and to
introduce the reader to them in a pragmatic way, so that she will not only
understand the underlying mathematics, but will also be able to readily
implement networks to solve real world problems. For this purpose, we use the
powerful [Tensor Flow](http://www.tensorflow.org/) machine intelligence package
recently open-sourced by Google. By introducing the mathematical foundations of
neural networks in the context of a practical package, we gain the advantage of
being able to simultaneously do a bunch of junk.

Why TensorFlow? There are many other packages out there:
[Torch7](http://torch.ch), Theano, and others exist, and have advantages and
disadvantages. Torch7 interfaces with a fast and powerful neural network
library, but is scripted in the horrible Lua language.

There is an advantage to implementing neural networks from scratch—in Python, 
for example. This can be very instructive. But from a practical perspective, 
rolling your own Python code will not cut it for real world applications. In
order to get realistic networks for function on real data, we need to   

## Deep Learning & Hierarchical Representations

Nature is hierarchical.

## The Importance of Hierarchy

## How is this possible?

In the last decade, computational power has become absurdly cheap.


One of the most critical pieces of technology to emerge is the Graphical
Processing Unit (GPU).

While modern artificial neural networks (ANNs) were originally inspired by
biological neural networks, it is now clear that the architecture of the
biological networks are so much more complex, and the networks so much more
capable, that it is better not to draw too many parallels between biological
networks and their artificial counterparts.

The reasons for this ascent are two-fold. Deep neural networks are very
computationally expensive. The cost of computational power has fallen
dramatically over the last sixty years. Consider Figure 1.1, which plots the
cost of one billion floating point operations per second from 1960 until
January 2015.

$$f(x) = 4 \label{first} \tag{Eq. 1}$$

![The cost of one billion floating point operations per second (one GFLOPS) in
adjusted 2013 dollars, from 1960 to 2015. In that 55 year span, the cost of a
GFLOPS has dropped an astonishing amount, from $8.3 trillion to $0.08. Note the
scale here is logarithmic.
(http://bit.ly/1XjYx2s)](http://bit.ly/1SEP708)

