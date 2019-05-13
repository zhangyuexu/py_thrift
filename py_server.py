from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol
from thrift.server import TServer

from py.thrift.generated import PersonService
import PersonServiceImpl

try:
    personServicerHandler = PersonServiceImpl.PersonServiceImpl()
    processor = PersonService.Processor(personServicerHandler)

    serverSocket = TSocket.TServerSocket(port=8899)
    transportFactory = TTransport.TFramedTransportFactory()
    protocolFactory = TCompactProtocol.TCompactProtocolFactory()

    server = TServer.TSimpleServer(processor,serverSocket,transportFactory,protocolFactory)

    server.serve()

except Thrift.TException,ex:
    print '%s' % ex.message

