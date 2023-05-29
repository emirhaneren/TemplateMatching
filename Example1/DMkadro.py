import cv2

sourceimage=cv2.imread("kaynakKadro.jpg")
templateimage=cv2.imread("sablonKadro.jpg")

matchimage=cv2.matchTemplate(sourceimage,templateimage,cv2.TM_CCOEFF_NORMED)
minval,maxval,minloc,maxloc=cv2.minMaxLoc(matchimage)
topleft=maxloc

h,w,c=templateimage.shape
bottomright=(topleft[0]+w,topleft[1]+h)
cv2.rectangle(sourceimage,topleft,bottomright,(0,255,0),10)

cv2.imshow("Tespit edilen resim",sourceimage)
cv2.imshow("Tespit",matchimage)
cv2.imshow("Sablon",templateimage)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)