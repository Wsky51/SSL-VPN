# SSL-VPN

## 说明
一个简单的SSL VPN实验，主要有三部分，CA,Client,Server.  
其中CA模拟CA认证中心，向用户发送证书的功能
Client端通过和Server端建立Socket连接，并进行SSL连接确认通过后，再进行VPN访问

非对称加密算法主要实现为rsa.py,对称加密算法为AES（16 bit）加密，其主要实现为aes.py