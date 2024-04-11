# networkScanner
A network scanner is a tool used to scan a computer network to discover connected devices and gather information about them. It can detect active hosts, open ports, services running on those ports, and other details about the devices on the network. Network scanners are commonly used for security auditing, network inventory management, and troubleshooting. They can be either passive, meaning they observe network traffic without sending any packets, or active, where they actively send packets to probe devices and gather information.

This is a basic network scanner. Put in your ip address and let it scan the networks you are connected to. 
I have added a packet sniffer to detect traffic coming from a network or a website.
To access it run ***Python3 networkScanner.py -[argument tag] or --[arguments] [your target ip address/interface]***

To run the interface, simply run ***Python3 networkScanner.py -i [your interface] or Python networkScanner.py --interface [your interface]***

You might need to run the spoofer differently because you will need it to spoof and capture the MAC address of your target to run MITM attacks. To do this, simply run ***Python3 spoofer.py -t [your Target IP] -g [your Gateway IP]***
The code will get your IP address and your Target's Ip address and swap them so that you can intercept your targets network traffic. You can then use the packet sniffer to collect data from web traffic and sniff any web packets that your target may input in their web browser. If you are lucky, you can even use this to get your targets username and password from the website they access. 

However, if you find this, do not use this for malicious purposes. This is just for entertainment and educational purposes only.