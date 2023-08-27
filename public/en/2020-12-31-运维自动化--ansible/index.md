# Operation and maintenance automation -- Ansible


### 1. Operation and maintenance automation application scenarios

- OS preparation automation

   Batch OS deployment to hosts. PXE

- Configuration automation

   Perform batch configuration on hosts or batch configuration on host applications. Ansible, saltstack, puppet.

   Ansible, using the ssh protocol, works out of the box.

   Saltstack requires the cooperation of the agent side, and the configuration and deployment are fast.

   Puppet, an old-fashioned configuration automation tool, requires the cooperation of agents.

   Improve configuration efficiency and reduce manual involvement.

- Monitoring automation

   Monitoring of server applications and performance.

   1> System and application monitoring. Prometheus

   2> Log monitoring. ELK

- Code continuous integration and code continuous release automation

### 2. How Ansible works

Out-of-the-box, no master-slave structure. The batch management of hosts is completed through the ssh protocol. Each internal functional module of Ansible is independent, and the functional management is performed through each functional module. Ansible has a host list, which can be managed in batches by setting the information of batch hosts in the host list.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/0081Kckwgy1glm4o7ici2j31h40u0x59.jpg" style="zoom:200%;" />



### 3. Ansible host list

Ansible operates the host through the host list; at the same time, the host list can also group the hosts to facilitate the operation of the group.

There are two ways to set the host list, one is to add IP or host name directly after the list. The other is to add a group of hosts, and add the IP or host name of the host in the group.

```powershell
192.168.2.1
monitor
or
[webgroup]
monitor
```

### 4. Ansible ping module usage

Scenario analysis: Use Ansible's ping module to test the connectivity of other hosts.

Problem analysis and solution:

The first is to copy the ssh key to the target host to enable it to log in without secrets. Here to mention the process of ssh logging in to other hosts.

The ssh password login is encrypted with RSA, which is asymmetric encryption. The source host first generates a pair of public-private key pairs and stores them in the path of the source host. Then, when connecting via ssh, the target host reads the source host key pair, encrypts the password with the source host’s public key, and sends it to the source host. Host, the source host uses the private key to decipher, and sends the deciphered password to the target host, and the target host judges whether the password is correct.

```powershell
The source host generates the password pair
root@agent:/etc# ssh-keygen -t rsa -f /root/.ssh/id_rsa -N ''

key pair synchronization
root@agent:/etc# ssh-copy-id vagrant@192.168.2.7
```

The second step is to modify the ansible configuration file and add the host IP to be configured in the host list.

Add the host IP to be connected to the host list.

```powershell
root@agent:/etc# ansible 192.168.2.7 -m ping
192.168.2.7 | SUCCESS => {
     "ansible_facts": {
         "discovered_interpreter_python": "/usr/bin/python"
     },
     "changed": false,
     "ping": "pong"
}
```

Proof that it has been debugged.

### 5. Ansible Cron realizes the clock synchronization of the host

Scenario analysis: The periodic clock synchronization between the remote host and the Alibaba Cloud server is realized through the cron module.

Use the cron command directly to achieve periodic synchronization.

```powershell
root@agent:/etc# ansible 192.168.2.6 -m cron -a 'name="test cron1" \
> job="ntpdate time1.aliyun.com" minute=0 hour=*/1'
```

Then check the cron periodic task list in the remote host.

```powershell
vagrant@monitor:~$ crontab -l
#Ansible: test cron1
0 */1 * * * ntpdate time1.aliyun.com
```

### 6. Ansible copy realizes file copy

Scenario analysis: Ansible copy is now used to synchronize files between different hosts. The way to use hostname.

If you want to use hostname for ssh connection, you need to declare the correspondence between the host's IP and hostname in the /etc/host file.

```powershell
root@agent:/tmp# cat /etc/hosts
127.0.1.1 agent agent
127.0.0.1 localhost

192.168.2.6 monitor

# The following lines are desirable for IPv6 capable hosts
::1 ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
ff02::3 ip6-allhosts
```

Match 192.168.2.6 with the host name of monitor. Then add the monitor host to the host list in the ansible configuration file.

```powershell
root@agent:/tmp# ansible monitor -m copy -a "src=/tmp/4.sh dest=/tmp/4.sh"
```

Through this command, the copy between hosts is realized.
