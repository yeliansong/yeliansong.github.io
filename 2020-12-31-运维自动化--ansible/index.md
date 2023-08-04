# 运维自动化 -- Ansible


### 1. 运维自动化应用场景

- 操作系统预备自动化

  对主机进行批量操作系统部署。PXE

- 配置自动化

  对主机进行批量配置或对主机的应用程序进行批量配置。 Ansible， saltstack, puppet.

  Ansible, 用的ssh协议，开箱即用。

  saltstack，需要agent端配合，配置部署速度快。

  puppet，老牌配置自动化工具，需要agent配合。

  提高配置效率，降低人工参与度。

- 监控自动化

  对服务器的应用，性能的监控。

  1> 系统与应用监控。 普罗米修斯

  2> 日志监控。 ELK

- 代码持续集成与代码持续发布自动化

### 2. Ansible 工作原理

即开即用，没有主从结构。是通过ssh协议来完成对主机的批量管理，Ansible的内部各个功能模块是独立，通过各个功能模块来进行功能的管理。Ansible有一个主机清单，通过在主机清单中设置批量主机的信息，来批量管理。

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/0081Kckwgy1glm4o7ici2j31h40u0x59.jpg" style="zoom:200%;" />



### 3. Ansible 主机清单

Ansible 是通过主机清单来对主机进行操作；同时主机清单也可以对主机进行分组，便于对组进行操作。

主机清单的设置两种方式，一种是直接在清单后添加IP或者主机名。另外一种是添加主机的分组，在分组中添加主机的IP或主机名。

```powershell
192.168.2.1
monitor
或
[webgroup]
monitor
```

### 4. Ansible ping 模块使用

场景分析：使用Ansible的ping模块来对其他主机来测试其联通性。

问题分析解决：

首先是将ssh的密钥拷贝到目标主机，使其登陆实现免密登陆。这里来提一嘴ssh登陆其他主机的过程。

ssh密码登陆是用的RSA加密，就是非对称加密。源主机先是生成一对公私钥密钥对，存放在源主机路径下，然后ssh连接时，目标主机会去读取源主机密钥对，用源主机的公钥对密码进行加密，发给源主机，源主机用私钥揭秘，将揭秘后的密码发给目标主机，目标主机判断密码是否正确。

```powershell
源主机生成密码对
root@agent:/etc# ssh-keygen -t rsa -f /root/.ssh/id_rsa -N ''

密钥对同步
root@agent:/etc# ssh-copy-id  vagrant@192.168.2.7
```

第二步，修改ansible的配置文件，在主机清单中加上要配置的主机IP。

在主机清单中加上要连接的主机IP。

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

证明已经调试通了。

### 5. Ansible Cron 实现主机的时钟同步

场景分析：通过cron模块实现远程主机和阿里云服务器的周期性时钟同步。

直接使用cron 命令来实现周期性同步。

```powershell
root@agent:/etc# ansible 192.168.2.6 -m cron -a 'name="test cron1" \
> job="ntpdate time1.aliyun.com" minute=0 hour=*/1'
```

然后在远程主机中查看cron 周期性任务列表。

```powershell
vagrant@monitor:~$ crontab -l
#Ansible: test cron1
0 */1 * * * ntpdate time1.aliyun.com
```

###   6. Ansible copy 实现文件的拷贝

场景分析： 现在是用Ansible copy实现不同主机间的文件同步。使用hostname的方式。

如果要用hostname来进行ssh的连接，需要在/etc/host文件中声明主机的IP和hostname的对应。

```powershell
root@agent:/tmp# cat /etc/hosts
127.0.1.1	agent	agent
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

把192.168.2.6 和 monitor的主机名做了对应。然后再再ansible的配置文件的主机列表中加上monitor主机。

```powershell
root@agent:/tmp# ansible monitor -m copy -a "src=/tmp/4.sh dest=/tmp/4.sh"
```

通过这条命令就实现了主机间的拷贝。


