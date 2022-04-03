close all; clear all; clc;
for k=1:65
    %******<100*****
    if(k<10)
        e=0;
        b=sprintf('%d%d',e,k);
    else
        b=sprintf('%d',k);
    end
    %CHUM 65
    a='C:\Users\16941\Desktop\biye\CHUM\HN-CHUM-0';
    c='\CT\RTS\RTSS.mat';
    
    %HGJ 91
    %a='C:\Users\16941\Desktop\biye\HGJ\HN-HGJ-0';
    %c='\CT\RTS\RTSS.mat';
   
    %HMR 41
    %a='C:\Users\16941\Desktop\biye\HMR\HN-HMR-0';
    %c='\CT\RTS\RTSS.mat';
    
    d='\CT\position.txt';
    
    %****>100****
    %CHUS 102
    %if(k>=100)
    %    a='C:\Users\16941\Desktop\biye\CHUS\HN-CHUS-';
    %else
    %   a='C:\Users\16941\Desktop\biye\CHUS\HN-CHUS-0';
    %end
    %c='\PET\CT\RTS\RTSS.mat';
    %d='\PET\CT\position.txt';
    
    
    path = sprintf('%s%s%s',a,b,c)
    path_pos = sprintf('%s%s%s',a,b,d)
    
    fp=fopen(path_pos,'w');
    fclose(fp);
    
    
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
            if(tag1==999&&tag3==999)
                y = m/2;
                x = n/2;
            else
                y=(tag2+tag1)/2
                x=(tag4+tag3)/2
            end
            r_y=y/m
            r_x=x/n
            fp=fopen(path_pos,'a');
            fprintf(fp,'%f %f\n',r_x,r_y);
            fclose(fp);
        end 
    end     
