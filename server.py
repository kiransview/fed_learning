import flwr as fl

fl.server.start_server(
    server_address = "0.0.0.0:8080", 
    config=fl.server.ServerConfig(num_rounds=3))


# import flwr as fl

# # Start Flower server for three rounds of federated learning
# if __name__ == "__main__":
#     strategy = fl.server.strategy.FedAvg(
#         fraction_fit=0.1,
#         min_available_clients=2
#     )
    
#     # Create a Config object
#     config = fl.server.config.Config(num_rounds=3)

#     fl.server.start_server(config=config, strategy=strategy)


    ###"[::]:8080",