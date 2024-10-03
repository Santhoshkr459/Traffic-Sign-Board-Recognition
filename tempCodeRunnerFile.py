def image_processing(img):
	model = load_model('./model/traffic.h5')
	data=[]
	image = Image.open(img)
	image = image.resize((30,30))
	data.append(np.array(image))
	X_test=np.array(data)
	# Y_pred = model.predict_classes(X_test)
	# return Y_pred
	Y_pred = model.predict(X_test)    
	# Get the predicted class
	predicted_class = np.argmax(Y_pred, axis=1)

	return predicted_class