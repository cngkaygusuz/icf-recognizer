#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"

#include <iostream>
#include <cmath>

using namespace std;
using namespace cv;

void gradient_orientation(Mat& source, Mat& destination, bool quadrant_aware, int lower_bound, int upper_bound){
    int scale = 1;
    int delta = 0;
    int ddepth = CV_16S;

    lower_bound = quadrant_aware ? lower_bound % 180 : lower_bound % 360;
    upper_bound = quadrant_aware ? upper_bound % 180 : upper_bound % 360;

    Mat grad_x;
    Mat grad_y;
    Mat gray;

    destination = Mat::zeros(source.rows, source.cols, CV_8U);

    cvtColor(source, gray, CV_RGB2GRAY);
    //GaussianBlur(gray, gray, Size(3,3), 0, 0, BORDER_DEFAULT);
    //GaussianBlur(gray, gray, Size(3,3), 0, 0, BORDER_DEFAULT);

    Sobel(gray, grad_x, ddepth, 1, 0, 3, scale, delta);
    //convertScaleAbs(grad_x, grad_x);

    Sobel(gray, grad_y, ddepth, 0, 1, 3, scale, delta);
    //convertScaleAbs(grad_y, grad_y);

    short* pix = (short*)  grad_x.data;
    short* piy = (short*)  grad_y.data;
    uchar* dst = destination.data;

    for (int i=0; i < source.rows * source.cols; i++){
        double radian = atan2((double)piy[i], (double) pix[i]);
        int deg = (int)(radian / M_PI * 180);
        
        if (quadrant_aware && deg < 0){
            deg += 360;
        }
        else if (!quadrant_aware && deg < 0){
            deg = 180-deg;
        }
        
        if (deg >= lower_bound && deg <= upper_bound){
            dst[i] = 255;
        }
    }
}

int main(int argc, char** argv){
    
    if (argc != 2){
        cout << "args?" << endl;
        return 1;
    }

    Mat picture = imread(argv[1]);
    

    if (!picture.data){
        cout << "bad filename input" << endl;
        return 1;
    }

    //cout << format(picture_gray, "python") << endl;

    Mat orn;
    namedWindow("Orientation", CV_WINDOW_AUTOSIZE);

    for (int i=0; i<8; i++){
        gradient_orientation(picture, orn, false, 22.5*i-5, 22.5*i+5);

        imshow("Orientation", orn);
        waitKey(0);
    }

    return 0;
    
}
