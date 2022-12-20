import cv2

soltık = cv2.EVENT_LBUTTONDOWN
sagtık = cv2.EVENT_RBUTTONDOWN
kayıt = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX



def kareçizme(a,s,d,f,g):
    global q,w
    if a == soltık:
        q = (s,d)
        
    if a == sagtık:
        w = (s,d)
        

        
        
q = (0,0)
w = (0,0)

r = True


cv2.namedWindow("Hello")
cv2.setMouseCallback("Hello",kareçizme)

while True:

    z,x = kayıt.read()
    cv2.rectangle(x,q,w,(0,255,255),2)
    cv2.putText(x,"A",q,font,1,(255,0,0),2,cv2.LINE_4)
    cv2.putText(x,"B",w,font,1,(255,0,0),2,cv2.LINE_4)



    cv2.imshow("Hello",x)
    if cv2.waitKey(1) & 0xFF == 27:
        break

kayıt.release()
cv2.destroyAllWindows()








