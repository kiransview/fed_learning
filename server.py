import flwr as fl

# Start Flower server for three rounds of federated learning
if __name__ == "__main__":
    strategy = fl.server.strategy.FedAvg(
        fraction_fit=0.1,
        min_available_clients=2
)
fl.server.start_server("[::]:8080", config={"num_rounds": 3}, strategy=strategy)