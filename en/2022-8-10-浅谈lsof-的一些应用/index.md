# Talking about some uses of lsof


## 1 Linux everything is a file

In a Linux system, everything is a file. Files provides access not only to file data stored to disk, but also to network connections and hardware. The problem is that everything is a file, so how to view and manage these open files through commands. You can use the lsof command. Not only can you view the files and directories opened by the process, but you can also view the socket information such as the port the process listens to.

<br>

## 2 Common options of lsof command

> **-a** Indicates an AND relationship between other options\
> **-c** <process name> output the files opened by the specified process\
> **-d** <file descriptor> list the processes that occupy the file number\
> **+d** <directory> output directory and opened files and directories under the directory (not recursive)\
> **+D** <directory> Recursive output and opened files and directories under the directory\
> **-i** <condition> output network-related files that match the condition\
> **-n** Do not resolve hostname\
> **-p** <process ID> output the files opened by the process with the specified PID\
> **-P** Do not parse port numbers\
> **-t** output only PID\
> **-u** Output the files opened by the specified user\
> **-U** output opened UNIX domain socket files\
> **-h** display help information\
> **-v** Display version information

<br>

## 3 Some simple applications

I won’t list all the application scenarios here, and you can search according to your specific needs. What you need to remember is that you can think of using the lsof command when it comes to files. List some simple application scenarios to deepen the use of commands.

### 3.1 **Check which processes have opened a file**

This should be used frequently. In windows, for example, if you want to close a certain file, you can’t close it. The reason is that this file is used by many processes at the same time. If you want to close it, you can’t close it. You can only close it first. All the processes that are using the file should be killed. At this time, lsof can be used.

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/06973eb2b4514ad5af77075630136bad~tplv-k3u1fbpfcp-zoom-1.image" style="zoom:200%;" />

+d is an operation for folders, and if you need to kill all process ids, you can use awk to list the pid numbers and then kill them.

### 3.2 **View all files opened by a process**

This sometimes needs to be used, what operations a certain process has done, and which files have been opened.
<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/8b897ce13cf04690ac6a4cdbaf9ee9f6~tplv-k3u1fbpfcp-zoom-1.image" style="zoom:200%;" />

Use lsof -p + pid to see which files the process has open.

### 3.3 **View files opened by ipv4 and ipv6**

Network-related file operations are also used a lot, so to locate some problems, you need to use lsof to view some network-related operations on files. lsof -i is to view the operations of ipv4 and v6 on files.
<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/fa82058ffef840d1aec4fe97c3fbedcd~tplv-k3u1fbpfcp-zoom-1.image" style="zoom:200%;" />
Of course, if you need to see ipv4 or ipv6 separately, you can directly specify lsof -i ipv4/ipv6

```
$ sudo lsof -i 4
$ sudo lsof -i 6
```

### 3.4 **List the files related to the port**

This is used a lot, and you often need to check the files used by the relevant ports, such as port 22 or something. Use lsof -i:port.
<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/2b7aa57bcd6c40bcb9e41ebdadf690cb~tplv-k3u1fbpfcp-zoom-1.image" style="zoom:200%;" />

<br>

## 4 A specific practice

I have encountered a case before, that is, using df -h and du -sh / a certain folder, and found that the disk space occupied by the two displays is very different, because df -h is the statistical folder space in the disk , including this folder may have been deleted or referenced elsewhere, but du counts the actual size of the current folder, so it may be that a certain folder counted by df -h is larger than du -sh. I encountered this situation at the time, and the difference between the two is still very large. How to solve this problem, you can use lsof | grep delete to find the folder occupied by the delete process, and then kill these processes.

<br>

## 5 Summary

That's all about the main uses of lsof, and there are many other uses, which can be oriented according to the needs of daily work.

You can refer to: https://www.cnblogs.com/sparkdev/p/10271351.html
