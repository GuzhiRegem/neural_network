from network import Network

net = Network(
    inp_size=2,
    out_size=1
)
training = [
    [[0.0, 0.0], [0.0]],
    [[1.0, 0.0], [1.0]],
    [[0.0, 1.0], [1.0]],
    [[1.0, 1.0], [0.0]]
]
net.train(training)
result = net.get([1.0, 0.0])
result = net.get([0.0, 1.0])
print(result)
for a in net.nodes:
    print(a)
for a in net.connections:
    print(a)