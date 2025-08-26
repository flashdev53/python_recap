def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"Running: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_action
def deploy_service(service):
    print(f"Deploying {service}...")

deploy_service("nginx")
