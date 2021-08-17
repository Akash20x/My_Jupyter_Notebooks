Optimizers are algorithms or methods used to change the attributes of the neural network such as weights and learning rate to reduce the losses. Optimizers are used to solve optimization problems by minimizing the function. Various optimizers are researched within the last few couples of years each having its advantages and disadvantages.

Gradient Descent (GD): Gradient descent is the most basic and first-order optimization algorithm which is dependent on the first-order derivative of a loss function. Very simple to implement but this algorithm can be stuck at local minima or saddle point. This algorithm takes an entire dataset of n-points at a time to compute the derivative to update the weights which require a lot of memory.

Stochastic Gradient Descent (SGD):SGD algorithm is an extension of the GD algorithm and it overcomes some of the disadvantages of the GD algorithm. SGD algorithm derivative is computed taking one point at a time. Memory requirement is less compared to the GD algorithm but Takes a long time to converge and may be stuck in local minima.

Mini Batch Stochastic Gradient Descent (MB-SGD): MB-SGD algorithm is an extension of the SGD algorithm and it overcomes the problem of large time complexity in the case of the SGD algorithm. MB-SGD algorithm takes a batch of points or subset of points from the dataset to compute derivate. Less time complexity to converge, but may be too noisy and can get stuck in local minima.

SGD with momentum: This algorithm is used to over come the noise in MB-SGD. Has all advantages of the SGD algorithm and Converges faster than the GD algorithm

Adaptive Gradient (AdaGrad):Key idea of AdaGrad is to have an adaptive learning rate for each of the weights. The learning rate for weight will be decreasing with the number of iteration. No need to update the learning rate manually as it changes adaptively with iterations. As the number of iteration becomes very large learning rate decreases to a very small number which leads to slow convergence.

Adadelta: Adadelta is an extension of Adagrad that seeks to reduce its aggressive, monotonically decreasing learning rate. Instead of accumulating all past squared gradients, Adadelta restricts the window of accumulated past gradients to some fixed size.

RMSprop: RMSprop balances the step size (momentum), decreasing the step for large gradients to avoid exploding, and increasing the step for small gradients to avoid vanishing.

Adam: Adam combines the best properties of the AdaGrad and RMSProp algorithms to provide an optimization algorithm that can handle sparse gradients on noisy problems
