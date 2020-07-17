import sys
import time
import urllib.request
from win10toast_persist import ToastNotifier as Toast


def main(website, interval_mins):
    try:
        toaster = Toast()
    
        urllib.request.urlcleanup()
        start_webpage = urllib.request.urlopen(website).read()
        while(True):
            urllib.request.urlcleanup()
            now_webpage = urllib.request.urlopen(website).read()
            if (start_webpage != now_webpage):
                toaster.show_toast("Website changed Notifier",
                                   "Website '{}' changed!".format(website),
                                   duration=None)
                break
            
            time.sleep(interval_mins * 60)
        
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 15)
    input("Press Enter to continue...")