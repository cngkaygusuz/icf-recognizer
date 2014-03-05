/*
 * =====================================================================================
 *
 *       Filename:  ex_main.cpp
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  05-03-2014 12:36:27
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */

#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/highgui/highgui.hpp"

#include <iostream>
#include "orientation.hpp"

using namespace std;

int main(int argc, char** argv){
    if (argc != 2){
        cout << "args?" << endl;
        return 1;
    }

    cv::Mat picture = cv::imread(argv[1]);
    
    if (!picture.data){
        cout << "Bad file" << endl;
        return 1;
    }

    cv::Mat gray;
    cv::Mat orientation;
   
    cv::cvtColor(picture, gray, CV_RGB2GRAY);
    get_oriented_gradient(gray, orientation, 45, 5);

    cv::namedWindow("Orientation", CV_WINDOW_AUTOSIZE);
    cv::imshow("Orientation", orientation);
    cv::waitKey(0);
    
    return 0;
}
