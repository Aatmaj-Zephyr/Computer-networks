Microsoft Windows [Version 10.0.18363.418]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Users\kjsce_comp10>ipconfig

Windows IP Configuration


Ethernet adapter Ethernet:

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::80a:19b6:68b7:c111%6
   IPv4 Address. . . . . . . . . . . : 172.17.14.20
   Subnet Mask . . . . . . . . . . . : 255.255.254.0
   Default Gateway . . . . . . . . . : 172.17.15.254

Ethernet adapter VirtualBox Host-Only Network:

   Connection-specific DNS Suffix  . :
   Link-local IPv6 Address . . . . . : fe80::490f:5:dfde:4b4e%15
   IPv4 Address. . . . . . . . . . . : 192.168.56.1
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . :

C:\Users\kjsce_comp10>ping 127.17.14.23

Pinging 127.17.14.23 with 32 bytes of data:
Reply from 127.17.14.23: bytes=32 time<1ms TTL=128
Reply from 127.17.14.23: bytes=32 time<1ms TTL=128
Reply from 127.17.14.23: bytes=32 time<1ms TTL=128
Reply from 127.17.14.23: bytes=32 time<1ms TTL=128

Ping statistics for 127.17.14.23:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 0ms, Maximum = 0ms, Average = 0ms

C:\Users\kjsce_comp10>traceroute 127.17.14.23
'traceroute' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\kjsce_comp10>tracert 127.17.12.23

Tracing route to 127.17.12.23 over a maximum of 30 hops

  1    <1 ms    <1 ms    <1 ms  127.17.12.23

Trace complete.

C:\Users\kjsce_comp10>netstat

Active Connections

  Proto  Local Address          Foreign Address        State
  TCP    172.17.14.20:49998     sc-in-f188:5228        ESTABLISHED
  TCP    172.17.14.20:50072     bom12s18-in-f14:https  ESTABLISHED
  TCP    172.17.14.20:50083     bom12s17-in-f14:https  ESTABLISHED
  TCP    172.17.14.20:50102     maa03s45-in-f10:https  ESTABLISHED
  TCP    172.17.14.20:50116     20.198.118.190:https   ESTABLISHED
  TCP    172.17.14.20:50148     a23-207-180-137:https  TIME_WAIT
  TCP    172.17.14.20:50204     sg-in-f113:https       ESTABLISHED
  TCP    172.17.14.20:50215     bom07s33-in-f14:https  ESTABLISHED
  TCP    172.17.14.20:50216     bom07s30-in-f3:https   ESTABLISHED
  TCP    172.17.14.20:50219     hkg12s10-in-f3:https   ESTABLISHED
  TCP    172.17.14.20:50220     hkg12s10-in-f3:https   ESTABLISHED
  TCP    172.17.14.20:50221     bom07s37-in-f14:https  ESTABLISHED
  TCP    172.17.14.20:50222     bom07s36-in-f3:https   ESTABLISHED
  TCP    172.17.14.20:50224     bom07s36-in-f1:https   ESTABLISHED
  TCP    172.17.14.20:50225     bom07s37-in-f14:https  ESTABLISHED
  TCP    172.17.14.20:50226     maa03s46-in-f14:https  ESTABLISHED
  TCP    172.17.14.20:50227     bom07s25-in-f13:https  ESTABLISHED
  TCP    172.17.14.20:50228     maa05s24-in-f10:https  ESTABLISHED
  TCP    172.17.14.20:50229     maa03s40-in-f4:https   ESTABLISHED
  TCP    172.17.14.20:50230     maa03s40-in-f4:https   ESTABLISHED
  TCP    172.17.14.20:50231     maa05s24-in-f10:https  ESTABLISHED
  TCP    172.17.14.20:50244     a-0001:https           ESTABLISHED
  TCP    172.17.14.20:50245     a-0001:https           ESTABLISHED
  TCP    172.17.14.20:50247     a122-252-138-234:https  ESTABLISHED
  TCP    172.17.14.20:50248     13.107.6.254:https     ESTABLISHED
  TCP    172.17.14.20:50249     13.107.253.48:https    ESTABLISHED
  TCP    172.17.14.20:50250     204.79.197.254:https   ESTABLISHED
  TCP    172.17.14.20:50251     204.79.197.222:https   ESTABLISHED
  TCP    172.17.14.20:50252     20.219.9.219:https     TIME_WAIT


C:\Users\kjsce_comp10>nslookup www.google.com
Server:  svvpdc.svv.local
Address:  172.31.0.25

Non-authoritative answer:
Name:    www.google.com
Addresses:  2404:6800:4009:827::2004
          142.250.195.132


