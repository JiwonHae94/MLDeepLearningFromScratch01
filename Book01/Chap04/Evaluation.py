import numpy as np
from dataset import mnist
from TwoLayerNetwork import TwoLayerNet

if __name__ == '__main__':
    (x_train, t_train), (x_test, t_test) = mnist.load_mnist(normalize=True, one_hot_label=True)

    network = TwoLayerNet(input_size=784, hidden_size=50, output_size=10)

    iters_num = 10
    train_size = x_train.shape[0]
    batch_size = 100
    learning_rate = 1

    train_loss_list = []
    train_acc_list = []
    test_acc_list = []

    iters_per_epoch = max(train_size / batch_size, 1)

    for i in range(iters_num):
        batch_mask = np.random.choice(train_size, batch_size)
        x_batch = x_train[batch_mask]
        t_batch = t_train[batch_mask]

        grads = network.numerical_gradient(x_batch, t_batch)

        for key in ("W1", "b1", "W2", "b2"):
            network.params[key] -= learning_rate * grads[key]

        loss = network.loss(x_batch, t_batch)
        train_loss_list.append(loss)

        if i % iters_per_epoch == 0:
            train_acc = network.accuracy(x_batch, t_batch)
            test_acc = network.accuracy(x_test, t_test)
            train_acc_list.append(train_acc)
            test_acc_list.append(test_acc)

            print("train acc, test acc : ", str(train_acc) + " | " + str(test_acc))

