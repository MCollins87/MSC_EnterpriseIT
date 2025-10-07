

def handle(event, context):
	name = event.body.strip() if event.body else "stranger"

	return f"Hello, {name}! Welcome to OpenFaaS."





