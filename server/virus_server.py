import Database
import socket
import struct

class Server:
    def __init__(self, ip, port):
        self.db = Database.Database()
        self.listVirusMd5 = self.db.getVirusMd5()
        # print(self.listVirusMd5)

        self.sockServ = socket.socket()
        self.sockServ.bind((ip, port))
        self.sockServ.listen(socket.SOMAXCONN)

        pass

    #
    #   Send msg format:
    #       md5 num : md5......
    #
    def __sendTo(self, sockClient):
        nMD5 = len(self.listVirusMd5)
        strMD5 = ""
        for dictMD5 in self.listVirusMd5:
            strMD5 += dictMD5['md5']
        lenMD5 = len(self.listVirusMd5[0]['md5'])
        strMD5 = strMD5.encode('gb2312')
        msg = struct.pack("i%ds" % (nMD5 * lenMD5), nMD5, strMD5);
        sockClient.send(msg)
        pass;

    def run(self):
        print("server starts")
        while True:
            sockClient, clientAddr = self.sockServ.accept()
            if(sockClient):
                self.__sendTo(sockClient)
        pass





if __name__ == "__main__":
    server = Server("127.0.0.1", 8888)
    server.run()

