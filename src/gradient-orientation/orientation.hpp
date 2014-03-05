#ifndef __ORIENTATION_HPP__
#define __ORIENTATION_HPP__

#include "opencv2/imgproc/imgproc.hpp"

void get_oriented_gradient(cv::Mat& destination, cv::Mat& source, int degree, int bin_variance);

#endif
