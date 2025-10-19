[Back to Module](./README.md)

## Brief
Using TensorFlow and Keras (both open-source AI tools), build and deploy a simple AI model for image recognition on Oracle Cloud Infrastructure.  

**Reflection**: Reflect on how you technically built, deployed, and evaluated the AI model. Reflect on how AI can enhance cloud computing operations, especially in resource management and optimisation.

# Set by step
On Ubuntu Compute node:
- Build and train model using dataset such as CIFAR-10
- Built model using python and deep learning Framework TensorFlow
- ```python
import tensorflow as tf
from tensorflow.keras import layers, models

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))
model.save("image_model.keras")
  ```
- Wrapped the model in a Flask API
```python
from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("image_model.h5")
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    image = np.array(request.json['image']) / 255.0
    image = image.reshape(1, 32, 32, 3)
    prediction = model.predict(image)
    return jsonify({'class': int(np.argmax(prediction))})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

Created a Dockerfile to package Flask app and model into a container to ensure consistency across environments:
```dockerfile
FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install tensorflow flask
CMD ["python", "app.py"]
```

Pushed to Oracle container:
```bash
(ai-env) ubuntu@TestStack:~$ docker login uk-london-1.ocir.io
Username: lriejvhhbyfh/swampy10@gmail.com
Password: 

WARNING! Your credentials are stored unencrypted in '/home/ubuntu/.docker/config.json'.
Configure a credential helper to remove this warning. See
https://docs.docker.com/go/credential-store/

Login Succeeded
(ai-env) ubuntu@TestStack:~$ docker tag image-recognition uk-london-1.ocir.io/lriejvhhbyfh/image-recognition
(ai-env) ubuntu@TestStack:~$ docker push uk-london-1.ocir.io/lriejvhhbyfh/image-recognition
Using default tag: latest
The push refers to repository [uk-london-1.ocir.io/lriejvhhbyfh/image-recognition]
c710b054a074: Pushed 
989a324073a5: Pushed 
521c681338e1: Pushed 
fe6298715fa6: Pushed 
4eef699c8b95: Pushed 
d189770036e1: Pushed 
25bde18331a6: Pushed 
698d92e1248d: Pushed 
1260506aec83: Pushed 
a5ec5ec9d16c: Pushed 
latest: digest: sha256:7d2a7d9b6fffc429198f1fa9570d3c91db167461a9e9320cb785afd4f7f3f13b size: 2430
```

Log into cloud shell to access the cluster. 
created a deployment file `deployment.yaml`
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: image-recognition
spec:
  replicas: 1
  selector:
    matchLabels:
      app: image-recognition
  template:
    metadata:
      labels:
        app: image-recognition
    spec:
      containers:
      - name: image-recognition
        image: uk-london-1.ocir.io/lriejvhhbyfh/image-recognition:latest
        ports:
        - containerPort: 5000
      imagePullSecrets:
      - name: ocirsecret
```
 and load balancer as a service `service.yaml`
 ```yaml
 apiVersion: v1
kind: Service
metadata:
  name: image-recognition-service
spec:
  type: LoadBalancer
  selector:
    app: image-recognition
  ports:
    - protocol: TCP
      port: 80
      targetPort: 5000
 ```
Simulated a test with python script to generate random image:
```python
import requests
import numpy as np

# Generate a random 32x32 RGB image
image = np.random.rand(32, 32, 3).tolist()

# Send to your API
response = requests.post("http://141.147.78.12/predict", json={"image": image})
print(response.json())
```

received a response: 
```bash
swampy10@cloudshell:~ (uk-london-1)$ python test.py 
{'class': 3}
```


# Case Study: Deploying an AI-Powered Image Recognition Model on Oracle Cloud

## Overview

This case study explores the end-to-end process of building, deploying, and evaluating an AI-based image recognition model using Oracle Cloud Infrastructure (OCI). It highlights the technical steps taken to operationalize the model using containerization and Kubernetes, and reflects on how AI can enhance cloud computing operations, particularly in resource management and optimization.

## Objectives

- Develop a deep learning model for image classification
    
- Containerize the model and expose it via a RESTful API
    
- Deploy the model on Oracle Kubernetes Engine (OKE)
    
- Evaluate the model’s performance in a cloud-native environment
    
- Reflect on AI’s role in optimizing cloud infrastructure
    

## Model Development and Evaluation

### Model Architecture

The image recognition model was built using a convolutional neural network (CNN) trained on a dataset such as CIFAR-10. The model was designed to classify 32×32 RGB images into one of 10 categories.

### API Integration

The trained model was wrapped in a Flask application, exposing a `/predict` endpoint that accepts JSON-formatted image data and returns a predicted class label.

### Evaluation

To validate the deployment, a simulated image (random pixel array) was sent to the API. The model responded with a valid prediction, confirming successful inference in a production environment.

## Technical Deployment Workflow

### 1. **Containerization**

- A `Dockerfile` was created to package the Flask app and model.
    
- The image was tagged and pushed to Oracle Cloud Infrastructure Registry (OCIR) using an OCI auth token for secure access.
    

### 2. **Kubernetes Deployment**

- A Kubernetes `Deployment` was defined to manage the container lifecycle.
    
- A `Service` of type `LoadBalancer` exposed the API to the public internet.
    
- A Kubernetes secret (`ocirsecret`) was created to authenticate image pulls from OCIR.
    

### 3. **Cloud Shell Integration**

- Oracle Cloud Shell was used to configure `kubectl` and interact with the OKE cluster.
    
- Deployment and service YAML files were applied directly from Cloud Shell.
    
- The public IP of the service was retrieved and used to test the API endpoint.
    

## Results

- The model was successfully deployed and served via a public endpoint.
    
- A test image was sent to the `/predict` endpoint, and the model returned a valid class label (`{'class': 3}`).
    
- The deployment demonstrated full-stack AI integration in a cloud-native environment.
    

## Strategic Reflection: AI in Cloud Operations

### Intelligent Resource Management

AI can analyze usage patterns to dynamically allocate compute and storage resources, enabling predictive autoscaling and cost-aware provisioning.

### Predictive Monitoring

AI models can detect anomalies in system behavior, reducing downtime and enabling proactive incident response.

### Smart Scheduling

AI-enhanced orchestration can optimize workload placement, minimize latency, and balance energy consumption across clusters.

### Security Automation

AI can identify suspicious access patterns, enforce data policies, and automate compliance checks.

### DevOps Acceleration

AI-driven tools can auto-generate CI/CD pipelines, recommend infrastructure changes, and optimize container deployments.

## Conclusion

This case study demonstrates how AI models can be effectively deployed and evaluated in a cloud-native environment using OCI and Kubernetes. Beyond application-level benefits, AI has the potential to transform cloud infrastructure itself — making it more intelligent, adaptive, and efficient.