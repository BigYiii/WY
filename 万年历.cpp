#include<stdio.h>
#include<stdlib.h>
long mon[2][13] = {{0,31,28,31,30,31,30,31,31,30,31,30,31},{0,31,29,31,30,31,30,31,31,30,31,30,31}};
//判断闰年
int isleap(int year)
{
	if((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)
		return 1;
	else
		return 0;
}
//年份的第一天
int first_day_of_year(int year)
{
	int base_year = 2000;
	int first_day = 6;
	int i = 2000;
	int total = 0;
	for(i = base_year;i < year;i++)
	{
		total = total+365+isleap(i);
	}
	return (total+first_day)%7;
}
//月份第一天
int first_day_of_month(int year,int month,int first_year)
{
	int total = 0;
	int i = 0;
	for(i=1;i<month;i++)
	{
		total = total + mon[isleap(year)][i];
	}
	return (total+first_year)%7;
}
//展示日历

void show(int year,int month,int first_month)
{
	int i =0;
	printf("一   二   三   四   五   六   日\n");
	for(i=0;i<first_month-1;i++)
	{
		printf(" ");
	}
	for(i=1;i<=mon[isleap(year)][month];i++)
	{
		printf("%-5d",i);
		if((first_month-1+i)%7==0)
		{
			printf("\n");
		}
	}
	printf("\n");
	
}
int main()
{
	int year, month;
	printf("年/月： ");
	scanf("%d/%d",&year,&month);
	int first_year = first_day_of_year(year);
	int first_month = first_day_of_month(year,month,first_year);
	show(year,month,first_month);
	system("pause");
	return 0;
}