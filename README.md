# networkScanner
A network scanner is a tool used to scan a computer network to discover connected devices and gather information about them. It can detect active hosts, open ports, services running on those ports, and other details about the devices on the network. Network scanners are commonly used for security auditing, network inventory management, and troubleshooting. They can be either passive, meaning they observe network traffic without sending any packets, or active, where they actively send packets to probe devices and gather information.

This is a basic network scanner. Put in your ip address and let it scan the networks you are connected to. 
I have added a packet sniffer to detect traffic coming from a network or a website.
I have also added a Geo Locator as well as a port scanner to scan open ports within the network.

This is specifically and can only be used during the enumeration stages of hacking. Do not attempt to use this as an actual exploitation device else I will not be liable for any damage that might occur to you. Oyo lo wa meaning you are on your own. This can be very useful during a CTF challenge and/or pentesting your local network.

The code runs in the main.py where you will be given options to choose what you want to do with your target IP. To run this, simply type *** Python[Python3 for linux] main.py [IP Address]***. It will ask what type of attacks you want to use. Select any options by typing the number selected in the code. This will then run the attack that you specified. Simple and easy!

You can also run the code individually and according to your specifications, you can edit it to specify the type of attack you want to run. However, it will be much simpler to run the main.py code. 

The network scanner scans your target IP and MAC addressesas well as the range of networks within your target system. It also supports CIDR notations meaning you can run a range of IP addresses and MAC addresses needed for enumeration.

The port scanner can be used to scan for open ports within an organization network. You can run the port scanner independently or you can use the main.py to run it. As it should, it scans for open ports however, its kind of slow and will be subject to change in future times. It runs and scans the entire port specifications i.e (1-65535) ports. So, good luck with that!

The MAC Spoofer will get your IP address and your Target's IP address and swap them so that you can intercept your target's network traffic. 

You can then use the packet sniffer to collect data from web traffic and sniff any web packets that your target may input in their web browser. If you are lucky, you can even use this to get your targets username and password from the website they access. 

However, if you find this, do not use this for malicious purposes. This is just for entertainment and educational purposes only.