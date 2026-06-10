import pywhatkit as pwk
import datetime
#from geopy.geocoders import Nominatim

def sendInfoWA(imagepath,HOD_name, HOD_mob, Block_Number):
   
    
    message="Dear Sir, \nALERT ALERT ALERT !!! \n"+"Cheating has been Detected in block : "+Block_Number+" \n";
    message=message+". And also attached Surveilliance Image for your reference. PLEASE TAKE ACTION IMMMEDIATLY \n ";
    message=message+" Regards - \n AI based Anti Cheating System"
    mobilenumber="+91"+HOD_mob;
 
    
    pwk.sendwhats_image(mobilenumber, imagepath, message)
    
 
if __name__ == '__main__':
    
    sendInfoWA("Captured_images//0.jpg", 'jadhav sir', '8767574749', '01')
 
    