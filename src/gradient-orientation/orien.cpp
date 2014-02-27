oid getGradients(IplImage* original, cv::Mat* gradArray)
{

void main(int argc, char** argv){

	if (argc!=2){
		cout << "args?" << endl;
		return 1;
	}

	cv::Mat original;
	original = imread(argv[1]);

	if (!original.data){
		cout << "not good pic" << endl;
		return 1;
	}

	cv::Mat original_Mat(original, true);

	// Convert it to gray
	cv::cvtColor( original_Mat, original_Mat, CV_RGB2GRAY );
	//cv::blur(original_Mat, original_Mat, cv::Size(7,7));

	/// Generate grad_x and grad_y
	cv::Mat grad_x = cv::Mat::zeros(original->height, original->width, CV_16S); 
	cv::Mat grad_y = cv::Mat::zeros(original->height, original->width, CV_16S);

	/// Gradient X
	cv::Sobel(original_Mat, grad_x, CV_16S, 1, 0, 3);

	/// Gradient Y
	cv::Sobel(original_Mat, grad_y, CV_16S, 0, 1, 3);

	uchar* pixelX = grad_x.data;
	uchar* pixelY = grad_y.data;
	uchar* grad1 = gradArray[0].data;
	uchar* grad2 = gradArray[1].data;
	uchar* grad3 = gradArray[2].data;
	uchar* grad4 = gradArray[3].data;
	uchar* grad5 = gradArray[4].data;
	uchar* grad6 = gradArray[5].data;
	uchar* grad7 = gradArray[6].data;
	uchar* grad8 = gradArray[7].data;
	int count = 0;
	int min = 999999;
	int max = -1;

	for(int i = 0; i < grad_x.rows * grad_x.cols; i++) 
	{
		double directionRAD = atan2(pixelY[i], pixelX[i]);
		int directionDEG = (int)(180 + directionRAD / M_PI * 180);

		if(directionDEG < min){min = directionDEG;}
		if(directionDEG > max){max = directionDEG;}

		if(directionDEG >= 0 && directionDEG <= 45)         { grad1[i] = 255; count++;}         
		if(directionDEG >= 45 && directionDEG <= 90)        { grad2[i] = 255; count++;}         
		if(directionDEG >= 90 && directionDEG <= 135)       { grad3[i] = 255; count++;}         
		if(directionDEG >= 135 && directionDEG <= 190)      { grad4[i] = 255; count++;}         
		if(directionDEG >= 190 && directionDEG <= 225)      { grad5[i] = 255; count++;}         
		if(directionDEG >= 225 && directionDEG <= 270)      { grad6[i] = 255; count++;}     
		if(directionDEG >= 270 && directionDEG <= 315)      { grad7[i] = 255; count++;}
		if(directionDEG >= 315 && directionDEG <= 360)      { grad8[i] = 255; count++;}

		if(directionDEG < 0 || directionDEG > 360)
		{
		    cout<<"Weird gradient direction given in method: getGradients.";
		}

}