C:\Users\kjsce_comp10>arp -a

Interface: 172.17.14.20 --- 0x6
  Internet Address      Physical Address      Type
  172.17.14.52          d8-cb-8a-8d-20-aa     dynamic
  172.17.14.60          d8-cb-8a-8d-15-0f     dynamic
  172.17.14.66          d8-cb-8a-8d-10-b6     dynamic
  172.17.15.254         b0-aa-77-66-d1-41     dynamic
  172.17.15.255         ff-ff-ff-ff-ff-ff     static
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.251           01-00-5e-00-00-fb     static
  224.0.0.252           01-00-5e-00-00-fc     static
  239.255.255.250       01-00-5e-7f-ff-fa     static

Interface: 192.168.56.1 --- 0xf
  Internet Address      Physical Address      Type
  192.168.56.255        ff-ff-ff-ff-ff-ff     static
  224.0.0.22            01-00-5e-00-00-16     static
  224.0.0.251           01-00-5e-00-00-fb     static
  224.0.0.252           01-00-5e-00-00-fc     static
  239.255.255.250       01-00-5e-7f-ff-fa     static

C:\Users\kjsce_comp10>telnet 172.17.14.19
'telnet' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\kjsce_comp10>Enable-WindowsOptionalFeature -Online -FeatureName TelnetClient
'Enable-WindowsOptionalFeature' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\kjsce_comp10>hostname
16DCEB217-10

C:\Users\kjsce_comp10>hostname 172.17.14.19
sethostname: Use the Network Control Panel Applet to set hostname.
hostname -s is not supported.

C:\Users\kjsce_comp10>systeminfo

Host Name:                 16DCEB217-10
OS Name:                   Microsoft Windows 10 Pro for Workstations
OS Version:                10.0.18363 N/A Build 18363
OS Manufacturer:           Microsoft Corporation
OS Configuration:          Member Workstation
OS Build Type:             Multiprocessor Free
Registered Owner:          ROB-03
Registered Organization:
Product ID:                00391-90090-60463-AA574
Original Install Date:     08-09-2022, 11:23:37
System Boot Time:          01-08-2023, 05:30:52
System Manufacturer:       LENOVO
System Model:              10HJA02AHF
System Type:               x64-based PC
Processor(s):              1 Processor(s) Installed.
                           [01]: Intel64 Family 6 Model 60 Stepping 3 GenuineIntel ~3500 Mhz
BIOS Version:              LENOVO FCKT69AUS, 10-04-2015
Windows Directory:         C:\Windows
System Directory:          C:\Windows\system32
Boot Device:               \Device\HarddiskVolume2
System Locale:             en-us;English (United States)
Input Locale:              00004009
Time Zone:                 (UTC+05:30) Chennai, Kolkata, Mumbai, New Delhi
Total Physical Memory:     8,105 MB
Available Physical Memory: 3,403 MB
Virtual Memory: Max Size:  9,385 MB
Virtual Memory: Available: 4,011 MB
Virtual Memory: In Use:    5,374 MB
Page File Location(s):     C:\pagefile.sys
Domain:                    SVV.local
Logon Server:              \\SVVPDC
Hotfix(s):                 7 Hotfix(s) Installed.
                           [01]: KB4601556
                           [02]: KB4513661
                           [03]: KB4516115
                           [04]: KB4517245
                           [05]: KB4521863
                           [06]: KB4577586
                           [07]: KB4517389
Network Card(s):           2 NIC(s) Installed.
                           [01]: Realtek PCIe GbE Family Controller
                                 Connection Name: Ethernet
                                 DHCP Enabled:    No
                                 IP address(es)
                                 [01]: 172.17.14.20
                                 [02]: fe80::80a:19b6:68b7:c111
                           [02]: VirtualBox Host-Only Ethernet Adapter
                                 Connection Name: VirtualBox Host-Only Network
                                 DHCP Enabled:    No
                                 IP address(es)
                                 [01]: 192.168.56.1
                                 [02]: fe80::490f:5:dfde:4b4e
Hyper-V Requirements:      VM Monitor Mode Extensions: Yes
                           Virtualization Enabled In Firmware: No
                           Second Level Address Translation: Yes
                           Data Execution Prevention Available: Yes

C:\Users\kjsce_comp10>nslookup
Default Server:  svvpdc.svv.local
Address:  172.31.0.25

> ww.google.com
Server:  svvpdc.svv.local
Address:  172.31.0.25

Non-authoritative answer:
Name:    www3.l.google.com
Addresses:  2404:6800:4009:80a::200e
          172.217.160.174
Aliases:  ww.google.com
