#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;
double func(double x1, double x2, double x3, double x4) {
    return pow((x1 - x2), 2) + 4 * pow((x3 - x4), 2) + pow((x2 - 6 * x3), 4) + 2 * pow((x1 - x4), 2);
}
double minimum(int i, int x[]) {
    double a = x[i] * 0.5;
    double b = x[i] * 1.5;
    double x0 = (a + b) / 2;
    double l = b - a;
    double x1 = a + l / 4;
    double x2 = b - l / 4;
    double fx0 = 0, fx1 = 0, fx2 = 0;
    switch (i) {
    case 1:
        fx0 = func(x0, 0, 0, 0);
        fx1 = func(x1, 0, 0, 0);
        fx2 = func(x2, 0, 0, 0);
        break;

    case 2:
        fx0 = func(0, x0, 0, 0);
        fx1 = func(0, x1, 0, 0);
        fx2 = func(0, x2, 0, 0);
        break;
    case 3:
        fx0 = func(0, 0, x0, 0);
        fx1 = func(0, 0, x1, 0);
        fx2 = func(0, 0, x2, 0);
        break;
    case 4:
        fx0 = func(0, 0, 0, x0);
        fx1 = func(0, 0, 0, x1);
        fx2 = func(0, 0, 0, x2);
        break;
    }
    if (fx1 < fx0) {
        b = x0;
        x0 = x1;
    }
    else if (fx2 < fx0) {
        a = x0;
        x0 = x2;
    }
    return x0;
}
int main() {
    int n = 4;
    bool prov = 1;
    double eps = 0.01;
    int x[5]{ 0, 3, 3, 3, 3 };
    int xp[5]{ 0, 2, 2, 2, 2 };
    for (int j = 0; j < 4; j++) {
        int i = 1, k = 1;
        while (prov) {
            x[i] = minimum(i, x);
            if (i < n) i += 1;
            else {
                if (pow((pow(x[1] - xp[1], 2) + pow(x[2] - xp[2], 2) + pow(x[3] - xp[3], 2) + pow(x[4] - xp[4], 2)), 2) <= eps) {
                    cout << setprecision(16);
                    cout << eps << std::endl;
                    cout << k << std::endl;
                    cout << x[1] << std::endl;
                    cout << x[2] << std::endl;
                    cout << x[3] << std::endl;
                    cout << x[4] << std::endl;
                    cout << func(x[1], x[2], x[3], x[4]);
                    break;
                }
                int xp[5]{ 0,x[1], x[2],x[3], x[4] };
                i = 1;
                k += 1;
            }
        }
        eps /= 100;
        int x[5]{ 0,3,3,3,3 };
        int xp[5]{ 0,2,2,2,2 };
    }
}
