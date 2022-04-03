close all; clear all; clc;
fp=fopen('C:\Users\16941\Desktop\毕业设计\result\result.txt','w');
fprintf(fp,'\n');
fclose(fp);
for k=1:101
    max1=0
    max2=0
    if(k<10)
        e=0;
        b=sprintf('%d%d',e,k)
    else
        b=sprintf('%d',k)
    end
    %CHUM 65
    %a='C:\Users\16941\Desktop\毕业设计\CHUM\HN-CHUM-0';
    %c='\CT\RTS\RTSS.mat';
    %CHUS 101
    %a='C:\Users\16941\Desktop\毕业设计\CHUS\HN-CHUS-0'
    %c='\PET\CT\RTS\RTSS.mat'
    %HGJ 91
    a='C:\Users\16941\Desktop\毕业设计\HGJ\HN-HGJ-0'
    c='\CT\RTS\RTSS.mat'
    %HMR 41
    %a='C:\Users\16941\Desktop\毕业设计\HMR\HN-HMR-0'
    %c='\CT\RTS\RTSS.mat'
    path=sprintf('%s%s%s',a,b,c)
    try
        TestData = load(path);
        matrix=TestData.contours.Segmentation;%0无病1有病灶
        [m,n,l]=size(matrix)%m行数 n列数 l 层数
        for p=1:l 
            tag1=999;%shang
            tag2=0;%xia
            tag3=999;%zuo
            tag4=0;%you
            for i=1:m
                for j=1:n
                    if(matrix(i,j,p)==1)
                        if(i<tag1)
                            tag1=i;
                        end
                        if(i>tag2)
                            tag2=i;
                        end
                        if(j<tag3)
                            tag3=j;
                        end
                        if(j>tag4)
                            tag4=j;
                        end
                    end
                end
            end
            patch(1,2)=0
            if(tag1==999&&tag3==999)
                patch
            else
                patch(1,1)=tag2-tag1
                patch(1,2)=tag4-tag3
                patch
            end
            if(max1<patch(1,1))
                max1=patch(1,1)
            end
            if(max2<patch(1,2))
                max2=patch(1,2)
            end
        end 
            fp=fopen('C:\Users\16941\Desktop\毕业设计\result\result.txt','a');
            fprintf(fp,'%d %d\n',max1,max2);
            fclose(fp);
    end     
end