#include<time.h>
int main(void)
{
    struct tm *ptr;
    time tm 1t;

    1t=time(NULL);
    ptr=localtime(&1t);
    printf(asctime(ptr));

    return 0;
}
