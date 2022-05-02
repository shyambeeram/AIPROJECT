# AIPROJECT
Breast cancer Prediction 

Abstract/Inspiration/Goal:

Breast cancer is one of the main causes of cancer death worldwide. Computer-aided diagnosis systems showed the potential for improving diagnostic accuracy. But early 
detection and prevention can significantly reduce the chances of death. It is important to detect breast cancer as early as possible. 
The goal is to classify images into two classifications of malignant and benign. As early diagnostics significantly increases the chances of correct treatment and 
survival. In this application, we are helping the doctors and patients to classify the Type of Tumour for the specific image given with the help of Neural Networks.

Convolution neural network
Computers see images using pixels. Pixels in images are usually related. For example, a certain group of pixels may indicate the edge on an image or other pattern. Convolutions use this to help identify images. Convolution multiplies the pixel matrix with a filter matrix or 'kernel' and summarizes the multiplication values. Then the slide convolution slides to the next pixel and repeats the same process until all the pixels of the image are covered.

Technical Flow:
 ![image](https://user-images.githubusercontent.com/64300588/166172886-a6b94a57-35ce-4123-87de-f8f2a031cd9a.png)


PROJECT FLOW:

![image](https://user-images.githubusercontent.com/64300588/166173273-733ba26d-26f5-4997-b78f-985a248c4202.png)

 The technology/concept behind the project is CNN.
 We use python and its libraries to load explore and analyze the data. 
 Then we preprocess the data.  Pre-process[resize, rescale, converting labels] 
 In our preprocessing module it consists of loading dataset, initializing dataset, 
 Building CNN layers, training and saving the model. 
 We saved the model in H5 format
 Then we optimize the code and load the saved model and test the results. 
 Then we build an application (App built in a way that usage is friendly) 
 Server scripting code (flask concept).
 integrating the app code with our saved model and HTML file 
 Then test the Results

Environment and tools

Jupyter Notebook
Numpy
Pandas
Scikit-image
Matplotlib
Scikit-learn
Keras



Prerequisites:
To build Deep learning models you must require the following packages

Tensor flow: TensorFlow is an end-to-end open-source platform for machine learning. It has a comprehensive, flexible ecosystem of tools, libraries, and community resources that lets researchers push the state-of-the-art in ML and developers can easily build and deploy ML-powered applications.


Keras: Keras leverages various optimization techniques to make high-level neural network API easier and more performant. It supports the following features:

Consistent, simple, and extensible API.
Minimal structure - easy to achieve the result without any frills.
It supports multiple platforms and backends.
It is a user-friendly framework that runs on both CPU and GPU.
Highly scalability of computation.
Flask: Web framework used for building  Web applications


If you are using anaconda navigator, follow the below steps to download the required packages

Open anaconda prompt.

Type “pip install boto3” and press enter.
Type “pip install opencv-python” and press enter.
Type “pip install imutils” and press enter.
Type “pip install requests” and press enter.
Type “pip install flask” and press enter.

Project Structure:
In order to run this project, place the files same as shown.	
![image](https://user-images.githubusercontent.com/64300588/166173132-0ac64c2d-8c4d-4669-99a2-d984e28888d5.png)
![image](https://user-images.githubusercontent.com/64300588/166173137-ee2425a4-16a1-41a9-b357-1e4ba6deabb6.png)
![image](https://user-images.githubusercontent.com/64300588/166173147-232f90f9-364d-4c85-b4e2-c1fd837958a4.png)
![image](https://user-images.githubusercontent.com/64300588/166173163-3f2e436d-fab9-4cf1-a540-a76b02569830.png)
![image](https://user-images.githubusercontent.com/64300588/166173167-4f33e5d0-8a66-4bf2-93a5-e936e97c39ec.png)
![image](https://user-images.githubusercontent.com/64300588/166173175-a36ce351-54aa-48f9-a3ec-8ce738def816.png)

EXECUTION STEPS:

Run The App
Open anaconda prompt from the start menu.
Navigate to the folder where your app.py resides.
Now type “python app.py” command.
It will show the local host where your app is running on http://127.0.0.1.5000/
Copy that localhost URL and open that URL in the browser. It does navigate you to where you can view your web page application.
•	Enter the url in the browser to check the output.

Thank you.





