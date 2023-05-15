img_html = ['a.jpg', 'b.jpg','c.jpg']
blobName = ['URA','URB','URC']
img = [list(img_html) for img_html in zip(img_html, blobName)]
print(img)
for index, i in enumerate(img):
    #print(index,i)
    print(i[0])