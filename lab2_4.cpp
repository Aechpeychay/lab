#include <vector>
#include <cmath>
#include <iostream>
double f(double x1, double x2, double x3, double x4) {
    return std::pow(x1 - x2, 2) + 4 * std::pow(x3 - x4, 2) + std::pow(x2 - 6 * x3, 4) + 2 * std::pow(x1 - x4, 2);
}
template <typename T>
bool search(T& arr, T& delta){
	bool res = 0;
	double fr = f(arr[0],arr[1],arr[2],arr[3]);
	const T tmp{arr};
	for(size_t i = 0; i < 4; i++){
		arr[i] = arr[i] + delta[i];
		if (f(arr[0], arr[1], arr[2], arr[3]) < fr) {
			res = 1;
			break;	
		};
		arr = tmp;
		arr[i] = arr[i] - delta[i];
		if (f(arr[0], arr[1], arr[2], arr[3]) < fr) {
			res = 1;
			break; 
		}
		arr = tmp;
	}
	return res;
}

static const int n = 4;

int main(){
		std::vector<double> arr = {1,2,3,4};
		std::vector<double> prev_arr = arr;
		std::vector<double> tmp;
		std::vector<double> delta = {0.1,0.1,0.1,0.1};
		double a = 2;
		double eps = 0.01;
		int k = 0;	
		int i = 0;
		int j = 2;
		while (true) {
			std::cout<<arr[0] <<'|'<< arr[1] << '|' << arr[2]<<'|'<< arr[3]<<std::endl;
			if (search(arr, delta)) {
				tmp = arr;
				for(int i = 0; i < n; i++){
					arr[i] = arr[i] + (arr[i] - prev_arr[i]);
				}
				if (f(arr[0],arr[1],arr[2],arr[3]) < f(tmp[0], tmp[1], tmp[2], tmp[3])){
					j = 2;
					while (true) {
						double fr = f(arr[0],arr[1],arr[2],arr[3]);
						for(int i = 0; i < n; i++){
							arr[i] = tmp[i] + j * (tmp[i] - prev_arr[i]);
						}
						j += 1;
						if (fr > f(arr[0], arr[1], arr[2], arr[3])) break;
					}
				}
			}
			else{
				for(int i = 0; i < n; i++){
					delta[i] = delta[i]/a;
				}
			}
			if (std::sqrt(delta[0] * delta[0] + delta[1] * delta[1]) <= eps
				&& f(arr[0], arr[1], arr[2], arr[3]) - f(prev_arr[0], prev_arr[1], prev_arr[2], prev_arr[3]) <= eps) break;
			k += 1;
		}
}
