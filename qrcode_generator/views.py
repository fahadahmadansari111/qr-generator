from django.shortcuts import render
from qrcode import *
data=None
def home(request):
    global data
    if request.method=="POST":
        data=request.POST['data']
        img=make(data)
        img.save("static/image/test.png")
        # data=request.POST['data']
        # qr = qrcode.QRCode(
        #     version=1,
        #     error_correction=qrcode.constants.ERROR_CORRECT_L,
        #     box_size=10,
        #     border=4,
        # )
        # qr.add_data(data)
        # qr.make(fit=True)
        # img = qr.make_image(fill_color="red", back_color="black")
        # img.save("static/image/test.png")
    else:
        pass
    return render(request,"homepage.html",{'data':data})