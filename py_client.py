from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TCompactProtocol

from py.thrift.generated import PersonService
from py.thrift.generated import ttypes

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

try:
    tSocket = TSocket.TSocket('localhost',8899)
    tSocket.setTimeout(600)

    transport = TTransport.TFramedTransport(tSocket)

    protocol = TCompactProtocol.TCompactProtocol(transport)

    client = PersonService.Client(protocol)

    transport.open()
    person = client.getPersonByUsername("zhangsan")

    print person.username
    print person.age
    print person.married

    print '-----------------------------'

    person2 = ttypes.Person()
    person2.username = "lisi"
    person2.age = 20
    person2.married = True

    client.savePerson(person2)

    transport.close()

except Thrift.TException,tx:
    print '%s' % tx.message