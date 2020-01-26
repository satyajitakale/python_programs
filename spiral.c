
#include <stdio.h>

int main()
{
    int cnt=1,i=1,j=1,n,i_fl=0,j_fl=0,min1;
    printf("Enter a num:");
    scanf("%d",&n);
    while(cnt!=2*n)
    {
        if(j>n)
            j_fl+=2;
        if(i-i_fl >j-j_fl)
            min1=j-j_fl;
        else
            min1=i-i_fl;
        printf("%d",min1);
        if (j==2*n-1)
        {
            j=0;
            i++;
            cnt++;
            j_fl=0;
            if(i>n)
                i_fl+=2;
       
            printf("\n");
        }
        j++;
    }

    return 0;
}
