import time
from plyer import notification


if __name__=="__main__":
    while True:
        notification.notify(
            title="please sir Ashish Drink Water",
            message="To prevent dehydration, you need to drink adequate amounts of water. There are many different opinions on how much water you should be drinking every day. Health authorities commonly recommend eight 8-ounce glasses, which equals about 2 liters. ",
            app_icon="E:\my creation\software\water_drinking_msg\glass.ico",
            timeout=5

        )
        
        time.sleep(16)    