#include <iostream>
using namespace std;
double func(double x1, double x2, double x3, double x4) {
    return pow((x1 - x2), 2) + 4 * pow((x3 - x4), 2) + pow((x2 - 6 * x3), 4) + 2 * pow((x1 - x4), 2);
}
double minimum(double x1, double x2, double x3, double x4) {
    double a = 1.0;
    double b = 7.0;
    double l = b - a;
    double delta = 0.001;
    while ((l / 2) > delta) {
        x1 = (a + b) / 2;
        l = b - a;
        double fx1 = func(x1, x2, x3, x4);
        double c = a + l / 4;
        double d = b - l / 4;
        double fc = func(c, x2, x3, x4);
        double fd = func(d, x2, x3, x4);
        if (fc < fx1) {
            b = x1;
            x1 = c;
        }
        else {
            if (fd < fx1) {
                a = x1;
                x1 = d;
            }
            else {
                a = c;
                b = d;
            }
        }
    }
    return x1;
}

int main()
{
    setlocale(LC_ALL, "RUS");
    double eps = 0.001, x_check = 5.0, x1_start = -1, x2_start = 2, x3_start = 5, x4_start = 3.2, x1, x2, x3, x4;
    while (abs(x_check - x4_start) >= eps) {
        x_check = x4_start;
        x1 = minimum(x1_start, x2_start, x3_start, x4_start);
        x1_start = x1;
        x2 = minimum(x2_start, x1_start, x3_start, x4_start);
        x2_start = x2;
        x3 = minimum(x3_start, x1_start, x2_start, x4_start);
        x3_start = x3;
        x4 = minimum(x4_start, x1_start, x2_start, x3_start);
        x4_start = x4;
    }
    cout << "Минимум: " << x1 << ' ' << x2 << ' ' << x3 << ' ' << x4 << ' ' << func(x1, x2, x3, x4);
}
