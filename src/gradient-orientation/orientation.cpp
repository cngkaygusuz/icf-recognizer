#include "orientation.hpp"
#include "opencv2/imgproc/imgproc.hpp"

#include <cmath>


void get_oriented_gradient(cv::Mat& source, cv::Mat& destination, int degree, int bin_variance){
    int scale = 1;
    int delta = 0;
    int ddepth = CV_16S;

    int lower_bound = degree - bin_variance;
    int upper_bound = degree + bin_variance;

    cv::Mat grad_x;
    cv::Mat grad_y;
   
    destination = cv::Mat::zeros(source.rows, source.cols, CV_8U);
    
    cv::Sobel(source, grad_x, ddepth, 1, 0, 3, scale, delta);
    cv::Sobel(source, grad_y, ddepth, 0, 1, 3, scale, delta);

    short* pix = (short*) grad_x.data;
    short* piy = (short*) grad_y.data;
    uchar* dst = destination.data;

    for (int i=0; i<source.rows*source.cols; i++){
        double radian = atan2((double) piy[i], (double) pix[i]);
        int deg = (int)(radian / M_PI * 180);
        if (deg < 0){
            deg = 180-deg;
        }

        if (deg >= lower_bound && deg <= upper_bound){
            dst[i] = 255;
        }
    }
}
