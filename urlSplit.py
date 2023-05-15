from urllib.parse import urlsplit
url = 'https://minkonto.blob.core.windows.net/photos/DJI_0778.JPG?sv=2021-12-02&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2023-06-30T13%3A41%3A12Z&st=2023-05-03T05%3A41%3A12Z&spr=https&sig=YRtN%2FYiPlnSv4HGaxiVMcnoHUepI4lcLt4i8KkCfG6w%3D%27,%20%27/photos/DJI_0778.JPG%27'
r1 = urlsplit(url)
a =r1.path
b = a.rpartition('/')[2]
print(type(a))
